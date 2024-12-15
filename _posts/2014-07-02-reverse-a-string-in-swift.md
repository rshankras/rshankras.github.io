---
title: "Reverse a String in Swift"
date: "2014-07-02"
categories: 
  - "ios"
  - "programming"
  - "xcode"
tags: 
  - "reverse-string"
  - "swift"
  - "xcode"
---

Here is a simple code snippet written in Swift programming language for reversing a string.

`import Cocoa`

`   `

`//Assigning a value to a String variable`

`var str = "Hello, playground"`

`   `

`//Create empty character Array.`

`var strArray:Character[] = Character[]()`

`   `

`//Loop through each character in the String`

`for character in str {`

`//Insert the character in the Array variable.`

`strArray.append(character)`

`}`

`   `

`//Create a empty string`

`var reversedStr:String = ""`

`   `

`//Read the array from backwards to get the characters`

`for var index = strArray.count - 1; index >= 0;--index {`

`//Concatenate character to String.`

`reversedStr += strArray[index]`

`}`

`   `

`reversedStr`

`   `

`the shorter version to reverse is (thanks Andreas)`

`   `

var str = “Hello, playground”

var reverseStr = “”

for character in str {  
reverseStr = character + reverseStr  
}

  
  
![Reverse a String in Swift Programming language](/assets/images/201407021453.jpg)  
This code snippet demonstrates the following.

- How to assign a value to variable.

- How to create an Array of Characters and assign empty value.(Character)

- Iterate over the string using for-in loop.

- How to add new elements to an Array.

- How to create empty String variable.

- Use the standard for loop to traverse through an array.

- Concatenate Strings and character

- Using for .. in
