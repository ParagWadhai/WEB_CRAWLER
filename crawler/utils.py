def normalize_url(base_url, link):
    """Convert relative URLs to absolute URLs."""
    if link.startswith('http'):
        return link
    
    if link.startswith('/'):
        # Handle absolute paths
        base_parts = base_url.split('/')
        if len(base_parts) >= 3:  # Has schema and domain
            return f"{base_parts[0]}//{base_parts[2]}{link}"
        return link
    
    # Handle relative paths
    base_path = base_url.rsplit('/', 1)[0]
    return f"{base_path}/{link}"

def is_valid_url(url):
    """Check if URL is valid and starts with http/https."""
    return url.startswith(('http://', 'https://'))