import requests
from bs4 import BeautifulSoup
import time
import random
import urllib.parse

def search_duckduckgo(query, num_results=10):
    """
    Searches DuckDuckGo for the given query and returns a list of result URLs.
    Note: DuckDuckGo might block frequent requests.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://duckduckgo.com/'
    }
    # Using the standard DuckDuckGo search URL instead of the HTML-only one,
    # though the HTML-only one is usually easier to scrape.
    url = f"https://duckduckgo.com/html/?q={urllib.parse.quote(query)}"

    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Failed to fetch DuckDuckGo: {response.status_code}")
            return []

        soup = BeautifulSoup(response.text, 'html.parser')

        links = []
        # In the HTML-only version, results are usually in 'result__a'
        for a in soup.find_all('a', class_='result__a', href=True):
            href = a['href']
            # DuckDuckGo sometimes encodes the real URL in a redirect
            if 'uddg=' in href:
                actual_url = urllib.parse.unquote(href.split('uddg=')[1].split('&')[0])
                links.append(actual_url)
            elif href.startswith('http') and 'duckduckgo.com' not in href:
                links.append(href)

            if len(links) >= num_results:
                break

        # If no results in 'result__a', try finding links in common result containers
        if not links:
             for a in soup.find_all('a', href=True):
                 href = a['href']
                 if 'http' in href and 'duckduckgo.com' not in href and 'google' not in href:
                     links.append(href)
                     if len(links) >= num_results:
                         break

        return links
    except Exception as e:
        print(f"Error searching DuckDuckGo: {e}")
        return []

def discover_leads(industries, locations=None):
    """
    Discovers potential leads based on industries and locations.
    """
    leads = []
    for industry in industries:
        query = industry
        if locations:
            for location in locations:
                full_query = f"{query} {location}"
                print(f"Searching for: {full_query}")
                urls = search_duckduckgo(full_query)
                for url in urls:
                    # Basic extraction of company name from URL if possible
                    name = url.split('//')[-1].split('/')[0].replace('www.', '')
                    leads.append({
                        'name': name,
                        'website': url,
                        'industry': industry,
                        'location': location
                    })
                time.sleep(random.uniform(2, 5)) # Polite delay
        else:
            print(f"Searching for: {query}")
            urls = search_duckduckgo(query)
            for url in urls:
                name = url.split('//')[-1].split('/')[0].replace('www.', '')
                leads.append({
                    'name': name,
                    'website': url,
                    'industry': industry,
                    'location': 'Unknown'
                })
            time.sleep(random.uniform(2, 5))

    return leads

if __name__ == "__main__":
    # Test discovery
    test_industries = ["AI automation agency"]
    test_locations = ["New York"]
    found_leads = discover_leads(test_industries, test_locations)
    print(f"Found {len(found_leads)} leads.")
    for lead in found_leads:
        print(lead)
