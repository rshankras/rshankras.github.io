---
title: "Building a Personal Journal App: A Step-by-Step Guide to MVVM in SwiftUI"
date: "2024-02-08"
categories: 
  - "mvvm"
  - "swift"
  - "swiftui"
---

Are you ready to build a Personal Journal app while learning about the MVVM (Model-View-ViewModel) architecture? This tutorial will guide you through the process, explaining key concepts along the way. We'll use SwiftUI and Core Data to create a fully functional journal app.

## What is MVVM?

MVVM stands for Model-View-ViewModel. It's an architectural pattern that helps separate the concerns of your app:

- **Model**: Represents your data and business logic

- **View**: Displays the user interface

- **ViewModel**: Acts as a bridge between the Model and View, handling the presentation logic

Let's dive in and see how MVVM works in practice!

## Step 1: Setting Up the Project

First, create a new SwiftUI project in Xcode and enable Core Data. This sets up our basic structure and data persistence layer.

## Step 2: Creating the Model

In MVVM, the Model represents our data. For our journal app, we'll use Core Data to create a `JournalEntry` entity.

1. Open your `.xcdatamodeld` file

3. Add a new entity called `JournalEntry`

5. Add attributes: `title` (String), `content` (String), and `date` (Date)

Core Data will generate a `JournalEntry` class for us to use.

## Step 3: Creating the ViewModel

The ViewModel is the heart of MVVM. It will handle our business logic and data operations. Create a new Swift file called `JournalViewModel.swift`:

```swift
import Foundation
import CoreData

class JournalViewModel: ObservableObject {
    @Published var entries: [JournalEntry] = []
    private let viewContext: NSManagedObjectContext

    init(viewContext: NSManagedObjectContext) {
        self.viewContext = viewContext
        fetchEntries()
    }

    func fetchEntries() {
        let request = NSFetchRequest<JournalEntry>(entityName: "JournalEntry")
        request.sortDescriptors = [NSSortDescriptor(keyPath: \JournalEntry.date, ascending: false)]

        do {
            entries = try viewContext.fetch(request)
        } catch {
            print("Error fetching entries: \(error)")
        }
    }

    func addEntry(title: String, content: String) {
        let newEntry = JournalEntry(context: viewContext)
        newEntry.title = title
        newEntry.content = content
        newEntry.date = Date()

        save()
    }

    func updateEntry(_ entry: JournalEntry, title: String, content: String) {
        entry.title = title
        entry.content = content

        save()
    }

    func deleteEntry(_ entry: JournalEntry) {
        viewContext.delete(entry)
        save()
    }

    private func save() {
        do {
            try viewContext.save()
            fetchEntries()
        } catch {
            print("Error saving context: \(error)")
        }
    }
}
```

Let's break this down:

- `@Published var entries`: This property will notify our Views when the entries change.

- `fetchEntries()`: Retrieves all journal entries from Core Data.

- `addEntry()`, `updateEntry()`, `deleteEntry()`: Handle CRUD operations.

- `save()`: Saves changes to Core Data and refreshes the entries list.

## Step 4: Creating the Views

Now, let's create our Views. In MVVM, Views are responsible for displaying data and capturing user input.

### ContentView

Update your `ContentView.swift`:

```swift
import SwiftUI
import CoreData

struct ContentView: View {
    @Environment(\.managedObjectContext) private var viewContext
    @StateObject private var viewModel: JournalViewModel
    @State private var showingAddEntry = false
    @State private var searchText = ""

    init(viewContext: NSManagedObjectContext) {
        _viewModel = StateObject(wrappedValue: JournalViewModel(viewContext: viewContext))
    }

    var body: some View {
        NavigationView {
            List {
                ForEach(filteredEntries) { entry in
                    NavigationLink(destination: JournalEntryView(entry: entry, viewModel: viewModel)) {
                        VStack(alignment: .leading) {
                            Text(entry.title ?? "")
                                .font(.headline)
                            Text(entry.date ?? Date(), style: .date)
                                .font(.subheadline)
                                .foregroundColor(.secondary)
                        }
                    }
                }
                .onDelete(perform: deleteEntries)
            }
            .navigationTitle("Journal")
            .toolbar {
                ToolbarItem(placement: .navigationBarTrailing) {
                    Button(action: { showingAddEntry = true }) {
                        Label("Add Entry", systemImage: "plus")
                    }
                }
            }
            .sheet(isPresented: $showingAddEntry) {
                AddEntryView(viewModel: viewModel)
            }
        }
        .searchable(text: $searchText, prompt: "Search journal entries")
    }

    private var filteredEntries: [JournalEntry] {
        if searchText.isEmpty {
            return viewModel.entries
        } else {
            return viewModel.entries.filter { ($0.title ?? "").localizedCaseInsensitiveContains(searchText) || ($0.content ?? "").localizedCaseInsensitiveContains(searchText) }
        }
    }

    private func deleteEntries(offsets: IndexSet) {
        offsets.map { filteredEntries[$0] }.forEach(viewModel.deleteEntry)
    }
}
```

This view:

- Displays a list of journal entries

- Allows adding new entries

- Implements search functionality

- Handles deletion of entries

### AddEntryView

Create a new SwiftUI file called `AddEntryView.swift`:

```swift
import SwiftUI

struct AddEntryView: View {
    @ObservedObject var viewModel: JournalViewModel
    @State private var title = ""
    @State private var content = ""
    @Environment(\.presentationMode) var presentationMode

    var body: some View {
        NavigationView {
            Form {
                TextField("Title", text: $title)
                TextEditor(text: $content)
                    .frame(height: 200)
            }
            .navigationTitle("New Entry")
            .toolbar {
                ToolbarItem(placement: .navigationBarTrailing) {
                    Button("Save") {
                        viewModel.addEntry(title: title, content: content)
                        presentationMode.wrappedValue.dismiss()
                    }
                    .disabled(title.isEmpty || content.isEmpty)
                }
                ToolbarItem(placement: .navigationBarLeading) {
                    Button("Cancel") {
                        presentationMode.wrappedValue.dismiss()
                    }
                }
            }
        }
    }
}
```

This view allows users to add new journal entries.

### JournalEntryView

Create another SwiftUI file called `JournalEntryView.swift`:

```swift
import SwiftUI

struct JournalEntryView: View {
    @ObservedObject var entry: JournalEntry
    @ObservedObject var viewModel: JournalViewModel
    @State private var editedTitle: String
    @State private var editedContent: String
    @State private var isEditing = false

    init(entry: JournalEntry, viewModel: JournalViewModel) {
        self.entry = entry
        self.viewModel = viewModel
        _editedTitle = State(initialValue: entry.title ?? "")
        _editedContent = State(initialValue: entry.content ?? "")
    }

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 20) {
                if isEditing {
                    TextField("Title", text: $editedTitle)
                        .font(.title)
                    TextEditor(text: $editedContent)
                        .frame(minHeight: 200)
                } else {
                    Text(entry.title ?? "")
                        .font(.title)
                    Text(entry.date ?? Date(), style: .date)
                        .font(.subheadline)
                        .foregroundColor(.secondary)
                    Text(entry.content ?? "")
                }
            }
            .padding()
        }
        .navigationBarTitle("", displayMode: .inline)
        .toolbar {
            ToolbarItem(placement: .navigationBarTrailing) {
                Button(isEditing ? "Save" : "Edit") {
                    if isEditing {
                        viewModel.updateEntry(entry, title: editedTitle, content: editedContent)
                    }
                    isEditing.toggle()
                }
            }
        }
    }
}
```

This view displays and allows editing of individual journal entries.

## Step 5: Putting It All Together

Update your `PersonalJournalApp.swift` file:

```swift
import SwiftUI

@main
struct PersonalJournalApp: App {
    let persistenceController = PersistenceController.shared

    var body: some Scene {
        WindowGroup {
            ContentView(viewContext: persistenceController.container.viewContext)
                .environment(\.managedObjectContext, persistenceController.container.viewContext)
        }
    }
}
```

This sets up our app with the necessary Core Data context.

## Understanding MVVM in Our App

Now that we've built our app, let's see how MVVM is applied:

1. **Model**: The `JournalEntry` entity in Core Data represents our data model.

3. **ViewModel**: The `JournalViewModel` class acts as an intermediary between the Model and Views. It:

- Fetches data from Core Data

- Provides methods for CRUD operations

- Notifies Views of any data changes

1. **Views**: `ContentView`, `AddEntryView`, and `JournalEntryView` are responsible for displaying data and capturing user input. They don't interact directly with Core Data but instead use the ViewModel.

This separation of concerns makes our code more modular, testable, and maintainable.

## Conclusion

You've built a Personal Journal app using MVVM architecture in SwiftUI. You've learned how to:

- Set up a Core Data model

- Create a ViewModel to manage business logic

- Build Views that interact with the ViewModel

- Implement CRUD operations in an MVVM pattern

MVVM might seem complex at first, but it becomes more intuitive as you use it. It helps keep your code organized as your apps grow in complexity.
