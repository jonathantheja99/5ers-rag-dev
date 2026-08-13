import os
import requests
from bs4 import BeautifulSoup
import re

START_URL = "https://the5ers.com/faqs/"
OUTPUT_DIR = os.getenv("OUTPUT_DIR", r"C:\Users\USER\Documents\Obsidian Vault\5ers RAG")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "faq_data.md")
BASE_URL = "https://the5ers.com"

def scrape_faqs():
    print(f"Scraping {START_URL}...")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    response = requests.get(START_URL, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch FAQ page. Status: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all FAQ links
    faq_links = set()
    for a in soup.find_all('a', href=True):
        href = a['href']
        if '/faqs/' in href and href != '/faqs/':
            if href.startswith('/'):
                href = BASE_URL + href
            faq_links.add(href)
            
    print(f"Found {len(faq_links)} FAQ articles. Extracting content...")
    
    markdown_content = "# The 5ers FAQ\n\n"
    
    for idx, link in enumerate(faq_links):
        print(f"Scraping ({idx+1}/{len(faq_links)}): {link}")
        try:
            res = requests.get(link, headers=headers)
            if res.status_code == 200:
                page_soup = BeautifulSoup(res.text, 'html.parser')
                
                # Usually titles are in h1
                h1 = page_soup.find('h1')
                title = h1.text.strip() if h1 else link.split('/')[-2].replace('-', ' ').title()
                
                markdown_content += f"## {title}\n\n"
                
                # The main content is often in a specific div. We'll extract paragraphs from the main section.
                # Since we don't know the exact div class, we look for typical content containers or just extract all paragraphs.
                # A heuristic: find the div with the most p tags.
                divs = page_soup.find_all('div')
                best_div = max(divs, key=lambda d: len(d.find_all('p')), default=page_soup)
                
                paragraphs = best_div.find_all(['p', 'li'])
                for p in paragraphs:
                    text = p.get_text(strip=True)
                    if text and len(text) > 20: # filter out very short nav links
                        markdown_content += f"{text}\n\n"
                        
        except Exception as e:
            print(f"Error scraping {link}: {e}")
            
    # Ensure directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
        
    print(f"Successfully saved {len(faq_links)} FAQs to {OUTPUT_FILE}")

if __name__ == "__main__":
    scrape_faqs()
