import urllib.request
import urllib.parse
import urllib.error
from urllib.parse import urljoin
import ssl
import re
from html.parser import HTMLParser

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    self.links.append(attr[1])

def crawl_page(url, depth=1, visited=None):
    if visited is None:
        visited = set()
    
    if depth <= 0 or url in visited:
        return
    
    print(f"\nCrawling: {url}")
    visited.add(url)
    
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    try:
        # Open the URL
        response = urllib.request.urlopen(url, context=ctx)
        
        # Check if the response is HTML
        content_type = response.headers.get('Content-Type', '').lower()
        if 'text/html' not in content_type:
            print(f"Skipping non-HTML content: {content_type}")
            return
        
        # Read and decode the content
        html = response.read().decode()
        
        # Parse links
        parser = LinkParser()
        parser.feed(html)
        
        print(f"Found {len(parser.links)} links")
        
        # Process each link
        for link in parser.links:
            absolute_link = urljoin(url, link)
            if absolute_link.startswith('http'):
                crawl_page(absolute_link, depth - 1, visited)
                
    except Exception as e:
        print(f"Error crawling {url}: {str(e)}")

if __name__ == "__main__":
    # Example usage
    start_url = "https://www.youtube.com/"
    print("Starting web crawler...")
    print("Initial URL:", start_url)
    crawl_page(start_url, depth=2)