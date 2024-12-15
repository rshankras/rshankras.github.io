---
title: "MemoMinder: A Swift Tutorial on File System and Plist Usage"
date: "2024-04-01"
categories: 
  - "swift"
  - "swiftui"
---

## Introduction

In this tutorial, we'll explore the MemoMinder app, a note-taking application that demonstrates the use of the file system for storing notes and property lists (plists) for managing settings. We'll break down the app's architecture, focusing on how it implements these storage mechanisms and adheres to Protocol-Oriented Programming (POP) and SOLID principles.

## Part 1: File System Usage for Note Storage

### Step 1: The Note Model

First, let's look at our `Note` model:

```swift
struct Note: Codable, Identifiable {
    let id: UUID
    var title: String
    var content: String
    let createdAt: Date
}
```

This struct represents a single note and conforms to `Codable` for easy serialization.

### Step 2: The NoteStorage Protocol

We define a protocol for note storage operations:

```swift
protocol NoteStorage {
    func saveNote(_ note: Note) throws
    func loadNotes() throws -> [Note]
    func deleteNote(_ note: Note) throws
}
```

This protocol allows us to implement different storage mechanisms while keeping a consistent interface.

### Step 3: File System Implementation

Now, let's implement the `NoteStorage` protocol using the file system:

```swift
class FileSystemNoteStorage: NoteStorage {
    private let fileManager = FileManager.default
    private var notesDirectory: URL {
        fileManager.urls(for: .documentDirectory, in: .userDomainMask)[0].appendingPathComponent("Notes")
    }

    init() {
        try? fileManager.createDirectory(at: notesDirectory, withIntermediateDirectories: true, attributes: nil)
    }

    func saveNote(_ note: Note) throws {
        let data = try JSONEncoder().encode(note)
        let fileURL = notesDirectory.appendingPathComponent("\(note.id).json")
        try data.write(to: fileURL)
    }

    func loadNotes() throws -> [Note] {
        let noteURLs = try fileManager.contentsOfDirectory(at: notesDirectory, includingPropertiesForKeys: nil)
        return try noteURLs.compactMap { url in
            let data = try Data(contentsOf: url)
            return try JSONDecoder().decode(Note.self, from: data)
        }
    }

    func deleteNote(_ note: Note) throws {
        let fileURL = notesDirectory.appendingPathComponent("\(note.id).json")
        try fileManager.removeItem(at: fileURL)
    }
}
```

This class uses the file system to store each note as a separate JSON file.

## Part 2: Property List (Plist) Usage for Settings

### Step 1: The SettingsManager

Now, let's look at how we manage settings using a property list:

```swift
class SettingsManager: ObservableObject {
    @Published var settings: [String: Any] {
        didSet {
            saveSettings()
        }
    }

    private let settingsURL: URL
    private let fileManager = FileManager.default

    init() {
        let appSupportURL = fileManager.urls(for: .applicationSupportDirectory, in: .userDomainMask)[0]
        settingsURL = appSupportURL.appendingPathComponent("settings.plist")

        // Initialize with default settings
        settings = [
            "sortOrder": "dateCreated",
            "fontSize": 16,
            "colorScheme": "system"
        ]

        // Ensure directory exists
        createDirectoryIfNeeded()

        // Try to load existing settings, if available
        loadSettings()
    }

    private func createDirectoryIfNeeded() {
        let directory = settingsURL.deletingLastPathComponent()
        if !fileManager.fileExists(atPath: directory.path) {
            do {
                try fileManager.createDirectory(at: directory, withIntermediateDirectories: true, attributes: nil)
            } catch {
                print("Error creating directory: \(error)")
            }
        }
    }

    private func loadSettings() {
        guard fileManager.fileExists(atPath: settingsURL.path) else {
            print("Settings file does not exist. Using default settings.")
            return
        }

        do {
            let data = try Data(contentsOf: settingsURL)
            if let loadedSettings = try PropertyListSerialization.propertyList(from: data, options: [], format: nil) as? [String: Any] {
                settings = loadedSettings
            }
        } catch {
            print("Error loading settings: \(error)")
        }
    }

    private func saveSettings() {
        do {
            let data = try PropertyListSerialization.data(fromPropertyList: settings, format: .xml, options: 0)
            try data.write(to: settingsURL)
        } catch {
            print("Error saving settings: \(error)")
        }
    }
}
```

This class manages app settings using a property list (plist) file.

## Part 3: Bringing It All Together

### Step 1: The NoteManager

The `NoteManager` class ties everything together:

```swift
class NoteManager: ObservableObject {
    @Published var notes: [Note] = []
    private let storage: NoteStorage

    init(storage: NoteStorage = FileSystemNoteStorage()) {
        self.storage = storage
        loadNotes()
    }

    func loadNotes() {
        do {
            notes = try storage.loadNotes()
        } catch {
            print("Error loading notes: \(error)")
        }
    }

    func saveNote(_ note: Note) {
        do {
            try storage.saveNote(note)
            if let index = notes.firstIndex(where: { $0.id == note.id }) {
                notes[index] = note
            } else {
                notes.append(note)
            }
        } catch {
            print("Error saving note: \(error)")
        }
    }

    func deleteNote(_ note: Note) {
        do {
            try storage.deleteNote(note)
            notes.removeAll { $0.id == note.id }
        } catch {
            print("Error deleting note: \(error)")
        }
    }
}
```

## Protocol-Oriented Programming (POP) in MemoMinder

MemoMinder demonstrates POP through the `NoteStorage` protocol. This allows us to:

1. Define a common interface for note storage operations.

3. Implement different storage mechanisms (like `FileSystemNoteStorage`) that conform to this protocol.

5. Easily swap out storage implementations without changing the rest of the app.

## SOLID Principles in MemoMinder

1. **Single Responsibility Principle**: Each class has a single purpose. For example, `FileSystemNoteStorage` handles file system operations, while `SettingsManager` manages app settings.

3. **Open-Closed Principle**: The app is open for extension (we can add new storage types) but closed for modification (existing code doesn't need to change to add new storage types).

5. **Liskov Substitution Principle**: Any class that implements `NoteStorage` can be used interchangeably in `NoteManager`.

7. **Interface Segregation Principle**: The `NoteStorage` protocol includes only the methods necessary for note storage operations.

9. **Dependency Inversion Principle**: High-level modules (`NoteManager`) depend on abstractions (`NoteStorage` protocol), not concrete implementations.

## Conclusion

MemoMinder demonstrates effective use of the file system for note storage and property lists for settings management. By leveraging Protocol-Oriented Programming and adhering to SOLID principles, the app achieves a flexible, maintainable architecture that can easily adapt to future changes or extensions.

This approach allows for easy transitions between different storage mechanisms. For example, if we wanted to switch to a database for note storage, we would only need to create a new class that conforms to the `NoteStorage` protocol, without changing the rest of the app's code.
