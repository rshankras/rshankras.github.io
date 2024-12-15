---
title: "Difference between Delegate and Notifications in iOS"
date: "2023-06-29"
categories: 
  - "interview-questions"
  - "ios-developer"
---

| Delegates | Notifications |
| --- | --- |
| One-to-one communication | One-to-many or many-to-many communication |
| Customized behavior | Broadcasting information/events |
| Delegate object holds a reference | Observing objects don't need references |
| Specific responsibilities/tasks | Widely distributed information/events |
| Tight coupling between objects | Loose coupling between objects |
| Object needs to know its delegate | Posting object doesn't know receivers |
| Callbacks, data source protocols, event handling | Application-wide event handling |
