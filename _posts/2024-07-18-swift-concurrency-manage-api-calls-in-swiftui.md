---
title: "Swift Concurrency -Manage API Calls in SwiftUI"
date: "2024-07-18"
---

Managing API calls efficiently in SwiftUI is crucial for building responsive and user-friendly apps. By using a network service class and Swift concurrency with `async/await`, you can handle API requests smoothly. This guide will show you how to structure your code to manage API calls, handle errors, and display appropriate messages to users.

## Step 1: Define the Data Model

First, define the data model that represents the expense data.

```swift
import Foundation

struct Expense: Codable, Identifiable {
    var id: String
    var name: String
    var amount: Double
    var date: Date
    var category: String
    var payer: String
    var participants: [String]
}
```

## Step 2: Create a Network Service

Next, create a network service class that handles API requests using `URLSession` and `async/await`. This class also monitors the network connection status.

```swift
import Foundation
import Network

class NetworkService {
    private let monitor = NWPathMonitor()
    private let queue = DispatchQueue(label: "NetworkMonitor")
    private var isConnected: Bool = true

    init() {
        monitor.pathUpdateHandler = { path in
            self.isConnected = path.status == .satisfied
        }
        monitor.start(queue: queue)
    }

    func fetchExpenses() async throws -> [Expense] {
        guard isConnected else {
            throw NetworkError.noInternetConnection
        }

        let url = URL(string: "https://api.example.com/expenses")!

        let (data, response) = try await URLSession.shared.data(from: url)

        guard let httpResponse = response as? HTTPURLResponse, httpResponse.statusCode == 200 else {
            throw NetworkError.apiError
        }

        let decoder = JSONDecoder()
        decoder.dateDecodingStrategy = .iso8601
        return try decoder.decode([Expense].self, from: data)
    }
}

enum NetworkError: Error, LocalizedError {
    case noInternetConnection
    case apiError

    var errorDescription: String? {
        switch self {
        case .noInternetConnection:
            return "No internet connection. Please check your network settings."
        case .apiError:
            return "Failed to fetch data from the server. Please try again later."
        }
    }
}
```

## Step 3: Create the ViewModel

Create a ViewModel to manage the state and handle the API call using the network service.

```swift
import Foundation

class ExpenseViewModel: ObservableObject {
    @Published var expenses: [Expense] = []
    @Published var errorMessage: String?

    private let networkService = NetworkService()

    func loadExpenses() {
        Task {
            do {
                let fetchedExpenses = try await networkService.fetchExpenses()
                DispatchQueue.main.async {
                    self.expenses = fetchedExpenses
                }
            } catch {
                DispatchQueue.main.async {
                    self.errorMessage = error.localizedDescription
                }
            }
        }
    }
}
```

## Step 4: Create the SwiftUI View

Create the SwiftUI view to display the expenses and show error messages if any.

```swift
import SwiftUI

struct ContentView: View {
    @StateObject var viewModel = ExpenseViewModel()

    var body: some View {
        NavigationView {
            VStack {
                if let errorMessage = viewModel.errorMessage {
                    Text(errorMessage)
                        .foregroundColor(.red)
                        .padding()
                }

                List(viewModel.expenses) { expense in
                    VStack(alignment: .leading) {
                        Text(expense.name)
                            .font(.headline)
                        Text("Amount: \(expense.amount)")
                        Text("Category: \(expense.category)")
                        Text("Payer: \(expense.payer)")
                        Text("Participants: \(expense.participants.joined(separator: ", "))")
                    }
                }
                .navigationTitle("Expenses")
                .onAppear {
                    viewModel.loadExpenses()
                }
            }
        }
    }
}

#Preview {
    ContentView()
}

```

## Final Step: Handle No Internet Connection

The `NetworkService` already monitors the network connection status and throws an appropriate error if there’s no internet connection. The ViewModel handles this error and updates the `errorMessage` property, which the view then displays.

By following this approach, you ensure a clean separation of concerns with the network service handling the API calls, the ViewModel managing the state, and the SwiftUI view displaying the data and errors. This setup makes your code more maintainable and easier to understand.

Note: The API URL used in the `fetchExpenses` function (`https://api.example.com/expenses`) is a placeholder. You need to replace it with a valid API endpoint. If the provided URL is not reachable or invalid, it will result in an error such as "hostname could not be found." Make sure to use a working API endpoint for the actual implementation.
