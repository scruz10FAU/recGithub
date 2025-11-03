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
    

def main():
    #get csv file
    df = pd.read_csv("combined.csv")
    #Choose 3 repo names randomly for recommendation
    rec_input = []
    ratings = []
    print("Welcome to the repository recommendation system.")
    print("Based on your preferences, This program will recommend a repository for you to explore.")
    num_recs = int(input("Number of repos to recommended: "))
    choose_repo = input("Enter repos you like (else random)? Enter y or n: ")
    rate_repos = input("Do you want to rate repos? Enter y or n: ")
    if choose_repo == "y":
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
        if rate_repos == "y":
            for rec in rec_input:
                rating = int(input(f"Enter a rating score from 1-10 for the repo {rec}: "))
                ratings.append(rating)
        else:
            ratings=None

    
    #ratings = None
    #rec_input = ["scruz10FAU/ShellHacks2025", "k2-fsa/sherpa-onnx", "dyad-sh/dyad"]
    print(rec_input)
    scores = get_repo_scores(df.copy(), rec_input, ratings=ratings)
    print(scores)
    get_recs = add_user_match_score(df.copy(), scores, rec_input)
    df_recs = get_recs[0].head(num_recs)
    rec_names = df_recs["Repository Name"].tolist()
    rec_scores = df_recs["user_match_score"].tolist()
    print(f"Your recommendations are {rec_names}, {rec_scores}")

    plot_scores_dist(rec_input, scores, ratings=ratings, recs=rec_names)

if __name__ == "__main__":
    main()



