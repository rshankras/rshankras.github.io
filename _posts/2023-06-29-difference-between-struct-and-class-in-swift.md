---
title: "Class and Struct in Swift"
date: "2023-06-29"
categories: 
  - "apple"
  - "ios"
  - "programming"
tags: 
  - "apple"
  - "classes"
  - "structures"
  - "swift"
---

Download the playground file from [github](https://github.com/rshankras/Playground) (Classes and Struct)

### Class

A class is a blue print for a real-word entity such Player, Person etc. and it is used for creating objects. Class can have properties to store values and methods to add behaviour. Let us see this with an example class called Rectangle which has some properties and two methods for calculating area and for drawing a rectangle.

```
class Rectangle {

var name:String = ""
var length:Double = 0
var breadth:Double = 0

 func area() -> Double {
   return length * breadth
 }

 func draw() -> String {
   return "Draw rectangle with area \(area()) "
 }
}

let rect = Rectangle()

rect.length = 20
rect.breadth = 10
rect.draw()

```

In the above example, we have a class named Rectangle, with name, length and breadth as properties, area and draw are functions. rect is a instance variable or object of Rectangle class. On setting the length and breadth and calling draw function should provide the following output in Playground.

![201505101309.jpg](images/2015051013091.jpg)

Similarly the below code create a Square class

```
class Square {

 var name:String = ""
 var length:Double = 0

 func area() -> Double {
  return length * length
 }

 func draw() -> String {
  return "Draw a square with area \(area()) "
 }
}

let squr = Square()
squr.length = 20
squr.draw()
```

Now instead of repeating property and functions in each classes let us use class inheritance to simplify these classes.

#### Class Inheritance

Let us create a parent class called Shape and its properties and functions will be inherited by Sub Classes Rectangle and Square.

**Parent Class - Shape**

```
class Shape {
    var name: String = ""

    func area() ->Double {
        return 0
    }

    func draw() ->String {
        return "Draw a \(name) with area \(area()) "
    }
}

```

**Sub Class - Square**

```
class Square:Shape {
    var length: Double = 0

    override func area() ->Double {
        return length * length
    }
}

let squr = Square()
squr.name = "My Square"
squr.length = 5
squr.draw()

```

**Sub Class - Rectangle**

```
class Rectangle:Shape {
    var length: Double = 0
    var breadth: Double = 0

    override func area() -> Double {
        return length * breadth
    }
}

let rect = Rectangle()
rect.name = "My Rectangle"
rect.length = 5
rect.breadth = 10
rect.draw()
```

Parent class Shape has been created with name property and with functions area and draw. The child class Square and Rectangle will inherit these property and methods. Apart from the parent class property, Square can have its own property length and Rectangle has length and breadth.

The parent class area function has been overridden by Square and Rectangle class to calculate corresponding areas. Now if you want add one more Shape such as Triangle, Circle etc the new class has to inherit Parent class (Shape) and add its own property and methods (or override methods).

### Initialisers

Initialisers in Class and Struct are used for setting the default values for properties and for doing some initial setup. Here is a typical example of initialiser in a Class where the name property is initialised at the time of creating an instance.

```
class Shape {
    var name: String
    
    init(name: String) {
        self.name = name
    }

    func area()-> Double {
        return 0
    }

    func draw()-> String {
        return "Draw a \(name) with area \(area())"
    }
}

class Square: Shape {
    var length: Double = 0

    init() {
        super.init(name: "MySquare")
    }

    override func area()-> Double {
        return length * length
    }

    override func draw()-> String {
        return "Draw a \(name) with area \(area())"
    }
}

let squr = Square()
squr.length = 10
squr.draw()
```

The sub class Square initialises the name property in init function by calling super.init and after creating the Square instance you need to pass value for the length property.

#### Designated and Convenience Initialisers

Initialiser which initialises all the properties in a class is known as designated initialiser. A convenience initialiser will initialise only selected properties and in turn will call the designated initialiser in init function. Listed below is a Square class with designated initialiser and convenience initialiser

```
class Shape {
    var name: String

    init(name: String) {
        self.name = name
    }

    func area()-> Double {
        return 0
    }

    func draw()-> String {
        return "Draw a \(name) with area \(area())"
    }
}

class Square: Shape {

    var length: Double

    // Designated Initialiser
    init(length:Double, name:String) {
        self.length = length
        super.init(name: name)
    }

    // Convenience Initialiser
    convenience init(length: Double) {
        self.init(length:length, name:"MySquare")
    }

    override func area()-> Double {
        return length * length
    }

    override func draw()-> String {
        return "Draw a \(name) with area \(area())"
    }
}

let squr = Square(length: 10,name: "MySquare")
squr.draw()

let squrNew = Square(length: 20)
squrNew.draw()
```

### Computed Property

A property in swift can be used for performing operation at the time of assigning value. Here is an example, where the length of Square is computed based on assigned area.

```
class Square {
    var length: Double = 0
    
    var area: Double {
        get {
            return length * length
        }

        set (newArea) {
            self.length = sqrt(newArea)
        }
    }
}

let square = Square()
square.area = 4 // set call
square.length = 6
square.area // get call
```

### lazy Property

Swift also provides lazy property whose value is assigned when the user access the property.

```
class Person {

    var name: String

    init (name: String) {
        self.name = name
    }


    lazy var message: String = self.getMessage()


    func getMessage()-> String {
        return "Hello \(name)"
    }
}

let person = Person(name: "Jason")
person.message
```

in the above code example, the value for message property is not set at the initialisation and will be set only when call the message property in person object. Some typical where you could due lazy property is when retrieving values from performance intensify operation such as Network or Read/Write.

### Property Observers

Swift provides two property observers, willSet and didSet. These methods gets triggered when a value is about to be set for a property or after setting the property.

```
class Square {
    var length: Double = 0 {

        willSet(newLength) {
            print("Setting length \(self.length) to new length \(newLength)")
        }

        didSet {
            print("Length is modified - do some action here")
        }
    }

    var area: Double {
        get {
            return length * length
        }

        set (newArea) {
            self.length = sqrt(newArea)
        }
    }
}

let square = Square()
square.length = -6
square.area
```

In the above example, Square class length property has a willSet and didSet observers.

### Struct

Struct and Class can both have properties, methods, protocols, extensions and initialisers. You can use struct to hold simple values and when you want to pass around those across your program.

```
struct GeoDetails {
    var country: String
    var ip: String
    var isp: String
    var latitude: Double
    var longitude: Double
    var timeZone: String

    init(country: String, ip: String, isp: String, latitude:Double, longitude:Double, timeZone:String) {
        self.country = country
        self.ip = ip
        self.isp = isp
        self.latitude = latitude
        self.longitude = longitude
        self.timeZone = timeZone
    }

    func description()-> String {
        return "Country " + self.country + ", ip " + self.ip + ", isp " + self.isp + ", latitude \(self.latitude), longitude \(self.longitude) "
    }
}
```

Download the playground file from [github](https://github.com/rshankras/Playground) (Classes and Struct)
