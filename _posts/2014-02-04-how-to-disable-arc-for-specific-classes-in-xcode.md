---
title: "How to disable arc for specific classes in Xcode"
date: "2014-02-04"
categories: 
  - "apple"
  - "ios"
  - "xcode"
tags: 
  - "apple"
  - "disable-arc"
  - "xcode"
---

Xcode provides option to disable arc only for specific classes by providing a compiler flag. This is quite useful when you are including framework written prior to iOS 5 in your project. Let us see the steps required for specifying the compiler flag in Xcode.

![ARC errors in Xcode](/assets/images/201402041847.jpg)

In the above screenshot, you can see errors rested ARC restrictions for NSStream+ SKSMTPExtensions.m class file. You can resolve this error by providing the compiler flag -fno-objc-arc for this class.

![201402041850.jpg](/assets/images/201402041850.jpg)

Click the Project on Xcode then Build Phases tab. Navigate to Compile Sources section and double click on Compiler flags for the corresponding file. Now enter the flag “ -fno-objc-arc” as shown in the below screenshot.

![disable ARC in Xcode](/assets/images/201402041853.jpg)

This should resolve all the compilation related with ARC.
