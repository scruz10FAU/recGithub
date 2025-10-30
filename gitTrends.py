import requests
from bs4 import BeautifulSoup
import pandas as pd
import argparse
import os

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
        
def get_topics(url):
    if url:
        # Ensure the link is complete (add base URL if necessary, e.g., for GitHub)
        base_url = "https://github.com"  # Adjust if you're scraping a different site
        full_url = base_url + url if not url.startswith('http') else url
        
        # Make a request to the repository page
        try:
            response = requests.get(full_url)
            
            response.raise_for_status()  # Check for HTTP errors
            repo_soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract topics (GitHub topics are typically in <a> tags with class 'topic-tag')
            topics = repo_soup.select('a.topic-tag')
            #print(f"topics: {topics}")
            return [topic.text.strip() for topic in topics] if topics else ["No topics"]
            
        except requests.RequestException as e:
            print(f"Error fetching {full_url}: {e}")
            return ["Error fetching topics"]
    else:
        return ["No topics found"]


def transform(repos_html, page_type="explore"):
    result=[]
    for r in repos_html:
        try:
            language = r.select_one('span[itemprop="programmingLanguage"]').text.strip() if r.select_one('span[itemprop="programmingLanguage"]') else "Unknown"
            if page_type == "explore":
                number_of_stars = convert_number(r.select_one('span.Counter.js-social-count').text.strip())
                topics = [a.get_text(strip=True) for a in r.select('a[href^="/topics/"]')]
                repository_name = ''.join(r.select_one('h3').text.split())
                result.append({'Repository Name': repository_name, 'Number of Stars': number_of_stars, 'Language': language, 'Topics': topics})
            else:

                number_of_stars = ''.join(r.select_one('a[href$="/stargazers"]').text.split())
                number_of_stars = int(number_of_stars.replace(",",""))
                stars_today = ''.join(r.select_one('span.float-sm-right').text.split())
                stars_today = stars_today.replace(f"stars{page_type}", "")
                stars_today = int(stars_today.replace(",", ""))
                forks = ''.join(r.select_one('a[href$="/forks"]').text.split())
                forks = int(forks.replace(",",""))
                repository_name = ''.join(r.select_one('h2').text.split()) 
                developer_name = r.select_one('img.avatar.mb-1.avatar-user')['alt']
                try:
                    repo_link = r.select_one('h2 a')['href'] if r.select_one('h2 a') else None
                    topics = get_topics(repo_link)
                except Exception as e:
                    print(f"Error getting repo link topics: {e}")
                    topics = None
                result.append({'Developer': developer_name, 'Repository Name': repository_name, 'Number of Stars': number_of_stars, 'Forks': forks, 'Stars Today': stars_today, 'Language': language, 'Topics': topics})
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

def upsert_csv(repository_data, filename):
    new_df = pd.DataFrame(repository_data)

    if os.path.exists(filename):
        existing_df = pd.read_csv(filename)
        key_col = existing_df.columns[1]
        print(key_col)
        combined = pd.concat([existing_df, new_df], ignore_index=True)
        # keep the last occurrence of each key (new data wins)
        combined = combined.drop_duplicates(subset=[key_col], keep="last")
    else:
        combined = new_df

    combined.to_csv(filename, index=False)



def main(url, page_type, outputcsv): 
    #url = "https://github.com/trending"
    #url = "https://github.com/trending?since=monthly"
    #url = "https://github.com/trending?since=weekly"
    #url = "https://github.com/explore"
    page = request_github_tranding(url)
    repos_html = extract(page)
    #print(repos_html)
    #types for transfom: 'explore', 'today', 'thisweek', 'thismonth'
    repo_data = transform(repos_html, page_type)
    #print(repo_data)
    print(format(repo_data))
    #out_to_csv(repo_data, outputcsv)
    upsert_csv(repo_data, outputcsv)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='Scrape Github',
                    description='scrapes github repos for information'
                    )
    
    parser.add_argument("-w", action="store_const", const="thisweek", dest="page", help="Set page to this week")
    parser.add_argument("-t", action="store_const", const="today", dest="page", help="Set page to today")
    parser.add_argument("-m", action="store_const", const="thismonth", dest="page", help="Set page to this month")
    parser.add_argument("-e", action="store_const", const="explore", dest="page", help="Set page to explore")
    parser.set_defaults(page="explore")

    args = parser.parse_args()
    match args.page:
        case "thisweek":
            output = "trending_week.csv"
            url = "https://github.com/trending?since=weekly"
        case "thismonth":
            output = "trending_month.csv"
            url = "https://github.com/trending?since=monthly"
        case "today":
            output = "trending.csv"
            url = "https://github.com/trending"
        case _:
            output = "explore.csv"
            url = "https://github.com/explore"

    print(url, args.page, output)
    
    main(url, args.page, output)
