---
title: "NSUnknownKeyException - this class is not key value coding-compliant for the key"
date: "2019-11-06"
categories: 
  - "iboutlet"
  - "ios"
  - "nsuknownkeyexception"
---

NSUnknownKeyException - this class is not key value coding-compliant for the key common error that most of the Swift beginners would face during the learning period.  

> Terminating app due to uncaught exception 'NSUnknownKeyException', reason: '\[<Handbook.StudentEntryController 0x78f948a0> setValue:forUndefinedKey:\]: this class is not key value coding-compliant for the key nametxt.'  
> \*\*\* First throw call stack:  
> (  
> 0 CoreFoundation 0x02316a14 \_\_exceptionPreprocess + 180  
> 1 libobjc.A.dylib 0x01751e02 objc\_exception\_throw + 50  
> 2 CoreFoundation 0x02316631 -\[NSException raise\] + 17  
> 3 Foundation 0x013e71bc -\[NSObject(NSKeyValueCoding) setValue:forUndefinedKey:\] + 282  
> 4 Foundation 0x0134183a \_NSSetUsingKeyValueSetter + 115  
> 5 Foundation 0x013417bf -\[NSObject(NSKeyValueCoding) setValue:forKey:\] + 295  
> 6 UIKit 0x02cac06d -\[UIViewController setValue:forKey:\] + 85  
> 7 Foundation 0x0137601d -\[NSObject(NSKeyValueCoding) setValue:forKeyPath:\] + 384  
> 8 UIKit 0x02f1fcb4 -\[UIRuntimeOutletConnection connect\] + 132  
> 9 libobjc.A.dylib 0x0176600c -\[NSObject performSelector:\] + 62  
> 10 CoreFoundation 0x02246f51 -\[NSArray makeObjectsPerformSelector:\] + 273  
> 11 UIKit 0x02f1e34e -\[UINib instantiateWithOwner:options:\] + 2102  
> 12 UIKit 0x02cb3abc -\[UIViewController \_loadViewFromNibNamed:bundle:\] + 429  
> 13 UIKit 0x02cb44f4 -\[UIViewController loadView\] + 189  
> 14 UIKit 0x02f47b66 -\[UITableViewController loadView\] + 88  
> 15 UIKit 0x02cb4900 -\[UIViewController loadViewIfRequired\] + 154  
> 16 UIKit 0x02cbb406 -\[UIViewController \_\_viewWillAppear:\] + 114  
> 17 UIKit 0x02cde5b9 -\[UIViewController(UIContainerViewControllerProtectedMethods) beginAppearanceTransition:animated:\] + 202  
> 18 UIKit 0x02cf09cc -\[UINavigationController \_startCustomTransition:\] + 1389  
> 19 UIKit 0x02d02769 -\[UINavigationController \_startDeferredTransitionIfNeeded:\] + 803  
> 20 UIKit 0x02d03ada -\[UINavigationController \_\_viewWillLayoutSubviews\] + 68  
> 21 UIKit 0x02edfc4a -\[UILayoutContainerView layoutSubviews\] + 252  
> 22 UIKit 0x02bb5008 -\[UIView(CALayerDelegate) layoutSublayersOfLayer:\] + 810  
> 23 libobjc.A.dylib 0x01766059 -\[NSObject performSelector:withObject:\] + 70  
> 24 QuartzCore 0x029b480a -\[CALayer layoutSublayers\] + 144  
> 25 QuartzCore 0x029a84ee \_ZN2CA5Layer16layout\_if\_neededEPNS\_11TransactionE + 388  
> 26 QuartzCore 0x029a8352 \_ZN2CA5Layer28layout\_and\_display\_if\_neededEPNS\_11TransactionE + 26  
> 27 QuartzCore 0x0299ae8b \_ZN2CA7Context18commit\_transactionEPNS\_11TransactionE + 317  
> 28 QuartzCore 0x029cee03 \_ZN2CA11Transaction6commitEv + 561  
> 29 QuartzCore 0x029d0674 \_ZN2CA11Transaction17flush\_transactionEv + 50  
> 30 UIKit 0x02ae28bc \_UIApplicationHandleEventQueue + 8398  
> 31 CoreFoundation 0x022306ff \_\_CFRUNLOOP\_IS\_CALLING\_OUT\_TO\_A\_SOURCE0\_PERFORM\_FUNCTION\_\_ + 15  
> 32 CoreFoundation 0x0222638b \_\_CFRunLoopDoSources0 + 523  
> 33 CoreFoundation 0x022257a8 \_\_CFRunLoopRun + 1032  
> 34 CoreFoundation 0x022250e6 CFRunLoopRunSpecific + 470  
> 35 CoreFoundation 0x02224efb CFRunLoopRunInMode + 123  
> 36 GraphicsServices 0x05cf5664 GSEventRunModal + 192  
> 37 GraphicsServices 0x05cf54a1 GSEventRun + 104  
> 38 UIKit 0x02ae8bfa UIApplicationMain + 160  
> 39 Handbook 0x0007513d main + 93  
> 40 libdyld.dylib 0x04b11a21 start + 1  
> 41 ??? 0x00000001 0x0 + 1  
> )  
> libc++abi.dylib: terminating with uncaught exception of type NSException

This issue occurs when a storyboard refers to a deleted or renamed IBOutlet. If you navigate to the connection instepctor of the ViewController, you shoud notice an exclaimation mark as shown below.  

![](/assets/images/UnKnownKey.png)

Remove the IBOutlet mapping by clicking on X mark and remove the orphaned IBOutlet.
