import pandas as pd
from genre_keywords import score_cols
import matplotlib.pyplot as plt

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



plot_max_scores("combined.csv")
add_top_scores("combined.csv")

