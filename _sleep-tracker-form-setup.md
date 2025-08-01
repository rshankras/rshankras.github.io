# SleepTracker Waitlist Form Setup Guide

## Form Handling Options

### Option 1: Formspree (Recommended - Free)
1. Go to [Formspree.io](https://formspree.io) and create a free account
2. Create a new form called "SleepTracker Waitlist"
3. Copy the form endpoint (e.g., `https://formspree.io/f/xaybzwkd`)
4. Replace `your-form-id` in the form action with your actual form ID
5. Configure email notifications and redirect to `/sleep-tracker/waitlist-success/`

### Option 2: Netlify Forms (If using Netlify hosting)
1. Add `netlify` attribute to form: `<form netlify name="waitlist">`
2. Netlify will automatically handle form submissions
3. Configure form notifications in Netlify dashboard

### Option 3: EmailJS (Client-side)
1. Sign up at [EmailJS.com](https://www.emailjs.com)
2. Configure email service (Gmail, Outlook, etc.)
3. Replace form with EmailJS implementation

## Current Form Configuration

The waitlist forms are configured with your Formspree endpoint:

```html
<form action="https://formspree.io/f/mqalqoov" method="POST">
```

## Form Fields

- **Email**: Required field for waitlist signup
- **Source**: Hidden field to track where signups come from
- **Timestamp**: Automatically added by form service

## Success Page

After form submission, users will be redirected to:
`/sleep-tracker/waitlist-success/`

## Analytics Integration

Consider adding:
- Google Analytics event tracking
- Facebook Pixel for retargeting
- Email marketing service integration (Mailchimp, ConvertKit)

## Next Steps

1. Choose a form handling service
2. Update the form action URLs
3. Test the form submission
4. Set up email notifications
5. Configure analytics tracking 