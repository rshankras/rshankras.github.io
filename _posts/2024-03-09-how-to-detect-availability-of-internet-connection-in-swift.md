---
title: "How to detect availability of internet connection in Swift"
date: "2024-03-09"
categories: 
  - "swift"
  - "swiftui"
---

In today's world, mobile apps are a big part of our lives. Many of these apps need an internet connection to work properly. This is why it's so important for app developers to make sure users have a smooth experience, whether they are connected to the internet or not. On iOS devices, developers can use something called `NWPathMonitor`. This class helps keep an eye on the internet connection. When the connection changes, the app can react in helpful ways. Let's see how this can be done

[NWPathMonitor](https://developer.apple.com/documentation/network/nwpathmonitor) is a class that will observe for any change in network. We can create a class called NetworkMonitor based on NWPathMonitor.

```swift
import Network

class NetworkMonitor {
    static let shared = NetworkMonitor()
    
    private let queue = DispatchQueue.global()
    private let monitor: NWPathMonitor
    
    var isConnected: Bool {
        return monitor.currentPath.status == .satisfied
    }
    
    private init() {
        monitor = NWPathMonitor()
    }
    
    func startMonitoring() {
        monitor.start(queue: queue)
        monitor.pathUpdateHandler = { _ in
            if self.isConnected {
                // Trigger syncing with Firebase here
                let managedObjectContext = PersistenceController.shared.container.viewContext
                StorageManager.shared.syncPlacesWithFirebase(managedContext: managedObjectContext)
            }
        }
    }
    
    func stopMonitoring() {
        monitor.cancel()
    }
    
    deinit {
        monitor.cancel()
    }
}
```

In the above code snippet of NetworkMonitor, an instance of NWPathMonitor is created in the init method.

1. The startMonitor function begins monitoring the network status by calling `monitor.start(queue: queue)`. This line tells `NWPathMonitor` to start monitoring on a specific dispatch queue named `queue`. Network status updates will be delivered asynchronously on this queue.

2\. It assigns a closure to `monitor.pathUpdateHandler`. This closure is executed every time there's a change in network connectivity. The closure captures `self` strongly, meaning it has full access to the enclosing function's properties and methods.

3\. Inside the update handler, it first checks if the device is currently connected to the internet by evaluating `self.isConnected`. This likely involves checking if `NWPathMonitor`'s current path status indicates an active and available network connection.

In the above code snippet, the syncing of local storage (core data) and firebase is done when then the connection is available. You can replace this with the action required for your app.

The NetworkMonitor class can be called at the time of the app launch.

```swift
import SwiftUI

@main
struct SampleApp: App {
    // Initialize the NetworkMonitor
    let networkMonitor = NetworkMonitor.shared

    init() {
        // Start monitoring network status
        networkMonitor.startMonitoring()
    }
    
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}

```

Here are more real world use cases of Network Monitor

### Real World Use Cases

Implementing NetworkMonitor in SwiftUI apps can be particularly beneficial in several real-world scenarios:

#### 1\. Streaming Services

For apps that stream video or music, NetworkMonitor can help manage streaming quality. When a high speed connection is detected, the app can stream high definition content. Conversely, it can automatically switch to lower quality streams to maintain smooth playback on slower connections.

#### 2\. Social Media and Messaging Apps

In social media or messaging applications, NetworkMonitor ensures messages or posts are sent as soon as an internet connection is available. If the user attempts to post something while offline, the app can save the post and automatically send it once the device connects to the internet.

#### 3\. Navigation and Maps

Navigation apps can use NetworkMonitor to inform users about the availability of live traffic updates or online maps based on their connectivity status. It can also trigger automatic downloading of offline maps when a good connection is detected.

#### 4\. Cloud Syncing

For apps that sync data with cloud services (like note-taking apps), NetworkMonitor can pause syncing tasks when offline and resume or initiate them when the network becomes available, ensuring data consistency across devices.

#### 5\. Content Downloading

Download managers or apps that allow offline reading or viewing can benefit from NetworkMonitor by scheduling downloads during periods of strong connectivity. Users could select content to download, and the app manages these downloads intelligently, prioritising them based on network status.
