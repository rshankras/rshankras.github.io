#!/usr/bin/env python3
import os
import re
import shutil
from datetime import datetime

def update_image_paths(posts_dir, backup=True):
    old_path_pattern = re.compile(r'!\[(.*?)\]\(images/(.*?)\)')
    files_updated = []
    
    for filename in os.listdir(posts_dir):
        if filename.endswith('.md'):
            filepath = os.path.join(posts_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if file needs updating
            if old_path_pattern.search(content):
                # Create backup if requested
                if backup:
                    backup_path = filepath + '.bak'
                    shutil.copy2(filepath, backup_path)
                
                # Replace old paths with new format
                updated_content = old_path_pattern.sub(r'![\1](/assets/images/\2)', content)
                
                # Write updated content back to file
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                
                files_updated.append(filename)
    
    return files_updated

def main():
    posts_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '_posts')
    print(f"Updating files in: {posts_dir}")
    
    # Create backup directory
    backup_dir = os.path.join(os.path.dirname(posts_dir), '_posts_backup')
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    # Update files
    updated_files = update_image_paths(posts_dir)
    
    if not updated_files:
        print("\nNo files needed updating!")
        return
        
    print("\nUpdated files:")
    print("==============")
    for filename in updated_files:
        print(f"- {filename}")
    
    print(f"\nTotal files updated: {len(updated_files)}")
    print("Backup files have been created with '.bak' extension")

if __name__ == '__main__':
    main()
