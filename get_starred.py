import requests
import json
import os
import argparse
from dotenv import load_dotenv
load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # put your PAT in env var

def get_starred_repos(username, token=GITHUB_TOKEN):
    """
    Get all starred repositories for a GitHub user.
    
    Args:
        username: GitHub username
        token: Personal access token (optional, but recommended for higher rate limits)
    """
    headers = {}
    if token:
        headers['Authorization'] = f'token {token}'
    
    starred_repos = []
    page = 1
    
    while True:
        url = f'https://api.github.com/users/{username}/starred'
        params = {'page': page, 'per_page': 100}
        
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            print(response.json())
            break
        
        repos = response.json()
        
        if not repos:
            break
        
        for repo in repos:
            starred_repos.append({
                'name': repo['full_name'],
                'url': repo['html_url'],
                'description': repo['description'],
                'stars': repo['stargazers_count'],
                'language': repo['language'],
                'updated_at': repo['updated_at']
            })
        
        page += 1
    
    return starred_repos

def main(username, token):

    repos = get_starred_repos(username, token)
    repo_list = []

    print(f"Found {len(repos)} starred repositories:\n")
    for repo in repos[:10]:  # Show first 10
        print(f"{repo['name']}")
        print(f"  URL: {repo['url']}")
        print(f"  Stars: {repo['stars']}")
        print(f"  Language: {repo['language']}\n")
        repo_list.append(repo['name'])
    print(repo_list)
    # Save to JSON
    #with open('starred_repos.json', 'w') as f:
    #    json.dump(repos, f, indent=2)

    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                prog='Get Starred repos',
                description='scrapes github starred page to get list of starred repos'
                )
    username = 'scruz10FAU'
    token = GITHUB_TOKEN  # Optional but recommended
    parser.add_argument("--username", "-u", type=str, default=username, help="Your username")
    parser.add_argument("--token", "-t", default=token, type=str, help="Enter github token")
    args = parser.parse_args()

    main(args.username, args.token)

    