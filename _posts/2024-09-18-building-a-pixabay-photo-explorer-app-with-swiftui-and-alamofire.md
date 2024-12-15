---
title: "Building a Pixabay Photo Explorer App with SwiftUI and Alamofire"
date: "2024-09-18"
categories: 
  - "swiftui"
tags: 
  - "alamofire"
---

In this tutorial, we'll create an iOS app that allows users to search for photos using the Pixabay API, display the results in a [photo gallery](https://rshankar.com/building-a-simple-photo-gallery-app-in-swiftui/), and view individual photos in detail. We'll use SwiftUI for the user interface, Alamofire for networking, and integrate with the Pixabay API for fetching images.

## Project Setup

First, create a new SwiftUI project in Xcode. Then, we'll use CocoaPods to manage our dependencies. Create a Podfile in your project directory with the following content:

```swift
platform :ios, '14.0'
use_frameworks!

target 'PhotoExplorer' do
  pod 'Alamofire'
  pod 'SDWebImageSwiftUI'
end
```

Run `pod install` in your terminal, then open the `.xcworkspace` file.

## The Photo Model

Let's start by defining our Photo model:

```swift
import Foundation

struct Photo: Identifiable, Codable {
    let id: Int
    let pageURL: String
    let previewURL: String
    let largeImageURL: String
    let user: String
    let tags: String
}

struct PixabayResponse: Codable {
    let total: Int
    let totalHits: Int
    let hits: [Photo]
}
```

This model matches the JSON structure returned by the Pixabay API.

## Networking Service

Next, let's create a networking service using Alamofire:

```swift
import Foundation
import Alamofire

class PixabayService {
    static let shared = PixabayService()
    private init() {}

    private let baseURL = "https://pixabay.com/api/"
    private let apiKey = "YOUR_PIXABAY_API_KEY"

    func searchPhotos(query: String, completion: @escaping (Result<[Photo], Error>) -> Void) {
        let parameters: [String: Any] = [
            "key": apiKey,
            "q": query,
            "image_type": "photo",
            "per_page": 50
        ]

        AF.request(baseURL, parameters: parameters).responseDecodable(of: PixabayResponse.self) { response in
            switch response.result {
            case .success(let pixabayResponse):
                completion(.success(pixabayResponse.hits))
            case .failure(let error):
                completion(.failure(error))
            }
        }
    }
}
```

Don't forget to replace `"YOUR_PIXABAY_API_KEY"` with your actual Pixabay API key.

## Main View

Now, let's create our main view with a search bar and photo grid:

```swift
import SwiftUI
import SDWebImageSwiftUI

struct ContentView: View {
    @State private var searchText = "famous quotes"
    @State private var photos: [Photo] = []

    let columns = [GridItem(.adaptive(minimum: 100))]

    var body: some View {
        NavigationView {
            VStack {
                SearchBar(text: $searchText, onSearchButtonClicked: fetchPhotos)

                ScrollView {
                    LazyVGrid(columns: columns, spacing: 20) {
                        ForEach(photos) { photo in
                            NavigationLink(destination: PhotoDetailView(photo: photo)) {
                                PhotoThumbnail(imageURL: photo.previewURL)
                            }
                        }
                    }
                    .padding()
                }
            }
            .navigationTitle("Pixabay Gallery")
        }
        .onAppear(perform: fetchPhotos)
    }

    private func fetchPhotos() {
        PixabayService.shared.searchPhotos(query: searchText) { result in
            switch result {
            case .success(let fetchedPhotos):
                DispatchQueue.main.async {
                    self.photos = fetchedPhotos
                }
            case .failure(let error):
                print("Error fetching photos: \(error)")
            }
        }
    }
}

struct SearchBar: View {
    @Binding var text: String
    var onSearchButtonClicked: () -> Void

    var body: some View {
        HStack {
            TextField("Search photos", text: $text, onCommit: onSearchButtonClicked)
                .textFieldStyle(RoundedBorderTextFieldStyle())
            Button(action: onSearchButtonClicked) {
                Image(systemName: "magnifyingglass")
            }
        }
        .padding()
    }
}

struct PhotoThumbnail: View {
    let imageURL: String

    var body: some View {
        WebImage(url: URL(string: imageURL))
            .resizable()
            .indicator(.activity)
            .transition(.fade(duration: 0.5))
            .scaledToFill()
            .frame(width: 100, height: 100)
            .clipShape(RoundedRectangle(cornerRadius: 10))
    }
}
```

## Detail View

Finally, let's create our detail view:

```swift
import SwiftUI
import SDWebImageSwiftUI

struct PhotoDetailView: View {
    let photo: Photo
    @State private var scale: CGFloat = 1.0

    var body: some View {
        VStack {
            ZoomableImageView(imageURL: photo.largeImageURL, scale: $scale)
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

struct ZoomableImageView: View {
    let imageURL: String
    @Binding var scale: CGFloat

    var body: some View {
        WebImage(url: URL(string: imageURL))
            .resizable()
            .indicator(.activity)
            .transition(.fade(duration: 0.5))
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

## How It Works

1. When the app launches, it automatically searches for "famous quotes" using the Pixabay API.

3. The search results are displayed in a grid of thumbnails.

5. Users can enter a new search term and tap the search button to fetch new photos.

7. Tapping on a photo thumbnail navigates to the detail view.

9. In the detail view, users can:

- See the full-size photo

- Zoom in/out using pinch gestures or double-tap

This app demonstrates several important iOS development concepts:

- Using SwiftUI for building user interfaces

- Networking with Alamofire

- Integrating with a third-party API (Pixabay)

- Displaying and caching images with SDWebImageSwiftUI

- Implementing zoom functionality

- Navigation and data passing between views

By building this app, you've created a functional and interactive photo gallery that fetches real-world data from the internet. You can further enhance this app by adding features like pagination, saving favourite photos, or implementing more advanced search filters.
