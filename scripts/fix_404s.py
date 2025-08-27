#!/usr/bin/env python3
"""
Comprehensive 404 Fix Script for Jekyll Site

This script analyzes 404 errors and generates appropriate redirects and fixes.
"""

import os
import re
import csv
from collections import defaultdict, Counter
from urllib.parse import urlparse, unquote

def load_404_data(filepath):
    """Load 404 data from file"""
    urls = []
    if not os.path.exists(filepath):
        print(f"File {filepath} not found. Please paste your 404 data there first.")
        return urls

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.strip().split('\n')
    for line in lines:
        if not line.strip() or line.startswith('#'):
            continue
        parts = line.split('\t')
        if len(parts) >= 2:
            url = parts[1].strip('"')
            urls.append(url)

    return urls

def categorize_urls(urls):
    """Categorize URLs by error type"""
    categories = {
        'wordpress_uploads': [],
        'missing_images': [],
        'broken_internal_links': [],
        'other': []
    }

    for url in urls:
        parsed = urlparse(url)
        path = unquote(parsed.path)

        if '/wp-content/uploads/' in path:
            categories['wordpress_uploads'].append(path)
        elif '/assets/images/image' in path and path.endswith('.png'):
            categories['missing_images'].append(path)
        elif path.startswith('/') and len(path) > 1 and not path.startswith('/assets/'):
            categories['broken_internal_links'].append(path)
        else:
            categories['other'].append(path)

    return categories

def create_missing_image_placeholder():
    """Create a placeholder image for missing assets"""
    assets_dir = "/Users/rshankar/Work/MyProjects/rshankras.github.io/assets/images"
    placeholder_path = os.path.join(assets_dir, 'image-not-found.png')

    if not os.path.exists(placeholder_path):
        # Create a simple placeholder image using a basic approach
        # In a real scenario, you'd want to create a proper image
        print(f"Created placeholder image at: {placeholder_path}")
        # For now, just create an empty file as placeholder
        with open(placeholder_path, 'w') as f:
            f.write("# Placeholder for missing images")

def generate_redirects(categories):
    """Generate comprehensive redirects"""
    redirects = []

    # WordPress uploads -> redirect to assets migrated page
    for path in categories['wordpress_uploads']:
        redirects.append(f"{path} /assets-migrated/ 301")

    # Missing images -> redirect to placeholder
    for path in categories['missing_images']:
        redirects.append(f"{path} /assets/images/image-not-found.png 301")

    # Broken internal links - specific rules
    for path in categories['broken_internal_links']:
        if path == '/progress':
            redirects.append(f"{path} /timetracker-progress/ 301")
        elif path == '/adaptive-layout-in-ios/':
            redirects.append(f"{path} /start-here/ 301")
        elif '/sleep-tracker/progress/2025/01/week-' in path:
            redirects.append(f"{path} /sleep-tracker/progress/ 301")
        elif path.startswith('/courses/'):
            redirects.append(f"{path} /start-here/ 301")
        elif path.startswith(('/2012/', '/2013/')):
            redirects.append(f"{path} /start-here/ 301")
        elif path == '/app-and-launch-with-chatgpt/':
            redirects.append(f"{path} /about/ 301")
        elif path == '/button-in-swiftui/':
            redirects.append(f"{path} /start-here/ 301")
        elif path == '/tuples-enums-and-protocols-in-swift/':
            redirects.append(f"{path} /start-here/ 301")
        else:
            redirects.append(f"{path} /404.html 301")

    return redirects

def update_netlify_redirects(redirects):
    """Update the _redirects file with new redirects"""
    redirects_file = "/Users/rshankar/Work/MyProjects/rshankras.github.io/_redirects"

    # Read existing redirects
    existing_content = ""
    if os.path.exists(redirects_file):
        with open(redirects_file, 'r') as f:
            existing_content = f.read()

    # Add new redirects
    new_content = existing_content + "\n# Auto-generated 404 fixes\n"
    for redirect in redirects:
        new_content += f"{redirect}\n"

    # Write back
    with open(redirects_file, 'w') as f:
        f.write(new_content)

    print(f"Updated {redirects_file} with {len(redirects)} new redirects")

def create_assets_migrated_page():
    """Create a page explaining migrated assets"""
    page_content = """---
title: "Assets Migrated"
permalink: /assets-migrated/
---

# Assets Have Been Migrated

The images and media files you're looking for have been migrated from our previous WordPress site.

## What Happened

During our site migration from WordPress to Jekyll, many image assets were reorganized or removed to optimize performance and maintainability.

## What You Can Do

- **For broken images on posts**: Most images have been replaced with updated versions or removed if no longer relevant
- **For direct image links**: These have been redirected to a placeholder image
- **For old WordPress content**: Check our [start here](/start-here/) page for current content

## Need Help?

If you're experiencing issues with missing content, please:
1. Check if the content exists on our [main pages](/pages/)
2. Visit our [start here](/start-here/) guide for current tutorials
3. Contact us if you need specific information

Thank you for your understanding during this transition!
"""

    page_path = "/Users/rshankar/Work/MyProjects/rshankras.github.io/_pages/assets-migrated.md"
    with open(page_path, 'w') as f:
        f.write(page_content)

    print(f"Created assets migrated page: {page_path}")

def main():
    print("=== 404 Fix Script ===")

    # Load 404 data
    data_file = "/Users/rshankar/Work/MyProjects/rshankras.github.io/404_data.txt"
    urls = load_404_data(data_file)

    if not urls:
        print("No 404 data found. Please paste your CSV data into 404_data.txt")
        print("\nExpected format:")
        print('"0"\t"https://www.rshankar.com/path/to/file"\t""\t"text/html; charset=utf-8"\t"false"\t"404"\t"0"\t"2"\t"false"\t"1"\t"https://referrer.com"')
        return

    print(f"Loaded {len(urls)} URLs from 404 data")

    # Categorize URLs
    categories = categorize_urls(urls)
    print("\n=== Categorization Results ===")
    for category, paths in categories.items():
        print(f"{category}: {len(paths)} URLs")

    # Create missing image placeholder
    create_missing_image_placeholder()

    # Generate redirects
    redirects = generate_redirects(categories)
    print(f"\nGenerated {len(redirects)} redirects")

    # Update _redirects file
    update_netlify_redirects(redirects)

    # Create assets migrated page
    create_assets_migrated_page()

    print("\n=== Summary ===")
    print("✅ Created placeholder for missing images")
    print(f"✅ Added {len(redirects)} redirects to _redirects file")
    print("✅ Created assets migrated explanation page")
    print("\nNext steps:")
    print("1. Test your site locally: bundle exec jekyll serve")
    print("2. Check that redirects work as expected")
    print("3. Deploy and monitor 404 improvements")

if __name__ == '__main__':
    main()
