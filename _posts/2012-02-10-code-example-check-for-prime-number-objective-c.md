---
title: "Code Example - Check for Prime Number Objective C"
date: "2012-02-10"
categories: 
  - "testing"
  - "develop"
  - "ios"
tags: 
  - "objective-c"
  - "prime-number"
  - "program"
---

This is a simple **Objective C** program written to check whether a **number** is a **Prime number.**

//

// main.m

// PrimeNumbers

//

// Created by Ravi Shankar on 10/02/12.

// Copyright (c) 2012 rshankar.com. All rights reserved.

//

  

#import <Foundation/Foundation.h>

  

int main (int argc, const char \* argv\[\])

{

  

@autoreleasepool {

int number;

BOOL isPrime=YES;

NSLog (@"Enter a number");

scanf("%i",&number);

for (int i=2; i < number -1; i++)

{

if (number % i == 0)

{

isPrime = NO;

break;

}

}

if (isPrime)

{

NSLog (@"%i is a Prime Number",number);

}

else

{

   NSLog (@"%i is not a Prime Number", number);

}

}

return 0;

}

  
Output (as displayed in Xcode console window)  

**2012-02-10 15:53:52.072 PrimeNumbers\[1164:707\] Enter a number**

23

**2012-02-10 15:53:58.665 PrimeNumbers\[1164:707\] 23 is a Prime Number**

**2012-02-10 15:54:41.469 PrimeNumbers\[1176:707\] Enter a number**

24

**2012-02-10 15:54:44.589 PrimeNumbers\[1176:707\] 24 is not a Prime Number**

**This program checks whether the number is divisible by any of the n-1 number and if divisible (% operator returns reminder as 0) then the flag is set to false otherwise it is set to true. Then based on the flag value the message is printed to the console window.  
**
