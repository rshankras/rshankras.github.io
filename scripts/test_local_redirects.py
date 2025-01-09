import csv
import requests
from urllib.parse import urljoin
import time
from bs4 import BeautifulSoup

def test_redirect(source_url, target_url):
    base_url = "http://localhost:4000"
    full_source_url = urljoin(base_url, source_url.lstrip('/'))
    
    try:
        # Make request without following redirects
        response = requests.get(full_source_url, allow_redirects=False)
        
        if response.status_code in (301, 302):
            # Check HTTP redirect
            if response.headers.get('Location') == target_url:
                return f" {source_url} -> {target_url} (HTTP redirect)"
            else:
                return f" {source_url} -> Expected: {target_url}, Got HTTP redirect to: {response.headers.get('Location')}"
        
        # Check meta refresh and JavaScript redirect
        soup = BeautifulSoup(response.text, 'html.parser')
        meta_refresh = soup.find('meta', attrs={'http-equiv': 'refresh'})
        js_redirect = soup.find('script', string=lambda s: 'location' in str(s) if s else False)
        
        if meta_refresh and target_url in meta_refresh.get('content', ''):
            return f" {source_url} -> {target_url} (meta refresh)"
        elif js_redirect and target_url in js_redirect.string:
            return f" {source_url} -> {target_url} (JavaScript)"
        else:
            return f" {source_url} -> Expected: {target_url}, Got: HTML without proper redirect"
            
    except Exception as e:
        return f" {source_url} -> Error: {str(e)}"

def test_all_redirects():
    print("Testing redirects on local Jekyll server...")
    print("-" * 80)
    
    # First test if Jekyll server is running
    try:
        requests.get("http://localhost:4000", timeout=5)
    except requests.exceptions.ConnectionError:
        print(" Error: Jekyll server is not running on http://localhost:4000")
        print("Please run 'bundle exec jekyll serve' first")
        return
    except Exception as e:
        print(f" Error: {str(e)}")
        return
    
    with open('../redirects.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        redirects = [(row['source'], row['target']) for row in reader]
    
    # Test first few redirects
    print("Testing first 5 redirects:")
    for source, target in redirects[:5]:
        result = test_redirect(source, target)
        print(result)
        time.sleep(1)  # Small delay between requests
    
    print("\nWould you like to test all remaining redirects? (y/n)")

if __name__ == '__main__':
    test_all_redirects()
