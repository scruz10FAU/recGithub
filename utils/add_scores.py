from score_repos import classify_repo
from utils import score_repo_from_topics
from get_empty import get_empty_genres
import pandas as pd
import os
import re
from collections import defaultdict
import argparse


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
    if empty_only:
        empty_repos = get_empty_genres(csv_file)
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
            if ((idx+1) % 10 == 0 or idx+1 == len(df)) and not empty_only:
                #print update after every 10 repos are completed
                print(f"Completed {idx+1}/{len(df)}")
            if empty_only:
                #print update for every empty row completed
                index = empty_repos.index(repo_name)
                print(f"Completed {index+1}/{len(empty_repos)} of empty rows")


        df.to_csv(csv_file, index=False)
    else:
        print("File does not exist")
        return None



def main():
    parser = argparse.ArgumentParser(
        prog = "score repos from csv file",
        description = "score repositories in a csv file"
    )
    parser.add_argument("--empty_only", "-e", action="store_true", help="Only update empty rows in csv")
    parser.add_argument("--csv_file", "-c", type=str, default="assets/combined.csv", help="Enter csv file to use for program")
    args = parser.parse_args()
    add_genre_scores(args.csv_file, empty_only = args.empty_only)


if __name__ == "__main__":
    main()
