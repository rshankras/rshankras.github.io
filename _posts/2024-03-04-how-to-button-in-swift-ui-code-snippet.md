---
title: "Button in Swift UI - Code Snippet"
date: "2024-03-04"
categories: 
  - "swift"
  - "swiftui"
---

A button in SwiftUI is a fundamental interactive component that allows users to trigger actions.  

**SwiftUI Button Basics**

The two main elements for creating a button are

1. Label - A [closure](https://rshankar.com/closures-extensions-and-generics-in-swift/) that defines what happens when the button is tapped.

3. Action - A view that represents the button's appearance.

Let us see this with an example of having a button in [Expense Split app](https://rshankar.com/apps-2/expense-split/) to add expenses

```swift
Button(action: {
            print("Add Expense button was tapped.")
        }) {
            Text("Add Expense")
                .padding()
                .background(Color.blue)
                .foregroundColor(.white)
                .cornerRadius(8)
        }
```

The above code snippets defines the trigger action which is to print the text "Add Expense button was tapped" and add the view that represents the button appearance. This has been customised by adding blue background colour, white text colour, corner radius.

![](/assets/images/Screenshot-2024-03-04-at-6.47.58-AM.png)

While the example prints a message to the console, in a real [expense split](https://rshankar.com/apps-2/expense-split/) app, tapping the "Add Expense" button could navigate the user to a new view where they can fill out the details of the new expense
