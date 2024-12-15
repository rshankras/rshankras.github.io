---
title: "Building a SwiftUI Currency Converter App"
date: "2024-06-20"
categories: 
  - "ios"
  - "swift"
  - "swiftui"
tags: 
  - "spm"
---

In this tutorial, we'll walk through the process of creating a [currency converter](https://rshankar.com/swiftui-tutorial-building-a-currency-converter-app/) app using SwiftUI. This project is perfect for beginners to intermediate developers looking to enhance their skills in iOS development. We'll cover various concepts including SwiftUI, MVVM architecture, networking with Swift Concurrency, and more.

## Table of Contents

1. [Project Setup](#project-setup)

3. [Creating the Data Model](#creating-the-data-model)

5. [Building the ViewModel](#building-the-viewmodel)

7. [Implementing the Exchange Rate Service](#implementing-the-exchange-rate-service)

9. [Designing the Main View](#designing-the-main-view)

11. [Adding a Settings Screen](#adding-a-settings-screen)

13. [Finishing Touches](#finishing-touches)

## 1\. Project Setup

First, create a new SwiftUI project in Xcode and name it "LiveCurrency". We'll be using Swift Package Manager (SPM) to add the SwiftyJSON dependency, which will help us parse JSON data more easily.

To add SwiftyJSON:

1. Go to File > Add Packages

3. Search for "https://github.com/SwiftyJSON/SwiftyJSON.git"

5. Select the latest version and click "Add Package"

## 2\. Creating the Data Model

Let's start by defining our `Currency` model. Create a new Swift file called `CurrencyViewModel.swift` and add the following:

```swift
import Foundation

struct Currency: Identifiable, Hashable {
    let id = UUID()
    let name: String
    let symbol: String
    var conversionRate: Double
}
```

This structure represents a single currency with a name, symbol, and conversion rate.

## 3\. Building the ViewModel

In the same file, let's create our `CurrencyViewModel` class:

```swift
import SwiftUI

class CurrencyViewModel: ObservableObject {
    @Published var currencies: [Currency] = [
        Currency(name: "US Dollar", symbol: "USD", conversionRate: 1.0),
        Currency(name: "Euro", symbol: "EUR", conversionRate: 1.0),
        Currency(name: "British Pound", symbol: "GBP", conversionRate: 1.0),
        Currency(name: "Japanese Yen", symbol: "JPY", conversionRate: 1.0),
        Currency(name: "Indian Rupees", symbol: "INR", conversionRate: 1.0)
    ]

    @Published var isLoading = false
    @Published var errorMessage: String?
    @Published var selectedFromCurrency: Currency?
    @Published var selectedToCurrency: Currency?

    init() {
        selectedFromCurrency = currencies.first(where: { $0.symbol == "USD" })
        selectedToCurrency = currencies.first(where: { $0.symbol == "EUR" })
    }

    func updateExchangeRates() {
        // We'll implement this later
    }

    func swapCurrencies() {
        let temp = selectedFromCurrency
        selectedFromCurrency = selectedToCurrency
        selectedToCurrency = temp
    }
}
```

This ViewModel will manage the state of our app, including the list of currencies, selected currencies, and the loading state.

## 4\. Implementing the Exchange Rate Service

Now, let's create a service to fetch exchange rates. Create a new file called `ExchangeRateService.swift`:

```swift
import Foundation
import SwiftyJSON

class ExchangeRateService {
    static let shared = ExchangeRateService()
    private let baseURL = "https://open.er-api.com/v6/latest/USD"

    private init() {}

    func fetchExchangeRates() async throws -> [String: Double] {
        guard let url = URL(string: baseURL) else {
            throw URLError(.badURL)
        }

        let (data, _) = try await URLSession.shared.data(from: url)
        let json = try JSON(data: data)

        guard let rates = json["rates"].dictionary else {
            throw NSError(domain: "ParseError", code: 0, userInfo: [NSLocalizedDescriptionKey: "Failed to parse rates"])
        }

        return rates.mapValues { $0.doubleValue }
    }
}
```

This service uses Swift Concurrency to fetch exchange rates asynchronously. Now, let's update our `CurrencyViewModel` to use this service:

```swift
func updateExchangeRates() {
    isLoading = true
    errorMessage = nil

    Task {
        do {
            let rates = try await ExchangeRateService.shared.fetchExchangeRates()
            await MainActor.run {
                for i in 0..<currencies.count {
                    currencies[i].conversionRate = rates[currencies[i].symbol] ?? 1.0
                }
                // Update selected currencies with new rates
                if let fromIndex = currencies.firstIndex(where: { $0.symbol == selectedFromCurrency?.symbol }) {
                    selectedFromCurrency = currencies[fromIndex]
                }
                if let toIndex = currencies.firstIndex(where: { $0.symbol == selectedToCurrency?.symbol }) {
                    selectedToCurrency = currencies[toIndex]
                }
                isLoading = false
            }
        } catch {
            await MainActor.run {
                errorMessage = "Failed to fetch exchange rates: \(error.localizedDescription)"
                isLoading = false
            }
        }
    }
}
```

## 5\. Designing the Main View

Now, let's create our main view. Update your `ContentView.swift` file:

```swift
import SwiftUI

struct ContentView: View {
    @StateObject private var viewModel = CurrencyViewModel()
    @State private var amount: String = ""
    
    private var convertedAmount: Double {
        guard let amountDouble = Double(amount),
              let fromCurrency = viewModel.selectedFromCurrency,
              let toCurrency = viewModel.selectedToCurrency else { return 0 }
        let inUSD = amountDouble / fromCurrency.conversionRate
        return inUSD * toCurrency.conversionRate
    }
    
    var body: some View {
        NavigationView {
            Form {
                Section(header: Text("Amount to convert")) {
                    TextField("Amount", text: $amount)
                        .keyboardType(.decimalPad)
                }
                
                Section(header: Text("From")) {
                    Picker("From", selection: $viewModel.selectedFromCurrency) {
                        ForEach(viewModel.currencies) { currency in
                            Text(currency.name).tag(currency as Currency?)
                        }
                    }
                }
                
                Section(header: Text("To")) {
                    Picker("To", selection: $viewModel.selectedToCurrency) {
                        ForEach(viewModel.currencies) { currency in
                            Text(currency.name).tag(currency as Currency?)
                        }
                    }
                }
                
                Section(header: Text("Converted Amount")) {
                    Text(convertedAmount, format: .currency(code: viewModel.selectedToCurrency?.symbol ?? "USD"))
                        .font(.largeTitle)
                        .foregroundColor(.green)
                }
                
                Section {
                    Button("Swap Currencies") {
                        viewModel.swapCurrencies()
                    }
                }
                
                if viewModel.isLoading {
                    ProgressView()
                }
                
                if let errorMessage = viewModel.errorMessage {
                    Text(errorMessage)
                        .foregroundColor(.red)
                }
            }
            .navigationTitle("Currency Converter")
            .toolbar {
                ToolbarItem(placement: .navigationBarLeading) {
                    Button(action: {
                        viewModel.updateExchangeRates()
                    }) {
                        Image(systemName: "arrow.clockwise")
                    }
                    .disabled(viewModel.isLoading)
                }
                ToolbarItem(placement: .navigationBarTrailing) {
                    NavigationLink(destination: SettingsView()) {
                        Image(systemName: "gear")
                    }
                }
            }
        }
        .onAppear {
            viewModel.updateExchangeRates()
        }
    }
}
```

This view creates the main interface for our currency converter, allowing users to input an amount, select currencies, and see the converted amount.

## 6\. Adding a Settings Screen

Now, let's add a settings screen to our app. Create a new SwiftUI file called `SettingsView.swift`:

```swift
import SwiftUI

struct SettingsView: View {
    @AppStorage("isDarkMode") private var isDarkMode = false

    var body: some View {
        Form {
            Section(header: Text("Appearance")) {
                Toggle("Dark Mode", isOn: $isDarkMode)
            }

            Section(header: Text("Attribution")) {
                Link("Rates By Exchange Rate API", destination: URL(string: "https://www.exchangerate-api.com")!)
                    .foregroundColor(.blue)
            }
        }
        .navigationTitle("Settings")
    }
}
```

This view allows users to toggle dark mode and provides attribution for the exchange rate API.

Now, let's add a navigation link to this settings view in our `ContentView`:

```swift
.toolbar {
    ToolbarItem(placement: .navigationBarTrailing) {
        NavigationLink(destination: SettingsView()) {
            Image(systemName: "gear")
        }
    }
}
```

## 7\. Finishing Touches

Finally, let's update our `App` file to apply the dark mode setting:

```
import SwiftUI

@main
struct LiveCurrencyApp: App {
    @AppStorage("isDarkMode") private var isDarkMode = false

    var body: some Scene {
        WindowGroup {
            ContentView()
                .preferredColorScheme(isDarkMode ? .dark : .light)
        }
    }
}
```

And that's it! We've built a fully functional currency converter app with SwiftUI, incorporating MVVM architecture, networking with Swift Concurrency, and a settings screen with dark mode support.

This project demonstrates several key iOS development concepts:

- SwiftUI for building the user interface

- MVVM architecture for separating concerns

- Networking with URLSession and Swift Concurrency

- Using SwiftyJSON for parsing JSON data

- @AppStorage for persisting user preferences

- Dark mode support

By following this tutorial, you've created an app that not only provides useful functionality but also showcases modern iOS development practices.
