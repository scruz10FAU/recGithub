import pandas as pd

csv = "combined.csv"
df = pd.read_csv(csv)
score_cols = [
    "AI / Data / ML", "Systems / Embedded / Robotics", "Web / Mobile / Application Development", 
    "DevOps / Infrastructure / Cloud", "Security / Networking", "Data Platforms / Backend Services / Integrations", 
    "CLI / Utilities / Developer Tools", "Libraries / SDKs / Framework Components", "Research / Experiments / Demos", 
    "Education / Tutorials / Docs"
    ]

zero_mask = (df[score_cols] == 0).all(axis=1)

repos_all_zero = df.loc[zero_mask, "Repository Name"]
print(repos_all_zero.tolist())
