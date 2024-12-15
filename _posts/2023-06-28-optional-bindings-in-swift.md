---
title: "Optional binding and Optional Chaining"
date: "2023-06-28"
categories: 
  - "apple"
  - "ios"
tags: 
  - "apple"
  - "optional-bindings"
  - "optional-chaining"
  - "swift"
---

[Swift](https://rshankar.com/swift-quick-reference/) has a feature that lets users to assign optional value to a variable or a constant. Optional variable or constant can contain a value or a nil value. Let us take the following example which tries to find a given string in a array of string.

### Optional Binding

```
var fruits = ["Apple","Orange","Grape","Mango"] 
let searchIndex = fruits.firstIndex(of: "Apple")
```

The searchIndex would return value if the fruit exists or nil value if it doesn’t exist.

```
print("Fruit index is \(searchIndex)")
```

The proper way to handle this by using Optional binding method.

```
if let searchIndex = searchIndex {
 print("Fruit index is \(searchIndex)")
} else {
 print("Not available")
}
```

This would ensure only when searchIndex has a value the print with searchIndex gets executed.

### Optional Chaining

Optional chaining is the way by which we try to retrieve values from a chain of optional values. Let us take the following example classes.

```
class School {
  var director:Person?
}

class Person {
var name: String = ""

init(name: String) {
    self.name = name
  }
}
```

```
var school = School()
var person = Person(name: "Jason")
school.director = person
school.director?.name
```

The director property in School class is optional, when you try to access subsequent values from director property becomes optional (? mark after director when accessing name property). You can handle these optionals as shown below.

```
if let name = school.director?.name {
  print("Director name is \(name)")
} else {
  print("Director yet to be assigned")
}
```
