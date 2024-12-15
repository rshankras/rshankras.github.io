---
title: "Swift and Objective-C Interoperability"
date: "2024-05-18"
categories: 
  - "objective-c"
  - "swift"
---

In this tutorial, we'll explore how Swift and Objective-C can work together in a single project. We'll use a demo app to illustrate key concepts of interoperability between these two languages.

## Project Setup

First, let's set up our project structure. We'll have the following files:

1. SwiftObjCInteropDemoApp.swift (Swift)

3. SwiftPerson.swift (Swift)

5. ContentView.swift (Swift)

7. Person.h (Objective-C)

9. Person.m (Objective-C)

11. ObjCUser.h (Objective-C)

13. ObjCUser.m (Objective-C)

## Step 1: Creating the Swift App Entry Point

Let's start with our app's entry point in Swift:

```swift
// SwiftObjCInteropDemoApp.swift
import SwiftUI

@main
struct SwiftObjCInteropDemoApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
```

This is a standard SwiftUI app structure.

## Step 2: Defining a Swift Class for Objective-C Use

Next, let's create a Swift class that we'll use from Objective-C:

```swift
// SwiftPerson.swift
import Foundation

@objc class SwiftPerson: NSObject {
    @objc let name: String
    @objc private(set) var age: Int

    @objc init(name: String, age: Int) {
        self.name = name
        self.age = age
        super.init()
    }

    @objc func introduce() {
        print("Hi, I'm \(name), a Swift person aged \(age).")
    }
}
```

Key points:

- The `@objc` attribute makes this class and its members visible to Objective-C.

- We inherit from `NSObject`, which is required for most interop scenarios.

- Properties and methods we want to expose to Objective-C are marked with `@objc`.

## Step 3: Creating an Objective-C Class

Now, let's create an Objective-C class that we'll use from Swift:

```swift
// Person.h
#import <Foundation/Foundation.h>

@interface Person : NSObject

@property (nonatomic, copy, readonly) NSString *name;
@property (nonatomic, assign) NSInteger age;

- (instancetype)initWithName:(NSString *)name age:(NSInteger)age;
- (void)sayHello;

@end

// Person.m
#import "Person.h"

@implementation Person

- (instancetype)initWithName:(NSString *)name age:(NSInteger)age {
    if (self = [super init]) {
        _name = [name copy];
        _age = age;
    }
    return self;
}

- (void)sayHello {
    NSLog(@"Hello, I'm %@, an Objective-C person aged %ld.", self.name, (long)self.age);
}

@end
```

## Step 4: Creating the Bridging Header

To use Objective-C code in Swift, we need a bridging header:

```swift
// SwiftObjCInteropDemo-Bridging-Header.h
#import "Person.h"
#import "ObjCUser.h"
```

Make sure to set this file as your project's Objective-C Bridging Header in the build settings.

## Step 5: Implementing the Main View

Now, let's create our main view in Swift:

```swift
// ContentView.swift
import SwiftUI

struct ContentView: View {
    @State private var outputText = ""

    var body: some View {
        VStack {
            Text("Swift-Objective-C Interoperability Demo")
                .font(.headline)
                .padding()

            Button("Run Demo") {
                runInteropDemo()
            }
            .padding()

            ScrollView {
                Text(outputText)
                    .padding()
            }
        }
    }

    private func runInteropDemo() {
        var output = ""

        // Using Objective-C class in Swift
        let person = Person(name: "John Doe", age: 30)
        person?.sayHello()
        output += "Objective-C Person created and said hello.\n"

        // Extending Objective-C class in Swift
        person?.celebrateBirthday()
        output += "Person celebrated birthday.\n"

        // Using Swift class
        let swiftPerson = SwiftPerson(name: "Jane Smith", age: 25)
        swiftPerson.introduce()
        output += "Swift Person introduced themselves.\n"

        // Demonstrate Swift optional handling
        if let personName = person?.name {
            output += "OBJC Person's name: \(personName)\n"
        }

        // Using Swift closure with Objective-C
        let swiftClosure: @convention(block) (String) -> Void = { message in
            output += "Message from ObjC: \(message)\n"
        }

        // Using Objective-C class that uses Swift
        let objcUser = ObjCUser()
        objcUser.useSwiftPerson()
        output += "ObjCUser used SwiftPerson.\n"

        // Pass Swift closure to Objective-C
        objcUser.useSwiftClosure { message in
            output += "Received in Swift: \(message ?? "")\n"
        }

        outputText = output
    }
}

extension Person {
    func celebrateBirthday() {
        age += 1
        print("Happy Birthday! \(name ?? "") is now \(age) years old.")
    }
}
```

Key interoperability points:

1. We use the Objective-C `Person` class directly in Swift.

3. We extend the Objective-C `Person` class with a Swift method.

5. We create and use a `SwiftPerson` instance.

7. We demonstrate optional handling with Objective-C properties.

9. We create a Swift closure to pass to Objective-C.

## Step 6: Creating an Objective-C Class That Uses Swift

Finally, let's create an Objective-C class that uses our Swift code:

```swift
// ObjCUser.h
#import <Foundation/Foundation.h>

@interface ObjCUser : NSObject

- (void)useSwiftPerson;
- (void)useSwiftClosureWithBlock:(void (^)(NSString * _Nullable))block;

@end

// ObjCUser.m
#import "ObjCUser.h"
#import "SwiftObjCInteropDemo-Swift.h"

@implementation ObjCUser

- (void)useSwiftPerson {
    SwiftPerson *swiftPerson = [[SwiftPerson alloc] initWithName:@"Alice" age:28];
    [swiftPerson introduce];
}

- (void)useSwiftClosureWithBlock:(void (^)(NSString * _Nullable))block {
    if (block) {
        block(@"Hello from Objective-C!");
    }
}

@end
```

Key points:

- We import the `-Swift.h` header to use Swift classes in Objective-C.

- We create and use a `SwiftPerson` instance in Objective-C.

- We define a method that takes a block (closure) as a parameter.

## Conclusion

This tutorial demonstrated key aspects of Swift and Objective-C interoperability:

1. Using Objective-C classes in Swift

3. Extending Objective-C classes with Swift methods

5. Creating Swift classes that can be used in Objective-C

7. Handling Objective-C optionals in Swift

9. Passing Swift closures to Objective-C

11. Using Swift classes in Objective-C

By understanding these concepts, you can effectively work with projects that use both Swift and Objective-C, whether you're maintaining legacy code or gradually migrating to Swift.
