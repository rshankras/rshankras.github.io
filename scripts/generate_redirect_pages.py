import csv
import os

def create_redirect_page(source, target):
    # Remove leading slash and create directory structure
    path = source.lstrip('/')
    if path.endswith('/'):
        path = path[:-1]
    
    dir_path = os.path.join('../_posts/redirects', path)
    os.makedirs(os.path.dirname(dir_path), exist_ok=True)
    
    # Create the redirect file
    content = f"""---
layout: redirect
redirect_to: {target}
permalink: {source}
---"""
    
    with open(f"{dir_path}.md", 'w') as f:
        f.write(content)

def generate_all_redirects():
    # Create redirects directory if it doesn't exist
    os.makedirs('../_posts/redirects', exist_ok=True)
    
    # Read the CSV file and create redirect pages
    with open('../redirects.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            create_redirect_page(row['source'], row['target'])
            print(f"Created redirect for {row['source']} -> {row['target']}")

if __name__ == '__main__':
    generate_all_redirects()
