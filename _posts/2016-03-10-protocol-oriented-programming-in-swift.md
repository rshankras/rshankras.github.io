---
title: "Protocol Oriented Programming in Swift"
date: "2016-03-10"
categories: 
  - "ios"
  - "swift-2"
tags: 
  - "protocol"
  - "protocol-oriented-programming"
  - "struct"
---

Object Oriented Programming is a paradigm used by programmers many decades to solve computer problems by model them in to classes. In Swift 2.0 a new programming pattern has been introduced known as Protocol Oriented Programming. In this article, we will the three major feature as part of Protocol Oriented Programming

- Model with Protocols and Structs
- Protocol Extension
- Swift Standard Library Extension

### Using Protocols and Structs

Let us see an example by model Bicylce, MotorBike and Car with Protocols and Structs. Create Vehicle and MotorVehicle protocol with the following property definition

```
protocol Vehicle {
    var speed: Int { get }
    var color: String { get }
    var yearOfMake: Int { get }
}

protocol MotorVehicle {
    var engineSize: Int { get }
    var licensePlate: String { get }
}
```

In Swift we can make any type (Class. Struct, Enums) to conform to a Protocol. Let us go for a value type (Struct) and not class as we are moving away from inheritance. And it is always safe to use value type and avoid memory related issues by using object references (Class).

```
struct Bicyle: Vehicle {
    let speed: Int
    let color: String
    let yearOfMake: Int
}

struct MotorBike: MotorVehicle, Vehicle {
    let speed: Int
    let color: String
    let engineSize: Int
    let licensePlate: String
    let yearOfMake: Int
}
struct Car: MotorVehicle, Vehicle {
    let speed: Int
    let color: String
    let engineSize: Int
    let licensePlate: String
    let numberOfDoors: Int
    let yearOfMake: Int
}
```

In the above code snippet, we have created three structs Bicycle, MotorBike and Car. Bicyle conforms to Vehicle but Car and MotorBike conform to both Vehicle and MotorVehicle. Now start creating Cars, Bicycles and MotorBikes using corresponding structs.

```
let cycle = Bicyle(speed: 10, color: "Blue",yearOfMake: 2011)
let bike = MotorBike(speed: 65, color: "Red", engineSize: 100, licensePlate: "HT-12345",yearOfMake: 2015)
let bmw = Car(speed: 220, color: "Green", engineSize: 1200, licensePlate: "FC-20 435", numberOfDoors: 4,yearOfMake: 2016)
let audi = Car(speed: 220, color: "Cyan", engineSize: 1200, licensePlate: "FC-41 234", numberOfDoors: 4,yearOfMake: 2013)

```

### Protocol Extension

In Swift 2.0, the real power Protocol comes with its ability to add extension. It is not just adding method definition but now Protocol allows you to add implementation as well. Let us say you want to compare vehicles based on yearOfMake attribute. All you need to do is to add an extension for Vehicle Protocol

```
extension Vehicle {
    func isNewer(item: Vehicle) -> Bool {
        return self.yearOfMake > item.yearOfMake
    }
}

// comparing audi and bmw should return false
audi.isNewer(item: bmw)
```

### Swift Standard Library Extension

You can also add extension to Swift standard library such CollectionType, Range, Array etc.. Let us take the following scenario where you have an array of MotorBikes and want to filter them based on licensePlate information.

```
let bike1 = MotorBike(speed: 65, color: "Red", engineSize: 100, licensePlate: "HT-12345",yearOfMake: 2015)
let bike2 = MotorBike(speed: 75, color: "Black", engineSize: 120, licensePlate: "RV-453",yearOfMake: 2013)
let bike3 = MotorBike(speed: 55, color: "Blue", engineSize: 80, licensePlate: "XY-5 520",yearOfMake: 2012)
let bike4 = MotorBike(speed: 55, color: "Red", engineSize: 80, licensePlate: "XY-7 800",yearOfMake: 2009)

let motorbikes = [bike1,bike2, bike3, bike4]
```

How about filtering of all Small Mopeds based on licensePlate containing “XY” characters. This can be achieved by adding an extension to RangeReplaceableCollection which conforms to MotorVehicle protocol. Then create a new function “filterLicensePlate” as shown below

```
extension RangeReplaceableCollection where Iterator.Element:MotorVehicle {
    func filterLicensePlate(match: String) -> [Iterator.Element] {
        var result:[Iterator.Element] = []
        
        for item in self {
            if item.licensePlate.contains(match) {
                result.append(item)
                }
            }
        return result
    }
}
let motorbikes = [bike1,bike2, bike3, bike4]
// filter only small mopeds based on XY
motorbikes.filterLicensePlate(match: "XY").count
```

Hope you found this introduction to Protocol Oriented Programming useful. Please use the comment section to add your feedback/suggestion.

### References

[WWDC 2015 - Protocol Oriented Programming](https://developer.apple.com/videos/play/wwdc2015/408/) [Mixing and Traits in Swift 2.0](http://matthijshollemans.com/2015/07/22/mixins-and-traits-in-swift-2/) [Protocol-Oriented Programming in Swift 2](http://code.tutsplus.com/tutorials/protocol-oriented-programming-in-swift-2--cms-24979) [Introducing Protocol-Oriented Programming in Swift 2](https://www.raywenderlich.com/109156/introducing-protocol-oriented-programming-in-swift-2)
