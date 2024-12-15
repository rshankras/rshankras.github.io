---
layout: home
author_profile: true
---

<div class="newsletter-signup" style="padding: 20px; background-color: #f8f9fa; border-radius: 5px; margin: 20px 0;">
  <h2>Stay Updated</h2>
  <p>Subscribe to my newsletter for iOS development tips and updates.</p>
  
  <form
    action="https://buttondown.email/api/emails/embed-subscribe/YOUR_USERNAME"
    method="post"
    target="popupwindow"
    onsubmit="window.open('https://buttondown.email/YOUR_USERNAME', 'popupwindow')"
    class="newsletter-form">
    <div style="display: flex; gap: 10px; max-width: 500px;">
      <input
        type="email"
        name="email"
        placeholder="your@email.com"
        style="padding: 8px; border: 1px solid #ddd; border-radius: 4px; flex-grow: 1;">
      <input
        type="submit"
        value="Subscribe"
        style="padding: 8px 16px; background-color: #007bff; color: white; border: none; border-radius: 4px; cursor: pointer;">
    </div>
  </form>
  <p style="font-size: 0.8em; margin-top: 10px;">No spam. Unsubscribe at any time.</p>
</div>