---
title: "Apple Mach-O-Linker Id Error - OBJC_CLASS_$_MFMailComposeViewController"
date: "2012-03-11"
categories: 
  - "apple"
tags: 
  - "apple"
  - "apple-mach"
  - "linked-error"
---

Xcode displays the **Apple Mach-O undefined symbols for architecture error** when the library referred in the code is not included as part of Build Phases. For example, I was instantiating MFMailComposeViewController in one of my project

  MFMailComposeViewController \*mc = \[\[MFMailComposeViewController alloc\] init\];

  

And while trying to compile the code, the build failed and displayed the following error.

Undefined symbols for architecture i386:   

"\_OBJC\_CLASS\_$\_MFMailComposeViewController", referenced from:

objc-class-ref in RootViewController.o

ld: symbol(s) not found for architecture i386

clang: error: linker command failed with exit code 1 (use -v to see invocation)

I was able to fix this issue by including the MessgeUI.framework library as part of the Build Phases.

In Xcode, navigate to Project Summary screen then to the Build Phases tab

![201203110834.jpg](images/201203110834.jpg)

Click the Add Items (+ sign) under **Link Binary With Libraries** section then select MessageUI.frameework from the list and click the Add button.

![201203110836.jpg](images/201203110836.jpg)

![201203110842.jpg](images/201203110842.jpg)

Similarly by including the relevant libraries you can resolve the obj-class-ref errors.
