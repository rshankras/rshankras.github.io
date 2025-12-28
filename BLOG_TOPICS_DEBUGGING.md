# Blog Topics: Debugging, iOS, macOS, Instruments

## Easy to Verify (Short snippets, conceptual, or tool-focused)

### Instruments Deep Dives
1. **Memory Graph Debugger walkthrough** - Visual tool, screenshots > code
2. **Time Profiler: Finding the real bottleneck** - Interpreting call trees, minimal code
3. **Allocations instrument: Tracking transient memory** - Focus on using the tool
4. **Network Link Conditioner for testing slow connections** - Configuration, not code
5. **Energy Log instrument for battery debugging** - Interpreting graphs

### Xcode Debugging Features
6. **View Hierarchy Debugger secrets** - 3D view debugging, constraint issues
7. **Breakpoint actions beyond po** - Log messages, sounds, shell commands
8. **Symbolic breakpoints for framework code** - E.g., break on `UIViewAlertForUnsatisfiableConstraints`
9. **Quick Look in debugger** - Custom types with `debugQuickLookObject()`
10. **Environment overrides** - Dark mode, dynamic type, accessibility testing

### Console/Logging
11. **OSLog vs print: Structured logging** - Simple API, easy to test
12. **Console.app for device logs** - Filtering, persistence
13. **signpost for measuring intervals** - Small API surface

### Crash Analysis
14. **Reading crash logs without symbolicating** - Pattern recognition
15. **Common crash signatures and what they mean** - Educational, examples from Apple docs

## Moderate to Verify

16. **Thread Sanitizer findings explained** - Show common warnings, fixes
17. **Address Sanitizer: Catching memory corruption** - Requires triggering bugs

## macOS-Specific

18. **Activity Monitor deep dive for devs** - Energy, disk, network tabs
19. **Debugging sandboxing issues** - Console filtering, entitlement errors
20. **Notarization troubleshooting** - `spctl` and `codesign` commands

---

## Beginner Topics

### Xcode Basics
21. **Your first breakpoint: Stop, inspect, continue** - Basic breakpoint usage
22. **The Debug Area explained** - Variables view, console, what each panel shows
23. **Print debugging done right** - When and how to use `print()` effectively
24. **Reading error messages in Xcode** - Decoding red/yellow warnings
25. **Simulator tips every beginner should know** - Shortcuts, reset, slow animations

### Common Beginner Mistakes
26. **Why is my outlet nil?** - IBOutlet connection issues
27. **"Thread 1: Fatal error" - What it means** - Force unwrap crashes explained simply
28. **Why won't my UI update?** - Main thread basics
29. **"Use of unresolved identifier"** - Scope and typos
30. **App crashes on launch** - Info.plist issues, missing permissions

### First Steps in Debugging
31. **Using `po` in the console** - Print object basics
32. **Step over, step into, step out** - Debugger navigation
33. **Conditional breakpoints for beginners** - Only break when something is true
34. **Inspecting variables without breakpoints** - Quick Look, debug descriptions
35. **Console colors and what they mean** - System messages vs your logs

### Understanding Errors
36. **Optionals and nil: The #1 crash cause** - Safe unwrapping patterns
37. **"Index out of range" explained** - Array bounds checking
38. **Decoding Swift error messages** - Reading compiler complaints
39. **What is a stack trace?** - Reading the left panel after a crash
40. **Simulator vs Device: Why it works here but not there**

---

## Intermediate Topics

### Debugging Techniques
41. **Exception breakpoints: Catch crashes before they happen** - Setup and usage
42. **Watchpoints: Break when a value changes** - Memory debugging
43. **LLDB expressions: Modify state while debugging** - `expr` command
44. **Debugging async code with breakpoints** - Task context, continuation issues
45. **Zombie objects: Finding messages to deallocated instances**

### Memory & Performance
46. **Retain cycles in closures: Finding and fixing** - Weak/unowned patterns
47. **Autorelease pool debugging** - When memory spikes unexpectedly
48. **Lazy loading gone wrong** - Debugging initialization order
49. **Background thread crashes** - Thread safety debugging
50. **Debugging slow app launch times** - Pre-main vs post-main

### Networking
51. **Charles Proxy basics for iOS** - SSL pinning, request inspection
52. **Debugging URLSession with custom delegates** - Logging layer
53. **Timeout issues and how to debug them** - Connection vs request timeouts
54. **Mocking network responses for debugging** - Without third-party libs

### SwiftUI-Specific
55. **Debugging view identity issues** - Why your view keeps resetting
56. **Finding unnecessary view redraws** - Instruments + Self._printChanges
57. **Environment object nil crashes** - Debugging missing injection
58. **Navigation stack debugging** - Path issues, deep linking problems

### Core Data / Persistence
59. **Core Data debugging flags** - `-com.apple.CoreData.SQLDebug 1`
60. **Migration failures: Debugging lightweight migrations** - Model versioning

---

## High-Traffic Topics (Common Searches)

### Exact Error Messages
61. **"Cannot convert value of type" - Fixing type mismatches** - Very common search
62. **"Unexpectedly found nil while unwrapping"** - The #1 Swift crash
63. **"No such module" - Framework linking issues** - SPM, CocoaPods problems
64. **"Signing certificate invalid"** - Provisioning hell
65. **"This app has crashed because it attempted to access privacy-sensitive data"** - Info.plist keys
66. **"Unable to install app - device is passcode protected"** - Device trust issues
67. **"The operation couldn't be completed. (OSStatus error -10814)"** - Keychain errors

### App Store & TestFlight Debugging
68. **"App rejected for crashes" - Finding the crash Apple found**
69. **TestFlight builds not appearing** - Processing, entitlements
70. **"Missing compliance" for encryption** - Export compliance fix
71. **App size too large for cellular download** - Asset optimization
72. **In-App Purchase not working in sandbox** - Common IAP debugging

### iOS Version-Specific
73. **iOS 17 migration issues** - API deprecations, new requirements
74. **Xcode 15 build errors after update** - Common fixes
75. **Swift 6 concurrency warnings explained** - Sendable, actor isolation

### Common "How To" Searches
76. **How to debug on real device without paid account** - Free provisioning limits
77. **How to clear Xcode cache completely** - DerivedData, caches, all of it
78. **How to debug widgets** - WidgetKit debugging tricks
79. **How to see network requests in Xcode** - Without Charles/Proxyman
80. **How to debug push notifications** - Local, remote, APNs issues

### Frustrating Issues
81. **"Works in simulator, crashes on device"** - Architecture, permissions
82. **Build succeeds but app is blank/white** - Root view issues
83. **Xcode stuck on "Installing" or "Copying"** - Device sync issues
84. **Previews not loading** - SwiftUI preview debugging
85. **"Command PhaseScriptExecution failed"** - Build script errors

---

## Testing & CI/CD

86. **XCTest failures that pass locally** - CI environment differences
87. **UI tests timing out** - Waiting strategies, accessibility identifiers
88. **Code coverage not showing** - Configuration issues
89. **Xcode Cloud build failures** - Common fixes
90. **Flaky tests: Finding and fixing** - Non-deterministic test debugging

## Accessibility

91. **VoiceOver debugging** - Accessibility Inspector usage
92. **Dynamic Type breaking layouts** - Testing large text sizes
93. **Accessibility audit in Xcode** - Built-in tool walkthrough

## Localization

94. **"Missing localization" warnings** - Export/import issues
95. **Right-to-left layout bugs** - RTL debugging
96. **Pseudo-localization for testing** - Finding truncation issues

## Animation & UI

97. **Debugging janky animations** - 60fps issues, Core Animation
98. **Keyboard avoiding view issues** - Common SwiftUI/UIKit fixes
99. **Safe area debugging** - Notch, home indicator problems
100. **Dark mode colors not updating** - Asset catalog issues

## Extensions & Multi-Target

101. **App Extension debugging** - Share, Today, Keyboard extensions
102. **App Groups data not syncing** - Container issues
103. **Watch app debugging** - Pairing, connectivity issues
104. **Debugging Intent/Siri Shortcuts** - Voice command testing

## Swift Concurrency

105. **Actor isolation errors explained** - MainActor, nonisolated
106. **Data race debugging** - Thread Sanitizer for async code
107. **Task cancellation not working** - Cooperative cancellation patterns
108. **Deadlocks with async/await** - Common patterns that hang

## Build & Configuration

109. **Debug vs Release behavior differences** - Optimization gotchas
110. **Scheme environment variables** - Launch arguments debugging
