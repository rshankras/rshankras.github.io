---
title: "Understanding the iOS Delegate Pattern: A Simple Guide"
date: "2025-03-30"
description: "Learn how the delegate pattern works in iOS development with simple explanations and real-world code examples. Perfect for beginners and intermediate developers looking to understand this essential iOS design pattern."
categories: 
  - "ios"
  - "development"
  - "design-patterns"
tags: 
  - "swift"
  - "uikit"
  - "delegate"
  - "protocols"
  - "ios-development"
  - "communication-patterns"
  - "swift-programming"
---

The delegate pattern is one of the most common design patterns you'll encounter in iOS development. If you've used UIKit, you've already interacted with it, perhaps without fully understanding how it works. In this post, I'll break down the delegate pattern in simple terms and show you how to implement it in your own code.

## What is the Delegate Pattern?

At its core, the delegate pattern is a communication technique that allows one object to send messages to another object when specific events occur. 

Think of it like this: imagine you're at a restaurant. You (the customer) tell the waiter what you want to eat. The waiter doesn't cook the food themselves - they take your order to the kitchen. Later, when your food is ready, the waiter brings it back to you.

In this analogy:
- The kitchen is the object that does the work (the delegating object)
- You are the delegate (the object that responds to events)
- The waiter is the delegate protocol (the communication channel)

## Why Use the Delegate Pattern?

The delegate pattern offers several benefits:

1. **Separation of concerns**: Objects can focus on their core responsibilities and delegate other tasks
2. **Loose coupling**: Objects don't need to know details about each other, just the protocol they agree on
3. **One-to-one communication**: Clear, direct communication between two objects
4. **Reusability**: The same object can serve as a delegate for multiple objects

## How to Implement the Delegate Pattern

Implementing the delegate pattern involves three main components:

1. **Protocol**: Define the methods that the delegate must implement
2. **Delegating Object**: Contains a reference to the delegate and calls its methods
3. **Delegate**: Implements the protocol methods to respond to events

## Step-by-Step Implementation Example

Let's examine a real-world example of the delegate pattern using an Indian stock tracking app.

### 1. Define the Protocol

First, we define a protocol that outlines what the delegate needs to implement:

```swift
protocol StockManagerDelegate: AnyObject {
    func didUpdatePrice(stockManager: StockManager)
}
```

Notice that:
- We use `AnyObject` to ensure that only classes (not structs) can adopt this protocol
- We define a method that will be called when stock prices are updated
- The method includes a reference to the sender (`stockManager`) so the delegate knows where the event came from

### 2. Create the Delegating Object

Next, we create the object that will delegate tasks:

```swift
class StockManager {
    
    weak var delegate: StockManagerDelegate?
    
    var stocks = [
        Stock(symbol: "RELIANCE", name: "Reliance Industries Ltd.", price: 2450.75),
        // other stocks...
    ]
    
    func refreshPrices() {
        for i in 0..<stocks.count {
            let randomChange = Double.random(in: -5...5)
            stocks[i].price += randomChange
        }
        
        delegate?.didUpdatePrice(stockManager: self)
    }
}
```

Key points:
- We declare a `delegate` property as `weak` to avoid memory leaks (more on this later)
- We use optional chaining (`delegate?`) when calling the delegate method, as the delegate might not be set
- We pass `self` to the delegate method so it knows which manager is sending the update

### 3. Implement the Delegate

Finally, we implement the delegate protocol in our view controller:

```swift
class StockTrackerViewController: UITableViewController {
    
    let stockManager = StockManager()

    override func viewDidLoad() {
        super.viewDidLoad()
        setupUI()
        stockManager.delegate = self
    }
    
    // ...other methods...
}

extension StockTrackerViewController: StockManagerDelegate {
    func didUpdatePrice(stockManager: StockManager) {
        DispatchQueue.main.async {
            self.tableView.reloadData()
        }
    }
}
```

Notice how:
- We set `self` (the view controller) as the `stockManager`'s delegate
- We implement the required protocol method to reload the table view when prices update
- We use `DispatchQueue.main.async` to ensure UI updates happen on the main thread

## Memory Management with Delegates

An important aspect of the delegate pattern is proper memory management. Always declare your delegate properties as `weak` to avoid strong reference cycles (also called retain cycles).

```swift
weak var delegate: SomeProtocol?
```

This is crucial because:
- The delegating object (e.g., `StockManager`) holds a reference to its delegate
- The delegate (e.g., `StockTrackerViewController`) often holds a reference to the delegating object
- Without using `weak`, these objects would keep each other in memory forever, causing a memory leak

This is why delegate protocols typically require the `AnyObject` conformance - because only class types can be marked as `weak`.

## Real-World Examples in UIKit

UIKit uses the delegate pattern extensively:

- `UITableView` has `UITableViewDelegate` and `UITableViewDataSource`
- `UITextField` has `UITextFieldDelegate`
- `UIScrollView` has `UIScrollViewDelegate`

For example, when you implement `tableView(_:didSelectRowAt:)`, you're using the delegate pattern to respond to a table view's row selection event.

## When to Use the Delegate Pattern

The delegate pattern is most appropriate when:

1. You need one-to-one communication between objects
2. An object needs to notify another when specific events occur
3. You want to customize the behavior of a reusable component
4. You need to communicate back from a child view controller to a parent

## Alternatives to Delegates

While delegates are powerful, they're not the only communication pattern in iOS:

- **Callbacks/Closures**: For simpler scenarios where you don't need a formal protocol
- **Notification Center**: For one-to-many communication
- **Key-Value Observing (KVO)**: For observing property changes
- **Combine**: Apple's reactive framework for handling asynchronous events

## Conclusion

The delegate pattern is a fundamental communication technique in iOS development that enables loose coupling between objects. By understanding and implementing this pattern, you'll write more maintainable, flexible code that follows Apple's design guidelines.

In our stock tracker example, we used delegates to notify the view controller when stock prices changed, allowing it to update the UI accordingly. This separation of concerns keeps our code organized and makes each component more reusable.

--- 