---
title: "How to customize status bar in iOS"
date: "2024-03-04"
categories: 
  - "ios"
  - "programming"
  - "status-bar"
  - "swift"
  - "xcode"
tags: 
  - "style"
---

Status Bar appears at the top of your device displaying information such as battery left in your device and carrier details. The default style of status bar is black and looks as shown in the below screenshot.

[![](/assets/images/1437306660_thumb.png)](https://rshankar.com/wp-content/uploads/2015/07/1437306660_full.png)

But if your screen designs are dark then you can change the status bar style to Light Content. This can be done by adding an entry as part of info.plist file or by adding the required code in AppDelegate. And if you want to change status bar style for specific View Controllers then you can override the function `preferredStatusBarStyle`

### Add entry to info.plist

Navigate to info.plist under SupportFiles folder and add a new entry “`View controller-based status bar appearance`” with value as NO.

[![](/assets/images/1437307595_thumb.png)](https://rshankar.com/wp-content/uploads/2015/07/1437307595_full.png)

This would prevent developers from changing the status bar style for specifc View Controlllers. Now you can speciy the preferred style by selecting the project target and choosing the value for Status Bar Style drop down under Deployment Info

[![](/assets/images/1437307779_thumb.png)](https://rshankar.com/wp-content/uploads/2015/07/1437307779_full.png)

### Add code to AppDelegate

Instead of changing the option in Deployment Info, you can also do this through code by adding the following line inside AppDelegate’s `didFinishLaunchingWithOptions` method. Here we are changing the style to LightContent.

```swift
UIApplication.sharedApplication().statusBarStyle = UIStatusBarStyle.LightContent
```

### Customize style for specific ViewController

If you wish to apply the style for specific View Controllers then override the `preferredStatusBarStyle` function as shown below. This would work only if the entry “`View controller-based status bar appearance`” in info.plist file is not set NO

```swift
override func preferredStatusBarStyle() -> UIStatusBarStyle {
    return UIStatusBarStyle.LightContent
}
```
