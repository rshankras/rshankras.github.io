---
title: "Access Control in Swift"
date: "2015-07-20"
categories: 
  - "ios"
  - "programming"
  - "xcode"
tags: 
  - "access-control"
  - "target-dependencies"
---

Swift like other programming languages provides option to restrict access to classes, functions, variables, structs, enums etc applying the required Access Control. These restrictions are based on each module, as per [Apple documentation](https://developer.apple.com/library/ios/documentation/Swift/Conceptual/Swift_Programming_Language/AccessControl.html) a module is defined as

> A _module_ is a single unit of code distribution—a framework or application that is built and shipped as a single unit and that can be imported by another module with Swift’s `import` keyword.

### Access Levels

There are three types of Access Control restriction that can be applied to individual types inside a module

_public_ - The least restriction applied to a member and normally used when writing public interfaces

_internal_ \- Default access level and a member with this restriction can be accessed only within the module.

_private_ - Most restricted access level and member with this restriction can be accessed only within the source file.

Check out more on Access Controls in Apple documentation [Guiding Principles of Access Levels](https://developer.apple.com/library/ios/documentation/Swift/Conceptual/Swift_Programming_Language/AccessControl.html)

Now let us see a demo on how these access levels can be used with in Swift projects or frameworks.

### Access Control Demo

Create a project using Single View Application template (though this is going to be non-UI demo). Add a new swift file with name as `Greetings.swift` and following implementation.

```swift
class Greetings {
func displayMessage() -&gt; String {
return "Welcome !!!"
}
}
```

The above class has a method named `displayMessage` that returns `String`. The access level for both Greetings class and the method is set to internal (default access level). Hence users will be able to access this class and function with in the module.

Let us replace `viewDidLoad` method in ViewController.swift with the following code snippet.

```swift
override func viewDidLoad() {
super.viewDidLoad()

let greetings = Greetings()
println(greetings.displayMessage())

}
```

You will be able to access Greetings class as well as displayMessage() function. Now if you change the access level for displayMessage() to private then you should see an error message.

```swift
private func displayMessage() -&gt; String {
return "Welcome !!!"
}
```

[![](/assets/images/1437372714_thumb.png)](https://rshankar.com/wp-content/uploads/2015/07/1437372714_full.png)

You can define a member type as private when it should be available within the source file (here it is Greetings class).

### Add Second Module

Create a new framework within the AccessControlDemo project called `RSModule` and add new swift file with name as `StringExtras` and followinng implementation.

```swift
public class StringExtras {
public static func makeFirstCharacterUpperCasse(word: String) -> String {
return word.capitalizedString
}
}
```

Note that the access level for class and function is set to `public` as we want to make these members available outside `RSModule` framework. Also the scope of the function is set to be `static` as we want to make class level funciton.

#### Add and import framework

Now to access `StringExtras` class inside `Greetings.swift` file, we need to Add and import RSModule to AccessControlDemo project. You can make `RSModule` available to this project by incuding this as part of the Target Dependcies. Click AccessControlDemo target, navigate to Build Phases and pick RSModule framework.

[![](/assets/images/1437374205_thumb.png)](https://rshankar.com/wp-content/uploads/2015/07/1437374205_full.png)

[![](/assets/images/1437374236_thumb.png)](https://rshankar.com/wp-content/uploads/2015/07/1437374236_full.png)

Navigate to `Greetings.swift` file, import the framework by adding import RSModule at the begining of the class and call the funciton in `StringExtras` class which capitalizes the first letter.

```swift
import RSModule

class Greetings {
func displayMessage() -> String {
return StringExtras.makeFirstCharacterUpperCasse("welcome !!!")
}
}
```

Download the source code from [here](https://github.com/rshankras/AccessControlDemo).
