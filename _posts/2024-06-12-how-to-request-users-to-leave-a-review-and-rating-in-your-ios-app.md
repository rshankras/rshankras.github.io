---
title: "How to Request Users to Leave a Review and Rating in Your iOS App"
date: "2024-06-12"
categories: 
  - "swift"
  - "swiftui"
tags: 
  - "rating"
  - "review"
---

Encouraging users to leave a review and rating for your app can boost its ranking in the App Store and attract more downloads. In this tutorial, we will demonstrate how to use the SKStoreReviewController to request reviews and ratings in the Expense Split app.

### Step 1: Importing the StoreKit Framework

First, import the StoreKit framework in your Swift file. This framework provides the necessary classes for requesting reviews and ratings.

```swift
import StoreKit
```

### Step 2: Adding a Review Request Function

Create a function to request a review. You can call this function at appropriate times in your app, such as after a user successfully splits an expense or reaches a milestone.

```swift
import SwiftUI
import StoreKit

struct ContentView: View {
    var body: some View {
        VStack {
            Text("Welcome to Expense Split")
                .padding()

            Button(action: requestReview) {
                Text("Request Review")
                    .padding()
                    .background(Color.blue)
                    .foregroundColor(.white)
                    .cornerRadius(8)
            }
        }
    }

    func requestReview() {
        if let scene = UIApplication.shared.connectedScenes.first(where: { $0.activationState == .foregroundActive }) as? UIWindowScene {
            SKStoreReviewController.requestReview(in: scene)
        }
    }
}

@main
struct ExpenseSplitApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
```

### Step 3: Calling the Review Request Function at Appropriate Times

You should call the review request function at moments when the user is likely to feel satisfied with the app. For example, after successfully adding a new expense or splitting an expense among friends.

#### Example: Requesting a Review After Adding an Expense

Modify your add expense function to request a review after the expense is successfully added.

```swift
import SwiftUI
import StoreKit

class ExpenseViewModel: ObservableObject {
    @Published var expenses: [Expense] = []

    func addExpense(name: String, amount: Double) {
        let newExpense = Expense(name: name, amount: amount)
        expenses.append(newExpense)

        // Request review after adding an expense
        requestReview()
    }

    func requestReview() {
        if let scene = UIApplication.shared.connectedScenes.first(where: { $0.activationState == .foregroundActive }) as? UIWindowScene {
            SKStoreReviewController.requestReview(in: scene)
        }
    }
}

struct ContentView: View {
    @StateObject private var viewModel = ExpenseViewModel()
    @State private var name: String = ""
    @State private var amount: String = ""

    var body: some View {
        VStack {
            Text("Expense Split App")
                .font(.largeTitle)
                .padding()

            TextField("Expense Name", text: $name)
                .textFieldStyle(RoundedBorderTextFieldStyle())
                .padding()

            TextField("Amount", text: $amount)
                .keyboardType(.decimalPad)
                .textFieldStyle(RoundedBorderTextFieldStyle())
                .padding()

            Button(action: {
                if let amount = Double(amount) {
                    viewModel.addExpense(name: name, amount: amount)
                    name = ""
                    amount = ""
                }
            }) {
                Text("Add Expense")
                    .padding()
                    .background(Color.green)
                    .foregroundColor(.white)
                    .cornerRadius(8)
            }

            List(viewModel.expenses) { expense in
                HStack {
                    Text(expense.name)
                    Spacer()
                    Text("$\(expense.amount, specifier: "%.2f")")
                }
            }
        }
        .padding()
    }
}

struct Expense: Identifiable {
    let id = UUID()
    var name: String
    var amount: Double
}

@main
struct ExpenseSplitApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
```

### Step 4: Monitoring App Usage and Requesting Reviews

To avoid annoying users with frequent review requests, monitor app usage and only request reviews at appropriate intervals. For example, you could request a review after the user has added a certain number of expenses or reached a specific milestone.

#### Example: Requesting a Review After Adding Five Expenses

```swift
import SwiftUI
import StoreKit

class ExpenseViewModel: ObservableObject {
    @Published var expenses: [Expense] = []
    private var addExpenseCount = 0

    func addExpense(name: String, amount: Double) {
        let newExpense = Expense(name: name, amount: amount)
        expenses.append(newExpense)

        addExpenseCount += 1
        if addExpenseCount % 5 == 0 {
            requestReview()
        }
    }

    func requestReview() {
        if let scene = UIApplication.shared.connectedScenes.first(where: { $0.activationState == .foregroundActive }) as? UIWindowScene {
            SKStoreReviewController.requestReview(in: scene)
        }
    }
}

struct ContentView: View {
    @StateObject private var viewModel = ExpenseViewModel()
    @State private var name: String = ""
    @State private var amount: String = ""

    var body: some View {
        VStack {
            Text("Expense Split App")
                .font(.largeTitle)
                .padding()

            TextField("Expense Name", text: $name)
                .textFieldStyle(RoundedBorderTextFieldStyle())
                .padding()

            TextField("Amount", text: $amount)
                .keyboardType(.decimalPad)
                .textFieldStyle(RoundedBorderTextFieldStyle())
                .padding()

            Button(action: {
                if let amount = Double(amount) {
                    viewModel.addExpense(name: name, amount: amount)
                    name = ""
                    amount = ""
                }
            }) {
                Text("Add Expense")
                    .padding()
                    .background(Color.green)
                    .foregroundColor(.white)
                    .cornerRadius(8)
            }

            List(viewModel.expenses) { expense in
                HStack {
                    Text(expense.name)
                    Spacer()
                    Text("$\(expense.amount, specifier: "%.2f")")
                }
            }
        }
        .padding()
    }
}

struct Expense: Identifiable {
    let id = UUID()
    var name: String
    var amount: Double
}

@main
struct ExpenseSplitApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
```

### Conclusion

Requesting reviews and ratings from users is a critical part of maintaining and improving your app's visibility and success in the App Store. By strategically asking for reviews at appropriate moments, you can increase the likelihood of receiving positive feedback. Integrating this feature into your Expense Split app is straightforward with the SKStoreReviewController, ensuring a seamless user experience.

By following these steps, you can effectively request reviews and ratings in your iOS app, helping to boost its reputation and reach more users.
