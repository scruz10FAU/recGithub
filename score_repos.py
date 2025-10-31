import requests
import base64
import re
from collections import defaultdict
import math
import argparse
import pandas as pd
from genre_keywords import GENRE_KEYWORDS
import os

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # put your PAT in env var

def gh_get(url, accept="application/vnd.github.v3+json"):
    headers = {"Accept": accept}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"  # or "token ..."
    r = requests.get(url, headers=headers)
    return r


def score_repo_from_topics(topics_str):
    # normalize topics into a list of tokens
    if isinstance(topics_str, list):
        topics_list = topics_str
    elif isinstance(topics_str, str):
        # split on commas or whitespace
        topics_list = re.split(r"[,\s]+", topics_str.strip())
    else:
        topics_list = []

    topics_list = [t.lower() for t in topics_list if t]

    # join all topics into a single searchable blob for substring/phrase matches
    topic_blob = " ".join(topics_list)

    raw_scores = defaultdict(int)

    for genre, keywords in GENRE_KEYWORDS.items():
        for kw in keywords:
            kw_l = kw.lower()

            # If keyword is multiple words ("neural network"),
            # do substring search on the blob.
            # If it's a single token ("ros2"), also check exact topic match.
            if " " in kw_l:
                if kw_l in topic_blob:
                    raw_scores[genre] += 1
            else:
                # exact match in topics OR substring in blob
                if kw_l in topics_list or kw_l in topic_blob:
                    raw_scores[genre] += 1

    # normalize scores 0..1 per repo so the highest genre = 1.0
    if raw_scores:
        max_score = max(raw_scores.values())
        if max_score == 0:
            norm_scores = {g: 0.0 for g in GENRE_KEYWORDS.keys()}
        else:
            norm_scores = {
                g: (raw_scores.get(g, 0) / max_score)
                for g in GENRE_KEYWORDS.keys()
            }
    else:
        norm_scores = {g: 0.0 for g in GENRE_KEYWORDS.keys()}

    return norm_scores

def get_repo_readme(owner, repo, use_creds=False):
    #fetch github repo
    url = f"https://api.github.com/repos/{owner}/{repo}/readme"
    #get readme if it exists
    if use_creds:
        r = gh_get(url)
    else:
        r = requests.get(url, headers={"Accept": "application/vnd.github.v3+json"})
        
    if r.status_code != 200:
        return ""
    data = r.json()
    if "content" in data and data.get("encoding") == "base64":
        return base64.b64decode(data["content"]).decode("utf-8", errors="ignore")
    return ""

def get_repo_file_tree(owner, repo, use_creds=False):
    # recursive=1 gives the whole tree (paths only, not contents) for default branch
    url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/HEAD?recursive=1"
    if use_creds:
        r = gh_get(url)
    else:
        r = requests.get(url)
    if r.status_code != 200:
        return []
    data = r.json()
    tree = data.get("tree", [])
    return [item["path"] for item in tree if item["type"] == "blob"]

def score_genres(text_blob, file_paths):
    genre_scores = defaultdict(int)

    # Lowercase once
    blob = (text_blob + "\n" + "\n".join(file_paths)).lower()

    for genre, keywords in GENRE_KEYWORDS.items():
        for kw in keywords:
            # simple keyword frequency
            hits = len(re.findall(r"\b" + re.escape(kw.lower()) + r"\b", blob))
            genre_scores[genre] += hits

    return dict(genre_scores)


def normalize_scores(raw_scores):
    # avoid divide-by-zero
    if not raw_scores:
        return {}
    max_score = max(raw_scores.values()) or 1
    return {genre: score / max_score for genre, score in raw_scores.items()}

def classify_repo(owner_repo, use_creds=False):
    owner, repo = owner_repo.split("/", 1)

    readme_text = get_repo_readme(owner, repo, use_creds)
    file_paths = get_repo_file_tree(owner, repo, use_creds)

    print("DEBUG", owner_repo)
    print("  readme_len:", len(readme_text))
    print("  num_file_paths:", len(file_paths))

    raw_scores = score_genres(readme_text, file_paths)
    norm_scores = normalize_scores(raw_scores)

    # Pick top genre
    top_genre = max(norm_scores, key=norm_scores.get) if norm_scores else None

    return {
        "repo": owner_repo,
        "top_genre": top_genre,
        "scores": norm_scores,
        "debug": {
            "readme_len_chars": len(readme_text),
            "num_files_seen": len(file_paths),
        },
    }

def main():
    df = pd.read_csv("combined.csv")
    repo_name = "iam-veeramalla/aws-devops-zero-to-hero"
    result = classify_repo(repo_name, use_creds=True)
    print(repo_name)
    print(result["top_genre"])
    print(result["scores"])
    


if __name__ == "__main__":
    main()


