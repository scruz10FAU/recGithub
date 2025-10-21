import requests
from bs4 import BeautifulSoup
import pandas as pd

def request_github_tranding(url):
    return requests.get(url).text

def extract(page):
    soup = BeautifulSoup(page, 'html.parser')
    return soup.find_all('article')

def convert_number(string):
    if "k" in string:
        base = float(string.replace("k", ""))
        return int(base*1000)
    elif "M" in string:
        base = float(string.replace("M", ""))
        return int(base*1000000)
    else:
        try:
            return int(string)
        except:
            print(f"Unable to convert number {string}")
            return 0

def transform(repos_html):
    result=[]
    for r in repos_html:
        try:
            #number_of_stars = ''.join(r.select_one('a[href$="/stargazers"]').text.split())
            number_of_stars = convert_number(r.select_one('span.Counter.js-social-count').text.strip())

            #number_of_stars = ''.join(r.select_one('span.repo-stars-counter-star').text.split())
            #number_of_stars = 0
            #number_of_stars = int(number_of_stars.replace(",",""))
            topics = [a.get_text(strip=True) for a in r.select('a[href^="/topics/"]')]
            #print(topics)
            #stars_today = ''.join(r.select_one('span.float-sm-right').text.split())
            #stars_today = stars_today.replace("starstoday", "")
            #stars_today = stars_today.replace("starsthismonth", "")
            #stars_today = stars_today.replace("starsthisweek", "")
            #stars_today = int(stars_today.replace(",", ""))
            #forks = ''.join(r.select_one('a[href$="/forks"]').text.split())
            #forks = int(forks.replace(",",""))
            #repository_name = ''.join(r.select_one('h2').text.split()) 
            repository_name = ''.join(r.select_one('h3').text.split()) 
            #developer_name = r.select_one('img.avatar.mb-1.avatar-user')['alt']
            language = r.select_one('span[itemprop="programmingLanguage"]').text.strip() if r.select_one('span[itemprop="programmingLanguage"]') else "Unknown"
            #result.append({'Developer': developer_name, 'Repository Name': repository_name, 'Number of Stars': number_of_stars, 'Forks': forks, 'Stars Today': stars_today, 'Language': language})
            result.append({'Repository Name': repository_name, 'Number of Stars': number_of_stars, 'Language': language, 'Topics': topics})
        except Exception as e:
            print(f"Error processing result due to {e}.")
    return result

def format(repositories_data):
    #columns = ['Developer, Repository_name, Number of Stars', 'Forks', 'Stars Today', 'Language']
    columns = []
    columns = [','.join(list(repositories_data[0].keys()))]
    cols_for_processing = list(repositories_data[0].keys())
    #print(cols_for_processing)
    for repository in repositories_data:
        r = []
        for col in cols_for_processing:
            r.append(str(repository[col]))
        #r = [repository['Developer'], repository['Repository Name'], str(repository['Number of Stars']), str(repository['Forks']), str(repository['Stars Today']), repository['Language']]
        columns.append(','.join(r))
    return '\n'.join(columns) 

def out_to_csv(repository_data, filename):
    df = pd.DataFrame(repository_data)
    df.to_csv(filename, index=False)


def main():
    url = "https://github.com/trending"
    url = "https://github.com/trending?since=monthly"
    url = "https://github.com/trending?since=weekly"
    url = "https://github.com/explore"
    page = request_github_tranding(url)
    repos_html = extract(page)
    #print(repos_html)
    repo_data = transform(repos_html)
    #print(repo_data)
    print(format(repo_data))
    out_to_csv(repo_data, "explore.csv")

if __name__ == "__main__":
    main()
