import pandas as pd
from genre_keywords import score_cols

csv = "combined.csv"
df = pd.read_csv(csv)

zero_mask = (df[score_cols] == 0).all(axis=1)

repos_all_zero = df.loc[zero_mask, "Repository Name"]
print(repos_all_zero.tolist())
