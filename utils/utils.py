import pandas as pd
import os
import re
from collections import defaultdict
import requests
import base64
import pandas as pd
import numpy as np
from utils.genre_keywords import GENRE_KEYWORDS
from dotenv import load_dotenv
from utils.genre_keywords import score_cols
import matplotlib.pyplot as plt
import sys

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # put your PAT in env var
#print("Token loaded?", bool(GITHUB_TOKEN))


def gh_get(url, accept="application/vnd.github.v3+json"):
    headers = {"Accept": accept}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"  # or "token ..."
    r = requests.get(url, headers=headers)
    return r

def get_starred_repos(username, token=None):
    """
    Get all starred repositories for a GitHub user.
    
    Args:
        username: GitHub username
        token: Personal access token (optional, but recommended for higher rate limits)
    """
    headers = {}
    if token:
        headers['Authorization'] = f'token {token}'
    
    starred_repos = []
    page = 1
    
    while True:
        url = f'https://api.github.com/users/{username}/starred'
        params = {'page': page, 'per_page': 100}
        
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            print(response.json())
            break
        
        repos = response.json()
        
        if not repos:
            break
        
        for repo in repos:
            starred_repos.append({
                'name': repo['full_name'],
                'url': repo['html_url'],
                'description': repo['description'],
                'stars': repo['stargazers_count'],
                'language': repo['language'],
                'updated_at': repo['updated_at']
            })
        
        page += 1
    
    return starred_repos

def score_repo_from_topics(topics_str, normalize=False):
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
    if normalize:
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
    if raw_scores:
        return raw_scores
    else:
        return {g: 0.0 for g in GENRE_KEYWORDS.keys()}

def get_repo_readme(owner, repo, use_creds=False):
    #fetch github repo
    url = f"https://api.github.com/repos/{owner}/{repo}/readme"
    #get readme if it exists
    if use_creds:
        r = gh_get(url)
    else:
        r = requests.get(url, headers={"Accept": "application/vnd.github.v3+json"})
    if r.status_code != 200:
        print("WARN readme", url, r.status_code, r.text[:120])
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
        print("WARN tree", url, r.status_code, r.text[:120])
        return []
    data = r.json()
    tree = data.get("tree", [])
    return [item["path"] for item in tree if item["type"] == "blob"]

def error_check(user_input, choices=["y", "n"], user_type="str", user_min=0, user_max=10, tries=3):
    attempt = 0
    while attempt < tries:
        if user_type == "str":
            user_input = user_input.lower()
            if user_input in choices:
                return user_input
            else:
                user_input = input(f"Select an option from {choices}: ")
                attempt += 1
        elif user_type == "int":
            if user_input.isnumeric():
                user_input = int(user_input)
                if user_min <= user_input <= user_max:
                    return user_input
                else:
                    user_input = input(f"Enter an integer between {user_min} and {user_max}: ")
                    attempt+=1
            else:
                user_input = input(f"Enter an integer between {user_min} and {user_max}: ")
                attempt += 1
        elif user_type == "repo":
            pattern = r"^[^/]*\/[^/]*$"
            if bool(re.fullmatch(pattern, user_input)):
                return user_input
            else:
                user_input = input("Enter repos in the form 'x/y': ")
                attempt+=1

    print("Invalid input. Ending program.....")
    sys.exit(1)
            


    

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

def classify_repo(owner_repo, use_creds=False, normalize=False):
    owner, repo = owner_repo.split("/", 1)

    readme_text = get_repo_readme(owner, repo, use_creds)
    file_paths = get_repo_file_tree(owner, repo, use_creds)

    #print("DEBUG", owner_repo)
    #print("  readme_len:", len(readme_text))
    #print("  num_file_paths:", len(file_paths))

    raw_scores = score_genres(readme_text, file_paths)
    if normalize:
        norm_scores = normalize_scores(raw_scores)
    else:
        norm_scores = raw_scores


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

def blend_scores(content_scores, topic_scores, alpha=0.7, normalized=False):
    # ensure every genre exists in both dicts
    final = {}
    for genre in content_scores.keys():
        c = content_scores.get(genre, 0.0)
        t = topic_scores.get(genre, 0.0)
        if normalized:
            if c > 0 and t > 0:
                final[genre] = alpha * c + (1 - alpha) * t
            else:
                final[genre] = max(c, t)
            return final
        else:
            final[genre] = c + t
    if not normalized:
        max_val = max(final.values())
        return {genre: val / max_val for genre, val in final.items()}

def add_genre_scores(csv_file, alpha=0.5, empty_only=False):
    empty_repos = ['karpathy/micrograd', 'nitrojs/nitro', 'QwenLM/Qwen3-VL', 'allenai/olmocr', 'TheRobotStudio/SO-ARM100', 'anthropics/claude-cookbooks', 'allenai/olmocr', 'iam-veeramalla/aws-devops-zero-to-hero'] 
    if os.path.exists(csv_file):
        df = pd.read_csv(csv_file)
        for idx, row in df.iterrows():
            #row = df.iloc[1]
            #if True:
            repo_name = row["Repository Name"]
            if empty_only and repo_name not in empty_repos:
                continue
            topics = row["Topics"]
            feature_dict = classify_repo(repo_name, use_creds=True)['scores']
            topics_dict = score_repo_from_topics(topics)
            #print(feature_dict)
            #print(topics_dict)
            combined_dict = blend_scores(feature_dict, topics_dict, alpha)
            #debugging 
            if max(combined_dict.values()) == 0:
                print(f"No scores for {repo_name}")
                print(f"feature_dict: {feature_dict}")
                print(f"topics_dict: {topics_dict}")
                print(f"combined_dict: {combined_dict}")
            #print(combined_dict)
            for col, val in combined_dict.items():
                if col not in df.columns:
                    df[col] = None
                
                df.at[idx, col] = val
            if (idx+1) % 10 == 0 or idx+1 == len(df):
                print(f"Completed {idx+1}/{len(df)}")


        df.to_csv(csv_file, index=False)
    else:
        print("File does not exist")
        return None
    

def get_top_scores(csv_file):
    df = pd.read_csv(csv_file)
    #get top score for each row
    df["top_genre"] = df[score_cols].idxmax(axis=1)
    #count how many times each genre is a max
    win_counts = df["top_genre"].value_counts()
    return win_counts

def plot_max_scores(csv_file):
    counts = get_top_scores(csv_file)
    pretty_index = [label.replace(" / ", "\n") for label in counts.index]

    plt.figure(figsize=(10,6))
    plt.bar(pretty_index, counts.values)
    plt.xlabel("Genre")
    plt.ylabel("Number of repos where this is top genre")
    plt.title("Top Genre Frequency Across Repos")
    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()
    plt.show()

def add_top_scores(csv_file):
    df = pd.read_csv(csv_file)
    df["top_genre"] = df[score_cols].idxmax(axis=1)
    df.to_csv(csv_file)



def fill_missing_items(df, missing_list):
    df_new = df.copy()
    for repo_name in missing_list:
        repo_dict = {"Repository Name": repo_name}
        feature_dict = classify_repo(repo_name, use_creds=True, normalize=True)['scores']
        for col, val in feature_dict.items():
            repo_dict[col] = val
        df_new = pd.concat([df_new, pd.DataFrame([repo_dict])], ignore_index=True)
        print(f"added scores for {repo_name}")
        print(repo_dict)

    return df_new



def get_repo_scores(df, repo_list, ratings=None):
    #get rows from dataframe with scores
    missing_from_df = [item for item in repo_list if item not in df['Repository Name'].values]
    if len(missing_from_df) > 0:
        df = fill_missing_items(df.copy(), missing_from_df)

    selected_rows = df.loc[df['Repository Name'].isin(repo_list)]
    #sum the scores for each genre for chosen items
    if ratings is not None:
        ratings = np.array(ratings)
        weighted_scores = selected_rows[score_cols].mul(ratings, axis=0)
        total_scores = weighted_scores.sum()
    else:
        total_scores = selected_rows[score_cols].sum()

    print(total_scores)
    max_val = max(total_scores)
    return {genre: val / max_val for genre, val in total_scores.items()}

def plot_scores_dist(repos, scores, ratings=None, recs=None):
    pretty_index = [label.replace(" / ", "\n") for label in scores.keys()]
    repo_label = ""
    print(repos)
    for idx, item in enumerate(repos):
        repo_label += "\n" + item 
        if ratings is not None:
            repo_label += ": " + str(ratings[idx])
    weights_string = ""
    if ratings is not None:
        weights_string += "with weights"
    
    fig, ax = plt.subplots()
    
        
        
    ax.bar(pretty_index, scores.values())
    ax.set_xlabel("Genre")
    ax.set_ylabel("Genre Weight Based on Selection")
    ax.set_title(f"Weight of Each Genre Based on Repos Selected {weights_string} {repo_label}")
    ax.set_xticklabels(pretty_index, rotation=45, ha="right", fontsize=8, linespacing=1)
    fig.set_size_inches(8, 6)     # wider figure
    fig.subplots_adjust(bottom=0.28)  # extra bottom margin for labels
    
    if recs is not None:
        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width * 0.95, box.height])
        rec_text = "Your recommendations are: "
        for rec in recs:
            rec_text += "\n " + str(rec)
        ax.text(
            1.02, 0.5,
            rec_text,
            transform=ax.transAxes,
            ha="left",
            va="center",
            fontsize=10
        )

    plt.tight_layout()
    plt.show()
    


def add_user_match_score(df, weight_dict, input_repos, repo_col="Repository Name"):
    #remove input from repo list
    df = df.copy()
    mask = ~df[repo_col].isin(input_repos)
    df = df[mask]

    # genres we will actually use = intersection of df columns and weight_dict keys
    genre_cols = [g for g in weight_dict.keys() if g in df.columns]

    # build weight vector aligned with genre_cols
    w = np.array([weight_dict[g] for g in genre_cols])

    # matrix of repo scores for those genres
    M = df[genre_cols].values  # shape: (num_repos, num_genres)

    #weighted dot product per repo added to dataframe
    df["user_match_score"] = M.dot(w)

    # sort best -> worst
    df_sorted = df.sort_values("user_match_score", ascending=False)

    return df_sorted, genre_cols