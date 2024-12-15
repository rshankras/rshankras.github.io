---
permalink: /redirects/
title: "Redirects"
---

<!-- Example of redirecting an old WordPress post to an external blog -->
<script>
var redirects = {
    '/building-a-simple-photo-gallery-app-in-swiftui': 'https://rshankar.com'
    // Add more redirects as needed
};

var path = window.location.pathname;
if (path.endsWith('/')) {
    path = path.slice(0, -1);
}
if (redirects[path]) {
    window.location.href = redirects[path];
}
</script>
