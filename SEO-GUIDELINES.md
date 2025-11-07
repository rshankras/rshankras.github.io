# SEO Guidelines for Blog Posts

This document outlines SEO best practices for creating new blog posts on rshankar.com.

## Required Front Matter for Every Post

Every blog post should include these essential fields in the front matter:

```yaml
---
title: "Your SEO-Optimized Title (50-60 characters)"
date: "YYYY-MM-DD"
description: "Compelling meta description that includes primary keyword (120-155 characters)"
categories:
  - "primary-category"
  - "secondary-category"
tags:
  - "Relevant Tag 1"
  - "Relevant Tag 2"
image: "/assets/images/post-slug/featured-image.png"
permalink: "/post-slug/"
excerpt_separator: <!--more-->
---
```

## Essential SEO Elements

### 1. Title Optimization
- **Length**: 50-60 characters (displays well in search results)
- **Include primary keyword** near the beginning
- **Be specific and descriptive**
- **Avoid clickbait** - be accurate

**Good Examples:**
```
✅ "Building a SwiftUI Stopwatch App with Lap Timing"
✅ "Understanding iOS Delegate Pattern: A Beginner's Guide"
✅ "How to Fix CFBundleVersion Error in Xcode"
```

**Bad Examples:**
```
❌ "Stopwatch" (too short, not descriptive)
❌ "You Won't Believe How Easy This iOS Pattern Is!!!" (clickbait)
❌ "The Ultimate Complete Comprehensive Guide to Everything About iOS Development" (too long)
```

### 2. Meta Descriptions
- **Length**: 120-155 characters
- **Include primary keyword** naturally
- **Add a call-to-action** when appropriate
- **Be compelling** - this is your ad copy in search results

**Template:**
```
Learn [topic] with [approach]. [Benefit statement]. [Optional CTA].
```

**Good Examples:**
```
✅ "Learn how to build a SwiftUI stopwatch with lap timing. Complete tutorial with code examples and best practices."
✅ "Master the iOS delegate pattern with simple explanations and real-world examples. Perfect for beginners."
```

**Bad Examples:**
```
❌ "In this post I will talk about..." (boring, no value)
❌ "A blog post about SwiftUI" (too vague)
❌ [leaving it blank - lets search engines guess]
```

### 3. Featured Images (Open Graph)
Every post should have a featured image for social sharing:

**Specifications:**
- **Size**: 1200x630px (optimal for all platforms)
- **Format**: PNG or JPG
- **File size**: < 1MB (optimize for web)
- **Location**: `/assets/images/[post-slug]/featured.png`

**Image Content Guidelines:**
- Include post title or key visual
- Use readable fonts (min 48pt)
- High contrast for readability
- Brand colors when appropriate
- No text in critical areas (edges can be cropped)

**Front Matter:**
```yaml
image: "/assets/images/building-twaist/featured.png"
og_image: "/assets/images/building-twaist/featured.png"  # Optional, uses 'image' if not set
```

### 4. Image Alt Text
All images in content must have descriptive alt text:

```markdown
# Good - descriptive and keyword-rich
![TwAIst welcome screen showing multi-step composer interface](/assets/images/twaist/welcome.png)

# Bad - generic or missing
![Screenshot](/assets/images/twaist/welcome.png)
![](/assets/images/twaist/welcome.png)
```

### 5. URL Structure (Permalinks)
Use descriptive, keyword-rich URLs:

```yaml
# Good
permalink: "/building-swiftui-stopwatch-app-lap-timing/"
permalink: "/understanding-ios-delegate-pattern/"

# Bad
permalink: "/post-123/"  # not descriptive
permalink: "/2024/01/11/post/"  # date-based (unless intentional)
```

**Current standard**: `/:title/`

### 6. Categories & Tags

**Categories** (2-3 max):
- Primary topic areas
- Used for navigation
- Examples: `swift`, `swiftui`, `ios`, `watchos`, `ai`, `chrome-extensions`

**Tags** (4-8 recommended):
- Specific topics within the post
- More granular than categories
- Use title case
- Examples: `SwiftUI`, `Xcode`, `UIKit`, `Core Data`

```yaml
categories:
  - "swiftui"
  - "tutorial"
tags:
  - "SwiftUI"
  - "Stopwatch"
  - "Timer"
  - "iOS Development"
  - "Xcode"
```

### 7. Keywords (Optional but Recommended)

Add a keywords field for additional SEO context:

```yaml
keywords: "SwiftUI stopwatch, iOS timer app, lap timing tutorial, SwiftUI tutorial, iOS development"
```

### 8. Excerpt Separator

Always include an excerpt separator to control preview text:

```yaml
excerpt_separator: <!--more-->
```

Place `<!--more-->` after 1-2 compelling paragraphs (150-200 words).

## Enhanced Front Matter Template

For maximum SEO impact, use this comprehensive template:

```yaml
---
title: "Your SEO-Optimized Title (50-60 chars)"
date: "2025-11-01"
permalink: "/your-post-slug/"
description: "Compelling meta description with primary keyword (120-155 characters)"
categories:
  - "primary-category"
  - "secondary-category"
tags:
  - "Relevant Tag 1"
  - "Relevant Tag 2"
  - "Relevant Tag 3"
keywords: "primary keyword, secondary keyword, related terms"
image: "/assets/images/post-slug/featured.png"
og_title: "Title optimized for social sharing"
og_description: "Description optimized for social sharing (may differ from meta description)"
og_image: "/assets/images/post-slug/social.png"
og_type: "article"
twitter_card: "summary_large_image"
twitter_title: "Twitter-specific title (if different)"
twitter_description: "Twitter-specific description"
excerpt_separator: <!--more-->
toc: true  # Enable table of contents for long posts
toc_sticky: true
last_modified_at: "2025-11-01"  # Update when making significant changes
---
```

## Content Writing Guidelines

### Heading Structure
Use proper heading hierarchy for SEO and accessibility:

```markdown
# H1 - Post Title (automatically generated from front matter)

## H2 - Main Sections
Use H2 for primary sections. Include keywords naturally.

### H3 - Subsections
Use H3 for subsections within H2 blocks.

#### H4 - Detailed Points
Use sparingly for very detailed breakdowns.
```

**Best Practices:**
- Only one H1 per page (the title)
- Don't skip heading levels (don't jump from H2 to H4)
- Include keywords in headings naturally
- Make headings descriptive and scannable

### Internal Linking
Link to related posts within your content:

```markdown
Learn more about [SwiftUI basics](/swiftui-basics/)
or check out our [complete SwiftUI guide](/swiftui-guide/).
```

**Target:** 2-5 internal links per post to related content

### External Linking
Link to authoritative sources:
- Apple documentation
- Official GitHub repos
- Reputable tech blogs
- Original research/sources

Always use descriptive anchor text (not "click here").

### Content Length
- **Minimum**: 300 words
- **Optimal**: 1,000-2,000 words for tutorials
- **Long-form**: 2,000+ words for comprehensive guides

**Quality over quantity** - every word should add value.

### Code Blocks
Use syntax highlighting for better readability:

```markdown
\`\`\`swift
// Your Swift code here
struct ContentView: View {
    var body: some View {
        Text("Hello, World!")
    }
}
\`\`\`
```

### First Paragraph
Your opening paragraph is critical for SEO:
- Include primary keyword naturally
- Hook the reader with value proposition
- Summarize what they'll learn
- Keep it 2-3 sentences

**Example:**
```markdown
Learn how to build a sophisticated stopwatch app using SwiftUI with lap timing
functionality. This step-by-step tutorial covers state management, timer
implementation, and creating an intuitive user interface.<!--more-->
```

## Image Optimization Checklist

- [ ] Featured image created (1200x630px)
- [ ] All images compressed/optimized
- [ ] All images have descriptive alt text
- [ ] Images stored in `/assets/images/[post-slug]/`
- [ ] Image file names are descriptive (not IMG_1234.png)

## Pre-Publishing SEO Checklist

Before publishing any post, verify:

- [ ] Title is 50-60 characters with primary keyword
- [ ] Meta description is 120-155 characters
- [ ] Featured image added (og_image/image field)
- [ ] All images have alt text
- [ ] Permalink is descriptive and keyword-rich
- [ ] 2-3 categories assigned
- [ ] 4-8 relevant tags added
- [ ] Excerpt separator placed after intro (<!--more-->)
- [ ] 2-5 internal links to related posts
- [ ] Proper heading hierarchy (H2 → H3 → H4)
- [ ] First paragraph includes primary keyword
- [ ] Content is 300+ words (1000+ for tutorials)
- [ ] Code blocks use syntax highlighting
- [ ] External links open in new tab (if desired)
- [ ] Date is correct format (YYYY-MM-DD)

## Post-Publishing Tasks

After publishing:

1. **Test the post**:
   - [ ] Verify URL loads correctly
   - [ ] Check mobile responsiveness
   - [ ] Test all internal/external links
   - [ ] Verify images load properly

2. **Social Media**:
   - [ ] Share on Twitter with relevant hashtags
   - [ ] Share on LinkedIn
   - [ ] Add to relevant communities (if appropriate)

3. **Monitor**:
   - [ ] Check Google Search Console for indexing
   - [ ] Monitor analytics for traffic
   - [ ] Respond to comments/engagement

## Tools & Resources

### SEO Tools
- **Google Search Console**: Monitor indexing and performance
- **Google Analytics**: Track traffic and user behavior
- **Twitter Card Validator**: https://cards-dev.twitter.com/validator
- **LinkedIn Post Inspector**: https://www.linkedin.com/post-inspector/
- **Facebook Sharing Debugger**: https://developers.facebook.com/tools/debug/

### Image Tools
- **Optimization**: TinyPNG, ImageOptim
- **Design**: Canva, Figma, Photoshop
- **Screenshots**: CleanShot X, Xnapper

### Keyword Research
- **Google Keyword Planner**
- **Ahrefs** (if available)
- **Answer the Public**
- **Google Trends**

## Common Mistakes to Avoid

1. **Missing meta descriptions** - Always write your own
2. **Duplicate content** - Each post should be unique
3. **Thin content** - Minimum 300 words, prefer 1000+
4. **No internal links** - Link to related posts
5. **Generic images** - Create custom featured images
6. **Missing alt text** - Accessibility and SEO issue
7. **Keyword stuffing** - Use keywords naturally
8. **Broken links** - Test all links before publishing
9. **No mobile testing** - Always check mobile view
10. **Ignoring analytics** - Review what works

## Questions?

For questions about these guidelines or SEO best practices, refer to:
- [Google Search Central](https://developers.google.com/search)
- [Moz Beginner's Guide to SEO](https://moz.com/beginners-guide-to-seo)
- Jekyll documentation for technical questions

---

**Last Updated**: 2025-11-01
**Version**: 1.0
