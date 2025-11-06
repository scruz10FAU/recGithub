import pandas as pd
from genre_keywords import score_cols


def get_empty_genres(csv):
    df = pd.read_csv(csv)

    #get values
    vals = df[score_cols]

    #treat numeric-looking strings as numbers; non-numeric → NaN
    as_num = vals.apply(pd.to_numeric, errors="coerce")
    
    #build the mask
    zero_mask = (as_num.isna() | (as_num == 0)).all(axis=1)

    repos_all_zero = df.loc[zero_mask, "Repository Name"]
    return repos_all_zero.tolist()

if __name__ == "__main__":
    csv = "assets/combined.csv"
    print(get_empty_genres(csv))


