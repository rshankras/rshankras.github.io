---
title: "SwiftUI Tutorial: Building a Note Taking App"
date: "2024-05-08"
categories: 
  - "swift"
  - "swiftui"
---

This project will teach you about creating and managing lists, implementing CRUD (Create, Read, Update, Delete) operations, and using ToolBar items in SwiftUI.

## What We're Building

We'll create an app where users can:

- View a list of notes

- Create new notes

- Edit existing notes

- Delete notes

- Sort notes by date or title

## Prerequisites

- Xcode installed on your Mac

- Basic understanding of Swift and SwiftUI

- Familiarity with @State and basic SwiftUI views

## Step 1: Setting Up the Project

1. Open Xcode and create a new project.

3. Choose "App" under the iOS tab.

5. Name your project "NoteTaker" and ensure SwiftUI is selected for the interface.

## Step 2: Creating the Note Model

First, let's create our Note model:

```swift
import Foundation

struct Note: Identifiable, Codable {
    var id = UUID()
    var title: String
    var content: String
    var date: Date
}
```

## Step 3: Creating a Note Store

Now, let's create a class to manage our notes:

```swift
import Foundation

class NoteStore: ObservableObject {
    @Published var notes: [Note] = []

    init() {
        loadNotes()
    }

    func addNote(_ note: Note) {
        notes.append(note)
        saveNotes()
    }

    func updateNote(_ note: Note) {
        if let index = notes.firstIndex(where: { $0.id == note.id }) {
            notes[index] = note
            saveNotes()
        }
    }

    func deleteNote(_ note: Note) {
        notes.removeAll { $0.id == note.id }
        saveNotes()
    }

    func saveNotes() {
        if let encoded = try? JSONEncoder().encode(notes) {
            UserDefaults.standard.set(encoded, forKey: "notes")
        }
    }

    func loadNotes() {
        if let data = UserDefaults.standard.data(forKey: "notes"),
           let decoded = try? JSONDecoder().decode([Note].self, from: data) {
            notes = decoded
        }
    }
}
```

This `NoteStore` class handles the CRUD operations and persists the data using `UserDefaults`.

## Step 4: Creating the Main View

Let's create our main view with a list of notes:

```swift
import SwiftUI

struct ContentView: View {
    @StateObject private var noteStore = NoteStore()
    @State private var showingAddNote = false
    @State private var sortOrder: SortOrder = .date

    enum SortOrder {
        case date, title
    }

    var body: some View {
        NavigationView {
            List {
                ForEach(sortedNotes) { note in
                    NavigationLink(destination: NoteDetailView(note: note, noteStore: noteStore)) {
                        VStack(alignment: .leading) {
                            Text(note.title)
                                .font(.headline)
                            Text(note.date, style: .date)
                                .font(.subheadline)
                                .foregroundColor(.secondary)
                        }
                    }
                }
                .onDelete(perform: deleteNotes)
            }
            .navigationTitle("Notes")
            .toolbar {
                ToolbarItem(placement: .navigationBarTrailing) {
                    Button(action: { showingAddNote = true }) {
                        Image(systemName: "plus")
                    }
                }
                ToolbarItem(placement: .navigationBarLeading) {
                    Menu {
                        Button("Sort by Date") { sortOrder = .date }
                        Button("Sort by Title") { sortOrder = .title }
                    } label: {
                        Image(systemName: "arrow.up.arrow.down")
                    }
                }
            }
            .sheet(isPresented: $showingAddNote) {
                NoteDetailView(noteStore: noteStore)
            }
        }
    }

    var sortedNotes: [Note] {
        switch sortOrder {
        case .date:
            return noteStore.notes.sorted { $0.date > $1.date }
        case .title:
            return noteStore.notes.sorted { $0.title < $1.title }
        }
    }

    func deleteNotes(at offsets: IndexSet) {
        for index in offsets {
            noteStore.deleteNote(sortedNotes[index])
        }
    }
}
```

## Step 5: Creating the Note Detail View

Now, let's create a view for adding and editing notes:

```swift
import SwiftUI

struct NoteDetailView: View {
    @Environment(\.presentationMode) var presentationMode
    @ObservedObject var noteStore: NoteStore
    @State private var title: String
    @State private var content: String
    var note: Note?
    
    init(note: Note? = nil, noteStore: NoteStore) {
        self.noteStore = noteStore
        self.note = note
        _title = State(initialValue: note?.title ?? "")
        _content = State(initialValue: note?.content ?? "")
    }
    
    var body: some View {
        NavigationView {
            Form {
                TextField("Title", text: $title)
                TextEditor(text: $content)
            }
            .navigationTitle(note == nil ? "New Note" : "Edit Note")
            .toolbar {
                ToolbarItem(placement: .navigationBarTrailing) {
                    Button("Save") {
                        if let note = note {
                            let updatedNote = Note(id: note.id, title: title, content: content, date: Date())
                            noteStore.updateNote(updatedNote)
                        } else {
                            let newNote = Note(title: title, content: content, date: Date())
                            noteStore.addNote(newNote)
                        }
                        presentationMode.wrappedValue.dismiss()
                    }
                    .disabled(title.isEmpty)
                }
            }
        }
    }
}
```

## Conclusion

You've built a functional Note Taking app using SwiftUI. In this tutorial, you've learned:

1. How to implement CRUD operations in SwiftUI

3. How to use `@StateObject` and `@ObservedObject` for state management

5. How to persist data using `UserDefaults`

7. How to use `NavigationView` and `NavigationLink` for navigation

9. How to implement sorting functionality

11. How to use `ToolBar` items for additional functionality

This project serves as a great foundation for more complex productivity apps.
