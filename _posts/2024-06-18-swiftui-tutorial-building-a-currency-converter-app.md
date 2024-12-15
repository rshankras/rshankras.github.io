---
title: "SwiftUI Tutorial: Building a Currency Converter App"
date: "2024-06-18"
categories: 
  - "swift"
  - "swiftui"
---

Welcome to this SwiftUI tutorial! Today, we're going to build a Currency Converter app. This project will teach you about using Pickers, managing state, and performing real-time calculations in SwiftUI.

## What We're Building

We'll create an app where users can:

- Select currencies from a list

- Enter an amount to convert

- See the converted amount update in real-time

- Switch the direction of the conversion

## Prerequisites

- Xcode installed on your Mac

- Basic understanding of Swift and SwiftUI

## Step 1: Setting Up the Project

1. Open Xcode and create a new project.

3. Choose "App" under the iOS tab.

5. Name your project "CurrencyConverter" and ensure SwiftUI is selected for the interface.

## Step 2: Creating the Currency Model

First, let's create a simple model for our currencies:

```swift
struct Currency: Identifiable {
    let id = UUID()
    let name: String
    let symbol: String
    let conversionRate: Double // Relative to USD
}

let currencies = [
    Currency(name: "US Dollar", symbol: "USD", conversionRate: 1.0),
    Currency(name: "Euro", symbol: "EUR", conversionRate: 0.84),
    Currency(name: "British Pound", symbol: "GBP", conversionRate: 0.72),
    Currency(name: "Japanese Yen", symbol: "JPY", conversionRate: 109.51),
]
```

## Step 3: Creating the Main View

Now, let's create our main view:

```swift
import SwiftUI

struct ContentView: View {
    @State private var amount: String = ""
    @State private var selectedFromCurrency = currencies[0]
    @State private var selectedToCurrency = currencies[1]

    private var convertedAmount: Double {
        guard let amountDouble = Double(amount) else { return 0 }
        let inUSD = amountDouble / selectedFromCurrency.conversionRate
        return inUSD * selectedToCurrency.conversionRate
    }

    var body: some View {
        NavigationView {
            Form {
                Section(header: Text("Amount to convert")) {
                    TextField("Amount", text: $amount)
                        .keyboardType(.decimalPad)
                }

                Section(header: Text("From")) {
                    Picker("From", selection: $selectedFromCurrency) {
                        ForEach(currencies) { currency in
                            Text(currency.name).tag(currency)
                        }
                    }
                }

                Section(header: Text("To")) {
                    Picker("To", selection: $selectedToCurrency) {
                        ForEach(currencies) { currency in
                            Text(currency.name).tag(currency)
                        }
                    }
                }

                Section(header: Text("Converted Amount")) {
                    Text("\(convertedAmount, specifier: "%.2f") \(selectedToCurrency.symbol)")
                }

                Button("Swap Currencies") {
                    let temp = selectedFromCurrency
                    selectedFromCurrency = selectedToCurrency
                    selectedToCurrency = temp
                }
            }
            .navigationTitle("Currency Converter")
        }
    }
}
```

Let's break down what this code does:

1. We use `@State` properties to keep track of the input amount and selected currencies.

3. The `convertedAmount` computed property calculates the conversion in real-time.

5. We use a `Form` to organize our UI elements.

7. `TextField` is used for input, with the keyboard type set to decimal pad.

9. `Picker`s are used to select the "from" and "to" currencies.

11. We display the converted amount using a `Text` view.

13. A "Swap Currencies" button allows quick reversal of the conversion direction.

## Step 4: Improving the User Interface

Let's add some finishing touches to make our app more user-friendly: Let us change the Converted Amount and Swap Currencies button.

```swift
struct ContentView: View {
    var body: some View {
        NavigationView {
            Form {
                Section(header: Text("Amount to convert")) {
                    TextField("Amount", text: $amount)
                        .keyboardType(.decimalPad)
                }
                
                Section(header: Text("From")) {
                    Picker("From", selection: $selectedFromCurrency) {
                        ForEach(currencies) { currency in
                            Text(currency.name).tag(currency)
                        }
                    }
                }
                
                Section(header: Text("To")) {
                    Picker("To", selection: $selectedToCurrency) {
                        ForEach(currencies) { currency in
                            Text(currency.name).tag(currency)
                        }
                    }
                }
                Section(header: Text("Converted Amount")) {
                    Text("\(convertedAmount, specifier: "%.2f") \(selectedToCurrency.symbol)")
                        .font(.largeTitle)
                        .foregroundColor(.green)
                }

                Button(action: {
                    let temp = selectedFromCurrency
                    selectedFromCurrency = selectedToCurrency
                    selectedToCurrency = temp
                }) {
                    HStack {
                        Image(systemName: "arrow.left.arrow.right")
                        Text("Swap Currencies")
                    }
                }
                .buttonStyle(InteractiveButtonStyle())
            }
            .navigationTitle("Currency Converter")
        }
    }
}

struct InteractiveButtonStyle: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .padding()
            .background(configuration.isPressed ? Color.orange : Color.green)
            .cornerRadius(10)
            .frame(minWidth: 0, maxWidth: .infinity)
            .foregroundColor(.white)
    }
}
```

These changes make the converted amount more prominent and style the swap button to be more visually appealing.

## Conclusion

In this tutorial, you've learned:

1. How to use `Picker` for selection from a list of options

3. How to manage state with `@State` properties

5. How to perform real-time calculations based on user input

7. How to create a responsive UI that updates as the user interacts with it
