---
title: "UIKit Development: The Power of MVC"
date: "2024-03-13"
categories: 
  - "swift"
  - "uikit"
---

As iOS developers, we're always looking for ways to write cleaner, more maintainable code. One of the most fundamental patterns in iOS development is Model-View-Controller (MVC). In this article, we'll build a simple stock tracking app twice - once without MVC and once with MVC - to demonstrate the power and benefits of this architectural pattern.

## Part 1: UIKit Without MVC

Let's start by building our stock tracker app without any particular architectural pattern. We'll create a simple view controller that displays a list of stocks and their prices.

```swift
import UIKit

class StockListViewController: UIViewController, UITableViewDataSource {

    @IBOutlet weak var tableView: UITableView!

    var stocks: [(symbol: String, name: String, price: Double)] = [
        ("AAPL", "Apple Inc.", 150.25),
        ("GOOGL", "Alphabet Inc.", 2750.80),
        ("MSFT", "Microsoft Corporation", 305.50),
        ("AMZN", "Amazon.com, Inc.", 3380.15)
    ]

    override func viewDidLoad() {
        super.viewDidLoad()
        tableView.dataSource = self
        title = "Stock Tracker"
    }

    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return stocks.count
    }

    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "StockCell", for: indexPath)
        let stock = stocks[indexPath.row]
        cell.textLabel?.text = "\(stock.symbol) - \(stock.name)"
        cell.detailTextLabel?.text = String(format: "$%.2f", stock.price)
        return cell
    }

    @IBAction func refreshButtonTapped(_ sender: UIBarButtonItem) {
        // Simulate price updates
        for i in 0..<stocks.count {
            let randomChange = Double.random(in: -5...5)
            stocks[i].price += randomChange
        }
        tableView.reloadData()
    }
}
```

This approach works, but it has several drawbacks:

1. **Lack of Separation of Concerns**: The view controller is responsible for storing data, updating the UI, and handling user interactions. This makes it harder to maintain and test.

3. **Limited Reusability**: The stock data and logic for updating prices are tightly coupled to this specific view controller, making it difficult to reuse in other parts of the app.

5. **Scalability Issues**: As the app grows, this view controller could become massive and difficult to manage.

## Part 2: UIKit With MVC

Now, let's refactor our app to use the Model-View-Controller (MVC) pattern. We'll separate our concerns into distinct components:

### Model

```swift
struct Stock {
    let symbol: String
    let name: String
    var price: Double
}

class StockManager {
    var stocks: [Stock] = [
        Stock(symbol: "AAPL", name: "Apple Inc.", price: 150.25),
        Stock(symbol: "GOOGL", name: "Alphabet Inc.", price: 2750.80),
        Stock(symbol: "MSFT", name: "Microsoft Corporation", price: 305.50),
        Stock(symbol: "AMZN", name: "Amazon.com, Inc.", price: 3380.15)
    ]

    func refreshPrices() {
        for i in 0..<stocks.count {
            let randomChange = Double.random(in: -5...5)
            stocks[i].price += randomChange
        }
    }
}
```

### View

```swift
class StockCell: UITableViewCell {
    @IBOutlet weak var symbolLabel: UILabel!
    @IBOutlet weak var nameLabel: UILabel!
    @IBOutlet weak var priceLabel: UILabel!

    func configure(with stock: Stock) {
        symbolLabel.text = stock.symbol
        nameLabel.text = stock.name
        priceLabel.text = String(format: "$%.2f", stock.price)
    }
}
```

### Controller

```swift
class StockListViewController: UIViewController, UITableViewDataSource {
    @IBOutlet weak var tableView: UITableView!

    let stockManager = StockManager()

    override func viewDidLoad() {
        super.viewDidLoad()
        tableView.dataSource = self
        title = "Stock Tracker"
    }

    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return stockManager.stocks.count
    }

    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "StockCell", for: indexPath) as! StockCell
        let stock = stockManager.stocks[indexPath.row]
        cell.configure(with: stock)
        return cell
    }

    @IBAction func refreshButtonTapped(_ sender: UIBarButtonItem) {
        stockManager.refreshPrices()
        tableView.reloadData()
    }
}
```

## Benefits of MVC

1. **Separation of Concerns**: Each component has a clear responsibility. The Model manages data, the View displays information, and the Controller coordinates between them.

3. **Improved Testability**: With separated concerns, it's easier to write unit tests for each component.

5. **Enhanced Reusability**: The `StockManager` can be used in other parts of the app without modification. The `StockCell` can be reused in different table views.

7. **Better Scalability**: As the app grows, each component can be expanded independently without affecting the others.

9. **Easier Maintenance**: When bugs occur or features need to be added, it's clearer where changes should be made.

11. **Flexibility**: If we need to change how stocks are displayed (View) or how stock data is managed (Model), we can do so without affecting the other components.

## Conclusion

While the non-MVC approach might seem simpler at first, it quickly becomes unwieldy as an app grows in complexity. The MVC pattern, although requiring a bit more initial setup, provides a solid foundation for building maintainable, testable, and scalable iOS applications.

By separating concerns into Model, View, and Controller, we create a more robust architecture that can evolve with our app's needs. This separation allows multiple developers to work on different components simultaneously and makes it easier to update or replace individual parts of the app without affecting the whole system.
