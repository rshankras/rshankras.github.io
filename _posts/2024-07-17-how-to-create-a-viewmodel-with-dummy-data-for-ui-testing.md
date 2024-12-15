---
title: "How to Create a ViewModel with Dummy Data for UI Testing"
date: "2024-07-17"
---

In this guide, we'll walk you through the process of creating a ViewModel and loading it with dummy data from a JSON file for UI testing. This will help you test your UI with realistic data without relying on a network or external data source.

### Step 1: Define the Data Model

First, create a struct to represent the data. This struct will conform to the `Codable` and `Identifiable` protocols.

```swift
import Foundation

struct DataModel: Codable, Identifiable {
    var id: String
    var name: String
    var amount: Double
    var date: Date
    var category: String
    var payer: String
    var participants: [String]
}
```

### Step 2: Create the ViewModel

Next, create a ViewModel that will manage your data and handle loading it from a JSON file.

```swift
import Foundation

class DataViewModel: ObservableObject {
    @Published var dataList: [DataModel] = []

    func loadDummyData() {
        if let url = Bundle.main.url(forResource: "dummyData", withExtension: "json") {
            do {
                let data = try Data(contentsOf: url)
                let decoder = JSONDecoder()
                decoder.dateDecodingStrategy = .iso8601
                let decodedData = try decoder.decode([DataModel].self, from: data)
                self.dataList = decodedData
            } catch {
                print("Failed to load data: \(error)")
            }
        }
    }
}
```

### Step 3: Create a JSON File

Create a file named `dummyData.json` and place it in your project. Here’s an example of the dummy data:

```swift
[
    {
        "id": "1",
        "name": "Dinner",
        "amount": 45.5,
        "date": "2023-07-10T00:00:00Z",
        "category": "Food",
        "payer": "Alice",
        "participants": ["Alice", "Bob", "Charlie"]
    },
    {
        "id": "2",
        "name": "Movie Tickets",
        "amount": 30.0,
        "date": "2023-07-11T00:00:00Z",
        "category": "Entertainment",
        "payer": "Bob",
        "participants": ["Bob", "Alice"]
    }
]
```

### Step 4: Load the JSON Data in the ViewModel

In your SwiftUI view, create an instance of the `DataViewModel` and call the `loadDummyData()` method to load the dummy data.

```swift
import SwiftUI

struct ContentView: View {
    @StateObject var viewModel = DataViewModel()

    var body: some View {
        List(viewModel.dataList) { dataItem in
            VStack(alignment: .leading) {
                Text(dataItem.name)
                    .font(.headline)
                Text("Amount: \(dataItem.amount)")
                Text("Category: \(dataItem.category)")
                Text("Payer: \(dataItem.payer)")
                Text("Participants: \(dataItem.participants.joined(separator: ", "))")
            }
        }
        .onAppear {
            viewModel.loadDummyData()
        }
    }

   #Preview{
      ContentView()
   }
}
```

### Final Step: Run Your App

Make sure your `dummyData.json` is added to your project and included in the target. When you run your app, the dummy data should be loaded and displayed in the list.

### Conclusion

By following these steps, you can create a ViewModel and load it with dummy data from a JSON file. This approach allows you to test your UI with realistic data, ensuring that your app behaves as expected without relying on external data sources.
