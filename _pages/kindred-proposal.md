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
| **Status** | Fully built, 145 tests, ready for App Store |

---

## The Problem

Personal coaching is one of the most effective tools for self-improvement, but it remains inaccessible to most people. Professional coaching is expensive, putting it out of reach for students, early-career professionals, and anyone not backed by a corporate budget.

AI chatbots have attempted to fill this gap, but they come with a fundamental trust problem. To have a meaningful coaching conversation, you need to be honest — about your fears, your failures, your relationships. Most AI apps send every word to a remote server, store it indefinitely, and use it to train future models. People hold back when they know someone might be listening.

**The result:** the people who need coaching the most either can't afford it or don't trust the available alternatives.

## The Solution

Kindred Coach is a private AI coaching app for iPhone that runs entirely on-device using Apple Foundation Models. No accounts, no cloud, no data collection. Your conversations never leave your phone.

The app provides 5 expert-designed coaches, each built on a proven coaching framework — clarity coaching, goal setting, weekly reviews, morning intentions, and stress management. Users pick a coach, have a natural back-and-forth conversation, and receive auto-generated insights at the end: key themes, thinking patterns, and actionable next steps.

What makes Kindred Coach feel like real coaching rather than a chatbot:

- **Coaches remember you.** Insights from past sessions are carried forward, so each conversation builds on the last.
- **Conversations have structure.** Each coach follows a proven framework — they ask good questions rather than giving generic advice.
- **Sessions have closure.** Every conversation ends with a clear takeaway, not an open loop.

## Target Audience

**Primary:** Adults aged 22–40 who are interested in personal growth but have never worked with a professional coach. They journal, read self-help books, listen to podcasts, and are comfortable with technology. They value privacy and are skeptical of apps that harvest personal data.

**Secondary:** Existing coaching clients who want a tool for between-session reflection. People in career transitions, new managers, or anyone facing a specific decision who wants a thinking partner available at any time.

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

Apple Foundation Models launched with iOS 26, making high-quality on-device AI available for the first time without external API costs or privacy trade-offs. This is a new category — apps that offer intelligent, personal experiences with zero data collection. Kindred Coach is built specifically for this moment: the technology finally matches the promise.

## Challenges and Limitations

Building on on-device AI comes with real constraints:

| Challenge | How We Solved It |
|-----------|-----------------|
| ~4096 token context window | Automatic session rotation — the app summarizes the conversation and starts a fresh AI session seamlessly |
| Model leaks system prompt into responses | Real-time sanitization layer strips leaked content during streaming |
| Complex multi-step planning hits limits | Focused on conversational coaching where on-device AI excels |

The on-device model works best with focused, conversational coaching today. But Apple Intelligence capabilities will keep improving with each generation of hardware and software — and Kindred is built to take full advantage as they do.

## Technical Foundation

| | |
|---|---|
| **AI** | 100% on-device — Apple Foundation Models, no external API calls |
| **Storage** | Local only — SwiftData, no cloud sync |
| **Framework** | Native iOS — SwiftUI, built for iPhone |
| **Quality** | 145 automated tests — unit, integration, and end-to-end |
| **Purchases** | RevenueCat — reliable in-app purchase infrastructure |

The app is fully functional, tested, and ready for App Store submission.
