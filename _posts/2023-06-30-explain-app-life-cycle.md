---
title: "Explain App Life Cycle"
date: "2023-06-30"
categories: 
  - "interview-questions"
  - "ios"
---

The app life cycle refers to the sequence of steps that app takes when an user launches an app until it terminates. Understanding the life cycle will help the developer to manage app behaviour and proper allocation and deallocation of resources.

  
Image Credit :- [Apple](https://developer.apple.com/documentation/uikit/app_and_environment/managing_your_app_s_life_cycle)

![](/assets/images/image.png)

**Not Running** - Initial stage when the app is not launched or it has been terminated by user or by the system.

**Inactive** - The app enters Inactive state when it is launched but does not receiving any user inputs.

**Active** - The app is in the foreground and receiving user inputs.

**Background** - App enters background state when the user switches to another app or home screen. Please note that the app will not directly transition from Active to Background state, it will first transition to Inactive then to Background state.

**Suspended** - App enters suspended state when system wants to free resources.

**Terminate** - App enters terminate state when it is no longer running.

Which state an app is during the following scenario? share your answer in the comment section.

1. When the app is foreground and you receive a message notification.

3. When the app is foreground and you receive a phone call and start attending.
