import os
import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import markdownify

SITEMAP_URL = "https://wp.the5ers.com/frequently_questions-sitemap.xml"
OUTPUT_DIR = os.getenv("OUTPUT_DIR", r"C:\Users\USER\Documents\Obsidian Vault\5ers RAG")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "faq_data.md")

def get_faq_urls():
    print(f"Fetching sitemap from {SITEMAP_URL}...")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(SITEMAP_URL, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch sitemap. Status: {response.status_code}")
        return []

    root = ET.fromstring(response.text)
    namespaces = {'sitemap': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    
    urls = []
    # The sitemap XML has <url><loc>...</loc></url>
    for loc in root.findall('.//sitemap:loc', namespaces):
        url = loc.text
        # Filter for only English FAQs (skip /ar/, /es/, /fr/, etc)
        if '/frequently_questions/' in url and not any(lang in url for lang in ['/ar/', '/es/', '/fr/', '/ja/', '/jp/', '/pt/', '/ru/', '/zh-hans/', '/zh-hant/', '/ko/', '/hi/', '/id/', '/vi/', '/th/', '/ms/']):
            urls.append(url)
            
    print(f"Found {len(urls)} English FAQ articles.")
    return urls

def scrape_faqs():
    urls = get_faq_urls()
    if not urls:
        print("No URLs found to scrape.")
        return

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    markdown_content = "# The 5ers FAQ\n\n"
    
    for idx, link in enumerate(urls):
        print(f"Scraping ({idx+1}/{len(urls)}): {link}")
        try:
            res = requests.get(link, headers=headers)
            if res.status_code == 200:
                page_soup = BeautifulSoup(res.text, 'html.parser')
                
                # The main content is usually inside an <article> tag.
                article = page_soup.find('article')
                if not article:
                    # Fallback to main content div
                    article = page_soup.find('main') or page_soup.find('body')
                    
                if article:
                    # Remove "Was this article helpful?" section
                    helpful_blocks = article.find_all(string=lambda text: text and 'Was this article helpful?' in text)
                    for block in helpful_blocks:
                        if block.parent and block.parent.parent:
                            block.parent.parent.decompose()
                            
                    # Convert HTML directly to Markdown, preserving lists, bold text, tables, headers, etc.
                    md_text = markdownify.markdownify(str(article), heading_style="ATX")
                    
                    # Usually titles are in h1, if the article missed it, let's add the title manually
                    if not page_soup.find('h1'):
                        title = link.strip('/').split('/')[-1].replace('-', ' ').title()
                        markdown_content += f"\n\n## {title}\n\n"
                        
                    markdown_content += md_text.strip() + "\n\n---\n\n"
                
        except Exception as e:
            print(f"Error scraping {link}: {e}")
            
    # Ensure directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
        
    print(f"Successfully saved {len(urls)} FAQs to {OUTPUT_FILE}")

if __name__ == "__main__":
    scrape_faqs()
