---
title: "Managing Dark Mode and Light Mode in iOS Apps"
date: "2024-06-03"
categories: 
  - "ios"
  - "swift"
  - "swiftui"
tags: 
  - "dark-mode"
---

In today's mobile apps, supporting both dark mode and light modes isn't just a nice to have it's often expected by users who want their apps to integrate seamlessly with their device settings. Dark mode provides a darker colour palette for all screens, views, menus, and controls, and it's beneficial for both reducing eye strain in low-light conditions and preserving battery life on devices with OLED screens. On the other hand, light mode offers a brighter interface that's ideal for higher visibility in bright conditions.

In this blog post, we'll discuss how to effectively manage and switch between dark and light themes in iOS apps using Swift. We'll use a simple `AppearanceManager` class to handle these changes dynamically, providing a smooth user experience.

### Introduction to the AppearanceManager Class

The `AppearanceManager` is a singleton class, which means it's designed to have only one instance throughout the app. This makes it easy to manage the app's appearance from anywhere in your code. Here’s how it works:

```swift
enum AppearanceMode: String, CaseIterable {
    case auto = "Auto"
    case light = "Light"
    case dark = "Dark"
    
    var displayName: String {
        switch self {
        case .auto:
            return "Auto"
        case .light:
            return "Light"
        case .dark:
            return "Dark"
        }
    }
}

class AppearanceManager: ObservableObject {
    @AppStorage("appearanceMode") var appearanceMode: AppearanceMode = .auto {
        didSet {
            applyStoredAppearanceMode()
        }
    }

    static let shared = AppearanceManager()

    private init() {
        applyStoredAppearanceMode()
    }

    func applyStoredAppearanceMode() {
        let windows = UIApplication.shared.allWindows
        for window in windows {
            switch appearanceMode {
            case .auto:
                window.overrideUserInterfaceStyle = .unspecified
            case .light:
                window.overrideUserInterfaceStyle = .light
            case .dark:
                window.overrideUserInterfaceStyle = .dark
            }
        }
    }
}
```

### Breaking Down the Code

1. **Observable Object**: Our `AppearanceManager` class is an observable object, which allows it to be used within SwiftUI views to react to changes.

3. **Storing Appearance Mode**: The `appearanceMode` property is stored in `AppStorage`, a property wrapper that automatically reads and writes to the UserDefaults. This ensures that the user's preferred theme persists across app launches.

5. **Applying the Appearance**: The `applyStoredAppearanceMode` function is where the magic happens. It checks the current `appearanceMode` and sets the user interface style for all app windows accordingly:

- **Auto**: The system decides the best appearance based on device settings (e.g., light or dark).

- **Light**: Forces light mode regardless of system preference.

- **Dark**: Forces dark mode regardless of system preference.

1. **Getting All Windows**: We extend `UIApplication` to conveniently get all windows of the app. This is crucial for applying the appearance mode universally.

### Usage Scenario

Here's how you can use `AppearanceManager` in your app:

- Instantiate `AppearanceManager.shared` early in your app's lifecycle, typically in the `AppDelegate` or `SceneDelegate`.

- Bind to the `appearanceMode` property in your settings screen, allowing users to select their preferred mode.

### Conclusion

Implementing dark and light modes in your iOS app is not just about aesthetic preferences-it's also about enhancing accessibility and user comfort. With a simple setup using the `AppearanceManager`, you can offer your users the flexibility to choose their desired theme or to default to their system settings. This approach not only adheres to modern iOS development practices but also significantly improves the user experience in your app.

This guide has shown you a straightforward method to manage themes in iOS using Swift, making your app adaptable and user-friendly under various lighting conditions.
