---
title: "payworks SDK integration in Swift"
date: "2015-03-26"
categories: 
  - "apple"
  - "ios"
  - "iphone-4s"
  - "mac"
  - "programming"
tags: 
  - "apple"
  - "integration"
  - "payowrks"
  - "swift"
---

[payworks](http://www.payworksmobile.com/home) mPOS helps app developers to integrate their App with card reader. In this tutorial, we will see a sample app that integrates payworks mPOS using Swift.

Download the source code from [github](https://github.com/rshankras/SwiftPayworksDemo)  

Select New Project and choose Single View Application from the template.

![201503260807.jpg](/assets/images/201503260807.jpg)

In the Project Options window, provide a product name and make sure to select Language as Swift. Click Next and Save the project.

![201503260812.jpg](/assets/images/201503260812.jpg)

In the Project Navigator, select Main.storyboard and unmark check box "Use Size Classes" in the File Inspector. Then click Disable Size Classes button as this app is only designed for iPhone

![201503260825.jpg](/assets/images/201503260825.jpg)

**UI Design**

Design the user interface as shown below.

- Label to shown caption as Amount

- TextField for entering the amount

- Button to Charge Amount.

- Label to display the status message.

![201503260840.jpg](/assets/images/201503260840.jpg)

Just to reflect the purpose of this little app, let us rename the ViewController.Swift to ChargeViewController.swift. Make the corresponding changes to Class name as well in Identity Inspector.

**Integrate mPOS SDK**

We are going to add mPOS SDK to this project using CocoaPods by following the instructions [here](http://www.payworks.mpymnt.com/node/101).

Close your Xcode project, launch Terminal window and and navigate to project folder.

![201503260927.jpg](/assets/images/201503260927.jpg)

Create a new Podfile with the following statements

![201503260929.jpg](/assets/images/201503260929.jpg)

Doing a pod install should download the mPOS SDK’s to your project folder.

![201503260936.jpg](/assets/images/201503260936.jpg)

Now navigate to your project folder and open the file with extension as .xcworkspace. The Pods folder in the project navigator should contain the mPOS framework.

![201503260956.jpg](/assets/images/201503260956.jpg)

**Objective-C Bridging**

We need to create a bridge file to call the objective-c related framework files in our Swift app. The easiest way to do this is to create new Objective-C file in your project.

Right click on your project folder, select New File.

![201503260959.jpg](/assets/images/201503260959.jpg)

In the Choose a template screen, select Objective-C and click Next.

![201503261005.jpg](/assets/images/201503261005.jpg)

Provide a name for the Objective-C file and save the file.

![201503261007.jpg](/assets/images/2015032610071.jpg)

Now you will prompted whether you would like to configure an Objective-C bridging header. Click Yes to create the bridging header file.

![201503261007.jpg](/assets/images/201503261007.jpg)

As the header file is created, we do not need the temp objective-c file, you can delete this file.

![201503261021.jpg](/assets/images/201503261021.jpg)

Navigate to Bridging-Header file in Project navigator and the following lines.

@import Foundation;

#import

  
Now you can make sure every thing works fine by doing a build. Also make sure to add the additional steps as mentioned in the [instruction page](http://www.payworks.mpymnt.com/node/101) for Miura Readers. Navigate to info.plist and add supported external accessory protocols and Required background modes keys.  
![201503261032.jpg](/assets/images/201503261032.jpg)  
**mPOS integration**  
Create two IBOutlets, one for TextField and another for Message Label.  

  @IBOutlet weak var amountTxtField: UITextField!

@IBOutlet weak var messageLabel: UILabel!

Use the connection inspector to connect the IBOutlets with the controls.

  

![201503261037.jpg](/assets/images/201503261037.jpg)

  

In order to connect with mPOS SDK, you need to register and get the merchant credentials, You can do this by registering [here](https://test.payworks.io/uis/mngr/#/register). After receiving the credentials create two constants to hold the identifier and secret key.  

  

  let MERCHANT\_IDENTIFIER = "YOUR\_MERCHANT\_IDENTIFIER"

let MERCHANT\_SECRET\_KEY = "YOUR\_SECRET\_KEY"

  

![201503261049.jpg](/assets/images/201503261049.jpg)  
Now add the following IBAction method to ChangeViewController.swift and connect the IBAction with the button.

  

  @IBAction func chargeCard(sender: UIButton) {

let amount:NSDecimalNumber \= NSDecimalNumber(string: self.amountTxtField.text)

let transactionProvider:MPTransactionProvider = MPMpos .transactionProviderForMode( MPProviderMode.MOCK, merchantIdentifier: MERCHANT\_IDENTIFIER, merchantSecretKey: MERCHANT\_SECRET\_KEY)

let template: MPTransactionTemplate = transactionProvider.chargeTransactionTemplateWithAmount(amount, currency: MPCurrency.EUR, subject: "subject", customIdentifier: "customIdentifier")

let paymentProcess:MPPaymentProcess = transactionProvider.startPaymentWithTemplate(template, usingAccessory: MPAccessoryFamily.Mock, registered: { (let paymentProcess:MPPaymentProcess!, let transaction:MPTransaction!) -> Void in

}, statusChanged: { (let paymentProcess:MPPaymentProcess!, let transaction:MPTransaction!, let paymentProcessDetails:MPPaymentProcessDetails!) -> Void in

self.messageLabel.text = self.formatMessage(paymentProcessDetails.information)

}, actionRequired: { (let paymentProcess:MPPaymentProcess!, let transaction:MPTransaction!, let transactionAction:MPTransactionAction, let transactionActionSupport:MPTransactionActionSupport!) -> Void in

}) {(let paymentProcess:MPPaymentProcess!, let transaction:MPTransaction!, let paymentProcessDetails:MPPaymentProcessDetails!) -> Void in

self.messageLabel.text = self.formatMessage(paymentProcessDetails.information)

}

}

func formatMessage(information:AnyObject) -> String {

let temp = (information\[0\] as NSString) + "\\n"

return temp + (information\[1\] as NSString)

}

  
Since I don’t have a real reader to try this demo, I have used Mock mode for the transaction provider and payment process  
  let transactionProvider:MPTransactionProvider \= MPMpos .transactionProviderForMode( **MPProviderMode.MOCK**, merchantIdentifier: MERCHANT\_IDENTIFIER, merchantSecretKey: MERCHANT\_SECRET\_KEY)  
  
  let paymentProcess:MPPaymentProcess \= transactionProvider.startPaymentWithTemplate(template, usingAccessory: **MPAccessoryFamily.Mock**, registered:  
  
Now you are good to try this demo by entering an amount and tap the Pay button. The trisection status will be displayed in the message label.  
  
![201503261058.jpg](/assets/images/201503261058.jpg)  
You can also test your solution by entering different amount as mentioned in the [test page](http://www.payworks.mpymnt.com/node/104).  
![201503261101.jpg](/assets/images/201503261101.jpg)  
Download the source code from [github](https://github.com/rshankras/SwiftPayworksDemo)
