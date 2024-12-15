---
title: "My fiirst program in Objective C using Xcode"
date: "2012-01-11"
categories: 
  - "apple"
  - "develop"
  - "ios"
tags: 
  - "apple"
  - "objective-c"
  - "program"
  - "xcode"
---

This tutorial is about writing a basic and simple program in Objective C using Xcode. Let us see an example program that prints "My First Program" in the Console Window.

![Xcode new project window](/assets/images/201201110621.jpg)

Click the File menu on Xcode, then navigate to New -> New Project. This would display the following Choose a template window. Now select Application under Mac OS X then the Command Line Tool option.

![Xcode Command Line Tool](/assets/images/201201110622.jpg)

In the Choose options for your new project, enter the name of Product Name and select the Type as Foundation and leave the rest of the option as it is. Click Next to continue with the project creation.

![Xcode Choose Project Options](/assets/images/201201110627.jpg)

Now specify the location where you want to create the project folder and click Next to continue with the setup.

![Xcode Project Creation Folder](/assets/images/201201110629.jpg)

This would create a new project window as shown below.

![Xcode Project Window](/assets/images/201201110635.jpg)

Navigate to Project Navigator and edit main.m file. The Xcode would have already pre-populated code as shown below

//

// main.m

// Exercise1

//

// Created by Ravi Shankar on 11/01/12.

// Copyright (c) 2012 \_\_MyCompanyName\_\_. All rights reserved.

//

#import <Foundation/Foundation.h>

int main (int argc, const char \* argv\[\])

{

@autoreleasepool {

// insert code here...

NSLog(@"Hello, World!");

}

return 0;

}

Change the "Hello World" text to "My First Objective C Program using Xcode" and save the changes (Command + S).

@autoreleasepool {

// insert code here...

NSLog(@"My First Objective C Program using Xcode!");

}

You can Run the project in Xcode by clicking Product menu and select Run from the menu list.

![Xcode Project Build](/assets/images/201201110646.jpg)

You can Run Once the build is complete and successful, the output window in the bottom of Xcode will print the message as "My First Objective C Program using Xcode".

![Xcode Console Output Window](/assets/images/201201110650.jpg)
