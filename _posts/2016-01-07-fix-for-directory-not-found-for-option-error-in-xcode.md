---
title: "Fix for Directory not found for option error in Xcode"
date: "2016-01-07"
tags: 
  - "error"
  - "xcode"
---

You might see Directotry not found for option error when opening an iOS 8 existing project in Xcode 7. This error because of the invalid path sepcifed from the Framework Path for the test target,

> (null): Directory not found for option '-F/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator9.2.sdk/Developer/Library/Frameworks'  

This can be fixed by selected the test target, navigating Search Paths and removing the entry specified for “Framework Search Paths"  

[![](/assets/images/1452185363_thumb.png)](https://rshankar.com/wp-content/uploads/2016/01/1452185363_full.png)
