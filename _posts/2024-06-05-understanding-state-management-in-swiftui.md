---
title: "Understanding State Management in SwiftUI"
date: "2024-06-05"
categories: 
  - "swift"
  - "swiftui"
tags: 
  - "state"
---

State management is a crucial aspect of building dynamic and responsive applications in SwiftUI. For beginners, understanding how to manage state effectively can significantly enhance your ability to build robust applications. Let’s explore how to use various state management techniques in SwiftUI using an example of an expense split app. We'll cover `@State`, `@Binding`, `@StateObject`, `@ObservedObject`, and `@EnvironmentObject` property wrappers.

### The Expense Model

First, let's define a simple `Expense` model that represents an expense entry.

```swift
import Foundation

struct Expense: Identifiable {
    let id = UUID()
    var name: String
    var amount: Double
}
```

### @State

`@State` is used to declare state variables that are managed by the view itself. These variables are private to the view and should not be accessed or modified outside the view.

#### Example:

In our expense split app, let’s manage a simple list of expenses using `@State`.

```swift
import SwiftUI

struct ExpenseListView: View {
    @State private var expenses: [Expense] = []

    var body: some View {
        VStack {
            List(expenses) { expense in
                HStack {
                    Text(expense.name)
                    Spacer()
                    Text("$\(expense.amount, specifier: "%.2f")")
                }
            }
            Button("Add Expense") {
                expenses.append(Expense(name: "New Expense", amount: 20.0))
            }
        }
        .padding()
    }
}

#Preview {
     ExpenseListView()
 }
```

### @Binding

`@Binding` is used to create a two-way connection between a parent view and a child view. It allows the child view to read and write to a value owned by the parent view.

#### Example:

Let’s pass an expense from a parent view to a child view for editing using `@Binding`.

```swift
struct ParentView: View {
    @State private var expenses: [Expense] = [
        Expense(name: "Lunch", amount: 15.0)
    ]

    var body: some View {
        NavigationView {
            List(expenses) { expense in
                NavigationLink(destination: EditExpenseView(expense: $expenses[0])) {
                    Text(expense.name)
                }
            }
            .navigationTitle("Expenses")
        }
    }
}

struct EditExpenseView: View {
    @Binding var expense: Expense

    var body: some View {
        Form {
            TextField("Name", text: $expense.name)
            TextField("Amount", value: $expense.amount, formatter: NumberFormatter())
        }
        .navigationTitle("Edit Expense")
    }
}

#Preview {
    ParentView()
}
```

### @StateObject

`@StateObject` is used to create and manage an observable object. It ensures that the object’s lifecycle is tied to the view’s lifecycle.

#### Example:

Let’s manage a list of expenses using `@StateObject` in our ViewModel.

```swift
import SwiftUI
import Combine

class ExpenseViewModel: ObservableObject {
    @Published var expenses: [Expense] = []

    func addExpense(name: String, amount: Double) {
        let newExpense = Expense(name: name, amount: amount)
        expenses.append(newExpense)
    }
}

struct ExpenseListView: View {
    @StateObject var viewModel = ExpenseViewModel()

    var body: some View {
        VStack {
            List(viewModel.expenses) { expense in
                HStack {
                    Text(expense.name)
                    Spacer()
                    Text("$\(expense.amount, specifier: "%.2f")")
                }
            }
            Button("Add Expense") {
                viewModel.addExpense(name: "New Expense", amount: 20.0)
            }
        }
        .padding()
    }
}

#Preview {
    ExpenseListView()
}
```

### @ObservedObject

`@ObservedObject` is used to observe an observable object that is created and owned elsewhere. It allows the view to update when the observed object changes.

#### Example:

Let’s observe an `ExpenseViewModel` owned by a parent view in a child view.

```swift
struct ParentView: View {
    @StateObject var viewModel = ExpenseViewModel()

    var body: some View {
        NavigationView {
            List(viewModel.expenses) { expense in
                Text(expense.name)
            }
            .navigationTitle("Expenses")
            .toolbar {
                NavigationLink(destination: ChildView(viewModel: viewModel)) {
                    Text("Add Expense")
                }
            }
        }
    }
}

struct ChildView: View {
    @ObservedObject var viewModel: ExpenseViewModel

    var body: some View {
        Button("Add Expense in Child") {
            viewModel.addExpense(name: "Child Expense", amount: 10.0)
        }
    }
}

#Preview {
    ParentView()
}
```

### @EnvironmentObject

`@EnvironmentObject` is used to pass data that needs to be shared across many views in your app. The data is typically injected into the environment higher up in the view hierarchy.

#### Example:

Let’s share an `ExpenseViewModel` across multiple views.

```swift
@main
struct ExpenseManagerApp: App {
    var body: some Scene {
        WindowGroup {
            ParentView()
                .environmentObject(ExpenseViewModel())
        }
    }
}

struct ParentView: View {
    @EnvironmentObject var viewModel: ExpenseViewModel

    var body: some View {
        NavigationView {
            VStack {
                List(viewModel.expenses) { expense in
                    Text(expense.name)
                }
                NavigationLink(destination: ChildView()) {
                    Text("Go to Child View")
                }
            }
            .navigationTitle("Expenses")
        }
    }
}

struct ChildView: View {
    @EnvironmentObject var viewModel: ExpenseViewModel

    var body: some View {
        VStack {
            Button("Add Expense in Child") {
                viewModel.addExpense(name: "Child Expense", amount: 10.0)
            }
            List(viewModel.expenses) { expense in
                Text(expense.name)
            }
        }
    }
}

#Preview {
        ParentView()
            .environmentObject(ExpenseViewModel())
}

```

### Conclusion

In SwiftUI, managing state effectively is key to building dynamic and responsive applications. Here's a summary of the property wrappers we covered:

- **@State**: Manages local state within a view.

- **@Binding**: Creates a two-way binding between parent and child views.

- **@StateObject**: Manages the lifecycle of an `ObservableObject`.

- **@ObservedObject**: Observes an `ObservableObject` created elsewhere.

- **@EnvironmentObject**: Shares an `ObservableObject` across many views.

Understanding and using these property wrappers correctly will help you build more robust and maintainable SwiftUI applications.
