#!/usr/bin/env python3
import os
import re

def update_post_content(content):
    # Update image paths from ![](images/...) to ![](/assets/images/...)
    content = re.sub(r'!\[\]\(images/', '![](/assets/images/', content)
    
    # Update image paths from [![](images/...) to [![](/assets/images/...)
    content = re.sub(r'!\[\]\(https?://rshankar\.com/wp-content/uploads/\d{4}/\d{2}/', '![](/assets/images/', content)
    
    # Update WordPress style embeds to HTML5 iframes
    def replace_embed(match):
        url = match.group(1)
        video_id = url.split('/')[-1]
        return f'''<div class="video-container">
    <iframe 
        width="560" 
        height="315" 
        src="https://www.youtube.com/embed/{video_id}" 
        frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen>
    </iframe>
</div>'''
    
    content = re.sub(r'\[embed[^\]]*\](http://www\.youtube\.com/embed/[^\[]+)\[/embed\]', replace_embed, content)
    
    return content

def process_posts(posts_dir):
    for filename in os.listdir(posts_dir):
        if not filename.endswith('.md'):
            continue
            
        filepath = os.path.join(posts_dir, filename)
        print(f"Processing {filename}...")
        
        try:
            # Read the file content
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Update the content
            updated_content = update_post_content(content)
            
            # Only write if content has changed
            if content != updated_content:
                print(f"Updating {filename}")
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
            else:
                print(f"No changes needed for {filename}")
                
        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")

if __name__ == "__main__":
    posts_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "_posts")
    process_posts(posts_dir)
