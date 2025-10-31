import random
import pandas as pd
from genre_keywords import score_cols
import matplotlib.pyplot as plt
import numpy as np
from score_repos import classify_repo, score_repo_from_topics, normalize_scores
from add_scores import blend_scores


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

def plot_scores_dist(repos, scores, ratings=None):
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

    plt.figure(figsize=(10,6))
    plt.bar(pretty_index, scores.values())
    plt.xlabel("Genre")
    plt.ylabel("Genre Weight Based on Selection")
    plt.title(f"Weight of Each Genre Based on Repos Selected {weights_string} {repo_label}")
    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()
    plt.show()
    

def main():
    #get csv file
    df = pd.read_csv("combined.csv")
    #Choose 3 repo names randomly for recommendation
    rec_input = []
    ratings = []
    choose_repo = input("Enter repos you like (else random)? Enter y or n: ")
    if choose_repo == "y":
        rate_repos = input("Do you want to rate repos? Enter y or n: ")
        num_repos = int(input("Number of repos to input: "))
        print(f"You will enter {num_repos}")

        for i in range(num_repos):
            repo = input("Enter repo in the form 'x/y': ")
            rec_input.append(repo)
            if rate_repos == "y":
                rating = int(input("Enter a rating score from 1-10: "))
                ratings.append(rating)
        if rate_repos != "y":
            ratings = None
    else:
        rec_input = df.sample(n=3)["Repository Name"].to_list()
        ratings=None

    
    #ratings = None
    #rec_input = ["scruz10FAU/ShellHacks2025", "k2-fsa/sherpa-onnx", "dyad-sh/dyad"]
    print(rec_input)
    scores = get_repo_scores(df, rec_input, ratings=ratings)
    print(scores)
    plot_scores_dist(rec_input, scores, ratings=ratings)

if __name__ == "__main__":
    main()



