---
title: "A SwiftUI Stopwatch App with Lap Timing"
date: "2024-01-11"
categories: 
  - "swift"
  - "swiftui"
---

In this tutorial, we'll create a sophisticated [stopwatch](https://rshankar.com/building-a-stopwatch-app-in-swiftui/) app called "LapTrack" using SwiftUI. LapTrack will feature a sleek interface with start/stop functionality, lap timing, and a list view of recorded laps.

## Setting Up the Project

1. Open Xcode and create a new SwiftUI project.

3. Name your project "LapTrack".

5. Replace the contents of your `ContentView.swift` file with the following code:

```swift
import SwiftUI

struct ContentView: View {
    @State private var elapsedTime: TimeInterval = 0
    @State private var timer: Timer?
    @State private var isRunning = false
    @State private var lapTimes: [TimeInterval] = []

    var body: some View {
        VStack {
            Text("LapTrack")
                .font(.largeTitle)
                .fontWeight(.bold)
                .padding(.top)

            Text(timeString(from: elapsedTime))
                .font(.system(size: 60, weight: .thin, design: .monospaced))
                .padding()

            HStack(spacing: 20) {
                Button(action: {
                    if isRunning {
                        stopTimer()
                    } else {
                        startTimer()
                    }
                }) {
                    Text(isRunning ? "Stop" : "Start")
                        .font(.title2)
                        .foregroundColor(.white)
                        .frame(width: 100, height: 50)
                        .background(isRunning ? Color.red : Color.green)
                        .cornerRadius(10)
                }

                Button(action: recordLapTime) {
                    Text("Lap")
                        .font(.title2)
                        .foregroundColor(.white)
                        .frame(width: 100, height: 50)
                        .background(Color.blue)
                        .cornerRadius(10)
                }
                .disabled(!isRunning)

                Button(action: resetTimer) {
                    Text("Reset")
                        .font(.title2)
                        .foregroundColor(.white)
                        .frame(width: 100, height: 50)
                        .background(Color.gray)
                        .cornerRadius(10)
                }
            }
            .padding()

            List {
                ForEach(lapTimes.indices, id: \.self) { index in
                    HStack {
                        Text("Lap \(lapTimes.count - index)")
                            .font(.headline)
                        Spacer()
                        Text(timeString(from: lapTimes[index]))
                            .font(.system(.body, design: .monospaced))
                    }
                }
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
        lapTimes.removeAll()
    }

    func recordLapTime() {
        lapTimes.insert(elapsedTime, at: 0)
    }

    func timeString(from timeInterval: TimeInterval) -> String {
        let minutes = Int(timeInterval) / 60
        let seconds = Int(timeInterval) % 60
        let hundredths = Int((timeInterval.truncatingRemainder(dividingBy: 1)) * 100)
        return String(format: "%02d:%02d.%02d", minutes, seconds, hundredths)
    }
}
```

## Understanding the Code

Let's break down the key components of our LapTrack app:

### State Variables

- `elapsedTime`: Stores the current time of the stopwatch.

- `timer`: An optional Timer object to manage the stopwatch updates.

- `isRunning`: A boolean to track whether the stopwatch is running or not.

- `lapTimes`: An array to store recorded lap times.

### User Interface

The UI is structured using a `VStack` containing:

1. App title

3. Large time display

5. Control buttons (Start/Stop, Lap, Reset)

7. List of recorded lap times

### Key Functions

1. `startTimer()`: Initializes a Timer that updates `elapsedTime` every 0.01 seconds.

3. `stopTimer()`: Stops the timer and updates the UI state.

5. `resetTimer()`: Resets the stopwatch and clears lap times.

7. `recordLapTime()`: Adds the current elapsed time to the lap times list.

9. `timeString(from:)`: Formats a TimeInterval into a readable string (MM:SS.hh).

## Conclusion

This project demonstrates several important concepts in iOS development:

- State management in SwiftUI

- Working with timers and time intervals

- Creating a responsive and intuitive user interface

- Handling user input and updating the UI accordingly

- Managing and displaying lists of dynamic data
