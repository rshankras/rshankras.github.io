---
title: "iPad App that prints Welcome Message"
date: "2012-02-02"
categories: 
  - "apple"
  - "develop"
  - "ios"
  - "ipad"
tags: 
  - "app"
  - "apple"
  - "ipad"
  - "welcome"
---

Here is an example of writing an iPad app that prints a Welcome message.

Launch Xcode, click File -> New -> New Project.

![New Project](images/201202011215.jpg)

Now select the template for the project as Single View Application.

![Project Template ](images/201202011219.jpg)

Provide the details for your project, like Product Name, Company Name then choose the device for which you are writing the App. Also mark the check box with label as Use Automatic Reference Counting and click the Next button.

![Options for New IPad Project](images/201202011223.jpg)

And finally click the Create button to complete the project creation. Now Open the ViewController.xib file and using the Interface Builder designed add two label controls , TextField and Button as shown below.

![UI Interface Builder](images/201202021110.jpg)

Label 1 is used for displaying the caption "Enter your Name", TextField is used for accepting user input, Display button is used for printing the Welcome message in the second label.

Now edit ViewController.h file and add two IBOutlet elements for UITextField and UILabel and IBAction element for button as shown below.

#import <UIKit/UIKit.h>

@interface ViewController : UIViewController

{

IBOutlet UITextField \*txtName;

IBOutlet UILabel \*lblMessage;

}

\-(IBAction) btnDisplay;

@end

Then edit ViewController.m file and implement the IBAction function as shown below

\- (IBAction)btnDisplay {

lblMessage.text \= \[@"Welcome " stringByAppendingString: \[txtName text\]\];

}

This function creates local string by adding "Welcome " and suffixing it with the name entered in the Textfield. After completing the coding part, it is time to connect the UI Interface elements with the Object References in code. Select ViewController.xib in the Project Navigator section then click the File's Owner under Place Holder section. Drag and drop the respective object references to the UI element and connect map the btnDisplay with the Button Touch Down event. The completing mapping of UI Interface elements with Object References is shown below. ![UI Elements and Object Reference Mapping](images/201202021441.jpg)

Now the Run the App in iPad simulator by clicking the Run option on the menu bar or by pressing Control + R on the Keyboard. ![iPad Simulator](images/201202021444.jpg) Now entering the name and clicking the Display button will print the Welcome message as shown below. ![Welcome App in iPad Simulator](images/201202021445.jpg)
