---
title: "Kindred Coach — Written Proposal"
permalink: /kindred-proposal/
layout: single
author_profile: false
sitemap: false
---

> **Kindred Coach** — A private AI coaching app that runs entirely on your device. Pick a coach, have a real conversation, and get clear takeaways — no accounts, no cloud, no tracking.

---

### At a Glance

| | |
|---|---|
| **What** | AI coaching app for iPhone, 100% on-device |
| **Who** | Adults 22-40 interested in personal growth |
| **Model** | Freemium + $9.99 one-time Pro upgrade |
| **AI** | Apple Foundation Models (private, on-device) |
| **Status** | Fully built, 145 tests, in beta via TestFlight |

---

## The Problem

Personal coaching is one of the most effective tools for self-improvement, but it remains inaccessible to most people. Professional coaching is expensive, putting it out of reach for students, early-career professionals, and anyone not backed by a corporate budget.

AI chatbots have attempted to fill this gap, but they come with a fundamental trust problem. To have a meaningful coaching conversation, you need to be honest — about your fears, your failures, your relationships. Most AI apps send every word to a remote server, store it indefinitely, and use it to train future models. People hold back when they know someone might be listening.

And there's a deeper problem: many people don't even know what coaching feels like. They've never experienced someone asking them the right questions. So they never seek it out.

**The result:** the people who would benefit most from coaching either can't access it, don't trust the available alternatives, or don't know it exists.

## The Solution

Kindred Coach is a private AI coaching app for iPhone that runs entirely on your device using Apple's on-device AI. No accounts, no cloud, no data collection. Your conversations never leave your phone.

The app provides 5 expert-designed coaches, each built on a proven coaching framework — clarity coaching, goal setting, weekly reviews, morning intentions, and stress management. You pick a coach, have a natural back-and-forth conversation, and receive auto-generated insights at the end: key themes, thinking patterns, and actionable next steps.

What makes Kindred Coach feel like real coaching rather than a chatbot:

- **Coaches remember you.** Insights from past sessions are carried forward, so each conversation builds on the last.
- **Conversations have structure.** Each coach follows a proven framework — they ask good questions rather than giving generic advice.
- **Sessions have closure.** Every conversation ends with a clear takeaway, not an open loop.
- **Share with your real coach.** Export any session as text — share your conversation and insights with a human coach to deepen the work you're doing together.

## Target Audience

**Primary:** Adults aged 22–40 who are interested in personal growth but have never worked with a professional coach. They journal, read self-help books, listen to podcasts, and are comfortable with technology. They value privacy and are skeptical of apps that harvest personal data.

**Secondary:** Existing coaching clients who want a tool for between-session reflection. Kindred doesn't replace a human coach — it's the practice between sessions, like a gym between training appointments. People in career transitions, new managers, or anyone facing a specific decision who wants a thinking partner available at any time.

**Device requirement:** iPhone 15 Pro or newer with Apple Intelligence enabled. This naturally targets engaged Apple users who invest in their tools — a demographic with high willingness to pay for quality apps.

## Monetization Strategy

Kindred Coach uses a **freemium model with a one-time purchase**.

| | Free | Pro ($9.99 one-time) |
|---|---|---|
| 5 built-in coaches | Included | Included |
| Unlimited conversations | Included | Included |
| Session insights & summaries | Included | Included |
| Coach memory across sessions | Included | Included |
| Create custom coaches | — | Included |
| Import shared coaches | — | Included |

The one-time pricing is a deliberate choice. Coaching is about building a long-term relationship — a subscription creates pressure to justify recurring cost, which undermines the experience. A single purchase removes friction and aligns the business model with user trust.

> **Revenue projection (conservative):** At a 3% free-to-paid conversion rate with 10,000 downloads in the first year, projected revenue is approximately $21,000 after Apple's commission. The one-time model means each new user contributes immediate revenue with no churn.

## Why Now

Apple launched on-device AI (Foundation Models) with iOS 26, making high-quality AI available on your phone for the first time — without sending data to external servers and without API costs. This is a new category: apps that offer intelligent, personal experiences with zero data collection. Kindred Coach is built specifically for this moment.

RevenueCat made the monetization side simple. Instead of building purchase infrastructure from scratch, I integrated RevenueCat in a day — product offerings, purchase verification, upgrade screen, and restore purchases all handled cleanly. That freed up time to focus on what matters: the coaching experience. This project was built for the Shipyard hackathon, and RevenueCat is a core part of how the app makes money.

## Challenges and Limitations

Building on on-device AI comes with real constraints:

| Challenge | How We Solved It |
|-----------|-----------------|
| The AI can only process a limited amount of conversation at once (~4096 tokens) | The app automatically summarizes the conversation and starts a fresh session behind the scenes — the user never notices |
| The AI model sometimes includes its own instructions in responses | A real-time filter catches and removes this before the user sees it |
| Complex multi-step planning can push against the model's limits | We focused on conversational coaching, where on-device AI works best |

The on-device AI works best with focused, conversational coaching today. But Apple Intelligence capabilities will keep improving with each generation of hardware and software — and Kindred is built to take full advantage as they do.

## Technical Foundation

| | |
|---|---|
| **AI** | 100% on-device — Apple's built-in AI, no external servers |
| **Storage** | All data stays on the phone — nothing synced to the cloud |
| **App** | Built natively for iPhone using Apple's latest frameworks |
| **Quality** | 145 automated tests — covering individual features, AI behavior, and full user flows |
| **Purchases** | RevenueCat — handles all purchase logic reliably |

The app is fully functional, tested, and currently in beta via TestFlight. Feedback is welcome — there are known edge cases with coach importing that are being refined.
