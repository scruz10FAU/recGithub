from score_repos import classify_repo, score_repo_from_topics
import pandas as pd
import os
import re
from collections import defaultdict


def blend_scores(content_scores, topic_scores, alpha=0.7):
    # ensure every genre exists in both dicts
    final = {}
    for genre in content_scores.keys():
        c = content_scores.get(genre, 0.0)
        t = topic_scores.get(genre, 0.0)
        final[genre] = alpha * c + (1 - alpha) * t
    return final

def add_genre_scores(csv_file, alpha=0.7):
    if os.path.exists(csv_file):
        df = pd.read_csv(csv_file)
        for idx, row in df.iterrows():
            #row = df.iloc[1]
            #if True:
            repo_name = row["Repository Name"]
            topics = row["Topics"]
            feature_dict = classify_repo(repo_name)['scores']
            topics_dict = score_repo_from_topics(topics)
            #print(feature_dict)
            #print(topics_dict)
            combined_dict = blend_scores(feature_dict, topics_dict, alpha)
            #print(combined_dict)
            for col, val in combined_dict.items():
                if col not in df.columns:
                    df[col] = None
                
                df.at[idx, col] = val
            if idx % 10 == 0 or idx == len(df):
                print(f"Completed {idx}/{len(df)}")


        df.to_csv(csv_file)
    else:
        print("File does not exist")
        return None



def main():

    add_genre_scores("combined.csv")


if __name__ == "__main__":
    main()