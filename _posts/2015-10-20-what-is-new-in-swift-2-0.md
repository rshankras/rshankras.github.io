---
title: "What is new in Swift 2.0"
date: "2015-10-20"
categories: 
  - "ios"
  - "swift-2"
tags: 
  - "defer"
  - "guard"
  - "try-and-catch"
---

Lots of new feature have been introduced as part of Swift 2.0. The list includes guard, repeat-while, defer, error handling, protocol extensions, print, pattern matching, early exits, UI Testing, UI Stackview etc. Let us see some of these cool features.

### guard, try and catch

```swift
func printISPDetails() {

let url = NSURL(string: "http://www.telize.com/geoip") 
let request = NSURLRequest(URL: url!)

let session = NSURLSession.sharedSession()

let task = session.dataTaskWithRequest(request) { (data: NSData?, response: NSURLResponse?, error: NSError?) -> Void in 
guard error == nil else { 
print("Error while calling the webservice " + error!.localizedDescription) 
return 
}

let status = (response as! NSHTTPURLResponse).statusCode

guard status == 200 else { 
print("Received response status code as \(status)") 
return 
}

guard data != nil else { 
print("data not received from webservice") 
return } 
do { 
let dict = try NSJSONSerialization.JSONObjectWithData(data!, options: NSJSONReadingOptions.AllowFragments) 
print(dict) 
} catch let error as NSError { 
print("Error parsing JSON response " + error.localizedDescription) 
} 
} 
task.resume() 
}
```

The guard statement is used for checking the else part i.e when there is error print the error and exit the function.  

```swift
guard error != nil else { 
print("Error while calling the webservice " + error!.localizedDescription) 
return 
}
```

Then we have the try catch statments used for parsing the JSON response. Prior to Swift 2.0, JSONObjectWithData method had an extra argument (NSError) for cpaturing the error. Now in Swit 2.0 this is done in cleaner way by throwing an exception when any errors occur while parsing the JSON response. And you can handle this using **do**, **try** , **catch** block as shown below.

```swift
do { 
let dict = try NSJSONSerialization.JSONObjectWithData(data!, options: NSJSONReadingOptions.AllowFragments) 
print(dict) 
} catch let error as NSError { 
print("Error parsing JSON response " + error.localizedDescription) 
}
```

### defer

if you coming from Java background then defer is simular to finally statement. You can use when you call a piece of code irrespective of success of failure of opertation. One common example would be closing the file handle in a function does a read write operation to a file.  

```swift
defer { 
..code... 
}
```

repeat

We all know how do while works, the gets executed for the first time irrespective of codition in the while loop.  

```swift
var index = 0 
do { 
print(index) 
index++ 
} while (index < 10)
```

In Swift 2.0, the do keyword is replaced by repeat. Makes more sense right!  

```swift
var index = 0 
repeat { 
print(index) 
index++ 
} while (index < 10)
```

```swift
// Swift 1.2
if let value = optional {
    // value is unwrapped
}

// Swift 2.0
guard let value = optional else {
    // value is nil
    return
}
// value is unwrapped
```

```swift
// Swift 1.2
if let value = optional {
    if let value2 = optional2 {
        // value and value2 are unwrapped
    }
}

// Swift 2.0
guard let value = optional, let value2 = optional2 else {
    // either value or value2 is nil
    return
}
// value and value2 are unwrapped
```

```swift
// Swift 1.2
func divide(dividend: Int, divisor: Int) -> Int {
    return dividend / divisor
}

// Swift 2.0
func divide(dividend: Int, divisor: Int) throws -> Int {
    guard divisor != 0 else {
        throw Error.DivisionByZero
    }
    return dividend / divisor
}
```

```swift
// Swift 1.2
func someFunction() {
    // do something
}

// Swift 2.0
func someFunction() throws {
    try divide(10, divisor: 0)
}

do {
    try someFunction()
} catch {
    print("An error occurred")
}
```

```swift
// Swift 1.2
for var i = 0; i < 10; i++ {
    // do something
}

// Swift 2.0
for i in 0..<10 {
    // do something
}
