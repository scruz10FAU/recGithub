import pandas as pd

df = pd.read_csv("assets/combined1.csv")

# drop duplicate repos, keep the first time we saw each repo
df = df.drop_duplicates(subset=["Repository Name"], keep="first")

df.to_csv("assets/combined1.csv", index=False)
