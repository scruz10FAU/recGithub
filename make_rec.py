import pandas as pd
from utils.utils import classify_repo, score_repo_from_topics, normalize_scores, blend_scores
from utils.utils import get_repo_scores, add_user_match_score, plot_scores_dist, get_starred_repos

def main():
    #get csv file
    df = pd.read_csv("assets/combined.csv")
    #Choose 3 repo names randomly for recommendation
    rec_input = []
    ratings = []
    print("Welcome to the repository recommendation system.")
    print("Based on your preferences, This program will recommend a repository for you to explore.")
    github_username = input("What is your github username?: ")
    github_token = input("Enter github token: ")
    print(github_token)
    num_recs = int(input("Number of repos to recommended: "))
    choose_repo = input("Enter repos you like (else random or starred)? Enter y or n: ")
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
        star_input = input("Would you like to use repos you starred (else random)? Enter y or n: ")
        if star_input == "y":

            repo_list = get_starred_repos(github_username)
            rec_input = [item['name'] for item in repo_list]
        else:
            rec_input = df.sample(n=3)["Repository Name"].to_list()
        if rate_repos == "y":
            for rec in rec_input:
                rating = int(input(f"Enter a rating score from 1-10 for the repo {rec}: "))
                ratings.append(rating)
        else:
            ratings=None


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



