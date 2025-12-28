# Blog Topics: macOS Development

## macOS SwiftUI

1. **SwiftUI for macOS: Key differences from iOS** - AppKit bridging, expectations
2. **MenuBarExtra: Building menu bar apps** - Simple utilities
3. **Settings/Preferences window in SwiftUI** - macOS Settings scene
4. **Window management in SwiftUI** - openWindow, WindowGroup, DocumentGroup
5. **Multiple windows in macOS apps** - Window state, restoration
6. **Sidebar navigation on Mac** - NavigationSplitView, three-column layout
7. **NSViewRepresentable basics** - Wrapping AppKit views
8. **Table view in SwiftUI (macOS)** - Sortable columns, selection
9. **Keyboard shortcuts in SwiftUI** - keyboardShortcut modifier
10. **Context menus for Mac** - Right-click menus, menu bar commands

## macOS-Specific Features

11. **Drag and drop on macOS** - Files, custom types, UTTypes
12. **File dialogs: Open, save, export** - fileImporter, fileExporter
13. **Dock icon customization** - Badges, progress, menus
14. **Sharing services on macOS** - NSSharingServicePicker
15. **Touch Bar support (legacy Macs)** - Still relevant for some users
16. **Spotlight integration** - Core Spotlight, indexing content
17. **Quick Look previews** - QLPreviewProvider
18. **Services menu integration** - NSServicesProvider
19. **AppleScript support in Swift apps** - Scriptable apps
20. **Handoff between Mac and iOS** - NSUserActivity

## Mac App Distribution

21. **Sandboxing explained** - Entitlements, capabilities
22. **Hardened runtime** - Required entitlements
23. **Notarization step by step** - Command line and Xcode
24. **Mac App Store vs Direct distribution** - Pros/cons
25. **Distributing outside the App Store** - DMG, pkg, Sparkle updates
26. **Developer ID signing** - Certificates explained
27. **Universal binaries (Apple Silicon + Intel)** - Build settings
28. **App Translocation issues** - Why your app doesn't work from Downloads

## Mac-Specific APIs

29. **NSWorkspace: Opening files, apps, URLs** - System integration
30. **FSEvents: Watching file system changes** - Folder monitoring
31. **Login items: Launch at startup** - SMAppService, modern API
32. **Global keyboard shortcuts** - CGEvent, accessibility permissions
33. **Screen capture permissions** - CGWindowList, privacy
34. **Accessibility API basics** - Automating other apps (authorized use)
35. **NSAppleEventManager** - Handling URL schemes on Mac

## AppKit Integration

36. **When to use AppKit vs SwiftUI on Mac** - Decision guide
37. **NSViewController in SwiftUI** - Complex AppKit views
38. **NSWindow customization** - Titlebar, toolbar, styles
39. **NSMenu for app menus** - Beyond SwiftUI Commands
40. **NSSplitView behavior** - Resizable panes

## Mac Utilities & Tools

41. **Building a menu bar utility** - Complete example
42. **System status monitoring app** - CPU, memory, network
43. **File batch processing tool** - macOS automation
44. **Clipboard manager basics** - NSPasteboard monitoring
45. **Screenshot utility** - CGWindowListCreateImage

## High-Traffic macOS Searches

46. **"App is damaged and can't be opened"** - Gatekeeper fix
47. **"Not notarized" error for users** - What to tell users
48. **SwiftUI app won't appear in Dock** - LSUIElement
49. **Menu bar app icon not showing** - Common issues
50. **Sandboxed app can't access files** - Security-scoped bookmarks
