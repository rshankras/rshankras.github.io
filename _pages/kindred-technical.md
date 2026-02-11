---
title: "Kindred Coach — Technical Documentation"
permalink: /kindred-technical/
layout: single
author_profile: false
sitemap: false
---

> **100% on-device AI coaching** — built with Swift, SwiftUI, SwiftData, Apple Foundation Models, and RevenueCat. No servers, no external APIs, no cloud. 145 automated tests.

---

### At a Glance

| | |
|---|---|
| **Language** | Swift 6 |
| **UI** | SwiftUI (Apple's modern interface framework) |
| **Data** | SwiftData (stored locally on the device) |
| **AI** | Apple Foundation Models (runs on-device, no server calls) |
| **Purchases** | RevenueCat SDK |
| **Platform** | iOS 26+, iPhone only |
| **Tests** | 145 (unit tests + AI integration tests + full user-flow tests) |
| **External dependencies** | RevenueCat only — everything else is built-in Apple technology |

---

## Architecture

Kindred follows the MVVM pattern (Model-View-ViewModel) — a standard way to separate the user interface from the business logic. Shared state is passed through the app using SwiftUI's environment system.

### How a Conversation Works

```
User sends a message
  --> The app saves it to the local database
  --> Builds a system prompt for the AI
        (combines coach personality + user's values/goals + memory from past sessions)
  --> Streams the AI response word-by-word from the on-device model
  --> Updates the screen in real-time as words arrive
  --> Saves the complete response to the database

When a session ends
  --> The AI analyzes the full conversation
  --> Generates a structured insight
        (key theme, patterns, emotion, actionable suggestion)
  --> Saves the insight locally
  --> The next session with the same coach includes this insight as memory
```

### Data Models

Five data models, all stored locally on the device:

```
User (one per device)
  |
Coach  <---->  ChatSession  (deleting a coach removes all its sessions)
                    |
                 Message     (deleting a session removes all its messages)

SessionInsight  (linked to a session by ID)
```

| Model | What it stores |
|-------|---------------|
| **User** | Name, personal values, goals, what they're currently working on |
| **Coach** | Name, icon, personality/instructions, whether it's a Pro coach |
| **ChatSession** | Links to a coach, contains all messages, tracks when it started |
| **Message** | The text content, who said it (user or coach), timestamp |
| **SessionInsight** | Summary, key theme, thinking patterns, suggestion, dominant emotion |

### How the AI Knows What to Say

Every coach has personality instructions stored as text. The app checks the format and picks the right approach:

| Approach | When it's used | Coach types |
|----------|---------------|-------------|
| **Structured template** | Instructions are stored as a detailed JSON template with role, framework, rules, and examples | Pre-built coaches and AI-generated custom coaches |
| **Simple instructions** | Instructions are plain text written by the user | Manually created custom coaches |

For structured coaches, the AI receives a layered prompt built from:

| # | Layer | What it provides |
|---|-------|-----------------|
| 1 | Role & personality | "You are a clarity coach who is warm and curious..." |
| 2 | Coaching framework | 3-5 named phases the coach follows |
| 3 | Behavioral rules | "Ask one question at a time", "Keep responses under 40 words" |
| 4 | User context | The user's name, values, and goals personalized into the prompt |
| 5 | Memory | Insights from the last 3 sessions with this coach |
| 6 | Example conversations | Sample exchanges showing how the coach should respond |
| 7 | Reminders | "Always end with an actionable next step" |

### Coach Memory — How Coaches Remember You

Each coach builds up memory over time:

```
Session 1 ends
  --> AI generates an insight (theme, patterns, suggestion)
  --> Stored on the device

Session 2 starts
  --> App retrieves the last 3 insights for this coach
  --> Formats them as "here's what you learned about this person"
  --> Feeds this into the AI's instructions
  --> The coach naturally references past conversations
```

- Users can clear a coach's memory at any time
- Mid-session quick reflections are kept separate and don't pollute memory
- Limited to the 3 most recent sessions to stay within the AI's processing capacity

### Handling the AI's Conversation Limit

The on-device AI can only process about 4,096 tokens (roughly 3,000 words) at a time. Here's how the app manages this:

| Strategy | How it works |
|----------|-------------|
| **Automatic session rotation** | After 24 messages, the app proactively starts a fresh AI session before hitting the limit |
| **Conversation summary** | Before rotating, the last 20 messages are summarized and carried into the new session for continuity |
| **Error recovery** | If the AI signals it's run out of space, the app automatically rotates and retries — the user doesn't see an error |
| **Response filtering** | Sometimes the AI accidentally includes its own instructions in a response. The app catches and removes this in real-time |

### Custom Coach Creation

| Mode | How it works | AI approach |
|------|-------------|-------------|
| **Manual** | User writes a name and personality description in their own words | Simple instructions — the app wraps it with coaching structure |
| **AI-assisted** | User describes the kind of coach they want, and the AI generates a complete coaching template with framework, rules, examples, and starter questions | Structured template — full coaching methodology |

---

## RevenueCat Implementation

### Setup

RevenueCat is initialized when the app launches, and the purchase manager is made available to every screen in the app.

```swift
// When the app starts
init() {
    PurchaseManager().configure()
}
```

### Product & Entitlement

| | |
|---|---|
| **Entitlement** | "Kindred Coach Pro" — unlocks all Pro features |
| **Product** | One-time lifetime purchase at $9.99 |
| **Package type** | Lifetime (not a subscription) |

### What the Purchase Manager Does

| Action | What happens |
|--------|-------------|
| **Initialize** | Connects to RevenueCat when the app launches |
| **Load offerings** | Fetches the current product and price to display on the upgrade screen |
| **Check entitlement** | Checks whether the user has already purchased Pro |
| **Purchase** | Handles the Apple Pay flow and confirms success or cancellation |
| **Restore** | Lets users restore a previous purchase (e.g., after reinstalling) |

### How Pro Status Flows Through the App

```
RevenueCat confirms purchase
  --> PurchaseManager updates its "Pro is active" flag
  --> AppState picks up the change
  --> All screens instantly reflect Pro status (locks removed, features unlocked)
```

### Where the Upgrade Screen Appears

The upgrade screen is shown when users try to access Pro features:

| Action | What the user sees |
|--------|-------------------|
| Tapping a locked Pro coach | "Unlock with Pro" message with upgrade button |
| Trying to create a custom coach | Gate screen explaining this is a Pro feature |
| Tapping "Upgrade" in Settings | Direct access to the upgrade screen |

### Free vs Pro

| Feature | Free | Pro |
|---------|:----:|:---:|
| 5 pre-built coaches | Yes | Yes |
| Unlimited conversations | Yes | Yes |
| Session insights | Yes | Yes |
| Coach memory | Yes | Yes |
| Create custom coaches | — | Yes |
| Import shared coaches | — | Yes |

---

## Privacy

| Aspect | How it works |
|--------|-------------|
| **AI processing** | Runs entirely on the device — no data sent to any server |
| **Data storage** | Everything stored locally on the phone — no cloud sync |
| **Accounts** | None required — no sign-up, no login |
| **Analytics** | Only RevenueCat's minimal purchase tracking |
| **Offline use** | Fully functional offline (after the initial product catalog loads) |

---

## Testing the AI

> **145 tests** — ~125 unit tests + ~20 real AI tests covering 9 different scenarios

Testing on-device AI is one of the hardest parts of this project. The AI isn't always available (it requires specific hardware), responses are different every time, and the conversation limit is small. We built a two-layer testing approach to handle this.

### The Challenge

Apple's on-device AI requires Apple Intelligence hardware. You can't fully simulate it, every response is slightly different, and long conversations can overflow the AI's memory. Tests need to handle all of this gracefully.

### Two-Layer Testing Strategy

| Layer | What it tests | How it runs |
|-------|--------------|-------------|
| **Simulated AI** | Everything around the AI — chat flow, error handling, screen states, data saving | Always runs, always passes — uses a fake AI stand-in |
| **Real AI** | Actual conversations with the on-device model, structured output, multi-turn coaching | Skips automatically if the AI hardware isn't available |

### Layer 1: Tests with Simulated AI

The chat system is designed so we can swap in a fake AI service during testing. This lets us test things that are hard to reproduce with real AI:

| Test | What it checks |
|------|---------------|
| Sending a blank message | The app correctly ignores it |
| AI not available | The right error message is shown to the user |
| Message saving | User messages are stored and the input field clears |
| Loading states | The "typing..." indicator appears and disappears at the right times |

### Layer 2: Tests with Real AI

These tests run actual conversations with Apple's on-device model. Each test checks if the AI is available first — if not, it skips instead of failing:

```swift
@Test(.timeLimit(.minutes(5)))
func prebuiltCoachConversation() async throws {
    let service = FoundationModelsService()
    guard service.isAvailable else { return }  // Skip if AI unavailable
    // ... run real conversation with the model
}
```

### 9 Scenarios Tested with Real AI

| # | Scenario | What it proves |
|---|----------|---------------|
| 1 | **Pre-built coach, 5-turn conversation** | A structured coach produces coherent, multi-turn coaching responses |
| 2 | **User-created coach conversation** | A coach created with simple text instructions also works well with the AI |
| 3 | **AI-generated coach creation, then chat** | Full pipeline: user describes a coach, AI builds it, then a real conversation works |
| 4 | **Share a coach, import it, then chat** | The sharing system preserves the coach's personality through export and import |
| 5 | **Session insight generation** | After a conversation, the AI produces a valid summary, patterns, theme, and suggestion |
| 6 | **Mid-session reflection** | A quick reflection mid-conversation is correctly generated and labeled |
| 7 | **AI-generated coach template** | The AI generates all required coaching fields (framework steps, rules, example conversations) |
| 8 | **Coach memory in prompts** | Past session insights are correctly included when starting a new conversation |
| 9 | **AI availability check** | The "available" and "unavailable" signals are always consistent |

### Key Testing Patterns We Learned

| What we do | Why it matters |
|-----------|---------------|
| **Skip tests when AI is unavailable** | Tests skip cleanly instead of failing — the full test suite runs on any machine |
| **Poll for completion instead of waiting a fixed time** | AI generation speed varies — we check every 200ms instead of guessing how long to wait |
| **Keep conversations short (max 5 turns)** | The AI's memory limit is small — long test conversations would overflow and hide the real thing being tested |
| **Verify the AI respects constraints** | We check that it generates the right number of items (e.g., 3-5 framework steps, 1-3 patterns) |
| **Test both coach types separately** | Structured coaches and simple text coaches produce different AI prompts — both need validation |
| **Use a temporary database for each test** | Each test gets its own fresh database so tests don't interfere with each other |
