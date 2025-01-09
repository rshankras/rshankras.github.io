import csv
import requests
from urllib.parse import urljoin
import concurrent.futures

def test_redirect(source_url, target_url):
    base_url = "https://rshankras.github.io"  # Replace with your actual domain
    full_source_url = urljoin(base_url, source_url)
    
    try:
        # Make request with allow_redirects=False to see the initial redirect
        response = requests.get(full_source_url, allow_redirects=False)
        
        if response.status_code in [301, 302]:
            location = response.headers.get('Location')
            if location == target_url:
                return f"✅ {source_url} -> {target_url}"
            else:
                return f"❌ {source_url} -> Expected: {target_url}, Got: {location}"
        else:
            return f"❌ {source_url} -> No redirect (Status: {response.status_code})"
    except Exception as e:
        return f"❌ {source_url} -> Error: {str(e)}"

def test_all_redirects():
    print("Testing redirects...")
    print("-" * 80)
    
    with open('../redirects.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        redirects = [(row['source'], row['target']) for row in reader]
    
    # Test redirects in parallel
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = {
            executor.submit(test_redirect, source, target): source 
            for source, target in redirects
        }
        
        for future in concurrent.futures.as_completed(future_to_url):
            print(future.result())
    
    print("-" * 80)
    print("Testing complete!")

if __name__ == '__main__':
    test_all_redirects()
