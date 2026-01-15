---
title: "Claudit - Track Claude Code Usage Costs"
layout: single
permalink: /claudit/
author_profile: true
toc: true
toc_sticky: true
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
description: "A native macOS menu bar app that tracks your Claude Code usage and calculates API costs in real-time. Monitor tokens, quotas, and spending with beautiful analytics—all while keeping your data private on your Mac."
keywords: "Claude Code, API cost tracker, macOS menu bar app, Claude AI usage monitoring, API tracking, cost calculator, developer tools, productivity, privacy-first, token tracking, quota monitoring"
og_title: "Claudit - Track Claude Code Usage Costs for macOS"
og_description: "Monitor Claude Code API usage and costs in real-time from your menu bar. Beautiful analytics, quota tracking, and privacy-first design."
og_type: "website"
twitter_card: "summary_large_image"
twitter_title: "Claudit - Track Claude Code Usage Costs for macOS"
twitter_description: "Track Claude Code API usage and costs in real-time. All data stays private on your Mac."
---

## Track Your Claude Code Spending, Effortlessly

Never wonder about your API costs again. Claudit runs quietly in your menu bar, automatically tracking your Claude Code usage and calculating costs in real-time—all while keeping your data 100% private on your Mac.

<a href="https://rshankar.com/downloads/claudit" class="app-store-link">Download Direct →</a>

## Why You Need This

### The Problem
- You use Claude Code frequently but don't track your actual costs
- API pricing is per-token, making it hard to estimate monthly spending
- No built-in way to see usage patterns across projects
- Need to manually check Anthropic dashboards or calculate costs yourself
- Can't identify which projects are costing the most

### The Solution
Claudit monitors your Claude Code activity, tracks tokens used, and calculates costs automatically. See your spending at a glance from the menu bar, understand which projects cost most, and optimize your usage—all without leaving your editor.

## Features

### Real-Time Cost Tracking
- Automatic monitoring of Claude Code API calls
- Token count display (input, output, cache read/write)
- Real-time cost calculation based on current API pricing
- Cumulative costs for Today, This Week, This Month, and All Time
- Model usage breakdown (Opus, Sonnet, Haiku)
- Beautiful cost cards with token counts in K/M/B format

### Project Insights
- Identify which projects cost the most
- Time range filtering (Week, Month, All Time)
- Search and sort projects by cost, tokens, or name
- See percentage of total spending per project
- Track usage across all your Claude Code projects
- Discover expensive projects you didn't know about

### Quota Management
- Live quota tracking for session (5-hour) and weekly limits
- Per-model quota monitoring (Sonnet and Opus tracked separately)
- Color-coded indicators (Green/Yellow/Red) for quota status
- Pacing warnings when on track to hit limits before reset
- Countdown to quota reset times
- Percentage and cost-based quota displays

### Cache Efficiency
- Track prompt cache hit rates
- See how much you've saved by caching
- Today vs Week cache efficiency comparison
- Cache read/write token breakdowns
- Understand caching effectiveness

### Dashboard Analytics
- 4 organized tabs: Overview, Projects, Models, Efficiency
- Daily cost chart with time range selector
- Model distribution donut chart
- Daily breakdown table (cost, tokens, messages, sessions, tool calls)
- AI-powered insights and recommendations
- Interactive visualizations with Swift Charts

## App Experience

### Menu Bar Quick View
<figure style="margin: 0 0 30px 0; text-align: center;">
  <img src="/assets/images/claudit/menu-bar.png" alt="Claudit Menu Bar"
       style="max-width: 400px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
  <figcaption style="margin-top: 12px; color: #666;">Quick access to quota status, cost summary cards, and top 3-4 projects right from your menu bar.</figcaption>
</figure>

### Dashboard Overview
<figure style="margin: 0 0 30px 0; text-align: center;">
  <img src="/assets/images/claudit/dashboard-overview.png" alt="Dashboard Overview"
       style="max-width: 100%; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
  <figcaption style="margin-top: 12px; color: #666;">Overview tab with daily cost chart, model distribution, and detailed daily breakdown table.</figcaption>
</figure>

### Projects Tab
<figure style="margin: 0 0 30px 0; text-align: center;">
  <img src="/assets/images/claudit/dashboard-projects.png" alt="Projects Tab"
       style="max-width: 100%; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
  <figcaption style="margin-top: 12px; color: #666;">Full project list with search, sort, and time range filtering. See which projects cost most over different periods.</figcaption>
</figure>

### Models Tab
<figure style="margin: 0 0 30px 0; text-align: center;">
  <img src="/assets/images/claudit/dashboard-models.png" alt="Models Tab"
       style="max-width: 100%; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
  <figcaption style="margin-top: 12px; color: #666;">Detailed model breakdown showing Input, Output, Cache Read, and Cache Write costs per model.</figcaption>
</figure>

### Efficiency Tab
<figure style="margin: 0 0 30px 0; text-align: center;">
  <img src="/assets/images/claudit/dashboard-efficiency.png" alt="Efficiency Tab"
       style="max-width: 100%; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
  <figcaption style="margin-top: 12px; color: #666;">Cache efficiency metrics and AI-powered recommendations to help you optimize costs.</figcaption>
</figure>

### Settings
<figure style="margin: 0 0 30px 0; text-align: center;">
  <img src="/assets/images/claudit/settings.png" alt="Settings Panel"
       style="max-width: 100%; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
  <figcaption style="margin-top: 12px; color: #666;">Configure API key for quota tracking, customize model pricing, and adjust display preferences.</figcaption>
</figure>

## Perfect For

**AI-Assisted Developers**
If you use Claude Code regularly for development, Claudit helps you understand and optimize your API spending without manual tracking.

**Freelancers & Agencies**
Track AI development costs per project to accurately bill clients or stay within project budgets.

**Budget-Conscious Teams**
Monitor costs in real-time across all team projects to ensure you stay within your AI development budget.

**Power Users**
Optimize your Claude Code usage by identifying expensive patterns, leveraging cache efficiency, and making informed model choices.

## 100% Private by Design

- **All Local**: Cost data and usage history stored only on your Mac with SwiftData
- **No Cloud Sync**: Zero external servers or cloud syncing—your data never leaves your computer
- **No Telemetry**: No usage tracking, analytics, or data collection of any kind
- **Secure Storage**: Optional Anthropic API key stored securely in macOS Keychain
- **Your Data**: Full control—export anytime, delete anytime, uninstall removes everything

### How It Works
Claudit reads your local Claude Code session files from `~/.claude/projects/*/[session].jsonl` to calculate accurate token usage and costs. It also optionally fetches real-time quota data from the Anthropic API if you provide your API key.

**Data sources:**
1. **JSONL session files** (local) - Token counts, cache usage, project paths
2. **SwiftData cache** (local) - Historical data for fast loading
3. **Anthropic API** (optional) - Real-time quota utilization only (requires API key)

## Technical Excellence

- **Built with SwiftUI** for a modern, native macOS experience
- **MVVM + Observable architecture** for reliability and maintainability
- **SwiftData** for efficient local caching and fast app startup (~58ms initial load)
- **Swift Charts** for beautiful, interactive visualizations
- **Background parsing** optimized for performance (~1-2 seconds for today's data)
- **Intelligent caching** parses only today's files after initial bootstrap
- **macOS 14.0+ (Sonoma)** and later
- **Universal binary** (Intel and Apple Silicon)

### Performance
- **Initial load**: ~58ms (from SwiftData cache)
- **Background parsing**: ~1-2s (parses today's files + project breakdowns)
- **Bootstrap**: ~4-5s (first run parses full month, then caches)

## Download

<a href="https://rshankar.com/downloads/claudit" class="app-store-link">Download Direct →</a>

Distributed directly—no App Store sandbox restrictions. Download, drag to Applications, and start tracking your Claude Code costs immediately.

**Requirements:** macOS 14.0 (Sonoma) or later

### Support

Have questions or feedback? I'd love to hear from you.

**Contact**: [ravi@rshankar.com](mailto:ravi@rshankar.com)

### Legal
- [Privacy Policy](/claudit/privacy/)

---

*Track smarter. Code faster. Know your costs.*
