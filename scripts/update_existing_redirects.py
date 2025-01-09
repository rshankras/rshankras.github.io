import csv
import os
import glob

def update_redirect_files():
    print("Updating existing redirect files...")
    print("-" * 80)
    
    # Read the redirects CSV
    with open('../redirects.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        redirects = {row['source']: row['target'] for row in reader}
    
    # Find all existing redirect files
    redirect_files = glob.glob('../_posts/redirects/**/*.md', recursive=True)
    
    # Update each redirect file
    for filepath in redirect_files:
        # Read the current content
        with open(filepath, 'r') as f:
            content = f.read()
        
        # Extract the permalink from the content
        permalink = None
        for line in content.split('\n'):
            if line.startswith('permalink:'):
                permalink = line.split(':', 1)[1].strip()
                break
        
        if permalink and permalink in redirects:
            # Create the new content with the redirect layout
            new_content = f"""---
layout: redirect
redirect_to: {redirects[permalink]}
permalink: {permalink}
---"""
            
            # Write the updated content
            with open(filepath, 'w') as f:
                f.write(new_content)
            print(f"Updated {os.path.basename(filepath)} -> {redirects[permalink]}")
        else:
            print(f"Skipped {os.path.basename(filepath)} - no matching redirect found")
    
    print("\nAll redirect files have been updated!")

if __name__ == '__main__':
    update_redirect_files()
