---
title: "What are the different lifecycle methods in a typical UIViewController?"
date: "2023-06-30"
categories: 
  - "interview-questions"
  - "ios"
---

Here is the list of Lifecycle methods in a ViewController are

**viewDidLoad** - Called after the view controller's view hierarchy has been loaded into memory. It is used for initial setup, such as creating and configuring UI elements.

**viewWillAppear** - Called just before the view is about to be added to the view hierarchy and become visible. It is used to perform tasks that need to be done every time the view appears.

**viewDidAppear** - Called when the view has been fully transitioned onto the screen and is visible to the user. It is used to perform tasks that require the view to be on the screen.

**viewWillDisappear** - Called just before the view is removed from the view hierarchy and becomes invisible. It is used to perform cleanup or save data before the view disappears.

**viewDidDisappear** - Called when the view has been fully transitioned off the screen and is no longer visible. It is used to perform additional cleanup or reset any state as needed.

**deinit** - Called when the view controller is being deallocated from memory. It is used to perform final cleanup and release any resources held by the view controller.
