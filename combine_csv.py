import os
import pandas as pd

def combine_csv(csv_list, output_csv):
    df = None
    for csv in csv_list:
        if os.path.exists(csv):
            new_df = pd.read_csv(csv)
            key_col = new_df.columns[1]
            if df is not None:
                df = pd.concat([df, new_df], ignore_index=True)
                df = df.drop_duplicates(subset=[key_col], keep="last")
            else:
                df = new_df

    
    df.to_csv(output_csv, index=False)

def main():
    csv_files = ["trending.csv", "trending_month.csv", "trending_week.csv", "explore.csv"]
    combine_csv(csv_files, "combined.csv")

if __name__ == "__main__":
    main()


