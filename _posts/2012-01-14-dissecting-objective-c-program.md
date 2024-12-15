---
title: "Dissecting Objective-C program"
date: "2012-01-14"
categories: 
  - "apple"
  - "develop"
  - "ios"
tags: 
  - "apple"
  - "objective-c"
  - "program"
---

![Fotolia_29238788_XS.jpg](images/Fotolia_29238788_XS.jpg)

We have already seen couple of examples in Objective-C like writing your [first program in Objective-C](https://rshankar.com/2012/01/11/my-fiirst-program-in-objective-c-using-xcode/) and [adding Objective-C classes](https://rshankar.com/2012/01/13/basic-tutorial-adding-objetive-c-in-xcode/). Now let us try and analyze the code to learn basic coding on Objective-C program.

**Adding Comments**

The very basic thing to learn is any programming language is "how to add comments". In Objective-C you can add comments by adding two consecutive slashes "//" before the text entries. And if you want to add block of comments (more than one line) then you start with /\* and end the comment with \*/

**Including Header files**

In Objective-C, users can include header files by adding "#import <header filename>". This would include functions and classes from the header files in to the current program. The examples that has been discussed includes "Foundation" and "Calci" header files.

#import <Foundation/Foundation.h>

#import "Calci.h"

**main keyword**

int main (int argc, const char \* argv\[\])

"main" is the keyword that marks the beginning line for execution of the program.

**Reserving memory**

  @autoreleasepool {

The execution code is provided within autoreleasepool and this allocates memory for the program. Now you do not have to explicitly drain the pool, the latest release will automatically drain the allocated memory.

**Printing Message**

  NSLog(@"My First Objective C Program using Xcode!");

NSLog routine is used for printing text messages to the console. The text that needs to be printed is preceded with "@" character. And if you want to print value from a variable then you can use "%i" along with text.

NSLog(@"Addition of two numbers %i", \[calculator addition\]);

**Method definition**

In Objective-C, you can define methods as shown below

\-(void) setNumber1:(int) n1

\-(int) addition

- "-" refers to the access specifier.
- void and int specifies the return type for the method.
- setNumber1 and addition refers to the method name.
- (int) n1 specifies the type of argument and argument that will be passed to the method.
- return number1+number2; - "return" keyword is used returning the value from the method.
