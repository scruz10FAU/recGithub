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


def main():
    #url = "https://github.com/trending"
    #url = "https://github.com/trending?since=monthly"
    url = "https://github.com/trending?since=weekly"
    #url = "https://github.com/explore"
    page = request_github_tranding(url)
    repos_html = extract(page)
    #print(repos_html)
    #types for transfom: 'explore', 'today', 'thisweek', 'thismonth'
    repo_data = transform(repos_html, "thisweek")
    #print(repo_data)
    print(format(repo_data))
    out_to_csv(repo_data, "trending_week.csv")

if __name__ == "__main__":
    main()
