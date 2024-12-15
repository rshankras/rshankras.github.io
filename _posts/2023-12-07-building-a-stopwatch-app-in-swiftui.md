---
title: "Building a Stopwatch App in SwiftUI"
date: "2023-12-07"
categories: 
  - "swift"
  - "swiftui"
---

In this tutorial, we'll walk through the process of creating a stopwatch app using SwiftUI. We'll start with a basic stopwatch and then enhance it with additional features like lap timing. This tutorial is perfect for beginners to intermediate Swift developers who want to improve their SwiftUI skills.

## Part 1: Building the Basic Stopwatch

Let's start by creating a simple stopwatch with start, stop, and reset functionality.

### Step 1: Setting Up the Project

Create a new SwiftUI project in Xcode and replace the contents of your `ContentView.swift` file with the following:

```swift
import SwiftUI

struct ContentView: View {
    @State private var elapsedTime: TimeInterval = 0
    @State private var timer: Timer?
    @State private var isRunning = false

    var body: some View {
        VStack {
            Text(timeString(from: elapsedTime))
                .font(.largeTitle)
                .padding()

            HStack {
                Button(isRunning ? "Stop" : "Start") {
                    if isRunning {
                        stopTimer()
                    } else {
                        startTimer()
                    }
                }
                .padding()

                Button("Reset") {
                    resetTimer()
                }
                .padding()
            }
        }
    }

    func startTimer() {
        timer = Timer.scheduledTimer(withTimeInterval: 0.01, repeats: true) { _ in
            elapsedTime += 0.01
        }
        isRunning = true
    }

    func stopTimer() {
        timer?.invalidate()
        timer = nil
        isRunning = false
    }

    func resetTimer() {
        stopTimer()
        elapsedTime = 0
    }

    func timeString(from timeInterval: TimeInterval) -> String {
        let minutes = Int(timeInterval) / 60
        let seconds = Int(timeInterval) % 60
        let hundredths = Int((timeInterval.truncatingRemainder(dividingBy: 1)) * 100)
        return String(format: "%02d:%02d.%02d", minutes, seconds, hundredths)
    }
}
```

### Step 2: Understanding the Code

Let's break down the key components of our basic stopwatch:

1. **State Variables**:

- `elapsedTime`: Stores the current time of the stopwatch.

- `timer`: An optional Timer object to manage the stopwatch updates.

- `isRunning`: A boolean to track whether the stopwatch is running or not.

1. **User Interface**:

- We use a `VStack` to arrange our elements vertically.

- The `Text` view displays the current time.

- Two buttons allow the user to start/stop and reset the stopwatch.

1. **Timer Functions**:

- `startTimer()`: Creates a new Timer that updates `elapsedTime` every 0.01 seconds.

- `stopTimer()`: Invalidates the timer and sets `isRunning` to false.

- `resetTimer()`: Stops the timer and resets `elapsedTime` to zero.

1. **Time Formatting**:

- The `timeString(from:)` function converts the `TimeInterval` into a readable string format (MM:SS.hh).

### Step 3: Testing the Basic Stopwatch

Run your app in the simulator or on a device. You should now have a functional stopwatch that you can start, stop, and reset.

## Conclusion

You've built a fully functional stopwatch app using SwiftUI. This project demonstrates several key concepts:

1. State management in SwiftUI

3. Working with timers in Swift

5. Formatting time intervals

7. Dynamically updating UI based on app state
