---
title: "How to rename default view controllers in XCode"
date: "2012-06-11"
categories: 
  - "xcode"
tags: 
  - "rename"
  - "view-controllers"
  - "xcode"
---

Xcode by default provides default name for the view controllers depending upon on the selected projects templates. For example, while creating Tabbed Application, you will find FirstViewController and SecondViewController as the name for default view controllers.

![NewImage](images/NewImage.png "NewImage.png")

Now if you want to provide a proper name to the FirstViewControllers and SecondViewControllers you can use the Rename option available under the Edit menu.

To rename FirstViewController,  

**Step 1**: Navigate to FirstViewController.h and select the name after interface keyword.

![NewImage](images/NewImage1.png "NewImage.png") 

**Step 2**: Click the Edit menu then Refactor and select Rename from the list of available option.

![NewImage](images/NewImage3.png "NewImage.png")

**Step 3**: Enter the name then select Rename related files and click the Preview button. This would display the list of files and location where the rename would affect.

**Step 4**: If you are happy with Preview then save the changes.

![NewImage](images/NewImage4.png "NewImage.png")

By this way you can rename the default view controller and their related files (.h, .m and XIB) in Xcode.
