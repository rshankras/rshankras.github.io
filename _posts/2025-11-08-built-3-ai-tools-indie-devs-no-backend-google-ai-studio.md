---
title: "I Built 3 AI Tools for Indie Devs in 3 Days (No Backend Required)"
date: "2025-11-08"
permalink: "/built-3-ai-tools-indie-devs-no-backend-google-ai-studio/"
description: "Build AI micro-tools with Google AI Studio: fitness coach, launch planner, and caption writer. Real projects, mistakes, and rapid prototyping lessons."
categories:
  - "ai"
  - "indie-development"
  - "web-development"
  - "entrepreneurship"
tags:
  - "Google AI Studio"
  - "Gemini"
  - "Cloud Run"
  - "Indie Apps"
  - "Rapid Prototyping"
  - "Build in Public"
  - "AI Development"
keywords: "indie developer tools, google ai studio projects, cloud run deployment, rapid prototyping, ai micro tools, build in public, gemini ai"
excerpt_separator: <!--more-->
toc: true
toc_sticky: true
---

Here's the indie developer paradox I live with:

I can build complex iOS apps with Core Data, CloudKit, HealthKit integration—the whole nine yards. But when it comes to simple tasks like writing launch checklists or social media captions, I freeze.

It's not lack of skill. It's decision fatigue.

By the time I've coded all day, designed UI, debugged edge cases, the thought of *also* planning a launch strategy or crafting marketing copy feels insurmountable.

So I built tools to handle it. Three AI micro-services in three days. No backend setup. No server management. Just clear problems and fast solutions.

If you're an indie maker who's great at building but struggles with everything around it, this is what I learned.<!--more-->

## The Challenge: Building ≠ Shipping

I've shipped over a dozen iOS apps. Some did well. Some flopped. The pattern I've noticed?

**The apps that succeeded weren't necessarily better code.**

They succeeded because I:
- Launched at the right time with the right messaging
- Stayed consistent with updates and social posts
- Tracked health metrics and iterated based on data
- Maintained momentum post-launch

All the "non-coding" parts.

But here's the thing: I'm an iOS developer. I love Swift, SwiftUI, solving technical problems. Marketing? Launch planning? Social media? Those feel like context-switching tax.

**The realization:**

What if I could build tiny AI tools that handle these tasks for me?

Not generic ChatGPT prompts. Custom micro-services designed exactly for my workflow.

That's what I set out to build this week.

## Why Google AI Studio + Cloud Run?

Coming from iOS development, I had specific criteria:

- ✅ **Fast iteration**: I wanted to build and test ideas in hours, not days
- ✅ **No infrastructure headache**: I don't want to manage servers or databases
- ✅ **Instant deployment**: TestFlight takes days; I wanted to go live in minutes
- ✅ **Cheap**: These are experiments, not revenue-generating products yet
- ✅ **Shareable**: I wanted to send links to beta testers immediately

Google AI Studio + Cloud Run hit all five.

**The workflow:**

1. Build the service in AI Studio (browser-based)
2. Define input/output JSON schema
3. Deploy to Cloud Run (one click)
4. Get a live URL instantly
5. Iterate based on real usage

No Docker. No backend frameworks. No database migrations.

Just pure focus on the problem I'm solving.

## Tool #1: AI Fitness Coach (Built in 10 Minutes)

### The Problem

I've been building a fitness app for Apple Watch. Users track daily steps, set goals, receive motivational messages.

The challenge: **Writing personalized coaching messages for different scenarios.**

- 3,500 steps at 9 AM → "Great start! Keep it up!"
- 3,500 steps at 9 PM → "Late push needed! You can still hit your goal!"
- 9,000 steps at 2 PM → "You're crushing it today!"

Writing these variations manually is tedious. I needed dynamic, context-aware messaging.

### The Solution

I built a web service that takes:

**Input:**
```json
{
  "current_steps": 3500,
  "goal_steps": 10000,
  "time_of_day": "evening",
  "coaching_tone": "coach"
}
```

**Output:**
```json
{
  "headline_text": "3.5K",
  "message_short": "Late push needed!",
  "message_long": "It's evening, and you've logged 3,500 steps. That's solid effort, but you've got work to do. Your goal is 10,000—time to lace up and close the gap. Let's finish strong!"
}
```

### How I Built It

**Step 1: Defined the schema in Google AI Studio**

Instead of building forms and UI first (my iOS instinct), I started with the data contract. What goes in? What comes out?

This shift in thinking—from UI-first to data-first—was surprisingly freeing.

**Step 2: Prompted the AI with context**

I gave Gemini 2.5 Pro this context:

> "You're a fitness coach. Based on someone's current steps, goal, and time of day, generate motivational messages. Adjust tone: if it's morning and they're ahead, celebrate. If it's evening and they're behind, motivate urgency without guilt."

**Step 3: Tested with different scenarios**

- Morning + low steps = "Get moving early!"
- Afternoon + high steps = "You're crushing it!"
- Evening + behind = "Late push, you've got this!"

**Step 4: Deployed to Cloud Run**

One click. Live in 30 seconds.

**Total time:** ~10 minutes.

### The Apple Watch Connection

Here's where it gets interesting.

I previewed how these messages would look on Apple Watch and iPhone. Same data, different screen layouts, consistent motivational tone.

This is the bridge I've been looking for: **AI-generated content + native Apple experiences.**

My SwiftUI app can call this Cloud Run endpoint, get contextual messages, and display them beautifully on Apple Watch complications or iPhone widgets.

**Rookie mistake #1:**

I initially tried to generate the UI in AI Studio too. Bad idea. The web preview looked fine, but translating HTML/CSS to SwiftUI was messy.

**The fix:** Use AI Studio for *logic and content*. Use SwiftUI for *native UI*. They're perfect partners.

### What I Learned

**1. Tiny services are powerful**

This isn't a full-featured fitness app. It's one micro-service: steps + context → motivational message.

But that's all I needed. By keeping scope small, I shipped fast.

**2. Context matters more than cleverness**

The AI doesn't need complex prompts. It needs *context*: time of day, progress percentage, user's goal.

Give good context, get good output.

**3. JSON schemas force clarity**

Defining input/output upfront made me think through edge cases:
- What if `current_steps` > `goal_steps`?
- What if `time_of_day` is invalid?
- Should `coaching_tone` be "friendly" or "coach" or "blunt"?

This upfront thinking saved debugging time later.

## Tool #2: Launch Checklist Generator (Built in 10 Minutes)

### The Problem

Every indie dev I know (myself included) has experienced this:

**You finish building the app… and then freeze at the launch step.**

- What do I post?
- In what order should things happen?
- Did I forget something important?
- Is 2 hours enough to launch, or do I need 2 weeks?

I've launched apps both ways: rushed 2-hour sprints and meticulously planned 2-week campaigns. Both can work. The key is having a *plan*.

But making the plan? That's where I procrastinate.

### The Solution

I built LaunchPad AI: a launch checklist generator for indie devs.

You enter:
- Your app name
- App category
- Launch timeline (2 hours / 1 week / 2 weeks)

It returns a structured, time-based checklist:

**Example output (2-hour sprint):**

**Pre-launch Readiness (T-0 to T-0)**
- ✅ Finalize app name and tagline
- ✅ Prepare App Store screenshots
- ✅ Write compelling app description

**Launch Hour (T-0 to T+1)**
- ✅ Submit to Product Hunt
- ✅ Post on X/Twitter with demo video
- ✅ Share in relevant Slack/Discord communities

**Post-Launch (T+1 to T+3 days)**
- ✅ Respond to all comments and feedback
- ✅ Monitor crash reports and fix critical bugs
- ✅ Share user testimonials

**For a 2-week timeline**, it adds:
- Pre-launch landing page
- Email list building
- Beta tester recruitment
- Teaser campaign

### How I Built It

**Step 1: Interviewed myself**

I listed every launch I'd done: what worked, what I forgot, what I'd do differently.

Then I turned that into prompt context.

**Step 2: Structured the output**

I didn't just want a blob of text. I wanted:
- Grouped tasks (Product / Social / App Store / Post-launch)
- Time-based phases
- Actionable items, not vague suggestions

**Step 3: Added interactivity**

The tool lets you:
- Add custom tasks
- Edit existing tasks
- Delete irrelevant tasks
- Export the final checklist to PDF

This took the longest—maybe 40 of the 60 total minutes.

**Step 4: Deployed and tested**

I used it for a real launch (the fitness app). It worked.

Instead of thinking "What do I do next?", I just followed the list.

**Rookie mistake #2:**

I initially generated checklists that were too generic.

"Promote on social media" → Okay, but *which* platforms? *What* content?

**The fix:** I refined prompts to generate specific, actionable tasks:

- ❌ "Promote on social media"
- ✅ "Post demo video on X/Twitter with 3 key features highlighted"

Specificity beats generality every time.

### What I Learned

**1. Decision fatigue is real**

Even simple decisions ("Should I post on Reddit first or Twitter?") compound when you're doing 20 things at once.

Pre-made checklists eliminate those micro-decisions.

**2. Templates reduce stress**

Knowing I can generate a launch plan in 30 seconds removes the "I don't know where to start" paralysis.

Now launching feels: clear, doable, repeatable.

**3. Export matters**

Being able to export to PDF means I can print it, check it off physically, or share it with collaborators.

This small feature made the tool 10x more useful.

## Tool #3: Caption Generator (Built in 15 Minutes)

### The Problem

I'm terrible at social media.

Not the technical side—I can record videos, edit screenshots, use scheduling tools. But the *writing*?

Every time I sit down to write a post about my app, I stare at a blank screen for 20 minutes.

**The inner monologue:**

- Is this too salesy?
- Should I be more casual?
- Do I sound like every other indie dev?
- What hashtags actually work?

By the time I've written something, I've lost momentum.

### The Solution

I built a caption generator designed specifically for indie app developers.

**Input:**
- App name
- What it does
- Target audience
- Tone (friendly / calm / energetic / professional)
- Auto-generate hashtags: Yes/No

**Output:**
- 5 different caption variations
- Hashtag set
- Call-to-action line

**Example:**

*App:* Expense Split
*What it does:* Splits expenses among roommates, couples, friends
*Audience:* Roommates, couples, friends
*Tone:* Friendly

**Generated captions:**

1. "Splitting expenses shouldn't mean splitting friendships. Expense Split makes it easy to track who owes what—no awkward conversations needed. Perfect for roommates, couples, and friend groups."

2. "Ever had that moment where someone says 'I'll Venmo you later' and… never does? Expense Split keeps everyone honest (and friendly). Track shared costs, settle up fast."

3. "Money + relationships = complicated. Expense Split keeps it simple. Add expenses, split them fairly, done. Built for roommates who want to stay friends."

4. "Stop doing mental math every time you grab dinner with friends. Expense Split handles the math, you handle the fun."

5. "Because 'I'll pay you back' shouldn't require a spreadsheet. Expense Split: fair splits, zero stress."

**Hashtags:** #ExpenseTracking #PersonalFinance #IndieApp #RoommateLife #SplitBills

**CTA:** "Try it free → [link]"

### How I Built It

**Step 1: Analyzed what works**

I looked at successful indie dev posts on X/Twitter and Product Hunt. Common patterns:

- Start with a relatable pain point
- Show the solution concisely
- End with clear CTA
- Friendly, conversational tone
- 1-3 sentences max

**Step 2: Turned patterns into prompts**

I gave Gemini these guidelines:

> "Write scroll-friendly social media captions for indie apps. Start with a pain point or relatable moment. Keep it under 3 sentences. Avoid buzzwords like 'game-changer' or 'revolutionary.' Be specific, not generic."

**Step 3: Added variety**

One caption isn't enough. Sometimes I need playful, sometimes urgent, sometimes calm.

The tool generates 5 variations so I can pick what fits my mood (or A/B test).

**Step 4: Made it fast**

Fill out the form, hit generate, get 5 captions in 3 seconds.

No more staring at blank screens.

**Rookie mistake #3:**

The first version generated captions that all sounded the same. Boring.

**The fix:** I added explicit instructions for variety:

- Caption 1: Pain-point focused
- Caption 2: Benefit-focused
- Caption 3: Scenario-based
- Caption 4: Question hook
- Caption 5: Bold statement

Now the outputs feel distinct.

### What I Learned

**1. Good prompts = good outputs**

The difference between "write a caption" and "write a scroll-friendly caption starting with a relatable pain point" is huge.

Specificity in prompts = quality in results.

**2. Options reduce perfectionism**

When I write manually, I agonize over every word. Is this the *perfect* caption?

With 5 variations, I just pick one and move on. Good enough is good enough.

**3. This works for me *because* I built it**

Generic caption generators exist. But they don't know my audience (indie devs, iOS users, people who appreciate authenticity).

Custom tools tuned to your niche > one-size-fits-all.

## Deploying to Cloud Run: The 30-Second Workflow

Here's the deployment process for all three tools:

**In Google AI Studio:**

1. Click "Deploy"
2. Select "Cloud Run"
3. Choose region (I use `us-central1`)
4. Click "Deploy"

**That's it.**

30 seconds later, I get a live URL:

```
https://fitness-coach-abc123-uc.a.run.app
```

**No configuration. No servers. No DevOps.**

For someone who's used to:
- TestFlight provisioning
- App Store review wait times
- Backend server setup (EC2, Docker, etc.)

This feels like magic.

**Cost:**

Cloud Run has a generous free tier. All three of these tools combined cost me **$0.00** so far because usage is low.

When they scale, pricing is pay-per-request. For micro-tools like these, that's perfect.

## What These Tools Taught Me

### 1. Micro-tools > Mega-platforms

I used to think tools had to be comprehensive to be useful.

"If I'm building a launch planner, it should also handle marketing analytics, email campaigns, social scheduling…"

No.

**A tool that does one thing really well beats a tool that does ten things poorly.**

These three tools are tiny. Single-purpose. And that's why they work.

### 2. Speed Unlocks Experimentation

In iOS development, the feedback loop is long:

- Code → Compile → Test → Debug → Repeat

With Google AI Studio + Cloud Run:

- Prompt → Test → Deploy → Share

The cycle is *minutes*.

This changes how I think about ideas. Instead of "Is this worth building?", I just build it and find out.

### 3. AI for Content, Native for Experience

Here's my new mental model:

**Use AI Studio for:**
- Backend logic
- Content generation
- Data transformation
- Quick prototypes

**Use Swift/SwiftUI for:**
- Native UI
- Offline features
- Platform-specific integrations (HealthKit, Widgets, Complications)
- Performance-critical code

**Use them together** for:
- SwiftUI app → calls Cloud Run endpoint → displays AI-generated content in beautiful native UI

This hybrid approach gives me the best of both worlds.

### 4. Context Switching Is Expensive

Before these tools, my workflow looked like this:

1. Code for 2 hours
2. Switch to marketing mode (write captions, plan launch)
3. Lose momentum
4. Struggle to get back into coding flow

Now:

1. Code for 2 hours
2. Open caption generator, get 5 options in 10 seconds
3. Back to coding in 30 seconds

Minimizing context switches keeps me in flow longer.

### 5. Tiny Tools Compound

One micro-tool is nice. Three micro-tools start to feel like a workflow.

I can imagine a future where I have:
- 10 tiny AI tools
- Each solving one specific problem
- All integrated into my daily routine

That's more powerful than one big monolithic platform.

## Rookie Mistakes Summary

Here's what I learned the hard way:

### Mistake #1: Trying to generate UI in AI Studio

**Problem:** Web UI doesn't translate well to native SwiftUI.

**Fix:** Use AI Studio for logic/content. Use Swift for UI.

### Mistake #2: Generic outputs

**Problem:** First versions generated bland, generic text.

**Fix:** Add specificity to prompts. Show examples of what "good" looks like.

### Mistake #3: Overcomplicating input schemas

**Problem:** I added too many optional fields, making the tool confusing.

**Fix:** Start with the minimum viable schema. Add complexity only when needed.

### Mistake #4: Not testing edge cases

**Problem:** Tools broke when users entered unexpected input (negative steps, invalid dates, etc.).

**Fix:** Test thoroughly before deploying. Add validation.

### Mistake #5: Forgetting to add export/share features

**Problem:** Generated great content but no way to save or share it.

**Fix:** Always include export (PDF, JSON, clipboard) from day one.

## What's Next

I'm participating in the #CloudRunHackathon and building one useful mini-tool every day.

**Coming up:**
- Screenshot to alt-text generator (for accessibility)
- Changelog writer (turns commit messages into user-friendly release notes)
- Pricing calculator (helps indie devs decide on pricing tiers)

All built with the same stack: Google AI Studio + Cloud Run.

**Why?**

Because these are problems I actually have. And building solutions for myself means they'll be genuinely useful for other indie devs too.

## Try It Yourself

If you're an indie maker and you've been curious about AI but intimidated by the complexity, here's my advice:

**Start with one annoying task in your workflow.**

For me, it was:
- Writing motivational messages for my fitness app
- Planning launches
- Writing social captions

For you, it might be:
- Generating app descriptions
- Writing support emails
- Summarizing user feedback

**Then build the tiniest possible tool to solve it.**

Don't aim for perfection. Aim for "works well enough that I'd use it tomorrow."

Google AI Studio makes this trivial. You can have a working prototype in 10 minutes.

**Deploy it. Use it. Iterate.**

If it saves you 10 minutes a day, that's 60 hours a year. Worth it.

## Final Thoughts

I've been an iOS developer for years. I love the craft of building native apps—the elegance of SwiftUI, the satisfaction of pixel-perfect animations, the joy of seeing someone use my app in the wild.

But I'm also a solo indie developer. I wear all the hats: coder, designer, marketer, support, finance.

**These AI micro-tools let me offload the parts I'm not great at** (or don't enjoy) **without hiring a team.**

- Need motivational messaging? Tool handles it.
- Need a launch plan? Tool generates it.
- Need social captions? Tool writes them.

I'm still doing the hard work—building the app, solving real user problems, iterating based on feedback.

But the surrounding tasks? Automated.

**This is the future I'm excited about:**

Not AI replacing developers. But AI *augmenting* indie makers so we can focus on what we do best.

And tools like Google AI Studio + Cloud Run make it accessible to anyone willing to experiment.

**So go build something tiny. Ship it today. See what happens.**

You might surprise yourself.

---

*If you want to try the working versions of these tools (deployed on Cloud Run), let me know! I'm sharing access as I build in public.*

*Follow along for daily updates as I build more micro-tools for indie developers: [@rshankra](https://x.com/rshankra)*

**Resources:**

- [Google AI Studio](https://aistudio.google.com)
- [Cloud Run Documentation](https://cloud.google.com/run/docs)
- [Cloud Run Hackathon](https://cloud.google.com/run/hackathon)
- [Gemini API Reference](https://ai.google.dev/docs)

**Related posts:**

- [From Xcode to No Code: Building AI Apps with Google AI Studio](/xcode-no-code-building-ai-apps-google-ai-studio/) (platform overview and getting started)
- [My Learnings as Indie App Developer: Building Identity Habits](/my-learnings-as-indie-app-developer/) (on indie dev workflows and habits)
- [Building TwAIst: An AI Twitter Assistant](/building-twaist-ai-twitter-assistant-chrome-built-in-ai/) (more on AI integration strategies)
