from crawler import WebCrawler

def main():
    crawler = WebCrawler()
    start_url = "https://www.youtube.com/"
    print("Starting web crawler simulation...")
    print("Initial URL:", start_url)
    crawler.simulate_crawl(start_url, depth=2)

if __name__ == "__main__":
    main()