#!/usr/bin/env python3
"""
Create individual redirect pages using jekyll-redirect-from plugin
This creates actual HTML pages that work with GitHub Pages
"""

import os
import re
from urllib.parse import unquote

def create_redirect_page(source_path, target_path):
    """
    Create a Jekyll redirect page
    """
    # Clean the source path to create a valid filename
    # Remove leading slash and replace special chars
    filename = source_path.lstrip('/')
    if not filename:
        return  # Skip root path

    # Replace slashes with dashes and clean up
    filename = re.sub(r'[^\w\-]', '-', filename)
    filename = re.sub(r'-+', '-', filename)  # Replace multiple dashes with single
    filename = filename.strip('-')  # Remove leading/trailing dashes

    if not filename:
        return

    # Create the redirect page content
    page_content = f"""---
title: "Redirect"
permalink: {source_path}
redirect_to: {target_path}
---

<script>
window.location.href = "{target_path}";
</script>

<noscript>
    <meta http-equiv="refresh" content="0;url={target_path}">
</noscript>

<p>Redirecting to <a href="{target_path}">{target_path}</a>...</p>
"""

    # Create the file path
    # For GitHub Pages, we need to create the directory structure
    page_path = f"_pages/redirects/{filename}.md"

    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(page_path), exist_ok=True)

    # Write the redirect page
    with open(page_path, 'w') as f:
        f.write(page_content)

    print(f"Created redirect: {source_path} -> {target_path}")

def main():
    redirects_file = "/Users/rshankar/Work/MyProjects/rshankras.github.io/_redirects"

    if not os.path.exists(redirects_file):
        print("No _redirects file found!")
        return

    # Read and parse redirects
    with open(redirects_file, 'r') as f:
        lines = f.readlines()

    redirect_count = 0

    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue

        # Parse redirect line: "source target status_code"
        parts = line.split()
        if len(parts) >= 2:
            source = parts[0]
            target = parts[1]

            # Skip the original redirect that was already there
            if source == "/building-a-simple-photo-gallery-app-in-swiftui":
                continue

            try:
                create_redirect_page(source, target)
                redirect_count += 1
            except Exception as e:
                print(f"Error creating redirect for {source}: {e}")

    print(f"\nCreated {redirect_count} redirect pages")
    print("These will work with GitHub Pages and the jekyll-redirect-from plugin")

if __name__ == '__main__':
    main()
