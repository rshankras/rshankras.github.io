import os
import glob
import re
from datetime import datetime

def get_post_title(content):
    match = re.search(r'title:\s*"([^"]+)"', content)
    return match.group(1) if match else None

def update_original_posts():
    print("Updating original posts with redirect information...")
    print("-" * 80)
    
    # Find all redirect files
    redirect_files = glob.glob('../_posts/redirects/**/*.md', recursive=True)
    
    for redirect_file in redirect_files:
        with open(redirect_file, 'r') as f:
            redirect_content = f.read()
        
        # Extract permalink and redirect_to
        permalink = None
        redirect_to = None
        for line in redirect_content.split('\n'):
            if line.startswith('permalink:'):
                permalink = line.split(':', 1)[1].strip()
            elif line.startswith('redirect_to:'):
                redirect_to = line.split(':', 1)[1].strip()
        
        if not permalink or not redirect_to:
            continue
        
        # Create the search pattern from permalink
        search_pattern = permalink.strip('/').replace('-', '[-]').replace('/', '[-]')
        original_posts = glob.glob(f'../_posts/*{search_pattern}.md')
        original_posts = [p for p in original_posts if 'redirects' not in p]
        
        if original_posts:
            original_post = original_posts[0]
            print(f"\nProcessing: {os.path.basename(original_post)}")
            
            # Read original post
            with open(original_post, 'r') as f:
                content = f.read()
            
            # Check if redirect_to is already present
            if 'redirect_to:' not in content:
                # Split front matter and content
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    front_matter = parts[1]
                    post_content = parts[2]
                    
                    # Add redirect_to to front matter
                    updated_front_matter = front_matter.rstrip() + f'\nredirect_to: {redirect_to}\n'
                    
                    # Reconstruct the post
                    updated_content = f'---{updated_front_matter}---{post_content}'
                    
                    # Write back to file
                    with open(original_post, 'w') as f:
                        f.write(updated_content)
                    
                    print(f"  Updated original post with redirect information")
                    
                    # Remove the redirect file
                    os.remove(redirect_file)
                    print(f"  Removed redirect file: {os.path.basename(redirect_file)}")
            else:
                print(f"  Original post already has redirect information")
                os.remove(redirect_file)
                print(f"  Removed redirect file: {os.path.basename(redirect_file)}")
        else:
            print(f"\nWarning: No original post found for {os.path.basename(redirect_file)}")
    
    print("\nUpdate complete!")

if __name__ == '__main__':
    update_original_posts()
