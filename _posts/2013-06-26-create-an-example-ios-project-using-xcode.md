---
title: "Create an example iOS Project using Xcode"
date: "2013-06-26"
categories: 
  - "apple"
  - "develop"
  - "iphone-4s"
  - "xcode"
tags: 
  - "apple"
  - "iphone"
  - "xcode"
---

We had already covered the **[basic overview of Xcode](https://rshankar.com/2013/06/21/basic-overview-of-xcode/)** and now we are going see the steps required for creating an sample iOS Project that displays Welcome message on Xcode simulator.

**Topics Covered**

1. Create New Project using Xcode.

3. Add label control to Interface Builder.

5. Edit label to add Welcome message

7. Choose simulator in Xcode.

9. Compile, Build and Run the project in Xcode.

**Step 1**: Launch Xcode then click FIle -> New -> Project.

![201306251050.jpg](/assets/images/201306251050.jpg)

**Step 2**: In the Choose a template for your new project, pick Single View Application under the IOS section and click the Next button.

![201306251052.jpg](/assets/images/201306251052.jpg)

Note :- We will cover the different templates in detail in future tutorials.

**Step 3**: Now in Choose options for your new project, enter the name for your project, organisation name and company identifier. In the Devices drop down select iPhone and mark the check box with caption as "Use Storyboards" and "Use Automatic Reference Counting" and click Next button.

![201306251100.jpg](/assets/images/201306251100.jpg)

Some of the above terms like Storyboards, Automatic Reference Counting will be covered in future tutorials.

**Step 4:** Specify the location for creating this project and click the Create button.

![201306251110.jpg](/assets/images/201306251110.jpg)  

Now a new project should be created and you should see a screen as shown below.

![201306251115.jpg](/assets/images/201306251115.jpg)  

**Step 5**: Select the MainStoryboard.storyboard in the Navigator Pane to access the Interface Builder.

![201306251120.jpg](/assets/images/201306251120.jpg)

**Step 6**: Navigate to Utilities section and click Object tab. Scroll down and pick label control from the list then drag and drop the label on to Interface Builder.

![201306251123.jpg](/assets/images/2013062511231.jpg)

  
![201306251123.jpg](/assets/images/201306251123.jpg)

**Step 7**: Edit the label and enter Welcome text.

![201306251125.jpg](/assets/images/201306251125.jpg)

**Step 8**: Now select the iPhone simulator under Scheme section in Xcode toolbar.

![201306251129.jpg](/assets/images/201306251129.jpg)

**Step 8**: Select Run option on Xcode toolbar or use the keyboard combination of command + R to run the sample project on [Xcode simulator for iPhone](https://rshankar.com/2013/03/02/xcodes-ios-simulator-for-iphone-and-ipad/). command + R will first compile and build the project before launching it on the simulator.
