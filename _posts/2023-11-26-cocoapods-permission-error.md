---
title: "Cocoapods Permission Error"
date: "2023-11-26"
categories: 
  - "swift"
  - "xcode"
---

Received the following error while trying to run pod install.

_errno::EACCES - Permission denied @ dir\_s\_mkdir - /Users/<username>/.cocoapods/repos/trunk/Specs/9/3_

So I had to run the command as sudo - _sudo pod install_. This successfully installed the pods for the project. But when trying to open the Xcode workspace, again received **permission denied** error for the Xcode workspace. Then following the below mentioned steps resolved the issue and I was able to open the Xcode project

1. _sudo chmod 777 <project workspace>_ file

3. _sudo chmod 777 <prokect.xcodeproj>_ file

5. _sudo chmod 777_ Pods
