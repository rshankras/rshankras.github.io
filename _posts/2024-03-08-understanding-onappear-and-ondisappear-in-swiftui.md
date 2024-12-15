---
title: "Understanding .onAppear and .onDisappear in SwiftUI"
date: "2024-03-08"
categories: 
  - "swift"
  - "swiftui"
---

SwiftUI simplifies the way developers think about the lifecycle of views with its declarative syntax. Unlike UIKit, which requires you to [manage the lifecycle](https://rshankar.com/what-are-the-different-lifecycle-methods-in-a-typical-uiviewcontroller/) through methods like `viewDidLoad`, `viewWillAppear`, and `viewWillDisappear`, SwiftUI provides `.onAppear` and `.onDisappear` modifiers for executing code when a view appears or disappears. This tutorial demonstrates how to use these modifiers in a real case scenario.

### The Basics

- **`.onAppear`**: This modifier allows you to perform actions right after the view has been added to the view hierarchy.

- **`.onDisappear`**: Conversely, this modifier lets you execute code just as the view is about to be removed from the view hierarchy.

### Example Scenarios

Let us take an example of an app that is used for [Splitting expenses between friends](https://rshankar.com/apps-2/expense-split/). The main screen will be showing list of shared expenses and this can be fetched from the API or database using the .onAppear modifier. Similarly when the user creates a new expense and leaves the screen the .onDisAppear modifier can be used to create a new expense and clean up the data.

```swift
import SwiftUI

struct ExpensesListView: View {
    @State private var expenses: [Expense] = []

    var body: some View {
        NavigationView {
            List(expenses) { expense in
                ExpenseRow(expense: expense)
            }
            .navigationBarTitle("Shared Expenses")
            .onAppear {
                loadExpenses()
            }
            .onDisappear {
                saveExpenses()
            }
        }
    }
    
    func loadExpenses() {
        // Add Logic to load expenses from your data source
        print("Expenses loaded.")
    }
    
    func saveExpenses() {
        // Add Logic to save any changes to the expenses
        print("Expenses saved.")
    }
}

```

Other real world examples use cases could be

1. Analytics - Track screen views and user interactions by triggering analytics events in `.onAppear` and `.onDisappear`.

3. **Releasing Resources**: Use `.onDisappear` to cancel network requests, timers, or free up any resources that are no longer needed.
