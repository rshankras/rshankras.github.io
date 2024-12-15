---
title: "Higher-Order Functions in Swift"
date: "2023-09-15"
categories: 
  - "ios"
  - "programming"
  - "swift"
---

Higher Order function are powerful tools can help you transform, filter, and combine data with ease.

## What are Higher-Order Functions?

Higher order functions can take other functions as input or return functions as output. In Swift, we often use them with closures to work with collections like arrays.

Let's start with a sample dataset to play with:

```swift
let transactions = [
    ("Grocery", 50.5),
    ("Gas", 30.0),
    ("Restaurant", 45.75),
    ("Movie", 12.0),
    ("Grocery", 35.25)
]
```

This array represents a list of financial transactions, where each transaction is a tuple containing a category and an amount.

## The Map Function: Transforming Data

The `map` function is like a magical transformer for your data. It takes each element in your collection, applies a transformation, and returns a new collection with the transformed elements.

Let's say we want to extract just the amounts from our transactions:

```swift
let amounts = transactions.map { $0.1 }
print("All amounts: \(amounts)")
// Output: All amounts: [50.5, 30.0, 45.75, 12.0, 35.25]
```

Here, `$0` refers to each transaction, and `$0.1` accesses the amount (the second element of the tuple).

We can also use `map` to create more human-readable strings:

```swift
let formattedTransactions = transactions.map { "\($0.0): $\($0.1)" }
formattedTransactions.forEach { print($0) }
// Output:
// Grocery: $50.5
// Gas: $30.0
// Restaurant: $45.75
// Movie: $12.0
// Grocery: $35.25
```

## The Filter Function: Selecting Data

The `filter` function is like a bouncer for your data party. It only lets in the elements that meet certain criteria.

Want to see only the expensive transactions (over $40)?

```swift
let expensiveTransactions = transactions.filter { $0.1 > 40 }
expensiveTransactions.forEach { print("\($0.0): $\($0.1)") }
// Output:
// Grocery: $50.5
// Restaurant: $45.75
```

You can even combine conditions:

```swift
let groceryOver30 = transactions.filter { $0.0 == "Grocery" && $0.1 > 30 }
groceryOver30.forEach { print("\($0.0): $\($0.1)") }
// Output:
// Grocery: $50.5
```

## The Reduce Function: Combining Data

The `reduce` function is like a master chef, taking all your ingredients (elements) and combining them into a single dish (value).

Let's calculate the total amount spent:

```swift
let totalSpent = transactions.reduce(0) { $0 + $1.1 }
print("Total amount spent: $\(totalSpent)")
// Output: Total amount spent: $173.5
```

Here, we start with 0 and keep adding the amount from each transaction.

We can use `reduce` for more complex operations too, like finding the most expensive transaction:

```swift
let mostExpensive = transactions.reduce(("", 0.0)) { $0.1 > $1.1 ? $0 : $1 }
print("Most expensive transaction: \(mostExpensive.0) at $\(mostExpensive.1)")
// Output: Most expensive transaction: Grocery at $50.5
```

## Combining Higher-Order Functions

The real magic happens when you combine these functions. Let's calculate the average amount spent on groceries:

```swift
let averageGrocery = transactions
    .filter { $0.0 == "Grocery" }  // Keep only grocery transactions
    .map { $0.1 }                  // Keep only the amounts
    .reduce(0, +)                  // Sum up all the amounts
    / Double(transactions.filter { $0.0 == "Grocery" }.count)  // Divide by the count of grocery transactions

print("Average spent on groceries: $\(averageGrocery)")
// Output: Average spent on groceries: $42.875
```

## Wrapping Up

Higher-order functions in Swift are powerful tools that can make your code more readable and concise. Here's what we've learned:

1. `map` transforms each element in a collection.

3. `filter` creates a new collection with elements that satisfy a condition.

5. `reduce` combines all elements into a single value.

7. These functions can be chained together for complex operations.
