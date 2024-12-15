---
title: "Integrating Stripe in Swift for iOS development"
date: "2014-09-02"
categories: 
  - "develop"
  - "ios"
  - "iphone-4s"
  - "programming"
tags: 
  - "stripe"
  - "swift"
---

[Stripe](https://stripe.com/) is payment gateway that can be integrated with any website and mobile apps. In this tutorial we will see a quick and simple integration of Stripe in Swift for iOS development using [Stripe documentation for iOS](https://stripe.com/docs/mobile/ios).

![201409021233.jpg](images/201409021233.jpg)

This hands on tutorial will help you to familiarise yourself in

- Validating and creating token using Stripe IOS SDK

- Installing third party library using Cocoa-pods (Stripe)

- Calling Objective-C framework in Swift (Objective-C Bridging Headers settings)

Click File menu and select New -> Project

![201409021049.jpg](images/201409021049.jpg)

Select Single View Application as the template for the project.

![201409021050.jpg](images/201409021050.jpg)

Provide a name for your project and select the language as Swift.

![201409021110.jpg](images/201409021110.jpg)

Now close the project in Xcode and launch terminal window.

### Setup Stripe using Cocoa-pods

Run the following commands on your terminal window to install Stripe.

\[code language="plain"\]sudo gem install cocoapods pod init\[/code\]

Edit Podfile under project directory and add pod ‘Stripe’ then execute the below command in Terminal window.

\[code language="plain"\]pod install\[/code\]

Navigate to the project folder and launch the file with extension as workspace. Now you should see the Stripe frameworks included under Pods directory along with your default project files.

![201409021131.jpg](images/201409021131.jpg)

### Write code to integrate Stripe

Edit ViewController.swift and add the following IBOutlet variable for the button.  

\[code language="swift"\]@IBOutlet var saveButton: UIButton!\[/code\]

Now add the following variable declaration to ViewController.swift file to hold the instance of STPView class.  

\[code language="swift"\]var stripeView: STPView = STPView()\[/code\]

Since the Stripe framework has been written in Objective-C, we need to make sure to add the implementation file as part of the **Objective-C bridging Headers** under Build Settings.

Select Project folder and navigate to Build Settings. Then use the search field to locate to Objective-C Bridging Header setting.

![201409021153.jpg](images/201409021153.jpg)

Then drag and drop the STPView.m file to Object-C Bridging Header section.

![201409021155.jpg](images/201409021155.jpg)![201409021156.jpg](images/201409021156.jpg)

Update the viewDidLoad function and add the following Stripe integration code. Make sure the ViewController class conforms to **STPViewDelegate** protocol  

\[code language="swift"\]class ViewController: UIViewController, STPViewDelegate{ override func viewDidLoad() { super.viewDidLoad() stripeView = STPView(frame: CGRectMake(15, 20, 290, 55), andKey: ) stripeView.delegate = self view.addSubview(stripeView) saveButton.enabled = false } }\[/code\]

The above lines of code will add the Stripe control that accepts credit card number, expiry date and code. The save button is by default disabled and will be enabled only after entering valid credit card number. Implement the following function that will be triggered after entering the card details. The boolean parameter in the function will indicate whether the user has entered a valid card information. Based on this value, the save button is enabled or disabled.  

\[code language="swift"\]func stripeView(view: STPView!, withCard card: PKCard!, isValid valid: Bool) { if (valid) { saveButton.enabled = true } else { saveButton.enabled = false } }\[/code\]

Add the following IBAction function which will be called on tap of the button. We are using STPView’s createToken function to generate token and a successful token will be written to the console window.  

\[code language="swift"\]@IBAction func saveButton(sender: AnyObject) { stripeView.createToken { (stpToken, error) -&gt; Void in if (error != nil) { println(error) } else { println(stpToken) } }\[/code\]

Navigate to Main.storyboard and add UIButton from object library to ViewController. Centre align the button both horizontally and vertically to the View Controller.  

![201409021138.jpg](images/201409021138.jpg)

Then use Connection Inspector to connect the button to IBOutlet variable and saveButton function to Tap Up Inside event of the button.

![201409021228.jpg](images/201409021228.jpg)

Now build and run the project on simulator and you can use dummy card number 4242 4242 4242 4242 to test your implementation. For more details refer to [Stripe Testing Documentation.](https://stripe.com/docs/testing)  

### Sample Output

\[code language="plain"\]Successful token - tok\_14YBF42eZvKYlo2CoZtuO3Md (test mode)

Error message - Error Domain=NSURLErrorDomain Code=-1009 "The Internet connection appears to be offline." UserInfo=0x7f9b7147b4a0 {NSUnderlyingError=0x7f9b71786ca0 "The Internet connection appears to be offline.", NSErrorFailingURLStringKey=https://pk\_test\_6pRNASCoBOKtIshFeQd4XMUh:@api.stripe.com/v1/tokens, NSErrorFailingURLKey=https://pk\_test\_6pRNASCoBOKtIshFeQd4XMUh:@api.stripe.com/v1/tokens, \_kCFStreamErrorDomainKey=12, \_kCFStreamErrorCodeKey=8, NSLocalizedDescription=The Internet connection appears to be offline.}\[/code\]

[Download Demo Project from GitHub](https://github.com/rshankras/SwiftStripeDemo.git)
