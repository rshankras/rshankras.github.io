---
title: "Kindred Coach — Technical Documentation"
permalink: /kindred-technical/
layout: single
author_profile: false
sitemap: false
---

> **100% on-device AI coaching** — Swift 6, SwiftUI, SwiftData, Apple Foundation Models, RevenueCat. No servers, no APIs, no cloud. 145 tests.

---

### At a Glance

| | |
|---|---|
| **Language** | Swift 6 |
| **UI** | SwiftUI |
| **Data** | SwiftData (local only) |
| **AI** | Apple Foundation Models (on-device) |
| **Purchases** | RevenueCat SDK |
| **Platform** | iOS 26+, iPhone only |
| **Tests** | 145 (unit + FM integration + E2E) |
| **External deps** | RevenueCat only — everything else is native Apple |

---

## Architecture

Kindred follows MVVM with `@Observable` and uses environment injection for shared state.

### Data Flow

```
User sends message
  --> ChatViewModel saves it to SwiftData
  --> FoundationModelsService builds system prompt
        (coach persona + user context + memory)
  --> Streams response from on-device Foundation Model
  --> ChatViewModel updates UI with each token
  --> Complete response saved to SwiftData

Session ends
  --> InsightGenerator analyzes the conversation
  --> Generates structured insight via @Generable
        (theme, patterns, emotion, suggestion)
  --> Saved as SessionInsight in SwiftData
  --> Next session includes this insight as memory
```

### Data Models

Five SwiftData models, all stored locally:

```
User (singleton)
  |
Coach  <---->  ChatSession  (cascade delete)
                    |
                 Message     (cascade delete)

SessionInsight  (linked via sessionId)
```

| Model | Key Fields |
|-------|-----------|
| **User** | name, values, goals, current context |
| **Coach** | name, icon, systemPrompt (JSON or plain text), isPro |
| **ChatSession** | links to Coach, contains Messages, timestamps |
| **Message** | content, role (user/assistant), timestamp |
| **SessionInsight** | summary, keyTheme, patterns, suggestion, emotion |

### The Two Prompt Paths

Every coach has a `systemPrompt` field. The app detects the format and picks the right path:

| Path | When Used | Coach Types |
|------|-----------|-------------|
| **Rich** (template JSON) | `systemPrompt` decodes as `CoachPromptTemplate` | Pre-built coaches, AI-assisted custom coaches |
| **Fallback** (plain text) | `systemPrompt` is plain text | Manual custom coaches |

**Rich path** builds a detailed system prompt with these layers:

| # | Layer | Source |
|---|-------|--------|
| 1 | Role & personality | Template JSON |
| 2 | Coaching framework | 3-5 named phases |
| 3 | Behavioral rules | Template JSON |
| 4 | User context | Name, values, goals (variable substitution) |
| 5 | Memory | Last 3 session insights via CoachMemoryService |
| 6 | Example conversations | Few-shot from template |
| 7 | Critical reminders | Action orientation |

### Coach Memory

`CoachMemoryService` gives each coach continuity across sessions:

```
Session 1 ends
  --> InsightGenerator produces SessionInsight
  --> Stored in SwiftData

Session 2 starts
  --> CoachMemoryService fetches last 3 insights
  --> Formats as "MEMORY FROM PAST SESSIONS"
  --> Injected into system prompt
  --> Coach references past conversations naturally
```

- Insights filtered by `coach.memoryClearedAt` (users can clear memory)
- Quick reflections excluded from memory context
- Max 3 past sessions to stay within token budget

### Context Window Management

The on-device model has a ~4096 token context window:

| Strategy | Details |
|----------|---------|
| **Proactive rotation** | At 24 messages, before the window fills |
| **Conversation summary** | Last 20 messages summarized and carried into new session |
| **Error recovery** | `exceededContextWindowSize` triggers automatic rotation + retry |
| **Sanitization** | Strips leaked system prompt content from responses in real-time |

### Custom Coach Creation

| Mode | How it works | Prompt path |
|------|-------------|-------------|
| **Manual** | User writes name + personality text | Fallback (plain text) |
| **AI-assisted** | User describes coach, `CoachTemplateGenerator` generates structured template via `@Generable` | Rich (JSON template) |

---

## RevenueCat Implementation

### Setup

RevenueCat is configured at app launch:

```swift
// KindredApp.swift
init() {
    PurchaseManager().configure()
}
```

`PurchaseManager` is `@Observable`, injected into the environment for all views.

### Entitlement & Product

| | |
|---|---|
| **Entitlement** | `"Kindred Coach Pro"` |
| **Product** | Lifetime (one-time) purchase, $9.99 |
| **Package** | `offerings.current?.lifetime` |

### Purchase Flow

| Method | What it does |
|--------|-------------|
| `configure()` | Initializes RevenueCat SDK |
| `loadOfferings()` | Fetches current offering |
| `checkEntitlement()` | Checks if Pro is active |
| `purchase(_ package:)` | Executes purchase, returns success/failure |
| `restorePurchases()` | Restores previous purchases |

All methods are `@MainActor` for thread safety.

### State Sync

Pro status flows through the app in one direction:

```
RevenueCat --> PurchaseManager.isProActive --> AppState.isPro --> Views
```

```swift
// KindredApp.swift
.task {
    await purchaseManager.checkEntitlement()
    appState.isPro = purchaseManager.isProActive
}
.onChange(of: purchaseManager.isProActive) { _, newValue in
    appState.isPro = newValue
}
```

### Paywall Triggers

The paywall is presented as a sheet from three places:

| Trigger | Location |
|---------|----------|
| Tap locked Pro coach | CoachDetailView |
| Create custom coach | CreateCoachView (ProGateView) |
| Upgrade button | SettingsView |

All set `appState.showPaywall = true`.

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

| Aspect | Implementation |
|--------|---------------|
| **AI processing** | On-device via Foundation Models, no API calls |
| **Data storage** | Local SwiftData, no cloud sync |
| **Authentication** | None required — no accounts, no sign-in |
| **Analytics** | RevenueCat minimal purchase analytics only |
| **Offline** | Fully functional (after initial offering fetch) |

---

## Testing Foundation Models

> **145 tests** — ~125 unit tests + ~20 Foundation Models integration tests covering 9 real AI scenarios

Testing on-device AI is one of the hardest parts of building with Foundation Models. The model isn't always available, responses are non-deterministic, and the context window is small. We built a layered testing strategy that covers both deterministic behavior and real AI interactions.

### The Challenge

Foundation Models run on-device and require Apple Intelligence hardware. You can't mock the model itself, responses vary between runs, and the ~4096 token context window means multi-turn conversations need careful management.

### Testing Strategy: Two Layers

| Layer | What it tests | Reliability |
|-------|--------------|-------------|
| **Mock AI** | Chat flow, error handling, UI state, persistence | Always runs, always passes |
| **Real FM** | Actual model responses, structured output, multi-turn conversations | Skips gracefully when model unavailable |

### Layer 1: Mock-Based Tests

`ChatViewModel` accepts an injectable `CoachAIService`, defaulting to `FoundationModelsService` in production. In tests, we swap in `MockCoachAIService`:

```swift
let mockService = MockCoachAIService()
mockService.isAvailable = false
mockService.unavailabilityReason = "AI not available for testing"
let vm = ChatViewModel(session: session, modelContext: context, aiService: mockService)
```

**Scenarios covered:**

| Test | What it verifies |
|------|-----------------|
| Empty input handling | App ignores whitespace-only messages |
| AI unavailable state | Correct error message surfaces |
| Message persistence | User messages save to SwiftData, input clears |
| State transitions | `isGenerating` flags toggle correctly |

### Layer 2: Real Foundation Models Integration Tests

Every FM test starts with an availability guard — skips gracefully instead of failing:

```swift
@Test(.timeLimit(.minutes(5)))
func prebuiltCoachConversation() async throws {
    let service = FoundationModelsService()
    guard service.isAvailable else { return }
    // ... test with real model
}
```

We use a polling helper instead of fixed delays:

```swift
private func waitForGeneration(_ vm: ChatViewModel) async throws {
    let deadline = Date().addingTimeInterval(30)
    while await MainActor.run(body: { vm.isGenerating }) {
        if Date() > deadline { break }
        try await Task.sleep(for: .milliseconds(200))
    }
}
```

### 9 Scenarios Tested with Real AI

| # | Scenario | What it proves |
|---|----------|---------------|
| 1 | **Pre-built coach, 5-turn conversation** | Rich prompt path produces coherent multi-turn coaching |
| 2 | **Manual coach conversation** | Fallback prompt path works with real model |
| 3 | **AI-assisted coach creation + chat** | Full pipeline: describe coach --> generate template --> encode JSON --> conversation works |
| 4 | **Export, import, then chat** | Sharing pipeline preserves coach personality through serialization |
| 5 | **Session insight generation** | `@Generable` produces valid structured output (summary, 1-3 patterns, theme, emotion) |
| 6 | **Quick reflection** | Mid-session reflection correctly marked and all fields populated |
| 7 | **Coach template generation** | Structured output has all required fields (3-5 steps, 5-7 rules, 3 examples) |
| 8 | **Prompt building with memory** | Past session insights correctly injected into system prompt |
| 9 | **Availability consistency** | `isAvailable` and `unavailabilityReason` always agree |

### Key Testing Patterns We Learned

| Pattern | Why |
|---------|-----|
| **Always guard on availability** | FM tests skip, not fail, when model isn't present |
| **Polling over fixed sleeps** | Generation time varies; poll every 200ms with 30s deadline |
| **Short multi-turn tests** | Cap at 5 turns to avoid context overflow masking real issues |
| **Test structured output constraints** | Verify `@Guide(.count(3...5))` ranges are respected |
| **Test both prompt paths** | Rich (JSON) and fallback (plain text) need separate FM validation |
| **In-memory SwiftData** | Isolated containers so FM tests don't touch real database |
