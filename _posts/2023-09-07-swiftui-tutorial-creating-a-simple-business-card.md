---
title: "SwiftUI Tutorial: Creating a Simple Business Card"
date: "2023-09-07"
categories: 
  - "swift"
  - "swiftui"
---

Are you just starting with SwiftUI and looking for a practical project to hone your skills? In this tutorial, we'll walk you through creating a simple, well-aligned business card using SwiftUI. This project is perfect for beginners and will teach you essential concepts like layout, styling, and basic interactions.

## Prerequisites

- Basic knowledge of Swift programming language

- Xcode installed on your Mac

- Some familiarity with SwiftUI basics (though we'll explain each step)

## Step 1: Setting Up the Project

1. Open Xcode and create a new project.

3. Choose "App" under the iOS tab.

5. Name your project "BusinessCard" and ensure SwiftUI is selected for the interface.

## Step 2: Creating the Basic Structure

Let's start by creating the basic structure of our business card. Replace the contents of `ContentView.swift` with the following:

```swift
import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack(spacing: 20) {
            // We'll add our content here
        }
        .padding()
        .frame(maxWidth: .infinity, maxHeight: .infinity)
        .background(Color.white)
    }
}
```

This creates a vertical stack (`VStack`) that will contain all our business card elements. The `padding()` ensures some space around the edges, and `frame(maxWidth: .infinity, maxHeight: .infinity)` makes the card take up the full screen.

## Step 3: Adding the Profile Image

Let's add a profile image to our card. Add this code inside the `VStack`:

```swift
Image("profile")
    .resizable()
    .aspectRatio(contentMode: .fill)
    .frame(width: 150, height: 150)
    .clipShape(Circle())
    .overlay(Circle().stroke(Color.gray, lineWidth: 2))
```

Note: You'll need to add an image named "profile" to your asset catalog. If you don't have one, you can use `Image(systemName: "person.circle.fill")` instead.

This code creates a circular profile image with a gray border.

## Step 4: Adding Name and Title

Next, let's add the name and job title. Add these lines after the image:

```swift
Text("Leonardo DiCaprio")
    .font(.title)
    .fontWeight(.bold)

Text("iOS Developer")
    .font(.subheadline)
    .foregroundColor(.secondary)
```

## Step 5: Adding Contact Information

Now, let's add some contact information. Add this code next:

```swift
VStack(alignment: .leading, spacing: 10) {
    HStack(spacing: 15) {
        Image(systemName: "envelope.fill")
        Text("leonardo.diCaprio@email.com")
    }
    HStack(spacing: 15) {
        Image(systemName: "phone.fill")
        Text("+1 (555) 123-4567")
    }
}
.font(.body)
```

This creates two rows of contact information, each with an icon and text.

## Step 6: Adding Action Buttons

Finally, let's add some action buttons for email and phone. Add this code at the end of the main `VStack`:

```swift
HStack(spacing: 30) {
    Button(action: {
        // Email action
    }) {
        Image(systemName: "envelope.fill")
            .foregroundColor(.white)
            .frame(width: 50, height: 50)
            .background(Color.blue)
            .clipShape(Circle())
    }

    Button(action: {
        // Phone action
    }) {
        Image(systemName: "phone.fill")
            .foregroundColor(.white)
            .frame(width: 50, height: 50)
            .background(Color.green)
            .clipShape(Circle())
    }
}
```

These buttons don't have any actions yet, but they provide a nice visual touch to our card.

## Final Code

Here's the complete `ContentView.swift` file:

```swift
import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack(spacing: 20) {
            Image("profile")
                .resizable()
                .aspectRatio(contentMode: .fill)
                .frame(width: 150, height: 150)
                .clipShape(Circle())
                .overlay(Circle().stroke(Color.gray, lineWidth: 2))

            Text("John Doe")
                .font(.title)
                .fontWeight(.bold)

            Text("iOS Developer")
                .font(.subheadline)
                .foregroundColor(.secondary)

            VStack(alignment: .leading, spacing: 10) {
                HStack(spacing: 15) {
                    Image(systemName: "envelope.fill")
                    Text("john.doe@email.com")
                }
                HStack(spacing: 15) {
                    Image(systemName: "phone.fill")
                    Text("+1 (555) 123-4567")
                }
            }
            .font(.body)

            HStack(spacing: 30) {
                Button(action: {
                    // Email action
                }) {
                    Image(systemName: "envelope.fill")
                        .foregroundColor(.white)
                        .frame(width: 50, height: 50)
                        .background(Color.blue)
                        .clipShape(Circle())
                }

                Button(action: {
                    // Phone action
                }) {
                    Image(systemName: "phone.fill")
                        .foregroundColor(.white)
                        .frame(width: 50, height: 50)
                        .background(Color.green)
                        .clipShape(Circle())
                }
            }
        }
        .padding()
        .frame(maxWidth: .infinity, maxHeight: .infinity)
        .background(Color.white)
    }
}
```

## Conclusion

This project has introduced you to several key SwiftUI concepts:

- Using `VStack` and `HStack` for layout

- Styling images and text

- Creating and styling buttons

- Using SF Symbols for icons

- Basic alignment and spacing

Feel free to customize the colors, fonts, and layout to make this business card your own. As you get more comfortable with SwiftUI, you can add more advanced features like animations or interactivity to the buttons.
