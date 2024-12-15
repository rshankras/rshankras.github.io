---
title: "How to preview SwiftUI views in Xcode Playground."
date: "2024-06-08"
categories: 
  - "swift"
  - "swiftui"
  - "xcode"
---

Previewing SwiftUi code using Xcode playgrounds can be done by using settings live view or UIHostingController.  
  
Let us see this by using the following code snippet (SwiftUI View) which displays a button that increments a counter.

```swift
import SwiftUI
import PlaygroundSupport

struct CounterView: View {
    @State private var count: Int = 0

    var body: some View {
        VStack {
            Text("Count: \(count)")
            Button("Increment") {
                count += 1
            }
        }
    }
}
```

**UIHostingController**  

```swift
//PlaygroundPage.current.liveView = UIHostingController.init(rootView: CounterView())
```

**Setting Live View**

```swift
PlaygroundPage.current.setLiveView(CounterView())
```
