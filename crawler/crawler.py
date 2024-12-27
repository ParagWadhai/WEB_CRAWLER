from .parser import LinkParser
from .utils import normalize_url, is_valid_url

class WebCrawler:
    def __init__(self):
        self.visited = set()
        
    def simulate_crawl(self, url, depth=1):
        """Simulate crawling without actually fetching pages."""
        if depth <= 0 or url in self.visited:
            return
            
        print(f"\nSimulating crawl of: {url}")
        self.visited.add(url)
        
        # Simulate finding some example links
        example_links = [
            "/about",
            "/products",
            "/services",
            "/contacts"
            "/help"
        ]
        
        print(f"Found {len(example_links)} example links")
        
        for link in example_links:
            absolute_link = normalize_url(url, link)
            if is_valid_url(absolute_link):
                print(f"Would crawl: {absolute_link}")
                self.simulate_crawl(absolute_link, depth - 1)