import requests
from bs4 import BeautifulSoup
import pandas as pd

def request_github_tranding(url):
    return requests.get(url).text

def extract(page):
    soup = BeautifulSoup(page, 'html.parser')
    return soup.find_all('article')

def transform(repos_html):
    result=[]
    for r in repos_html:
        number_of_stars = ''.join(r.select_one('a[href$="/stargazers"]').text.split())
        number_of_stars = int(number_of_stars.replace(",",""))
        stars_today = ''.join(r.select_one('span.float-sm-right').text.split())
        stars_today = stars_today.replace("starstoday", "")
        stars_today = int(stars_today.replace(",", ""))
        forks = ''.join(r.select_one('a[href$="/forks"]').text.split())
        forks = int(forks.replace(",",""))
        repository_name = ''.join(r.select_one('h2').text.split()) 
        developer_name = r.select_one('img.avatar.mb-1.avatar-user')['alt']
        language = r.select_one('span[itemprop="programmingLanguage"]').text.strip() if r.select_one('span[itemprop="programmingLanguage"]') else "Unknown"
        result.append({'Developer': developer_name, 'Repository Name': repository_name, 'Number of Stars': number_of_stars, 'Forks': forks, 'Stars Today': stars_today, 'Language': language})
    return result

def format(repositories_data):
    columns = ['Developer, Repository_ame, Number of Stars', 'Forks', 'Stars Today', 'Language']
    for repository in repositories_data:
        r = [repository['Developer'], repository['Repository Name'], str(repository['Number of Stars']), str(repository['Forks']), str(repository['Stars Today']), repository['Language']]
        columns.append(','.join(r))
    return '\n'.join(columns) 

def out_to_csv(repository_data, filename):
    df = pd.DataFrame(repository_data)
    df.to_csv(filename, index=False)


def main():
    url = "https://github.com/trending"
    page = request_github_tranding(url)
    repos_html = extract(page)
    #print(repos_html)
    repo_data = transform(repos_html)
    #print(repo_data)
    print(format(repo_data))
    out_to_csv(repo_data, "trending.csv")

if __name__ == "__main__":
    main()
