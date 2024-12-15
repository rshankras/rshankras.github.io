---
title: "Building Custom Views with SwiftUI"
date: "2024-06-06"
categories: 
  - "swift"
  - "swiftui"
---

SwiftUI provides a powerful and flexible framework for developing sophisticated user interfaces with less code and greater reuse. This blog post will demonstrate how to create custom views and incorporate animations in SwiftUI, using an expense split app as our example. The goal is to show you how to enhance the UI/UX of your apps with custom, creative view components that can be reused across different parts of your application.

#### Why Custom Views Matter

Custom views in SwiftUI allow you to encapsulate complex UI components and their behaviors in a reusable, maintainable way. This not only cleans up your codebase but also makes it easier to manage and update your UI as your app grows.

#### The Basics of Custom Views

A custom view in SwiftUI is simply a struct that conforms to the `View` protocol. You define its body to describe the view's content and behavior. Let’s start with a simple custom view for our expense split app.

### Example: Creating a ParticipantRow View

In our expense split app, we need to display a list of participants with their contribution details. Here's how we could create a reusable `ParticipantRow` view.

```swift
import SwiftUI

struct ParticipantRow: View {
    var name: String
    var amount: Double

    var body: some View {
        HStack {
            Text(name)
                .font(.headline)
                .foregroundColor(.primary)
            Spacer()
            Text("$\(amount, specifier: "%.2f")")
                .font(.subheadline)
                .foregroundColor(amount >= 0 ? .green : .red)
        }
        .padding()
    }
}
```

This custom view takes a participant's name and their contributed amount, displaying them in a horizontal stack with the amount colored green for positive values and red for negatives.

#### Enhancing the View with Animation

Let's add a simple animation that increases the engagement of our app. We will make the `ParticipantRow` slide in from the left when it appears.

```swift
struct ParticipantRow: View {
    var name: String
    var amount: Double
    @State private var loadState = false

    var body: some View {
        HStack {
            Text(name)
                .font(.headline)
                .foregroundColor(.primary)
            Spacer()
            Text("$\(amount, specifier: "%.2f")")
                .font(.subheadline)
                .foregroundColor(amount >= 0 ? .green : .red)
        }
        .padding()
        .offset(x: loadState ? 0 : -UIScreen.main.bounds.width)
        .animation(.easeOut(duration: 0.5), value: loadState)
        .onAppear {
            loadState = true
        }
    }
}
```

In this version, we add a `@State` variable `loadState` to track whether the view should be in its final position or start off-screen. The `.offset` modifier moves the view, and the `.animation` modifier adds an animation that plays when `loadState` changes to `true` as the view appears.

#### Reusing the Custom View

To use our `ParticipantRow` in the main `ContentView` of the app, you can simply iterate over a list of participants:

```swift
struct ContentView: View {
    var participants: [Participant] = [
        Participant(name: "Alice", amount: 50.00),
        Participant(name: "Bob", amount: -20.50),
        Participant(name: "Charlie", amount: 25.75)
    ]

    var body: some View {
        List(participants, id: \.name) { participant in
            ParticipantRow(name: participant.name, amount: participant.amount)
        }
    }
}
```

Here, `Participant` is a simple data model struct holding the name and amount for each participant.

### Conclusion

Creating custom views in SwiftUI is not only about making your code cleaner and more modular but also about giving your app a unique feel and look. By incorporating animations, you make the user experience smoother and more dynamic. Use these techniques to standardise the design elements in your app while maintaining flexibility to customise and improve components as your app evolves.
