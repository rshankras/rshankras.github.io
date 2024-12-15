---
title: "How to simplify persistent data using @AppStorage"
date: "2024-03-20"
categories: 
  - "swift"
  - "swiftui"
---

In SwiftUI, the `@AppStorage` property wrapper that assists how we interact with UserDefaults, streamlining the process of persisting data. By simplifying data persistence, `@AppStorage` makes reading from and writing to UserDefaults more straightforward and integrated within the SwiftUI framework.

Let us take the following example where we are trying to store tap count in User Defaults. Typically the code to read from User Defaults will look like this

```swift
let tapCount = UserDefaults.standard.integer(forKey: "Tap")
```

And code like this to write to UserDefaults

```swift
UserDefaults.standard.set(tapCount, forKey: "Tap")
```

You can replace the above code with `@AppStorage` for a more SwiftUI integrated approach. To do this, declare a property in your view like

```swift
@AppStorage("Tap") var tapCount: Int = 0
```

This does a few things for you:

- It automatically reads the current value of `"Tap"` from `UserDefaults` and assigns it to `tapCount`.

- Whenever `tapCount` changes, it automatically updates the value in `UserDefaults`.

- You have specified a default value of `0`, which means if `"Tap"` hasn't been set in `UserDefaults` yet, `tapCount` will default to `0`.

Here is an example of it in use within a view:

```swift
struct TapCounterView: View {
    @AppStorage("Tap") var tapCount: Int = 0

    var body: some View {
        Button("Tap me!") {
            tapCount += 1
        }
        Text("Tap count: \(tapCount)")
    }
}
```
