import os
import glob
from collections import defaultdict

def cleanup_duplicate_redirects():
    print("Cleaning up duplicate redirect files...")
    print("-" * 80)
    
    # Find all redirect files
    redirect_files = glob.glob('../_posts/redirects/**/*.md', recursive=True)
    
    # Group files by their permalink
    permalink_groups = defaultdict(list)
    for filepath in redirect_files:
        with open(filepath, 'r') as f:
            content = f.read()
            
        # Extract permalink
        permalink = None
        for line in content.split('\n'):
            if line.startswith('permalink:'):
                permalink = line.split(':', 1)[1].strip()
                break
        
        if permalink:
            permalink_groups[permalink].append(filepath)
    
    # Process each group
    removed_count = 0
    for permalink, files in permalink_groups.items():
        if len(files) > 1:
            print(f"\nFound {len(files)} files for {permalink}:")
            for f in files:
                print(f"  - {os.path.basename(f)}")
            
            # Keep the file with "2014-01-01" prefix and remove others
            files_to_keep = [f for f in files if "2014-01-01" in f]
            if not files_to_keep:
                files_to_keep = [min(files)]  # Keep the first file if no dated file exists
            
            # Remove other files
            for f in files:
                if f not in files_to_keep:
                    os.remove(f)
                    print(f"  Removed: {os.path.basename(f)}")
                    removed_count += 1
                else:
                    print(f"  Kept: {os.path.basename(f)}")
    
    print(f"\nCleanup complete! Removed {removed_count} duplicate files.")

if __name__ == '__main__':
    cleanup_duplicate_redirects()
