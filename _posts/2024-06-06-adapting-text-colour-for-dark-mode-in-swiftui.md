---
title: "Adapting Text Colour for Dark Mode in SwiftUI"
date: "2024-06-06"
categories: 
  - "swift"
  - "swiftui"
tags: 
  - "dark-mode"
---

In SwiftUI, ensuring text colour adapts appropriately to dark mode is crucial for readability. If your app supports an automatic appearance mode, the text colour needs to adjust dynamically based on the system's appearance settings. Here's a simple way to implement this:

```swift
var textColor: Color {
    if darkMode == .auto {
        return UITraitCollection.current.userInterfaceStyle == .dark ? Color.white : Color.black
    } else {
        return darkMode == .dark ? Color.white : Color.black
    }
}
```

This code snippet checks if the `darkMode` setting is set to `.auto`. If it is, it determines the system's current user interface style (`.dark` or `.light`) and sets the text color accordingly. If `darkMode` is explicitly set to `.dark` or `.light`, it sets the text colour based on that setting.

This approach ensures that your text remains visible and user-friendly regardless of the system's appearance mode. It's a simple yet effective way to enhance user experience in apps supporting dark mode.
