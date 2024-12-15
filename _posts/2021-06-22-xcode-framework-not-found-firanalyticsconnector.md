---
title: "Xcode - framework not found FIRAnalyticsConnector"
date: "2021-06-22"
categories: 
  - "swift"
  - "xcode"
---

Tried updating all pods in Xcode projects using pod update. Noticed the following messages in the log.

```
Removing FirebaseInstanceID
Generating Pods project
Integrating client project
```

After doing Xcode build, noticed the following error.

**Framework not found FIRAnalyticsConnector**

Looks like firebase pod has been updated and to remove the above error, navigate to Build Settings and search for "FIRAnalyticsConnector"

![](/assets/images/image-29-1024x272.png)

Open the "Other Linker Flags" setting and remove FIRAnalyticsConnector

![](/assets/images/image-30.png)

Next received "Framework not found FirebaseInstanceID" as well. Repeat the above steps and remove FirebaseInstanceID from Other Linker flags settings. Also make sure to remove from Framework Search Paths (Debug & Release) as well.
