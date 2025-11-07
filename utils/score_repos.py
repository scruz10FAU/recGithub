from utils import classify_repo


def main():
    #df = pd.read_csv("combined.csv")
    repo_name = "iam-veeramalla/aws-devops-zero-to-hero"

    result = classify_repo(repo_name, use_creds=True, normalize=False)
    print(repo_name)

    print(result["top_genre"])
    print(result["scores"])
    


if __name__ == "__main__":
    main()


