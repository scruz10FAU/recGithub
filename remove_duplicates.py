import pandas as pd

df = pd.read_csv("combined.csv")

# drop duplicate repos, keep the first time we saw each repo
df = df.drop_duplicates(subset=["Repository Name"], keep="first")

df.to_csv("combined.csv", index=False)
