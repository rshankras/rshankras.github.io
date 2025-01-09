import csv
import json

def generate_redirect_js():
    redirects = {}
    
    # Read the CSV file
    with open('../redirects.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            source = row['source']
            target = row['target']
            redirects[source] = target
    
    # Generate the JavaScript code
    js_code = """---
permalink: /redirects/
title: "Redirects"
---

<script>
var redirects = %s;

var path = window.location.pathname;
if (path.endsWith('/')) {
    path = path.slice(0, -1);
}

// Try exact match first
if (redirects[path]) {
    window.location.href = redirects[path];
}
// If no match, try adding a trailing slash
else if (redirects[path + '/']) {
    window.location.href = redirects[path + '/'];
}
</script>
""" % json.dumps(redirects, indent=4)
    
    # Write to the redirects.md file
    with open('../_pages/redirects.md', 'w') as f:
        f.write(js_code)

if __name__ == '__main__':
    generate_redirect_js()
