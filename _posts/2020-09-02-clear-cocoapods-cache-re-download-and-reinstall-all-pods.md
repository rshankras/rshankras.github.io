---
title: "Clear CocoaPods cache, re-download and reinstall all pods"
date: "2020-09-02"
tags: 
  - "cocoapods"
  - "swift"
---

Here is the code snippet to clear CocoaPods cache then re-download and reinstall all pods.

rm -rf "${HOME}/Library/Caches/CocoaPods"

rm -rf "\`pwd\`/Pods/"

pod update

[Source](https://gist.github.com/mbinna/4202236)
