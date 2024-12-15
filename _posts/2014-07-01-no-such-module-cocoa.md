---
title: "No such module Cocoa"
date: "2014-07-01"
categories: 
  - "develop"
  - "programming"
  - "xcode"
tags: 
  - "error"
  - "playground"
  - "xcode"
---

**No such module Cocoa** error message is displayed when the type of playground file selected is iOS instead of OS X. Make sure to select Playground under OS X if you want to use Cocoa framework and go for UIKit incase of iOS

![Choose a template from your new file](/assets/images/201407012048.jpg)

Another alternate way is to change the template using the Playground Settings. Use the toggle option to show the Utilities.

![Show the Utilities on Playground](/assets/images/201407012052.jpg)

Navigate to **Playground Settings** section, click the Platform drop down and select **OS X** from the list. This should also resolve the **No such module error** on **Playground**.

![Playground Settings](/assets/images/201407012053.jpg)
