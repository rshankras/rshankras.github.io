---
title: "Show hidden files and folders on Mac"
date: "2021-11-06"
categories: 
  - "mac"
  - "not-programming"
  - "tips"
tags: 
  - "hidden-files"
  - "hidden-folders"
---

Hidden files and folders are by default not shown on your Mac. Here are the different ways you can show hidden files and folders.

**Terminal**

1. Open Terminal and run this script, _defaults write com.apple.Finder AppleShowAllFiles true_
2. Make sure to close all finder windows and relaunch Finder -  _killall Finder_

And if you want turn off this option this change true to false, _defaults write com.apple.Finder AppleShowAllFiles false_

**Keyboard Shortcut**

Navigate to the folder you want to see the hidden files and folders and type "_Cmd + Shift + ._". And to turn off press the same keyboard combination again.

**Finder**

If you want to see the hidden library folder then follow the given steps.

1. Open Finder and navigate to Go menu bar
2. Navigate to Go to Folder and type  _~/Library_ (Keyboard shortcut in _Cmd + Shift + G_)
