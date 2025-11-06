import requests
from bs4 import BeautifulSoup
import pandas as pd
import argparse
import os

def request_github_tranding(url):
    #get text from webpage
    return requests.get(url).text

def extract(page):
    #get page data using beautiful soup
    soup = BeautifulSoup(page, 'html.parser')
    return soup.find_all('article')

def convert_number(string):
    #convert numbers that use k or M to integers
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
    #create an empty list for the results
    result=[]
    #loop through thelines of the html file
    for r in repos_html:
        try:
            #get the programming language
            language = r.select_one('span[itemprop="programmingLanguage"]').text.strip() if r.select_one('span[itemprop="programmingLanguage"]') else "Unknown"
            #use explore page data to create columns for pandas dataframe
            if page_type == "explore":
                number_of_stars = convert_number(r.select_one('span.Counter.js-social-count').text.strip())
                topics = [a.get_text(strip=True) for a in r.select('a[href^="/topics/"]')]
                repository_name = ''.join(r.select_one('h3').text.split())
                result.append({'Repository Name': repository_name, 'Number of Stars': number_of_stars, 'Language': language, 'Topics': topics})
            else:
                #use the trending pages data to create columns for dataframe
                number_of_stars = ''.join(r.select_one('a[href$="/stargazers"]').text.split())
                number_of_stars = int(number_of_stars.replace(",",""))
                stars_today = ''.join(r.select_one('span.float-sm-right').text.split())
                stars_today = stars_today.replace(f"stars{page_type}", "")
                stars_today = int(stars_today.replace(",", ""))
                forks = ''.join(r.select_one('a[href$="/forks"]').text.split())
                forks = int(forks.replace(",",""))
                repository_name = ''.join(r.select_one('h2').text.split()) 
                developer_name = r.select_one('img.avatar.mb-1.avatar-user')['alt']
                #error handling for topics list
                try:
                    repo_link = r.select_one('h2 a')['href'] if r.select_one('h2 a') else None
                    topics = get_topics(repo_link)
                except Exception as e:
                    print(f"Error getting repo link topics: {e}")
                    topics = None
                result.append({'Developer': developer_name, 'Repository Name': repository_name, 'Number of Stars': number_of_stars, 'Forks': forks, 'Stars Today': stars_today, 'Language': language, 'Topics': topics})
        except Exception as e:
            #exception if the loop iteration has an error
            print(f"Error processing result due to {e}.")
    return result

def format(repositories_data):
    #columns = ['Developer, Repository_name, Number of Stars', 'Forks', 'Stars Today', 'Language']
    columns = []
    #format the info from the repository column as a string list
    columns = [','.join(list(repositories_data[0].keys()))]
    #get the row headers
    cols_for_processing = list(repositories_data[0].keys())
    #print(cols_for_processing)
    for repository in repositories_data:
        #create empty list
        r = []
        #add each column's data to the list
        for col in cols_for_processing:
            r.append(str(repository[col]))
        #r = [repository['Developer'], repository['Repository Name'], str(repository['Number of Stars']), str(repository['Forks']), str(repository['Stars Today']), repository['Language']]
        columns.append(','.join(r))
    return '\n'.join(columns) 

def out_to_csv(repository_data, filename):
    #create csv file from dataframe
    df = pd.DataFrame(repository_data)
    df.to_csv(filename, index=False)

def upsert_csv(repository_data, filename):
    new_df = pd.DataFrame(repository_data)

    if os.path.exists(filename):
        #convert existing csv to pandas dataframe
        existing_df = pd.read_csv(filename)
        #get the repository names from the first column
        key_col = existing_df.columns[1]
        #combine previous repo data with new repo data
        combined = pd.concat([existing_df, new_df], ignore_index=True)
        # keep the last occurrence of each key (new data wins)
        combined = combined.drop_duplicates(subset=[key_col], keep="last")
    else:
        #if there is no existing csv, create a new one
        combined = new_df

    combined.to_csv(filename, index=False)


def main(url, page_type, outputcsv): 
    #get the github page
    page = request_github_tranding(url)
    #extract info from the page
    repos_html = extract(page)
    #get the data from the repo
    repo_data = transform(repos_html, page_type)
    #add info to csv if it is not already there
    upsert_csv(repo_data, outputcsv)

if __name__ == "__main__":
    #create arg parser for command line
    parser = argparse.ArgumentParser(
                    prog='Scrape Github',
                    description='scrapes github repos for information'
                    )
    #create arguments for each website type
    parser.add_argument("-w", action="store_const", const="thisweek", dest="page", help="Set page to this week")
    parser.add_argument("-t", action="store_const", const="today", dest="page", help="Set page to today")
    parser.add_argument("-m", action="store_const", const="thismonth", dest="page", help="Set page to this month")
    parser.add_argument("-e", action="store_const", const="explore", dest="page", help="Set page to explore")
    parser.set_defaults(page="explore")

    args = parser.parse_args()
    #set output & url for each page type
    match args.page:
        case "thisweek":
            output = "assets/trending_week.csv"
            url = "https://github.com/trending?since=weekly"
        case "thismonth":
            output = "assets/trending_month.csv"
            url = "https://github.com/trending?since=monthly"
        case "today":
            output = "assets/trending.csv"
            url = "https://github.com/trending"
        case _:
            output = "assets/explore.csv"
            url = "https://github.com/explore"

    #run main function to extract info & write csv for pages
    main(url, args.page, output)
