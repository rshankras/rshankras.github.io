#!/usr/bin/env python3
import os
import csv
from collections import defaultdict

def clean_url(url):
    # Remove trailing slashes and clean up URLs
    return url.strip('/')

def generate_redirect_content(source, target):
    return f'''---
title: "Redirect to Blogmines"
permalink: /{source}/
redirect_to: {target}
---

<script>
window.location.href = "{target}";
</script>

<noscript>
    <meta http-equiv="refresh" content="0;url={target}">
</noscript>

<p>Redirecting to <a href="{target}">{target}</a>...</p>
'''

def main():
    # Read the CSV file
    redirects = defaultdict(set)
    with open('redirects.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        for source, target in reader:
            source = clean_url(source)
            redirects[source].add(target)

    # Create _redirects directory if it doesn't exist
    redirects_dir = os.path.join('_posts', 'redirects')
    os.makedirs(redirects_dir, exist_ok=True)

    # Generate redirect files
    for source, targets in redirects.items():
        target = list(targets)[0]  # Take the first target URL
        filename = f"2014-01-01-{source.replace('/', '-')}.md"
        filepath = os.path.join(redirects_dir, filename)
        
        with open(filepath, 'w') as f:
            f.write(generate_redirect_content(source, target))
        print(f"Created redirect for {source} -> {target}")

if __name__ == '__main__':
    main()
