---
title: "Building a Transaction List App in SwiftUI"
date: "2024-09-01"
categories: 
  - "swift"
  - "swiftui"
---

In this tutorial, we'll walk through creating a transaction list app, explaining key SwiftUI concepts along the way.

## Step 1: Setting Up the Data Model

Let's start by defining our data model. We'll create a `Transaction` struct and an enum for the transaction type.

```swift
import SwiftUI

struct Transaction: Identifiable {
    let id: UUID
    let date: Date
    let amount: Double
    let description: String
    let type: TransactionType
}

enum TransactionType {
    case credit
    case debit
}
```

Key points:

- `Transaction` conforms to `Identifiable`, which is required for use in SwiftUI Lists.

- We use an enum for `TransactionType` to ensure type safety.

## Step 2: Creating the Main View

Now, let's create our main view, `TransactionListView`:

```swift
struct TransactionListView: View {
    @State private var transactions: [Transaction] = []

    var body: some View {
        NavigationView {
            VStack {
                List(transactions) { transaction in
                    NavigationLink(destination: TransactionDetailView(transaction: transaction)) {
                        TransactionRowView(transaction: transaction)
                    }
                }
                .navigationTitle("Transactions")
            }
            .onAppear {
                loadTransactions()
            }
            .refreshable {
                loadTransactions()
            }
        }
    }

    private func loadTransactions() {
        // Simulated API call
        DispatchQueue.main.asyncAfter(deadline: .now() + 1) {
            // Populate transactions array
        }
    }
}
```

Key components:

1. `@State`: This property wrapper is used for the `transactions` array. It tells SwiftUI to update the view when this value changes.

3. `NavigationView`: Provides a navigation container for our list.

5. `List`: Efficiently displays our transactions.

7. `NavigationLink`: Enables navigation to a detail view for each transaction.

9. `.onAppear`: Loads transactions when the view appears.

11. `.refreshable`: Adds pull-to-refresh functionality.

## Step 3: Creating a Row View

The `TransactionRowView` represents each row in our list:

```swift
struct TransactionRowView: View {
    let transaction: Transaction

    var body: some View {
        HStack {
            VStack(alignment: .leading) {
                Text(transaction.description)
                    .font(.headline)
                Text(transaction.date, style: .date)
                    .font(.subheadline)
                    .foregroundColor(.secondary)
            }
            Spacer()
            Text(String(format: "$%.2f", transaction.amount))
                .foregroundColor(transaction.type == .credit ? .green : .red)
        }
    }
}
```

Key points:

- `HStack` and `VStack` are used for horizontal and vertical layouts.

- We use different text styles and colors to distinguish between elements.

- The amount color changes based on the transaction type.

## Step 4: Creating a Detail View

The `TransactionDetailView` shows more information about a selected transaction:

```swift
struct TransactionDetailView: View {
    let transaction: Transaction

    var body: some View {
        VStack(alignment: .leading, spacing: 20) {
            Text(transaction.description)
                .font(.title)
            Text(transaction.date, style: .date)
            Text(String(format: "$%.2f", transaction.amount))
                .font(.title2)
                .foregroundColor(transaction.type == .credit ? .green : .red)
            Text("Type: \(transaction.type == .credit ? "Credit" : "Debit")")
            Spacer()
        }
        .padding()
        .navigationTitle("Transaction Details")
    }
}
```

Key points:

- We use `VStack` for vertical layout with custom spacing.

- Different font sizes and colors are used to highlight important information.

- `.navigationTitle` sets the title for this view when navigated to.

## Step 5: Implementing Data Loading

In a real app, you'd fetch data from an API or database. Here's a simulated data loading function:

```swift
private func loadTransactions() {
    // Simulate API call
    DispatchQueue.main.asyncAfter(deadline: .now() + 1) {
        self.transactions = [
            Transaction(id: UUID(), date: Date().addingTimeInterval(-86400 * 2), amount: 120.50, description: "Grocery Shopping", type: .debit),
            Transaction(id: UUID(), date: Date().addingTimeInterval(-86400), amount: 1500.00, description: "Salary Deposit", type: .credit),
            // Add more transactions...
        ]
    }
}
```

Key points:

- We use `DispatchQueue.main.asyncAfter` to simulate an asynchronous API call.

- In a real app, you'd replace this with actual networking code.

## Conclusion

This tutorial covered several key SwiftUI concepts:

1. Creating and using custom data models

3. Building list views with `NavigationView` and `List`

5. Implementing navigation with `NavigationLink`

7. Creating reusable subviews

9. Using `@State` for managing view state

11. Implementing pull-to-refresh functionality

By understanding these components, you're well on your way to building more complex SwiftUI applications.
