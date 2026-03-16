import requests
from bs4 import BeautifulSoup
import re
import urllib.parse

def get_page_content(url):
    """
    Fetches the content of a web page.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_text(html):
    """
    Extracts visible text from HTML content.
    """
    if not html:
        return ""
    soup = BeautifulSoup(html, 'html.parser')

    # Remove script and style elements
    for script_or_style in soup(["script", "style"]):
        script_or_style.decompose()

    text = soup.get_text()
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text

def find_links(html, base_url):
    """
    Finds and normalizes all links in the HTML content.
    """
    if not html:
        return []
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for a in soup.find_all('a', href=True):
        link = a['href']
        full_link = urllib.parse.urljoin(base_url, link)
        links.append(full_link)
    return list(set(links))

def find_contact_pages(links):
    """
    Identifies potential contact, about, or team pages from a list of links.
    """
    contact_keywords = ['contact', 'about', 'team', 'staff', 'reach-us', 'get-in-touch']
    contact_links = []
    for link in links:
        if any(keyword in link.lower() for keyword in contact_keywords):
            contact_links.append(link)
    return list(set(contact_links))

def crawl_website(url):
    """
    Crawls a website starting from the homepage and looks for contact info on important pages.
    """
    print(f"Crawling website: {url}")
    homepage_html = get_page_content(url)
    if not homepage_html:
        return None

    homepage_text = extract_text(homepage_html)
    all_links = find_links(homepage_html, url)
    contact_pages = find_contact_pages(all_links)

    # Also collect text from contact pages
    additional_text = ""
    # Limit to top 3 contact-related pages to be polite and efficient
    for contact_page in contact_pages[:3]:
        print(f"  Checking contact page: {contact_page}")
        contact_html = get_page_content(contact_page)
        if contact_html:
            additional_text += "\n" + extract_text(contact_html)

    return {
        'homepage_text': homepage_text,
        'additional_text': additional_text,
        'all_text': homepage_text + "\n" + additional_text
    }

if __name__ == "__main__":
    # Test crawling
    test_url = "https://www.aiagencyny.com/"
    data = crawl_website(test_url)
    if data:
        print(f"Successfully crawled {test_url}. Length of text collected: {len(data['all_text'])}")
        # print(data['all_text'][:500])
    else:
        print(f"Failed to crawl {test_url}")
