---
title: "Dependency Injection in Swift"
date: "2023-07-12"
categories: 
  - "design-pattern"
  - "interview-questions"
  - "ios"
---

Dependency injection is a design pattern that lets you to pass the dependencies for the object instances instead of creating the them inside the instances. Let us see this with an example of an app that manages Expenses.

In an Expense app we might have different components like

**ExpenseManager** - Responsible of managing business logic of expenses like creating, retrieving and deleting expenses.

**ExpenseRepository** - Responsible for data persistence of expenses, this interacts with database or network APIs to persists data.

**ExpenseViewController** - This is the UI component responsible for displaying Expenses and provides user interaction with the user.

ExpenseManager has a dependency on ExpenseRepository for saving and retrieving expense details. If we don't use Dependency injection then ExpenseManager has to create an instance of ExpenseRepository and will be tightly coupled with each other.

```
class ExpenseManager {
  private let repository = ExpenseRepository()
}
```

Instead we can create a separate protocol for ExpenseRepository with saveExpense and getExpenses functions. ExpenseManager depends on ExpenseRepositoryProtocol which is provided through initialiser. ExpenseRepository has to conform with ExpenseRepositoryProtocol and provides the implementation. ExpenseViewController depends on ExpenseManager and it is passed in the initialiser.

```
// ExpenseRepository protocol
protocol ExpenseRepositoryProtocol {
    func saveExpense(_ expense: Expense)
    func getExpenses() -> [Expense]
}

// ExpenseManager
class ExpenseManager {
    private let repository: ExpenseRepositoryProtocol
    
    init(repository: ExpenseRepositoryProtocol) {
        self.repository = repository
    }
    
    func addExpense(_ expense: Expense) {
        repository.saveExpense(expense)
    }
    
    func getAllExpenses() -> [Expense] {
        return repository.getExpenses()
    }
}

// ExpenseRepository implementation
class ExpenseRepository: ExpenseRepositoryProtocol {
    private var expenses: [Expense] = []
    
    func saveExpense(_ expense: Expense) {
        expenses.append(expense)
    }
    
    func getExpenses() -> [Expense] {
        return expenses
    }
}

// ExpenseViewController
class ExpenseViewController {
    private let expenseManager: ExpenseManager
    
    init(expenseManager: ExpenseManager) {
        self.expenseManager = expenseManager
    }
    
    func addExpense(_ expense: Expense) {
        expenseManager.addExpense(expense)
    }
    
    func displayExpenses() {
        let expenses = expenseManager.getAllExpenses()
        // Display expenses in the UI
    }
}

```

**Benefits of Dependency Injection**

- **Loose Coupling** - Each component depends only on the protocols allowing for flexibility and easier substitution of implementation.For example if you want to change the persistence from Core Data to Firebase, you have to make sure the Firebase Persistence class conforms to ExpenseRepositoryProtocol and ExpenseManager doesn't need to know about the Firebase Persistence class.
- **Testability** - With Dependency Injection it becomes easier to write unit tests by providing mock or stub implementations.
- **Scalability and Maintainability** - This promotes modular design, as it is easier to add or replace components without impacting the entire system.
