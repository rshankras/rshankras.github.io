#!/usr/bin/env python3
import os
import re
import csv
from collections import defaultdict
from urllib.parse import urlparse, unquote

def analyze_404_urls(csv_data):
    """
    Analyze 404 URLs and categorize them
    """
    categories = {
        'wordpress_uploads': [],
        'missing_images': [],
        'broken_internal_links': [],
        'other': []
    }

    # Parse CSV data (assuming it's tab-separated based on the format shown)
    lines = csv_data.strip().split('\n')[1:]  # Skip header

    for line in lines:
        if not line.strip():
            continue
        # Split by tab since the data appears to be tab-separated
        parts = line.split('\t')
        if len(parts) >= 2:
            url = parts[1].strip('"')  # Remove quotes

            # Parse the URL to get the path
            parsed = urlparse(url)
            path = unquote(parsed.path)

            # Categorize URLs
            if '/wp-content/uploads/' in path:
                categories['wordpress_uploads'].append(path)
            elif '/assets/images/image' in path and path.endswith('.png'):
                categories['missing_images'].append(path)
            elif path.startswith('/') and not path.startswith('/assets/') and not path.startswith('/wp-content/'):
                categories['broken_internal_links'].append(path)
            else:
                categories['other'].append(path)

    return categories

def generate_wordpress_redirects(wp_paths):
    """
    Generate redirects for WordPress upload paths
    """
    redirects = []

    for path in wp_paths:
        # Extract the filename from the WordPress path
        filename = os.path.basename(path)

        # Create redirect to a generic 404 page or asset not found page
        # For now, redirect to home page - can be customized later
        redirect_entry = f"{path}\thttps://www.rshankar.com/assets-migrated/\t301"
        redirects.append(redirect_entry)

    return redirects

def check_missing_images(image_paths):
    """
    Check which images are actually missing from assets
    """
    assets_dir = "/Users/rshankar/Work/MyProjects/rshankras.github.io/assets/images"
    missing_images = []
    existing_images = []

    for path in image_paths:
        # Extract filename from path
        filename = os.path.basename(path)
        full_path = os.path.join(assets_dir, filename)

        if os.path.exists(full_path):
            existing_images.append(filename)
        else:
            missing_images.append(filename)

    return missing_images, existing_images

def generate_internal_link_fixes(broken_links):
    """
    Suggest fixes for broken internal links
    """
    suggestions = {}

    for link in broken_links:
        if link == '/progress':
            suggestions[link] = '/timetracker-progress/'
        elif link == '/adaptive-layout-in-ios/':
            suggestions[link] = '/start-here/'
        elif '/sleep-tracker/progress/2025/01/week-' in link:
            # These are future-dated progress pages that don't exist yet
            suggestions[link] = '/sleep-tracker/progress/'
        elif link.startswith('/courses/'):
            suggestions[link] = '/start-here/'
        elif link.startswith('/2012/') or link.startswith('/2013/'):
            # Old dated posts - redirect to start-here or archive
            suggestions[link] = '/start-here/'
        else:
            suggestions[link] = '/404.html'

    return suggestions

def main():
    # Your 404 data - paste this from your CSV export
    csv_data = """PR	URL	Title	Content type	Is rendered page	HTTP status code	Organic traffic	Depth	Is indexable page	No. of all inlinks	First found at
"0"	"https://www.rshankar.com/wp-content/uploads/2015/08/1439303413_full.png"	""	"text/html; charset=utf-8"	"false"	"404"	"0"	"2"	"false"	"1"	"https://rshankar.com/wp-content/uploads/2015/08/1439303413_full.png"
"0"	"https://www.rshankar.com/assets/images/image66.png"	""	"text/html; charset=utf-8"	"false"	"404"	"0"	"1"	"false"	"1"	"https://www.rshankar.com/how-to-turn-off-the-safari-pop-up-blocker-in-ipad-2/"
"0"	"https://www.rshankar.com/assets/images/image99.png"	""	"text/html; charset=utf-8"	"false"	"404"	"0"	"1"	"false"	"1"	"https://www.rshankar.com/how-to-recover-deleted-folders-in-outlook-2010/" """

    # Analyze the URLs
    categories = analyze_404_urls(csv_data)

    print("=== 404 Analysis Results ===")
    print(f"WordPress uploads: {len(categories['wordpress_uploads'])} URLs")
    print(f"Missing images: {len(categories['missing_images'])} URLs")
    print(f"Broken internal links: {len(categories['broken_internal_links'])} URLs")
    print(f"Other: {len(categories['other'])} URLs")
    print()

    # Generate WordPress redirects
    if categories['wordpress_uploads']:
        print("=== WordPress Upload Redirects ===")
        wp_redirects = generate_wordpress_redirects(categories['wordpress_uploads'][:5])  # Show first 5
        for redirect in wp_redirects:
            print(redirect)

        # Save all WordPress redirects
        with open('wordpress_redirects.txt', 'w') as f:
            f.write("# WordPress upload redirects\n")
            for redirect in generate_wordpress_redirects(categories['wordpress_uploads']):
                f.write(f"{redirect}\n")
        print(f"\nSaved {len(categories['wordpress_uploads'])} WordPress redirects to wordpress_redirects.txt")

    # Check missing images
    if categories['missing_images']:
        print("\n=== Missing Images Analysis ===")
        missing_images, existing_images = check_missing_images(categories['missing_images'])

        print(f"Images confirmed missing: {len(missing_images)}")
        print(f"Images that exist: {len(existing_images)}")

        if missing_images:
            print("\nMissing image files:")
            for img in missing_images[:10]:  # Show first 10
                print(f"  - {img}")

    # Generate internal link fixes
    if categories['broken_internal_links']:
        print("\n=== Broken Internal Links ===")
        link_suggestions = generate_internal_link_fixes(categories['broken_internal_links'])

        print("Suggested redirects:")
        for link, suggestion in list(link_suggestions.items())[:10]:  # Show first 10
            print(f"  {link} -> {suggestion}")

        # Save suggestions
        with open('internal_link_fixes.txt', 'w') as f:
            f.write("# Internal link fixes\n")
            for link, suggestion in link_suggestions.items():
                f.write(f"{link}\t{suggestion}\n")
        print(f"\nSaved {len(link_suggestions)} internal link fixes to internal_link_fixes.txt")

if __name__ == '__main__':
    main()
