---
title: "Swift Enums"
date: "2015-01-13"
categories: 
  - "ios"
  - "programming"
tags: 
  - "apple"
  - "enum"
  - "initializer"
  - "member-function"
  - "rawvalue"
---

Enumerations, or enums, are a powerful feature in Swift that allow you to group related values under a single data type. Swift enums have significantly more capabilities compared to their counterparts in many other languages, including Objective-C. Let's explore the various features of Swift enums with examples.

## Basic Enum Declaration

Here's a simple enum representing the months of the year:

```swift
enum Month {
    case january, february, march, april, may, june, july, august, september, october, november, december
}
```

You can create a variable or constant of this enum type:

```swift
let currentMonth = Month.may

// If the type is explicitly declared, you can use a shorter dot syntax:
let nextMonth: Month = .june
```

## Enums with Raw Values

Enums in Swift can have raw values of any type. Here's an example with `String` raw values:

```swift
enum Month: String {
    case january, february, march, april, may, june, july, august, september, october, november, december
}
```

Swift automatically assigns the case name as the raw value when the type is `String`. You can access the raw value using the `rawValue` property:

```swift
let currentMonth: Month = .may
print(currentMonth.rawValue) // Prints "may"
```

## Enums with Associated Values

Enums can also have associated values, which allow you to attach additional information to each case:

```swift
enum Month {
    case january(avgTemp: Double), february(avgTemp: Double), march(avgTemp: Double)
    case april(avgTemp: Double), may(avgTemp: Double), june(avgTemp: Double)
    case july(avgTemp: Double), august(avgTemp: Double), september(avgTemp: Double)
    case october(avgTemp: Double), november(avgTemp: Double), december(avgTemp: Double)
}

let currentMonth = Month.may(avgTemp: 20.5)

switch currentMonth {
case .may(let avgTemp):
    print("May's average temperature is \(avgTemp)°C")
default:
    print("It's not May")
}
```

## Enum Methods

Enums in Swift can have methods, making them even more powerful:

```swift
enum Month: Int {
    case january = 1, february, march, april, may, june, july, august, september, october, november, december

    func monthsUntilYearEnd() -> Int {
        return Month.december.rawValue - self.rawValue
    }
}

let month: Month = .may
print(month.monthsUntilYearEnd()) // Prints "7"
```

## Enum Initializers

You can add initializers to enums for custom initialization logic:

```swift
enum Month: Int {
    case january = 1, february, march, april, may, june, july, august, september, october, november, december

    init?(monthNumber: Int) {
        guard let month = Month(rawValue: monthNumber) else {
            return nil
        }
        self = month
    }
}

if let someMonth = Month(monthNumber: 5) {
    print(someMonth) // Prints "may"
} else {
    print("Invalid month number")
}
```

## Conclusion

Swift enums are a versatile and powerful feature that goes beyond simple value grouping. With raw values, associated values, methods, and initializers, they can be used to model complex domains and create more expressive and safer code. As you become more familiar with Swift, you'll find enums to be an indispensable tool in your programming toolkit.
