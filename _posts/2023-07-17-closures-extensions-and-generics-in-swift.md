---
title: "Closures, Extensions and Generics in Swift"
date: "2023-07-17"
categories: 
  - "develop"
  - "interview-questions"
  - "ios"
  - "programming"
tags: 
  - "closures"
  - "extensions"
---

### Closures

Closures are self contained lines of code that can be passed around the application and similar to blocks in Objective-C. A typical closure syntax in Swift looks as shown below

#### Closure Syntax

```
{ (parameters) -> return type in
  statements
}
```

#### Example closure in Swift

```
var greetings = { (name:String, message:String) -> (String) in
   message + " " + name + " !!!"
}

greetings("Ravi","Welcome")
```

In the above code example, a closure has been assigned to a variable. The purpose of this closure is to concatenate the string parameters and return the appended message as return parameter.

#### Type Inference

The example closure can modified to ignore to the parameter types and closure supports type inference.

```
var greetings = { (name, message) -> (String) in
    return message + " " + name + " !!!"
}
greetings("Ravi","Welcome")
```

#### Implicit return

In single expression closure, you can omit the return keyword.

```
var greetings = { (name, message) -> (String) in
    return message + " " + name + " !!!"
}
greetings("Ravi","Welcome")

var numbers = [23,45,67,89,89,78]

numbers.sort {
    (number1, number2) -> Bool in return number1 < number2
}

numbers.sort { number1, number2 in return number1 < number2 }
numbers.sort { number1, number2 in number1 < number2 }

//Shorthand argument syntax
numbers.sort { $0 < $1 }

```

#### Shorthand Argument Syntax

Swift supports shorthand argument names for inline closures. In the above example used for implicit returns, the two parameters can be removed and represented in shorthand arguments as shown below.

```
numbers.sort { $0 < $1 }
```

#### Trailing Closure

In a function with closure as the last parameter, the closure can be treated as trailing closures i.e closures outside the function parenthesis call. This is quite helpful in reducing the long closure expression. For example, the sorted function has closure as the last parameter and with trailing closure this becomes as shown below.

```
var numbers = [23,45,67,89,89,78] 
var sortedNumbers = sorted(numbers, {$0 > $1}) 
// Without trailing closure 
 var sortedNumbers = sorted(numbers) {$0 > $1} 
// represented as trailing closure 
sortedNumbers
```

### Extensions

Swift extensions are similar to category in Objective-C which adds new functionally to existing class, enumeration or Struct. Extension does not require the source code of original class or enumeration type or struct to extend their functionality.

Listed below is an example which extends String class. A new function fromDouble has been added to String class which takes a double value and returns String.

```
extension String {
    static func fromDouble(doubleValue: Double) -> String {
        var temp = String(format: "%.2f", doubleValue)
        return temp as String
    }
}

String.fromDouble(doubleValue:24.50)
```

### Generics

Generics are code that produces the same result irrespective of the data type. Listed below is a function that accepts two numbers and swaps the values.

```
func swapValues(first: inout Int, second: inout Int) {
    let temp = first
    first = second
    second = temp
}

var number1 = 10
var number2 = 3

swapValues(first:&number1, second: &number2)
```

Now if we want to use the same function for swapping string values then we will have to re-write the function. Instead we can use Generics to use the function for any types. Generics solves the problem of having different set of code for different data types by implementing the functionality for a generic type.

```
func swapValues<T>(first: inout T, second: inout T) {
    let temp = first
    first = second
    second = temp
}

var first = "Ravi"
var second = "Satish"

swapValues(first:&first, second: &second)

first
second

```
