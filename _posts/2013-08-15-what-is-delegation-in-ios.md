---
title: "What is Delegation in iOS ?"
date: "2013-08-15"
categories: 
  - "apple"
  - "develop"
  - "ios"
tags: 
  - "apple"
  - "delegate-pattern"
  - "delegation"
  - "objective-c"
---

**Delegation** is one of the commonly used pattern in iOS. This is used tell an object to act on behalf of another. Refer to [Apple documentation](http://developer.apple.com/library/ios/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html) for detailed information on delegate pattern. Let us see this with an example program that uses UITextFieldDelegate.

This is a SingleView Project with one UITextField control.

#import "ViewController.h"

  

@interface ViewController ()

  

@end

  

@implementation ViewController

  

\- (void)viewDidLoad

{

\[super viewDidLoad\];

// Do any additional setup after loading the view, typically from a nib.

  

UITextField \*tfMessage1= \[\[UITextField alloc\] initWithFrame:CGRectMake(50, 80, 250, 150)\];

tfMessage1.borderStyle \= UITextBorderStyleRoundedRect;

\[self.view addSubview:tfMessage1\];

}

  

\- (void)didReceiveMemoryWarning

{

\[super didReceiveMemoryWarning\];

// Dispose of any resources that can be recreated.

}

  

@end

  
Now if you run the project using Xcode simulator, the UITextView will be displayed. You can type in the UITextField but when pressing Return on the keyboard will do nothing. By using delegate pattern we are going to tell UIViewController to process the pressing of the return button on behalf of UITextField and hide the keyboard.  

**Step 1**: Open the ViewController.h file and implement the UITextViewDelegate as shown below.

#import <UIKit/UIKit.h>

  

@interface ViewController : UIViewController <**UITextFieldDelegate**\>

  

@end

  
  
**Step 2**: Navigate to viewDidLoad method in implementation file, add "**self.tfMessage1.delegate= self**" as shown in the below code snippet.  
  

\- (void)viewDidLoad

{

\[super viewDidLoad\];

// Do any additional setup after loading the view, typically from a nib.

  

UITextField \*tfMessage1= \[\[UITextField alloc\] initWithFrame:CGRectMake(50, 80, 250, 150)\];

tfMessage1.borderStyle \= UITextBorderStyleRoundedRect;

\[self.view addSubview:tfMessage1\];

**tfMessage1.delegate = self;**

  

}

  
This makes the UIViewController to act on behalf of UITextField.  
  
**Step 3**: Now implement the following method that would process the "Pressing of return" key.  

\-(BOOL)textFieldShouldReturn:(UITextField \*)textField

{

\[textField setUserInteractionEnabled:YES\];

\[textField resignFirstResponder\];

return YES;

}
