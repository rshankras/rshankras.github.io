---
title: "Kindred Coach — Technical Documentation"
permalink: /kindred-technical/
layout: single
author_profile: false
sitemap: false
---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Swift 6 |
| UI | SwiftUI |
| Persistence | SwiftData (local only) |
| AI | Apple Foundation Models (on-device) |
| Purchases | RevenueCat SDK |
| Platform | iOS 26+, iPhone only |
| Testing | Swift Testing framework (145 tests) |
| External dependencies | RevenueCat only — everything else is native Apple |

There are no servers, no APIs, no cloud services. The entire app runs locally on the user's device.

## Architecture

Kindred follows MVVM with `@Observable` and uses environment injection for shared state.

### Data Flow

```
User sends message
  → ChatViewModel saves it to SwiftData
  → ChatViewModel calls FoundationModelsService
  → Service builds a system prompt (coach persona + user context + memory)
  → Service streams response from on-device Foundation Model
  → ChatViewModel updates UI with each token
  → Complete response saved to SwiftData

Session ends
  → InsightGenerator analyzes the conversation
  → Generates structured insight (theme, patterns, suggestion)
  → Saved as SessionInsight in SwiftData
  → Next session with same coach includes this insight as memory
```

### Data Models (SwiftData)

Five models, all stored locally:

- **User** — name, values, goals, current context. Single instance.
- **Coach** — name, icon, system prompt (JSON template or plain text), starter questions, isPro flag.
- **ChatSession** — links to a Coach, contains Messages, tracks timestamps.
- **Message** — content, role (user/assistant), timestamp.
- **SessionInsight** — summary, key theme, patterns, suggestion, emotion. Linked by session ID.

Relationships: Coach → ChatSession → Message (cascade delete). SessionInsight linked to sessions via `sessionId`.

### The Two Prompt Paths

Every coach has a `systemPrompt` field. The app checks what format it's in and picks the right path:

**Rich path** — If `systemPrompt` contains valid JSON (a `CoachPromptTemplate`), the app builds a detailed system prompt with sections for role, personality, coaching framework with phases, rules, user context, memory from past sessions, and example conversations. Used by all pre-built coaches and AI-generated custom coaches.

**Fallback path** — If `systemPrompt` is plain text, the app wraps it with a generic coaching structure and the user's context. Used by manually-created custom coaches.

The prompt is assembled by `PromptBuilder` in this order:

1. Role and personality
2. Coaching framework (name, description, 3-5 phases)
3. Behavioral rules
4. User context (name, values, goals — substituted via `{userName}`, `{userValues}`, `{userGoals}`)
5. Memory from past sessions (last 3 session insights)
6. Few-shot example conversations
7. Critical reminders and action orientation

### Coach Memory

`CoachMemoryService` gives each coach continuity across sessions:

- After each session, `InsightGenerator` (an actor) uses Foundation Models with `@Generable` structured output to produce a `SessionInsight` — summary, key theme, patterns, dominant emotion, and a suggestion.
- On the next session, `CoachMemoryService` fetches the last 3 insights for that coach, formats them as a memory section, and injects them into the system prompt.
- Users can clear a coach's memory. This sets `coach.memoryClearedAt` — only insights created after that date are included.

### Context Window Management

The on-device model has a ~4096 token context window. The app handles this:

- Proactive session rotation at 24 messages — before the window fills up.
- On rotation, the last 20 messages are summarized and carried into a new `LanguageModelSession` for continuity.
- If the model throws `exceededContextWindowSize`, the app automatically rotates and retries.
- Response sanitization strips any leaked system prompt content.

### Custom Coach Creation

Two modes:

- **Manual** — User writes a name and personality description. Stored as plain text in `systemPrompt`. Uses fallback prompt path.
- **AI-assisted** — User describes the coach they want. `CoachTemplateGenerator` (an actor) uses Foundation Models with `@Generable` to produce a `GeneratedCoachTemplate` with role, personality, framework, rules, examples, and starter questions. This is JSON-encoded into `systemPrompt` and uses the rich prompt path.

## RevenueCat Implementation

### Setup

RevenueCat is configured at app launch in `KindredApp.init()`:

```swift
init() {
    PurchaseManager().configure()
}
```

`PurchaseManager` is an `@Observable` class injected into the environment so all views can access purchase state.

### Entitlement

One entitlement: `"Kindred Coach Pro"`.

One product: a lifetime (one-time) purchase at $9.99.

### Purchase Flow

`PurchaseManager` handles everything:

| Method | What it does |
|--------|-------------|
| `configure()` | Initializes RevenueCat SDK |
| `loadOfferings()` | Fetches the current offering from RevenueCat |
| `checkEntitlement()` | Checks if `"Kindred Coach Pro"` is active |
| `purchase(_ package:)` | Executes purchase, returns success/failure |
| `restorePurchases()` | Restores previous purchases |

All methods are `@MainActor` for thread safety.

### State Sync

Pro status flows from RevenueCat → PurchaseManager → AppState → Views:

```swift
// In KindredApp.swift
.task {
    await purchaseManager.checkEntitlement()
    appState.isPro = purchaseManager.isProActive
}
.onChange(of: purchaseManager.isProActive) { _, newValue in
    appState.isPro = newValue
}
```

### Paywall

`PaywallView` displays the lifetime package from the current offering. It shows three value props (create custom coaches, unlock pro coaches, support indie development), the localized price, and a restore purchases option.

The paywall is triggered from three places:
- Tapping a locked Pro coach in the coach library
- Trying to create a custom coach without Pro
- The upgrade button in Settings

All trigger `appState.showPaywall = true`, which presents the paywall as a sheet.

### What's Free vs Pro

| Feature | Free | Pro |
|---------|------|-----|
| 5 pre-built coaches | Yes | Yes |
| Unlimited conversations | Yes | Yes |
| Session insights | Yes | Yes |
| Coach memory | Yes | Yes |
| Create custom coaches | No | Yes |
| Import shared coaches | No | Yes |

The free tier is generous by design — users get the full coaching experience. Pro unlocks creative tools (making and sharing coaches), which drives word-of-mouth growth.

## Privacy

- All AI processing happens on-device via Apple Foundation Models. No API calls.
- All data stored locally in SwiftData. No cloud sync.
- No accounts, no sign-in.
- RevenueCat collects minimal purchase analytics only.
- The app works fully offline (after initial RevenueCat offering fetch).

## Testing Foundation Models

Testing on-device AI is one of the hardest parts of building with Foundation Models. The model isn't always available, responses are non-deterministic, and the context window is small. We built a layered testing strategy that covers both deterministic behavior and real AI interactions across different scenarios.

### The Challenge

Foundation Models run on-device and require Apple Intelligence hardware. You can't mock the model itself, responses vary between runs, and the ~4096 token context window means multi-turn conversations need careful management. Tests need to handle all of this gracefully.

### Testing Strategy: Two Layers

**Layer 1: Deterministic tests with mock AI** — These test everything around the AI without calling it. We created a `MockCoachAIService` protocol implementation that returns configurable responses, letting us test the chat flow, error handling, and UI state transitions reliably.

**Layer 2: Real Foundation Models integration tests** — These call the actual on-device model to verify that prompts produce reasonable coaching responses, structured output generates valid insights, and multi-turn conversations work end-to-end.

### Mock-Based Tests (Always Run, Always Pass)

`ChatViewModel` accepts an injectable `CoachAIService`, defaulting to the real `FoundationModelsService` in production. In tests, we swap in `MockCoachAIService`:

```swift
let mockService = MockCoachAIService()
mockService.isAvailable = false
mockService.unavailabilityReason = "AI not available for testing"
let vm = ChatViewModel(session: session, modelContext: context, aiService: mockService)
```

This lets us test scenarios that are hard to reproduce with real AI:
- **Empty input handling** — verifies the app ignores whitespace-only messages
- **AI unavailable state** — verifies the correct error message surfaces when Foundation Models isn't available
- **Message persistence** — verifies user messages save to SwiftData and input clears after send
- **State transitions** — verifies `isGenerating` flags toggle correctly during the chat flow

### Real Foundation Models Integration Tests

These tests call the actual on-device model. Every FM test starts with an availability guard — if the model isn't available (e.g., running on simulator without Apple Intelligence), the test skips gracefully instead of failing:

```swift
@Test(.timeLimit(.minutes(5)))
func prebuiltCoachConversation() async throws {
    let service = FoundationModelsService()
    guard service.isAvailable else { return }
    // ... test with real model
}
```

We use a polling helper instead of fixed delays, since generation time varies:

```swift
private func waitForGeneration(_ vm: ChatViewModel) async throws {
    let deadline = Date().addingTimeInterval(30)
    while await MainActor.run(body: { vm.isGenerating }) {
        if Date() > deadline { break }
        try await Task.sleep(for: .milliseconds(200))
    }
}
```

### Scenarios Tested with Real AI

**1. Pre-built coach multi-turn conversation** — Creates a coach with a structured JSON template (rich prompt path), sends 5 messages simulating a real career coaching session, and verifies the model responds to each turn with non-empty content. Tests that the coaching framework, user context, and conversation history all work together.

**2. Manual custom coach conversation** — Creates a coach with plain text personality (fallback prompt path), sends multi-turn messages about motivation, and verifies the fallback prompt produces coherent coaching responses. Confirms both prompt paths work with the real model.

**3. AI-assisted coach creation → conversation** — End-to-end test that generates a complete coach template using `CoachTemplateGenerator` with `@Generable` structured output, saves it, then has a 5-turn conversation with the AI-created coach. Verifies the full pipeline: user describes a coach → AI generates structured template → template encodes to JSON → coach uses rich prompt path → real conversation works.

**4. Export → import → conversation** — Creates a manual coach, exports it via `CoachExporter`, imports it back, then has a real conversation with the imported coach. Verifies the entire sharing pipeline preserves the coach personality through serialization.

**5. Session insight generation** — Feeds a realistic 8-message coaching conversation into `InsightGenerator` and verifies the `@Generable` structured output produces valid fields: non-empty summary, 1-3 patterns, a key theme, dominant emotion, repeated words, and an actionable suggestion.

**6. Quick reflection generation** — Tests the mid-session reflection path (triggered at 6+ messages) and verifies the insight is correctly marked as `isQuickReflection = true` with all fields populated.

**7. Coach template generation** — Tests `CoachTemplateGenerator` with a natural language description and verifies the structured output contains all required fields: role, personality, 3-5 framework steps, 5-7 rules, 3 example exchanges, 3 starter questions, and context instructions. Also verifies the coach name appears in the generated content.

**8. Prompt building with memory** — Creates a coach with past session insights in SwiftData, builds a prompt, and verifies the memory context ("MEMORY FROM PAST SESSIONS") is correctly injected with themes from previous conversations.

**9. Availability consistency** — Verifies that `isAvailable` and `unavailabilityReason` are always consistent — if one says available, the other confirms it.

### Key Testing Patterns for Foundation Models

A few things we learned building these tests:

- **Always guard on availability.** FM tests should skip, not fail, when the model isn't present. This lets the full test suite run on any machine.
- **Use polling, not fixed sleeps.** Generation time varies. A polling helper that checks `isGenerating` every 200ms with a 30-second deadline is more reliable than `Task.sleep(for: .seconds(10))`.
- **Keep multi-turn tests short.** The ~4096 token context window fills fast. We cap integration tests at 5 turns to avoid context overflow masking the thing we're actually testing.
- **Test structured output constraints.** `@Generable` structs define count ranges (e.g., `@Guide(.count(3...5))`). Tests verify the model respects these — 3-5 framework steps, 1-3 patterns, exactly 3 examples.
- **Test both prompt paths.** The rich path (JSON template) and fallback path (plain text) produce different system prompts. Both need real FM tests to confirm the model responds well to each format.
- **Use in-memory SwiftData.** `SwiftDataTestSupport.makeContext()` creates isolated in-memory containers so FM tests can read/write models without touching the real database.
