---
title: "Attribute Unavailable: Estimated section warning before iOS 11.0"
date: "2021-11-12"
categories: 
  - "ios"
  - "swift"
  - "xcode"
tags: 
  - "ios-2"
  - "xcode-warning"
---

Xcode 13 (iOS 15) displays the following warning message for project having minimum deployment as iOS 10.

- **Attribute Unavailable: Estimated section header height before iOS 11.0**
- **Attribute Unavailable: Estimated section footer height before iOS 11.0**

This warning gets displayed for new UITableViewController added to the Storyboard file. You can get rid of the warning messages by adding 0 to **Estimate Header** and **Estimate footer** for **Sections** under **Size Inspector**

![](/assets/images/image-2.png)
