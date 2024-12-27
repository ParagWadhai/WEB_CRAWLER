from html.parser import HTMLParser

class LinkParser(HTMLParser):
    """HTML Parser that extracts links from a webpage."""
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    self.links.append(attr[1])

    def get_links(self):
        return self.links