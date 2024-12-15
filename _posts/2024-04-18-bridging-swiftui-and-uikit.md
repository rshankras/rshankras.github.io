---
title: "Bridging SwiftUI and UIKit"
date: "2024-04-18"
categories: 
  - "swift"
  - "swiftui"
  - "uikit"
---

As iOS development evolves, many projects find themselves in a transition phase between UIKit and SwiftUI. Understanding how to integrate these two frameworks is crucial for modern iOS developers. In this tutorial, we'll explore how to bridge SwiftUI and UIKit in a single app, allowing you to leverage the strengths of both frameworks.

## Project Overview

We'll create an app that demonstrates:

1. A SwiftUI-based main interface

3. Presenting a UIKit view controller from SwiftUI

5. Presenting a SwiftUI view from a UIKit view controller

Let's break this down step by step.

## Step 1: Setting Up the SwiftUI App

First, let's set up our SwiftUI app entry point:

```swift
import SwiftUI

@main
struct SwiftUI_UIKitApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
```

This is a standard SwiftUI app structure, which will use `ContentView` as the root view.

## Step 2: Creating the Main SwiftUI View

Now, let's create our main SwiftUI view:

```swift
import SwiftUI

struct ContentView: View {
    @State private var showUIKitView = false

    var body: some View {
        VStack {
            Text("SwiftUI View")
                .font(.largeTitle)

            Button("Show UIKit View") {
                showUIKitView = true
            }
        }
        .sheet(isPresented: $showUIKitView) {
            UIKitViewControllerRepresentable()
        }
    }
}
```

Key points:

- We use `@State` to manage whether the UIKit view should be shown.

- The `.sheet` modifier is used to present the UIKit view modally.

- `UIKitViewControllerRepresentable` is a SwiftUI view that wraps our UIKit view controller (we'll create this next).

## Step 3: Creating a UIViewControllerRepresentable

To use a UIKit view controller in SwiftUI, we need to wrap it in a `UIViewControllerRepresentable`:

```swift
struct UIKitViewControllerRepresentable: UIViewControllerRepresentable {
    func makeUIViewController(context: Context) -> UIKitViewController {
        UIKitViewController()
    }

    func updateUIViewController(_ uiViewController: UIKitViewController, context: Context) {}
}
```

This struct acts as a bridge between SwiftUI and UIKit, allowing us to use `UIKitViewController` in our SwiftUI view hierarchy.

## Step 4: Creating the UIKit View Controller

Now, let's create our UIKit view controller:

```swift
class UIKitViewController: UIViewController {
    private let button = UIButton(type: .system)

    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .white
        setupButton()
    }

    private func setupButton() {
        button.setTitle("Show SwiftUI View", for: .normal)
        button.addTarget(self, action: #selector(showSwiftUIView), for: .touchUpInside)

        view.addSubview(button)
        button.translatesAutoresizingMaskIntoConstraints = false
        NSLayoutConstraint.activate([
            button.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            button.centerYAnchor.constraint(equalTo: view.centerYAnchor)
        ])
    }

    @objc private func showSwiftUIView() {
        let swiftUIView = SwiftUIView {
            self.dismiss(animated: true, completion: nil)
        }
        let hostingController = UIHostingController(rootView: swiftUIView)
        present(hostingController, animated: true, completion: nil)
    }
}
```

Key points:

- This is a standard UIKit view controller with a button.

- The `showSwiftUIView` method demonstrates how to present a SwiftUI view from UIKit.

- We use `UIHostingController` to wrap our SwiftUI view for presentation in UIKit.

## Step 5: Creating a SwiftUI View for UIKit Presentation

Finally, let's create a SwiftUI view that can be presented from our UIKit view controller:

```swift
struct SwiftUIView: View {
    let dismiss: () -> Void

    var body: some View {
        VStack {
            Text("SwiftUI View presented from UIKit")
                .font(.headline)

            Button("Dismiss") {
                dismiss()
            }
        }
    }
}
```

This SwiftUI view takes a closure as a parameter, which it uses to dismiss itself when presented from UIKit.

## Key Concepts

1. **UIViewControllerRepresentable**: This protocol allows us to wrap UIKit view controllers for use in SwiftUI. It requires implementing `makeUIViewController(context:)` and `updateUIViewController(_:context:)`.

3. **UIHostingController**: This UIKit class allows us to present SwiftUI views in a UIKit context. It wraps a SwiftUI view and provides a UIViewController interface.

5. **Closures for Communication**: We use a closure in `SwiftUIView` to allow the UIKit controller to dismiss it. This demonstrates one way of handling communication between SwiftUI and UIKit.

7. **State Management**: The `@State` property wrapper in `ContentView` manages the presentation state of our UIKit view.

## Conclusion

This tutorial demonstrated key aspects of SwiftUI and UIKit interoperability:

1. Creating a SwiftUI-based app that incorporates UIKit components

3. Wrapping UIKit view controllers for use in SwiftUI

5. Presenting SwiftUI views from UIKit

7. Managing state and communication between SwiftUI and UIKit

By understanding these concepts, you can effectively work with projects that use both SwiftUI and UIKit, whether you're maintaining existing apps or gradually migrating to SwiftUI.
