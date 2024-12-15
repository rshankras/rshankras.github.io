---
title: "Turn off excessive logging in Xcode 8"
date: "2016-09-25"
categories: 
  - "logging"
  - "xcode-8"
---

Xcode 8 shows lots of logging message in the console window when you run the app. If you have any print statement in your app module then it can easily get lost in these warning messages.  

[![](/assets/images/1474782495_thumb.png)](https://rshankar.com/wp-content/uploads/2016/09/1474782495_full.png)

One of the solution to avoid this excessive logging is to add a property under enviromental variable section. Navigate to Product menu and select Scheme from the menu list then Edit Scheme (Product -> Scheme -> Edit Scheme )  

[![](/assets/images/1474782706_thumb.png)](https://rshankar.com/wp-content/uploads/2016/09/1474782706_full.png)

In the Scheme screen, select Run option. Navigate to Environment Variables section and add new variable **OS\_ACTIVITY\_MODE** with value as **disable**  

[![](/assets/images/1474782882_thumb.png)](https://rshankar.com/wp-content/uploads/2016/09/1474782882_full.png)

This shoud prevent these warning/logging messages in Console window. This property has to be configured for each project in Xcode, what would be nice to have is a single configuration in Xcode for all projects :-)
