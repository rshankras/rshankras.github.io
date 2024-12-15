---
title: "This bundle is invalid. The value for key CFBundleVersion error"
date: "2024-02-06"
categories: 
  - "mac"
  - "swift"
---

If you are receiving the following error while trying to upload your binary from Xcode organiser to AppStoreConnect then try incrementing the build number.

`This bundle is invalid. The value for key CFBundleVersion [1] in the Info.plist file must contain a higher version than that of the previously uploaded version [1]. Please find more information about CFBundleVersion at https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleversion (ID: be5c5eb9-2745-4eeb-bcee-a30c6249488b)`

I checked and found that I had correctly increased the "Version" number (CFBundleShortVersionString), but I had forgotten to change the "Build" number (CFBundleVersion), and it was still set to 1, which was the same as the previous version.

![](/assets/images/Screenshot-2024-02-06-at-4.58.54-PM.png)  
So, to fix the issue, they increased the "Build" version number, and after doing that, I was able to upload the app successfully. This was the first time I had encountered a problem like this because I usually don't change the build number when releasing new versions. Not sure whether this is related with only Mac OS apps.
