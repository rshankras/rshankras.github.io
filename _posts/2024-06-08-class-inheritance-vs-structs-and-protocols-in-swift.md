---
title: "Class Inheritance vs Structs and Protocols in Swift"
date: "2024-06-08"
categories: 
  - "swift"
tags: 
  - "inheritance"
  - "protocols"
---

To explain class inheritance using your example, we'll first demonstrate the class-based approach and then show how to achieve similar functionality using structs and protocols. This will help beginners understand the differences between classes and structs and when to use each.

### Class Inheritance

In Swift, class inheritance allows one class to inherit properties and methods from another class. This is useful when you want to create a hierarchy of classes that share common behaviour.

#### Example:

```swift
class Shape {
    var name: String = ""

    func area() -> Double {
        return 0
    }

    func draw() -> String {
        return "Draw a \(name) with area \(area())"
    }
}

class Square: Shape {
    var length: Double = 0

    override func area() -> Double {
        return length * length
    }
}

let square = Square()
square.name = "My Square"
square.length = 5
print(square.draw()) // Output: Draw a My Square with area 25.0

class Rectangle: Shape {
    var length: Double = 0
    var breadth: Double = 0

    override func area() -> Double {
        return length * breadth
    }
}

let rectangle = Rectangle()
rectangle.name = "My Rectangle"
rectangle.length = 5
rectangle.breadth = 10
print(rectangle.draw()) // Output: Draw a My Rectangle with area 50.0
```

### Structs and Protocols

In Swift, structs are value types, and they don’t support inheritance. Instead, you can use protocols to define shared behavior and then conform structs to those protocols. This approach promotes composition over inheritance.

#### Protocol Definition

First, we define a protocol to describe the common behavior.

```
protocol Shape {
    var name: String { get set }
    func area() -> Double
    func draw() -> String
}

extension Shape {
    func draw() -> String {
        return "Draw a \(name) with area \(area())"
    }
}
```

#### Struct Implementation

Next, we create structs that conform to the `Shape` protocol.

```swift
struct Square: Shape {
    var name: String = ""
    var length: Double = 0

    func area() -> Double {
        return length * length
    }
}

var square = Square()
square.name = "My Square"
square.length = 5
print(square.draw()) // Output: Draw a My Square with area 25.0

struct Rectangle: Shape {
    var name: String = ""
    var length: Double = 0
    var breadth: Double = 0

    func area() -> Double {
        return length * breadth
    }
}

var rectangle = Rectangle()
rectangle.name = "My Rectangle"
rectangle.length = 5
rectangle.breadth = 10
print(rectangle.draw()) // Output: Draw a My Rectangle with area 50.0
```

### Explanation

#### Classes:

- **Inheritance**: Classes support inheritance, allowing one class to inherit properties and methods from another.

- **Reference Types**: Classes are reference types, meaning instances are passed by reference.

- **Flexibility**: Classes can have deinitializers, reference counting, and can be subclassed.

#### Structs and Protocols:

- **Value Types**: Structs are value types, meaning instances are passed by value.

- **Composition**: Instead of inheritance, you use protocols to define shared behaviour and structs to implement that behaviour.

- **Performance**: Structs are generally more performant because they are simpler and don't have the overhead of reference counting.

### Conclusion

By using classes, you can leverage inheritance to create a hierarchy of related types. With structs and protocols, you can achieve similar functionality through composition, promoting a more flexible and modular design. Understanding when to use each approach is key to mastering Swift and building robust applications.
