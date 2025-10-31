import random
import pandas as pd
from genre_keywords import score_cols
import matplotlib.pyplot as plt



def get_repo_scores(df, repo_list, rating=False):
    #get rows from dataframe with scores
    selected_rows = df.loc[df['Repository Name'].isin(repo_list)]
    #sum the scores for each genre for chosen items
    total_scores = selected_rows[score_cols].sum()
    print(total_scores)
    max_val = max(total_scores)
    return {genre: val / max_val for genre, val in total_scores.items()}

def plot_scores_dist(repos, scores):
    pretty_index = [label.replace(" / ", "\n") for label in scores.keys()]
    repo_label = ""
    print(repos)
    for item in repos:
        repo_label += "\n" + item 

    plt.figure(figsize=(10,6))
    plt.bar(pretty_index, scores.values())
    plt.xlabel("Genre")
    plt.ylabel("Genre Weight Based on Selection")
    plt.title(f"Weight of Each Genre Based on Repos Selected{repo_label}")
    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()
    plt.show()
    

def main():
    #get csv file
    df = pd.read_csv("combined.csv")
    #Choose 3 repo names randomly for recommendation
    rec_input = df.sample(n=3)["Repository Name"].to_list()
    print(rec_input)
    scores = get_repo_scores(df, rec_input)
    print(scores)
    plot_scores_dist(rec_input, scores)

if __name__ == "__main__":
    main()



