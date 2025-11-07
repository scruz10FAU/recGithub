import pandas as pd
from utils.utils import get_repo_scores, add_user_match_score, plot_scores_dist, get_starred_repos, error_check
import random


def main():
    #get csv file
    df = pd.read_csv("assets/combined1.csv")
    #Choose 3 repo names randomly for recommendation
    rec_input = []
    ratings = []
    print("Welcome to the repository recommendation system.")
    print("Based on your preferences, This program will recommend a repository for you to explore.")
    github_username = input("What is your github username?: ")
    num_recs = input("Number of repos to recommended: ")
    num_recs = error_check(num_recs, user_type="int", user_min=1, user_max=10)
    choose_repo = input("Choose input mode. Enter r for random, i for custom input, s for starred: ")
    choose_repo = error_check(choose_repo, ["r", "i", "s"])
    rate_repos = input("Do you want to rate repos? Enter y or n: ")
    rate_repos = error_check(rate_repos, choices=["y", "n"])
    if choose_repo == "i":
        num_repos = input("Number of repos to input: ")
        num_repos = error_check(num_repos, user_type="int", user_min=1, user_max=10)
        print(f"You will enter {num_repos}")

        for i in range(num_repos):
            repo = input("Enter repo in the form 'x/y': ")
            repo = error_check(repo, user_type="repo")
            rec_input.append(repo)
            if rate_repos == "y":
                rating = input("Enter a rating score from 1-10: ")
                rating = error_check(rating, user_type="int", user_min=1, user_max=10)
                ratings.append(rating)
        if rate_repos != "y":
            ratings = None
    else:
        if choose_repo=="s":
            repo_list = get_starred_repos(github_username)
            if len(repo_list) > 10:
                #get random sample from list if list is too long (limited to 10)
                repo_list = random.sample(repo_list, 10)
            rec_input = [item['name'] for item in repo_list]
        else:
            rec_input = df.sample(n=3)["Repository Name"].to_list()
        if rate_repos == "y":
            for rec in rec_input:
                rating = input(f"Enter a rating score from 1-10 for the repo {rec}: ")
                rating = error_check(rating, user_type="int", user_min=1, user_max=10)
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



