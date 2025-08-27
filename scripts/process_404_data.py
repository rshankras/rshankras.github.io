#!/usr/bin/env python3
import os
import re
import csv
from collections import defaultdict, Counter
from urllib.parse import urlparse, unquote

def load_404_data_from_text(text_data):
    """
    Load 404 data from tab-separated text
    """
    urls = []
    lines = text_data.strip().split('\n')

    for line in lines[1:]:  # Skip header
        if not line.strip():
            continue
        parts = line.split('\t')
        if len(parts) >= 2:
            url = parts[1].strip('"')
            urls.append(url)

    return urls

def categorize_urls(urls):
    """
    Categorize URLs by type
    """
    categories = {
        'wordpress_uploads': [],
        'missing_images': [],
        'broken_internal_links': [],
        'external_redirects': [],
        'other': []
    }

    for url in urls:
        parsed = urlparse(url)
        path = unquote(parsed.path)

        if '/wp-content/uploads/' in path:
            categories['wordpress_uploads'].append(path)
        elif '/assets/images/image' in path and path.endswith('.png'):
            categories['missing_images'].append(path)
        elif path.startswith('/') and len(path) > 1:
            # Internal links
            if any(keyword in path for keyword in ['progress', 'adaptive-layout', 'courses', '2012', '2013']):
                categories['broken_internal_links'].append(path)
            else:
                categories['other'].append(path)
        else:
            categories['other'].append(path)

    return categories

def analyze_wordpress_uploads(wp_paths):
    """
    Analyze WordPress upload patterns
    """
    years = Counter()
    file_types = Counter()

    for path in wp_paths:
        # Extract year from path
        year_match = re.search(r'/wp-content/uploads/(\d{4})/', path)
        if year_match:
            years[year_match.group(1)] += 1

        # Extract file extension
        if '.' in path:
            ext = path.split('.')[-1].lower()
            file_types[ext] += 1

    return years, file_types

def create_redirect_strategy():
    """
    Create a comprehensive redirect strategy
    """
    strategy = {
        'wordpress_uploads': '/assets-migrated/',
        'missing_images': '/assets/images/image-not-found.png',
        'broken_links': {
            '/progress': '/timetracker-progress/',
            '/adaptive-layout-in-ios/': '/start-here/',
            'sleep-tracker-week': '/sleep-tracker/progress/',
            'courses': '/start-here/',
            'old-posts': '/start-here/'
        }
    }

    return strategy

def generate_netlify_redirects(categories, strategy):
    """
    Generate Netlify-style redirects
    """
    redirects = []

    # WordPress uploads
    for path in categories['wordpress_uploads']:
        redirects.append(f"{path} {strategy['wordpress_uploads']} 301")

    # Missing images
    for path in categories['missing_images']:
        redirects.append(f"{path} {strategy['missing_images']} 301")

    # Broken internal links
    for path in categories['broken_internal_links']:
        if '/sleep-tracker/progress/2025/01/week-' in path:
            redirects.append(f"{path} {strategy['broken_links']['sleep-tracker-week']} 301")
        elif path.startswith('/courses/'):
            redirects.append(f"{path} {strategy['broken_links']['courses']} 301")
        elif path.startswith(('/2012/', '/2013/')):
            redirects.append(f"{path} {strategy['broken_links']['old-posts']} 301")
        elif path == '/progress':
            redirects.append(f"{path} {strategy['broken_links']['/progress']} 301")
        elif path == '/adaptive-layout-in-ios/':
            redirects.append(f"{path} {strategy['broken_links']['/adaptive-layout-in-ios/']} 301")
        else:
            redirects.append(f"{path} /404.html 301")

    return redirects

def main():
    # Your 404 data goes here - I've included a sample from your data
    text_404_data = '''"0"	"https://www.rshankar.com/wp-content/uploads/2015/08/1439303413_full.png"	""	"text/html; charset=utf-8"	"false"	"404"	"0"	"2"	"false"	"1"	"https://rshankar.com/wp-content/uploads/2015/08/1439303413_full.png"
"0"	"https://www.rshankar.com/assets/images/image66.png"	""	"text/html; charset=utf-8"	"false"	"404"	"0"	"1"	"false"	"1"	"https://www.rshankar.com/how-to-turn-off-the-safari-pop-up-blocker-in-ipad-2/"
"0"	"https://www.rshankar.com/assets/images/image99.png"	""	"text/html; charset=utf-8"	"false"	"404"	"0"	"1"	"false"	"1"	"https://www.rshankar.com/how-to-recover-deleted-folders-in-outlook-2010/"
"0"	"https://www.rshankar.com/assets/images/image65.png"	""	"text/html; charset=utf-8"	"false"	"404"	"0"	"1"	"false"	"1"	"https://www.rshankar.com/how-to-turn-off-the-safari-pop-up-blocker-in-ipad-2/"
"0"	"https://www.rshankar.com/assets/images/image156.png"	""	"text/html; charset=utf-8"	"false"	"404"	"0"	"1"	"false"	"1"	"https://www.rshankar.com/online-payment-of-chennai-metro-water-tax/"
"0"	"https://www.rshankar.com/wp-content/uploads/2016/03/1457068314_full.png"	""	"text/html; charset=utf-8"	"false"	"404"	"0"	"2"	"false"	"1"	"https://rshankar.com/wp-content/uploads/2016/03/1457068314_full.png"
"0"	"https://www.rshankar.com/wp-content/uploads/2016/09/1474782706_full.png"	""	"text/html; charset=utf-8"	"false"	"404"	"0"	"2"	"false"	"1"	"https://rshankar.com/wp-content/uploads/2016/09/1474782706_full.png"
"0"	"https://www.rshankar.com/wp-content/uploads/2015/06/1433915244_full.png"	""	"text/html; charset=utf-8"	"false"	"404"	"0"	"2"	"false"	"1"	"https://rshankar.com/wp-content/uploads/2015/06/1433915244_full.png"'''

    urls = load_404_data_from_text(text_404_data)
    categories = categorize_urls(urls)

    print("=== 404 Analysis Report ===")
    print(f"Total 404 URLs: {len(urls)}")
    print()

    print("Categories:")
    for category, paths in categories.items():
        print(f"  {category}: {len(paths)} URLs")

    # Analyze WordPress uploads
    if categories['wordpress_uploads']:
        years, file_types = analyze_wordpress_uploads(categories['wordpress_uploads'])
        print("\nWordPress Upload Analysis:")
        print("Years:", dict(years))
        print("File types:", dict(file_types))

    # Generate redirects
    strategy = create_redirect_strategy()
    redirects = generate_netlify_redirects(categories, strategy)

    print(f"\nGenerated {len(redirects)} redirects")

    # Save redirects to file
    with open('_redirects_generated.txt', 'w') as f:
        f.write("# Generated 404 redirects\n")
        f.write("# Format: source_path target_path status_code\n\n")
        for redirect in redirects:
            f.write(f"{redirect}\n")

    print("Saved redirects to _redirects_generated.txt")

    # Show sample redirects
    print("\nSample redirects:")
    for redirect in redirects[:10]:
        print(f"  {redirect}")

if __name__ == '__main__':
    main()
