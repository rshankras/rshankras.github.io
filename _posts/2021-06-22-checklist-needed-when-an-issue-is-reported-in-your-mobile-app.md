---
title: "Checklist needed when an issue is reported in your mobile app."
date: "2021-06-22"
categories: 
  - "swift"
  - "tips"
tags: 
  - "issue"
---

The major work when a bug is reported in your production app is to identify the steps required to replicate the issue.

![](/assets/images/1991279-1024x1024.jpg)

1. Get the app version of the device.
2. Get the operating system version, device model, user locale. Incase of iOS the number of parameters or less where as in case Android it is more.
3. If it is visual or display error then try to get a screenshot.
4. If it is a crash then check **Firebase Crashlytics** or other crash recording framework that you are using.
5. Check if the crash or issue happening in previous version of the build. This way you can isolate if it is problem related with the latest build.

if you would like add any other steps, please use the comments section. Thank you.
