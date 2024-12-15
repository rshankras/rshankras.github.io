---
title: "Understanding REST and HTTP: Making API Calls in iOS with Swift"
date: "2024-06-19"
categories: 
  - "api"
  - "swift"
---

In the world of web and mobile development, you'll often hear terms like REST and HTTP. These concepts are fundamental to building robust applications that communicate with servers over the internet. In this blog post, we will explore the differences between REST and HTTP and learn how to make API calls in iOS using Swift.

#### Overview

- **What is HTTP?**

- **What is REST?**

- **Differences between REST and HTTP**

- **Making API Calls in iOS with Swift**

- **Using URLSession for network requests**

- **Parsing JSON responses**

- **Handling errors**

#### What is HTTP?

HTTP, or Hypertext Transfer Protocol, is the foundation of any data exchange on the web. It is a protocol used for transferring hypertext requests and information between web servers and browsers. HTTP follows a request-response model where a client sends a request to a server, and the server sends back a response.

Key Characteristics of HTTP:

- **Stateless**: Each request is independent and does not retain any state information between requests.

- **Methods**: Common HTTP methods include GET, POST, PUT, DELETE, PATCH, etc.

- **Headers**: HTTP headers provide essential information about the request or response, such as content type, authorization, etc.

- **Status Codes**: These codes indicate the result of the HTTP request (e.g., 200 OK, 404 Not Found, 500 Internal Server Error).

#### What is REST?

REST, or Representational State Transfer, is an architectural style for designing networked applications. It is a set of guidelines that developers follow when creating APIs that enable clients to interact with servers. RESTful APIs use HTTP methods and principles to perform CRUD (Create, Read, Update, Delete) operations on resources.

Key Principles of REST:

- **Stateless**: Each request from the client to the server must contain all the information needed to understand and process the request.

- **Resource-Based**: REST APIs use URLs to represent resources. For example, `/users/123` might represent a user resource with the ID 123.

- **Uniform Interface**: REST APIs follow standard conventions for HTTP methods. For instance, GET is used to retrieve data, POST to create data, PUT to update data, and DELETE to remove data.

- **Representation**: Resources can be represented in various formats, such as JSON, XML, or HTML.

#### Differences between REST and HTTP

- **Scope**: HTTP is a protocol, while REST is an architectural style that uses HTTP.

- **Usage**: HTTP provides the communication layer for transferring data, whereas REST defines how data should be structured and accessed.

- **Statelessness**: Both HTTP and REST are stateless, meaning each request is independent.

- **Resource Representation**: REST focuses on representing resources via URLs and HTTP methods, while HTTP alone does not define how resources should be represented or interacted with.

#### Making API Calls in iOS with Swift

Now that we understand the basics of HTTP and REST, let's dive into making API calls in iOS using Swift. We'll use the `URLSession` class to perform network requests and handle responses.

##### Example: Fetching Expenses from a REST API

1. **Setting Up the Project** Create a new iOS project in Xcode and add the following code to your view controller.

3. **Define the Expense Model**

```swift
   struct Expense: Codable {
       let id: Int
       let category: String
       let amount: Double
       let description: String
   }
```

3. **Make an API Call**

```swift
   import UIKit

   class ViewController: UIViewController {
       override func viewDidLoad() {
           super.viewDidLoad()
           fetchExpenses()
       }

       func fetchExpenses() {
           guard let url = URL(string: "https://api.example.com/expenses") else { return }

           let task = URLSession.shared.dataTask(with: url) { data, response, error in
               if let error = error {
                   print("Error: \(error.localizedDescription)")
                   return
               }

               guard let httpResponse = response as? HTTPURLResponse,
                     (200...299).contains(httpResponse.statusCode) else {
                   print("Invalid response")
                   return
               }

               guard let data = data else {
                   print("No data")
                   return
               }

               do {
                   let expenses = try JSONDecoder().decode([Expense].self, from: data)
                   DispatchQueue.main.async {
                       self.displayExpenses(expenses)
                   }
               } catch {
                   print("JSON Decoding Error: \(error.localizedDescription)")
               }
           }

           task.resume()
       }

       func displayExpenses(_ expenses: [Expense]) {
           for expense in expenses {
               print("\(expense.category): $\(expense.amount) - \(expense.description)")
           }
       }
   }
```

##### Explanation

1. **Define the Expense Model**: We create a `struct` called `Expense` that conforms to the `Codable` protocol, making it easy to encode and decode JSON data.

3. **Make an API Call**:

- **URLSession**: We use `URLSession.shared.dataTask(with: url)` to create a data task that fetches data from the given URL.

- **Error Handling**: We handle errors that might occur during the request, such as network issues or invalid responses.

- **Response Validation**: We check the HTTP status code to ensure we received a successful response (status code 200-299).

- **JSON Decoding**: We decode the JSON data into an array of `Expense` objects using `JSONDecoder`.

- **Display Expenses**: We print the fetched expenses to the console.

#### Conclusion

Understanding the differences between REST and HTTP is crucial for building networked applications. HTTP is the protocol that enables data transfer over the web, while REST is an architectural style that defines how to interact with resources using HTTP methods.

In iOS development, making API calls using `URLSession` and handling JSON data with `Codable` are essential skills. By following the examples provided, you can fetch data from RESTful APIs and integrate it into your Swift applications.

Feel free to explore more advanced topics like error handling, asynchronous operations, and data persistence to further enhance your app's networking capabilities.

* * *
