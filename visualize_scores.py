import pandas as pd
from genre_keywords import score_cols

def get_top_scores(csv_file):
    df = pd.read_csv(csv_file)
    #get repo name and scores only
    scores_df = df[["Repository Name"] + score_cols].copy()
    #get top score for each row
    df["top_genre"] = df[score_cols].idxmax(axis=1)
    #count how many times each genre is a max
    win_counts = df["top_genre"].value_counts()
    return win_counts



print(get_top_scores("combined.csv"))

