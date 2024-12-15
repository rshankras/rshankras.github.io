---
title: "Memory management in Swift"
date: "2023-07-01"
categories: 
  - "interview-questions"
  - "ios"
  - "swift"
  - "xcode"
tags: 
  - "arc"
  - "ipad"
  - "memory-management"
  - "xcode"
---

**Memory management in Swift** is done by **Automatic Reference Counting** or ARC. Whenever a variables holds an instance of an object the memory count for that object increases by 1. And when variable becomes out of scope or set to nil, the memory count decreases 1.

```swift
class Teacher {
    var name: String?
    var course: String?

    init (name: String, course: String) {
        self.name = name
        self.course = course
        print("Reference count increased by 1")
    }

    deinit{
        print("Reference count decreased by 1")
    }
}

let teacher1 = Teacher(name: "Ravi", course: "Swift")

func createTeacher() {
    let teacher2 = Teacher(name: "John", course: "Java")
}

createTeacher()
```

In the above example, we are creating two instances of Teacher class and storing it in variables teacher1 and teacher2. Since teacher2 variable is created within the function, it becomes out of scope after the function call. You should be able to observe the two init messages and one deinit (teacher2) message in console log. This should give you some idea on how reference counting works in Swift.

Increasing and decreasing of reference count are automatically handled by ARC but problem occurs when we have a strong reference cycle. A strong reference cycle refers to cyclic relationship between the objects.

```swift
class Teacher {
    var name:String?
    var course:String?
    var student: Student?

    init(name: String, course:String) {
        self.name = name
        self.course = course

        print("Reference count of Teacher increases by 1")
    }

    deinit {
        print("Reference count of Teacher decreases by 1")
    }
}

class Student {
    var name:String?
    var mentor: Teacher?

    init(name: String, course:String) {
        self.name = name

        print("Reference count of Student increases by 1")
    }

    deinit {
        print("Reference count of Student decreases by 1")
    }
}

func createInstance() {
    let teacher = Teacher(name: "Jason", course: "Swift")
    let student = Student(name: "Adam", course: "Swift")
    teacher.student = student
    student.mentor = teacher
}

createInstance()
```

In the above code snippet, **Teacher** and **Student** classes have a strong reference cycle and both student and teacher instances remain in memory even after the end of function call. A strong reference cycle can be avoided by declaring any one of the instance as **weak** or **unowned**

```swift
weak var student: Student?

```

**Unowned References**

An unowned reference does not keep a strong hold on the instance it refers to and is expected to never be `nil` once it is set.

**Example using Unowned References:**

```swift
class Customer {
    let name: String
    var card: CreditCard?

    init(name: String) {
        self.name = name
    }

    deinit {
        print("\(name) is being deinitialized")
    }
}

class CreditCard {
    let number: String
    unowned let customer: Customer

    init(number: String, customer: Customer) {
        self.number = number
        self.customer = customer
    }

    deinit {
        print("Card \(number) is being deinitialized")
    }
}

var john: Customer? = Customer(name: "John")
john?.card = CreditCard(number: "1234 5678 9012 3456", customer: john!)

john = nil
```

Using `unowned` for the `customer` property ensures that the `CreditCard` instance does not hold a strong reference to `Customer`, breaking the strong reference cycle.

#### Closures and Capture Lists

Closures can capture and store references to variables and instances. This can lead to strong reference cycles if the closure captures `self`.

**Example of Strong Reference Cycle with Closures:**

```swift
class ViewController {
    var name: String = "ViewController"

    lazy var printName: () -> Void = {
        print("My name is \(self.name)")
    }

    deinit {
        print("\(name) is being deinitialized")
    }
}

var viewController: ViewController? = ViewController()
viewController?.printName()

viewController = nil
```

To avoid the strong reference cycle, use a capture list:

**Example with Capture List:**

```swift
class ViewController {
    var name: String = "ViewController"

    lazy var printName: () -> Void = { [weak self] in
        guard let self = self else { return }
        print("My name is \(self.name)")
    }

    deinit {
        print("\(name) is being deinitialized")
    }
}

var viewController: ViewController? = ViewController()
viewController?.printName()

viewController = nil
```

By using `[weak self]` in the capture list, we ensure that the closure captures a weak reference to `self`, preventing a strong reference cycle.

#### Conclusion

Understanding memory management in iOS is essential to prevent memory leaks and ensure efficient use of resources. Swift's ARC handles most of the work, but developers must be aware of potential issues like strong reference cycles and how to use weak and unowned references to resolve them. Closures, a powerful feature in Swift, also require careful handling to avoid capturing references strongly. By following these practices, you can create robust and memory-efficient iOS applications.
