---
title: "NSLog datatype formatting option in Objective-C"
date: "2013-03-04"
categories: 
  - "apple"
  - "develop"
  - "programming"
tags: 
  - "apple"
  - "data-type"
  - "formatting-option"
  - "nslog"
  - "objective-c"
---

![201303040743.jpg](/assets/images/201303040743.jpg)

NSLog in Objective-C is function call that is useful during debugging of a program. A typical NSLog example is

> NSLog(@" How to use NSLog");

The above statement prints the message " How to use NSLog " in console window. If you want to print the value of Objective-C variable or data type then you need to pass the relevant formatting parameter depending on data type. We have already seen [different datatype and qualifiers in Objective-C](https://rshankar.com/2013/03/03/different-data-types-in-objective-c/), below is example Objective-C program with NSLog formatting option for each datatypes.

#import <Foundation/Foundation.h>

  

int main(int argc, const char \* argv\[\])

{

  

int i = 5;

float f = 5.3;

double d = 66.76;

long int li = 22;

short int si = 12;

char c = 'W';

signed int sint = 34;

unsigned int uint = -23;

int o = 024;

int h = 0xAD;

long long ll = 45;

long double lf = 34.5;

unsigned long long ull = 12;

NSString \*msg = @"NSLog Message";

@autoreleasepool {

  

NSLog(@" print int %d", i);

NSLog(@" print float %f", f); // use %e for exponential

NSLog(@" print double %f", d); // use %e for exponential

NSLog(@" print long int %li", li);

NSLog(@" print short int %i", si);

NSLog(@" print char %c", c);

NSLog(@" print signed int %i", sint);

NSLog(@" print unsigned int %u", uint);

NSLog(@" print octal %o", o);

NSLog(@" print hexadecimal %X", h);

NSLog(@" print long long %lld", ll);

NSLog(@" print long double %Lf", lf);

NSLog(@" print unsigned long long %llu", ull);

NSLog(@" print Object %@", msg);

}

return 0;

}

  

  

The console output of the above Objective-C program is shown below  

**2013-03-04 07:25:10.187 NSLog Example\[362:303\] print int 5**

**2013-03-04 07:25:10.189 NSLog Example\[362:303\] print float 5.300000**

**2013-03-04 07:25:10.189 NSLog Example\[362:303\] print double 66.760000**

**2013-03-04 07:25:10.190 NSLog Example\[362:303\] print long int 22**

**2013-03-04 07:25:10.190 NSLog Example\[362:303\] print short int 12**

**2013-03-04 07:25:10.190 NSLog Example\[362:303\] print char W**

**2013-03-04 07:25:10.191 NSLog Example\[362:303\] print signed int 34**

**2013-03-04 07:25:10.191 NSLog Example\[362:303\] print unsigned int 4294967273**

**2013-03-04 07:25:10.192 NSLog Example\[362:303\] print octal 24**

**2013-03-04 07:25:10.192 NSLog Example\[362:303\] print hexadecimal AD**

**2013-03-04 07:25:10.193 NSLog Example\[362:303\] print long long 45**

**2013-03-04 07:25:10.193 NSLog Example\[362:303\] print long double 34.500000**

**2013-03-04 07:25:10.194 NSLog Example\[362:303\] print unsigned long long 12**

**2013-03-04 07:25:10.194 NSLog Example\[362:303\] print Object NSLog Message**

> int %d or %i
> 
> float %f or %e
> 
> double %f or %e
> 
> long int %li
> 
> short int %i
> 
> char %c
> 
> signed int %i
> 
> unsigned int %u
> 
> octal %o
> 
> hexa %X
> 
> long long %lld
> 
> long double %Lf
> 
> unsigned long long %llu
> 
> object %@
