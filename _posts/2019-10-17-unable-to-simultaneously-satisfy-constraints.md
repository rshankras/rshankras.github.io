---
title: "Unable to simultaneously satisfy constraints."
date: "2019-10-17"
categories: 
  - "auto-layout"
  - "constraints"
  - "nslayoutconstraint"
---

A common error that we would see when using Auto Layout is

> Unable to simultaneously satisfy constraints. Probably at least one of the constraints in the following list is one you don't want.

Debugging the verbose shown in the console might look difficult but if you closely go through the messages you should be able to identify the issue.  

Let us take the following Auto Layout Constraint error messages.

> Try this:  
> (1) look at each constraint and try to figure out which you don't expect;  
> (2) find the code that added the unwanted constraint or constraints and fix it.  
> (  
> "<NSLayoutConstraint:0x281862940 UIImageView:0x14ddb28e0.width == UIImageView:0x14ddb28e0.height (active)>",  
> "<NSLayoutConstraint:0x28181c190 V:|-(5)-\[UIImageView:0x14ddb28e0\] (active, names: '|':UITableViewCellContentView:0x14ddb2750 )>",  
> "<NSLayoutConstraint:0x28181cc30 UIImageView:0x14ddb28e0.width == 0.22\*UITableViewCellContentView:0x14ddb2750.width (active)>",  
> "<NSLayoutConstraint:0x28181eb20 V:\[UIImageView:0x14ddb28e0\]-(5)-| (active, names: '|':UITableViewCellContentView:0x14ddb2750 )>",  
> "<NSLayoutConstraint:0x28186e080 'UIView-Encapsulated-Layout-Height' UITableViewCellContentView:0x14ddb2750.height == 93 (active)>",  
> "<NSLayoutConstraint:0x28186e030 'UIView-Encapsulated-Layout-Width' UITableViewCellContentView:0x14ddb2750.width == 375 (active)>"  
> )  
> 
> Will attempt to recover by breaking constraint  
> <NSLayoutConstraint:0x281862940 UIImageView:0x14ddb28e0.width == UIImageView:0x14ddb28e0.height (active)>

The constraints associated with this UIImageView are

![](/assets/images/Constraint1.png)

This error is result of more than one constraints staistying the same condition. The last line in the log message tells one of the constraint causes this issues. "width == height”. Now identify the second constraint which tries to set the width of this imageview.  

There are two constraints trying to set the width for the image view, 1. Propotional Width to and 2. Aspect Ratio. After removing the unwanted constraint and you are good to go.  

Let us see one more example for the Constraint errors.

> (  
> "<NSLayoutConstraint:0x281818f00 UIButton:0x14ddb7fe0'BOOK'.height == 50 (active)>",  
> "<NSLayoutConstraint:0x28186c050 V:|-(20)-\[UIButton:0x14ddb7fe0'BOOK'\] (active, names: '|':UITableViewCellContentView:0x14ddb7e50 )>",  
> "<NSLayoutConstraint:0x28186c0a0 V:\[UIButton:0x14ddb7fe0'BOOK'\]-(20)-| (active, names: '|':UITableViewCellContentView:0x14ddb7e50 )>",  
> "<NSLayoutConstraint:0x28181aad0 'UIView-Encapsulated-Layout-Height' UITableViewCellContentView:0x14ddb7e50.height == 90.5 (active)>"  
> )  
> 
> Will attempt to recover by breaking constraint  
> <NSLayoutConstraint:0x281818f00 UIButton:0x14ddb7fe0'BOOK'.height == 50 (active)>

![](/assets/images/Constraint2.png)

  
The last line gives a clue, there are two constraints trying to set the height of the BOOK button. And if you look at the constraints for the BOOK button, you can find 1. Top and Bottom constraints are set for button and 2. Height constraint is also set for Button. Removing any one of the constraint would fix the problem.
