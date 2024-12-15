#!/usr/bin/env python3
import os
import re

def check_image_paths(posts_dir):
    old_path_pattern = re.compile(r'!\[.*?\]\(images/[^)]+\)')
    files_with_old_paths = []
    
    for filename in os.listdir(posts_dir):
        if filename.endswith('.md'):
            filepath = os.path.join(posts_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                matches = old_path_pattern.findall(content)
                if matches:
                    files_with_old_paths.append({
                        'file': filename,
                        'matches': matches
                    })
    
    return files_with_old_paths

def main():
    posts_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '_posts')
    print(f"Checking directory: {posts_dir}")
    
    results = check_image_paths(posts_dir)
    
    if not results:
        print("No files found with old image paths (images/)")
        return
        
    print("\nFiles with old image paths:")
    print("===========================")
    
    for result in results:
        print(f"\nFile: {result['file']}")
        print("Old paths found:")
        for match in result['matches']:
            print(f"  {match}")

if __name__ == '__main__':
    main()
