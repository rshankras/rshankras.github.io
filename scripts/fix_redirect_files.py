import csv
import os
import glob

def fix_redirect_files():
    print("Fixing redirect files...")
    print("-" * 80)
    
    # Read the redirects CSV
    with open('../redirects.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        redirects = {row['source']: row['target'] for row in reader}
    
    # Create redirects directory if it doesn't exist
    os.makedirs('../_posts/redirects', exist_ok=True)
    
    # Create or update redirect files
    for source, target in redirects.items():
        # Remove leading slash and create filename
        path = source.lstrip('/')
        if path.endswith('/'):
            path = path[:-1]
        
        # Create the redirect file content
        content = f"""---
layout: redirect
redirect_to: {target}
permalink: {source}
---"""
        
        # Save the file
        filepath = f"../_posts/redirects/2014-01-01-{path}.md"
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        with open(filepath, 'w') as f:
            f.write(content)
            print(f"Updated {filepath}")
    
    print("\nAll redirect files have been updated!")

if __name__ == '__main__':
    fix_redirect_files()
