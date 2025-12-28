# 30 SwiftUI/iOS Blog Topics - Real-World Examples & Code Snippets

## Debugging & Performance (5 topics)

### 1. Print What Changed: Debug SwiftUI View Updates Like a Pro
**Real-world scenario**: Your expense split app list is re-rendering constantly, draining battery. Use `Self._printChanges()` to find the culprit property causing unnecessary redraws.
```swift
var body: some View {
    let _ = Self._printChanges()
    ExpenseListView(expenses: expenses, totalAmount: total)
}
// Output: ExpenseListView: @State expenses changed.
```

### 2. Why Is My SwiftUI View Rendering 10 Times? Using Instruments to Find the Culprit
**Real-world scenario**: Sleep tracker showing lag when scrolling through 100+ sleep entries. Use SwiftUI Instruments template to identify excessive `body` calls.

### 3. The `@State` vs `@StateObject` Bug That Cost Me 2 Hours: Memory Leaks in SwiftUI
**Real-world scenario**: Fitness app creating new HealthKit manager instances on every view update, causing memory to spike from 50MB to 300MB.

### 4. Debug Your Network Calls Without Proxyman: Using `URLProtocol` for Request Inspection
**Real-world scenario**: API calls failing in production but working in dev. Implement custom URLProtocol to log all requests in-app.

### 5. The Hidden `po` Commands That Saved My Debugging Session
**Real-world scenario**: App crashes when user taps notification. Using `po UIApplication.shared.keyWindow?.rootViewController` to inspect view hierarchy in lldb.

---

## Design Patterns (6 topics)

### 6. Repository Pattern: Stop Mixing Core Data Logic in Your SwiftUI Views
**Real-world scenario**: Expense split app with Core Data fetch requests scattered across 5 different views. Refactor to repository pattern for testability.

### 7. The Coordinator Pattern for SwiftUI Navigation (That Actually Works in 2025)
**Real-world scenario**: Managing complex navigation in fitness app: onboarding → home → workout detail → workout in progress → workout complete.

### 8. Dependency Injection in SwiftUI Without Third-Party Frameworks
**Real-world scenario**: Switching between mock and real HealthKit managers for testing. Using `@EnvironmentObject` and protocol-based injection.

### 9. MVVM is Not Enough: When to Use Interactors in SwiftUI Apps
**Real-world scenario**: Sleep tracker's "analyze sleep quality" feature has 200+ lines of business logic in ViewModel. Extract to Interactor.

### 10. The Service Locator Pattern: Managing Global Dependencies (AnalyticsManager, NetworkManager)
**Real-world scenario**: 15 different views need access to analytics and network managers. Implement lightweight service locator vs passing through environment.

### 11. State Machine Pattern for Complex UI Flows (App Onboarding, Multi-Step Forms)
**Real-world scenario**: User onboarding with 5 steps, each step can fail, skip, or complete. Using enum-based state machine.

---

## SwiftUI Tips & Tricks (8 topics)

### 12. The `.task()` Modifier That Replaced My `onAppear` + `.onDisappear` Cleanup Code
**Real-world scenario**: Fetching user's expenses when view appears and cancelling network request on disappear. Task handles both automatically.

### 13. Custom View Modifiers: Stop Repeating the Same 5 Lines of Code
**Real-world scenario**: Every card in expense app has same shadow, corner radius, padding. Create `.cardStyle()` modifier.

### 14. The `@AppStorage` Trick for Feature Flags Without Backend
**Real-world scenario**: A/B testing new expense split algorithm. Toggle between old/new logic using AppStorage.

### 15. PreferenceKey: How I Built a Dynamic Tab Bar That Knows Its Content Height
**Real-world scenario**: Custom tab bar that adjusts height based on longest tab title. Use PreferenceKey to bubble up height from children.

### 16. The `GeometryReader` Hack for Responsive Design (Without Breaking Layout)
**Real-world scenario**: Sleep tracker charts need to resize for iPhone SE vs iPhone 15 Pro Max. Using GeometryReader without causing layout issues.

### 17. Lazy Loading in SwiftUI: Stop Loading 1000 Rows at Once
**Real-world scenario**: Expense list with 500+ items causes memory spike. Implement `LazyVStack` with pagination and prefetching.

### 18. The `.onChange` Modifier: Replacing Combine Subscriptions in SwiftUI
**Real-world scenario**: Update chart when date range changes. Using `.onChange(of: dateRange)` instead of Combine `sink`.

### 19. Custom Animations: The `AnimatableModifier` That Made My Charts Smooth
**Real-world scenario**: Bar chart bars jump to new values. Implement AnimatableModifier for smooth transitions.

---

## HealthKit & System Integration (3 topics)

### 20. HealthKit Authorization: The Right Way to Ask for 15+ Permissions
**Real-world scenario**: Sleep tracker needs sleep data, heart rate, steps. Batching permissions vs one-by-one UX considerations.

### 21. Background Fetch for HealthKit: Syncing Sleep Data While App Is Closed
**Real-world scenario**: User tracks sleep with Apple Watch. App needs to fetch new sleep data at 8 AM daily for analysis.

### 22. Core Data + CloudKit: Syncing User's Expenses Across iPhone and iPad
**Real-world scenario**: User splits expense on iPhone, expects to see it on iPad immediately. Handling merge conflicts.

---

## Error Handling & Edge Cases (3 topics)

### 23. The `Result` Type: Cleaner Error Handling Than `do-catch` Everywhere
**Real-world scenario**: Network layer with 10 API endpoints. Using Result<T, APIError> for consistent error handling.

### 24. Graceful Degradation: When HealthKit Permission Is Denied
**Real-world scenario**: Sleep tracker's core feature needs sleep data, but user denies permission. Fallback to manual entry.

### 25. The Force Unwrap That Crashed in Production: Lessons in Optional Handling
**Real-world scenario**: `UserDefaults.standard.string(forKey: "userId")!` crashes when user clears app data. Defensive programming.

---

## Testing & Code Quality (2 topics)

### 26. Testing SwiftUI Views Without UI Tests: ViewInspector Basics
**Real-world scenario**: Testing expense split calculation displayed correctly in view without slow UI tests.

### 27. The Async/Await Refactor That Reduced My Code by 40%
**Real-world scenario**: Replacing completion handlers in networking layer with async/await. Before/after comparison.

---

## App Store & Production (3 topics)

### 28. The In-App Review Prompt That Increased My Ratings by 3x
**Real-world scenario**: Prompting after user successfully splits 3rd expense (moment of value) vs random prompt on app open.

### 29. Feature Flags Using Remote Config: Gradual Rollout Without App Store Review
**Real-world scenario**: New sleep analysis algorithm. Roll out to 10% of users first, monitor crash rate before 100% rollout.

### 30. The Analytics Event That Told Me Users Were Stuck (And How I Fixed It)
**Real-world scenario**: 40% of users abandon expense split on "Add Friends" screen. Analytics revealed confusing UI copy.

---

## Notes:
- All topics include real-world scenarios from your actual apps (Expense Split, Sleep Tracker, Fitness apps)
- Each has concrete code snippets potential
- Mix of quick tips (5-min read) and deeper dives (10-15 min read)
- Covers debugging, patterns, SwiftUI, system integration, production concerns
- Based on actual indie developer pain points, not just theory
