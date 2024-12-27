# Web Crawler Simulator

A Python-based web crawler simulator that demonstrates web crawling concepts without making actual network requests. This project is ideal for learning about web crawlers and testing crawling logic.

## Features

- Simulates web crawling behavior
- Handles both absolute and relative URLs
- Implements depth-limited crawling
- Tracks visited pages to avoid duplicates
- URL normalization and validation

## Project Structure

```
WEB_CRAWLER/
├── crawler/
│   ├── __init__.py
│   ├── crawler.py     # Main crawler implementation
│   ├── parser.py      # HTML parsing functionality
│   └── utils.py       # URL handling utilities
├── main.py            # Entry point
└── README.md
```

## Requirements

- Python 3.6 or higher

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ParagWadhai/WEB_CRAWLER.git
cd web-crawler-simulator
```

## Usage

Run the crawler simulation:

```bash
python main.py
```

Example output:
```
Starting web crawler simulation...
Initial URL: https://example.com

Simulating crawl of: https://example.com
Found 5 example links
Would crawl: https://example.com/about
Would crawl: https://example.com/products
Would crawl: https://example.com/contact
Would crawl: https://another-example.com
```

## Customization

You can modify the crawler behavior by:

1. Adjusting the crawl depth in `main.py`:
```python
crawler.simulate_crawl(start_url, depth=3)  
```

2. Adding custom example links in `crawler/crawler.py`:
```python
example_links = [
    "/your-custom-path",
    "https://your-domain.com/page"
]
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request


## Acknowledgments

- Built as an educational tool for understanding web crawlers
- Inspired by real-world web crawling systems
- Designed for learning and testing purposes