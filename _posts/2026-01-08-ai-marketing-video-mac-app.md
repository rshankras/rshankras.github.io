---
layout: post
title: "How I Made a Marketing Video for My Mac App Using AI — And What Went Wrong"
date: 2026-01-08
categories: indie design
tags: ai-video marketing google-veo elevenlabs ffmpeg video-editing indie-dev macos
description: "Learn how I created a 30-second marketing video for my Mac app using Google Veo, ElevenLabs, and ffmpeg with zero additional budget—and the mistakes I made along the way."
---

I built a Mac app called EaseEyes. It reminds you to take eye breaks when you're not in a meeting. Simple idea, but I needed a way to show people what it does.

I'm not a video editor. I don't have a budget for agencies or stock footage subscriptions. But I already pay for Claude Code Max ($100/month) for development work. What if I could use it for marketing too?

Here's what happened.

## Table of Contents
- [The Goal](#goal)
- [The Tools](#tools)
- [Generating Video Clips](#video-clips)
- [Using Real Screenshots](#screenshots)
- [Generating Voiceover](#voiceover)
- [Adding Music](#music)
- [Creating Vertical Versions](#vertical)
- [Adding End Card](#end-card)
- [Final Result](#result)
- [Key Learnings](#learnings)
- [Would I Do It Again?](#conclusion)

## The Goal {#goal}

A 30-second ad that shows the problem (endless screen time) and the solution (EaseEyes). Something I could post on YouTube, Twitter, and Instagram Reels.

I wrote a simple script:

```markdown
We spend our days in meetings.
Hour after hour.
Our eyes pay the price.

But what if your screen could be... kinder?

EaseEyes.
It knows when you're in a call.
It reminds you when you're not.

Your eyes deserve a break.
```

Now I needed visuals to match.

## The Tools {#tools}

Here's what I used:

| Tool | Cost | Purpose |
|------|------|---------|
| **Google Veo** | Free tier | AI video generation |
| **ElevenLabs** | Free tier | AI voiceover |
| **Claude Code Max** | $100/mo (already paying) | ffmpeg orchestration |
| **My screenshots** | Free | Actual app UI |

**Total additional cost:** $0

This is the beauty of the free tiers—if you're strategic, you can create real marketing assets without new expenses.

## Generating Video Clips {#video-clips}

I used Google Veo to generate 8 short clips:

```markdown
Shot List:
1. Close-up of tired eyes
2. Person at desk with Zoom calls
3. Clock showing time passing
4. Person rubbing their eyes
5. EaseEyes notification appearing
6. Person looking out window
7. Back to video call, notification pauses
8. Person smiling, refreshed
```

For each one, I wrote a prompt like:

```
Professional home office, person sitting at desk with multiple monitors
showing video call grid, afternoon light through window, cinematic
```

Veo generated 8-second clips for each. But here's where things got interesting.

### What Went Wrong #1: Different People in Every Shot

Each time Veo generated a clip, it created a different person. My "tired office worker" was a different human in every single shot.

**The fix for next time:** Use a tool like Google Nano or Banana to generate a reference person first, then pass that reference to each video prompt. This keeps the same "actor" throughout.

For this video, I decided to lean into it—framing it as "different people, same problem."

### What Went Wrong #2: The Clock Didn't Work

My prompt said "time-lapse of clock." Veo gave me a clock where only the second hand moved. The hour and minute hands stayed frozen.

**The lesson:** AI prompts need to be specific about what should animate.

```markdown
❌ Bad prompt:
Time-lapse of analog clock on wall

✅ Better prompt:
Time-lapse of analog clock, hour hand and minute hand visibly moving
clockwise showing passage of several hours, light transitioning from
afternoon to evening
```

### What Went Wrong #3: Veo Watermark

Every Veo clip had a watermark in the bottom-right corner. Not ideal for a polished ad.

**The fix:** I used ffmpeg to crop 60 pixels from the bottom and right edges, then scaled back to 1080p. Watermark gone.

```bash
ffmpeg -i input.mp4 \
  -vf "crop=1860:1020:0:0,scale=1920:1080" \
  output.mp4
```

## Using Real Screenshots {#screenshots}

For shots 5 and 7 (showing the actual EaseEyes notification), I didn't use AI. I took real screenshots of my app.

**Why?** Because AI mockups of your own UI never look right. Real screenshots are more authentic and show exactly what users will get.

I used a Ken Burns effect (slow zoom) to add motion:

```bash
ffmpeg -loop 1 -i screenshot.png \
  -vf "zoompan=z='1+0.15*on/100':x='iw-iw/zoom':y='0':d=100:s=1920x1080" \
  -t 4 output.mp4
```

This zooms slowly into the top-right corner where the notification appears.

**Recommendation:** Always use real screenshots for your actual product UI. Let AI handle the conceptual/emotional shots.

## Generating Voiceover {#voiceover}

I used ElevenLabs to generate the narration. But here's a key learning:

**Don't generate one long voiceover clip.**

Instead, generate each line separately:
- "We spend our days in meetings."
- "Hour after hour."
- "Our eyes pay the price."
- etc.

This lets you place each line at exactly the right moment to sync with the visuals.

### What Went Wrong #4: Voiceover Timing

My first attempt had the voiceover starting at shot boundaries. "Hour after hour" played during the home office shot, not the clock.

**The fix:** Map voiceover to visual meaning, not timing.

| Shot | Visual | Voiceover |
|------|--------|-----------|
| 1 | Tired eyes | *(music only — visual hook)* |
| 2 | Home office | "We spend our days in meetings." |
| 3 | Clock | "Hour after hour." |
| 4 | Rubbing eyes | "Our eyes pay the price." |

Now "hour after hour" plays when you see the clock. Much better.

## Adding Music {#music}

I found a relaxing ambient track and mixed it at about 12% volume—loud enough to set the mood, quiet enough to not compete with the voiceover.

```markdown
Key settings:
- Fade in over 2 seconds at the start
- Fade out over 2 seconds at the end
- Keep it low when voiceover is playing
- Use copyright-free music (YouTube Audio Library, Epidemic Sound)
```

## Creating Vertical Versions {#vertical}

Here's something I wish I'd planned from the start: **vertical video matters more than horizontal.**

YouTube Shorts, Instagram Reels, TikTok—they're all 9:16 vertical. That's where the eyeballs are.

I had to convert my horizontal videos to vertical after the fact. For most shots, center crop worked fine. But for the notification screenshots, I needed a "smart crop" that kept the right side of the frame where the UI appears.

**Lesson for next time:** Plan for vertical first. Frame your AI prompts so subjects are centered.

```bash
# Convert horizontal to vertical (center crop)
ffmpeg -i horizontal.mp4 \
  -vf "crop=1080:1920" \
  vertical.mp4

# Smart crop (keep specific area)
ffmpeg -i horizontal.mp4 \
  -vf "crop=1080:1920:840:0" \
  vertical-right.mp4
```

## Adding End Card {#end-card}

Every marketing video needs a call-to-action. I created a simple end card with the App Store badge and added it as the final 4 seconds.

Made sure to create both:
- Horizontal version (1920x1080)
- Vertical version (1080x1920)

## Final Result {#result}

Four videos ready to post:

| Platform | Aspect | Duration | Use Case |
|----------|--------|----------|----------|
| YouTube/Twitter | 16:9 | 35 seconds | Standard video posts |
| YouTube (long) | 16:9 | 62 seconds | More detail |
| YouTube Shorts | 9:16 | 34 seconds | Short-form vertical |
| Instagram Reels | 9:16 | 60 seconds | Full vertical experience |

**Total time:** About 3 hours
**Additional cost:** $0 (used existing Claude Code Max subscription)

[Watch the final result on YouTube Shorts](https://youtube.com/shorts/WBacqQe6cnU)

## Key Learnings {#learnings}

```markdown
1. Generate a reference person first
   → Keep the same "actor" across all shots

2. Be specific in AI prompts
   → Say exactly what should move and how

3. Use real screenshots for your UI
   → More authentic than AI mockups

4. Generate voiceover per line
   → Enables precise timing

5. Map voiceover to visual meaning
   → Not just shot boundaries

6. Plan for vertical first
   → Shorts/Reels are where the audience is

7. Crop out watermarks
   → Simple ffmpeg fix

8. First shot can be music-only
   → Lets the visual hook establish
```

### Cost Breakdown

| Item | Cost |
|------|------|
| Google Veo | $0 (free tier) |
| ElevenLabs | $0 (free tier) |
| Claude Code Max | $0 (already paying for dev) |
| ffmpeg | $0 (open source) |
| Music | $0 (YouTube Audio Library) |
| **Total** | **$0** |

Compare this to hiring a video agency ($2,000-5,000) or stock footage subscriptions ($30-50/month).

## Would I Do It Again? {#conclusion}

Absolutely. The process wasn't perfect, but I ended up with a real marketing video that I can use across all platforms.

The AI tools aren't magic—you still need to direct them carefully and fix their mistakes. But for an indie developer with no video budget, this workflow is a game changer.

**When this approach makes sense:**
- Solo developer with limited budget
- Need quick marketing assets
- Willing to iterate and fix AI mistakes
- Have basic command-line skills (ffmpeg)
- Already using AI tools for development

**When to hire a professional:**
- Brand video for funding pitch
- High-stakes product launch
- Need perfect execution first time
- Budget allows it (revenue > $5k/month)

### Further Reading

- [Essential Tools for Indie Developers](/indie/career/2024/08/19/indie-developer-essential-tools.html)
- [Real Cost of Being an Indie iOS Developer](/indie/career/2024/05/08/indie-developer-costs.html)
- [MVP Mindset: Ship Fast](/indie/career/2024/06/25/mvp-mindset-ship-fast.html)

---

*EaseEyes is a free Mac app that reminds you to take eye breaks. [Download on the Mac App Store](https://apps.apple.com/us/app/eye-rest-timer-ease-eyes/id6475638039)*

---

*The best marketing video is the one you actually ship.*
