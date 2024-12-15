---
title: "Building a Simple Photo Gallery App in SwiftUI"
date: "2024-09-18"
categories: 
  - "ios"
  - "swift"
  - "swiftui"
tags: 
  - "photo-gallery"
---

In this tutorial, we'll walk through creating a simple photo gallery app that displays a grid of images and allows users to view and zoom into individual photos.

## What We're Building

Our app will have two main screens:

1. A grid view showing thumbnails of all our photos

3. A detail view where users can see a larger version of a photo and zoom in

![](/assets/images/Simulator-Screenshot-iPhone-15-2024-09-18-at-11.30.52-472x1024.jpg)

Let's break down the key components and explain how they work.

## The Photo Model

First, we need to define what a photo is in our app:

```swift
struct Photo: Identifiable {
    let id = UUID()
    let name: String
}
```

This `Photo` struct is simple:

- It has an `id` (a unique identifier) which SwiftUI uses to keep track of each photo.

- It has a `name`, which we'll use to load the image file.

We also create some sample data:

```swift
let samplePhotos = (1...20).map { Photo(name: "photo\($0)") }
```

This creates 20 `Photo` objects with names like "photo1", "photo2", etc.

## The Main View

Our main view, `ContentView`, displays the grid of photos:

```swift
struct ContentView: View {
    let columns = [GridItem(.adaptive(minimum: 100))]

    var body: some View {
        NavigationView {
            ScrollView {
                LazyVGrid(columns: columns, spacing: 20) {
                    ForEach(samplePhotos) { photo in
                        NavigationLink(destination: PhotoDetailView(photo: photo)) {
                            Image(photo.name)
                                .resizable()
                                .scaledToFill()
                                .frame(width: 100, height: 100)
                                .clipShape(RoundedRectangle(cornerRadius: 10))
                        }
                    }
                }
                .padding()
            }
            .navigationTitle("Photo Gallery")
        }
    }
}
```

Let's break this down:

- We use a `NavigationView` to allow navigation between the grid and detail views.

- Inside, we have a `ScrollView` with a `LazyVGrid`. This creates a scrollable grid of items.

- The `ForEach` loop creates a `NavigationLink` for each photo. This link leads to the detail view when tapped.

- Each photo is displayed as an `Image`, resized to fit a 100x100 frame with rounded corners.

## The Detail View

When a user taps a photo, they see the `PhotoDetailView`:

```swift
struct PhotoDetailView: View {
    let photo: Photo
    @State private var scale: CGFloat = 1.0
    
    var body: some View {
        VStack {
            ZoomableImageView(imageName: photo.name, scale: $scale)
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
        .navigationTitle("Photo Details")
        .toolbar {
            ToolbarItem(placement: .navigationBarTrailing) {
                Button("Reset Zoom") {
                    scale = 1.0
                }
            }
        }
    }
}
```

This view:

- Displays a `ZoomableImageView` (which we'll explain next).

- Shows the photo's name as the navigation title.

- Adds a "Reset Zoom" button to the navigation bar.

## The Zoomable Image View

The `ZoomableImageView` allows users to zoom in on the photo:

```swift
struct ZoomableImageView: View {
    let imageName: String
    @Binding var scale: CGFloat

    var body: some View {
        Image(imageName)
            .resizable()
            .scaledToFit()
            .scaleEffect(scale)
            .gesture(
                MagnificationGesture()
                    .onChanged { value in
                        scale = value.magnitude
                    }
            )
            .onTapGesture(count: 2) {
                if scale > 1 {
                    scale = 1
                } else {
                    scale = 2
                }
            }
    }
}
```

Here's what's happening:

- The image is displayed and made resizable to fit the screen.

- We apply a `scaleEffect` based on the `scale` value.

- A `MagnificationGesture` allows the user to pinch to zoom.

- A double-tap gesture toggles between normal size and 2x zoom.

## Putting It All Together

When you run this app, you'll see a grid of photo thumbnails. Tapping on a photo takes you to a detail view where you can:

- See the full photo

- Pinch to zoom in or out (Use Option key to Zoom in Simulator)

- Double-tap to quickly toggle between normal and 2x zoom

- Tap the "Reset Zoom" button to return to the original size

This simple photo gallery app demonstrates several key SwiftUI concepts:

- Creating and using custom views

- Implementing navigation between views

- Using gestures for user interaction

- Creating a grid layout

- Basic state management with `@State` and `@Binding`

Feel free to expand on this app by adding your own photos, implementing more features, or customizing the design to make it your own!
