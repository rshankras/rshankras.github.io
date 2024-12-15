---
title: "SplitViewController example in Swift"
date: "2015-04-01"
categories: 
  - "ios"
  - "ipad"
  - "iphone-4s"
  - "programming"
  - "xcode"
tags: 
  - "demo"
  - "ipad"
  - "uisplitviewcontroller"
  - "xcode"
---

This is a beginners tutorial on SplitViewController using Interface builder with programming language as Swift. There are also some good articles available on SplitViewController, check them out as well - [nhipster](http://nshipster.com/uisplitviewcontroller/) and [whoisryannystrom](http://whoisryannystrom.com/2014/11/17/UISplitViewController-iOS-7/).

Create a new Single View Application.

![201503290525.jpg](images/201503290525.jpg)

Choose Language option as Swift and provide a product name.

![201504011302.jpg](images/201504011302.jpg)

Navigate to Main.Storyboard and select default View Controller and delete it.

![201504011304.jpg](images/201504011304.jpg)

Add a Split View Controller from the object library to the interface builder.

![201504011305.jpg](images/201504011305.jpg)

Using Attributes Inspector make Split View Controller as the Initial View Controller

![201504011307.jpg](images/201504011307.jpg)  
Select View Controller in the Interface builder then click Editor menu and select Navigation Controller under Embed In menu option.

![201504011308.jpg](images/201504011308.jpg)

Rename ViewController.swift to DetailViewController.swift and change the class name as well.

![201504011317.jpg](images/201504011317.jpg)

Navigate to Interface builder and set the class name for ViewController scene to DetailViewController

![201504011321.jpg](images/201504011321.jpg)

Now Control + drag and drop TablevIew Prototype cell to NavigationController (DetailViewController) and select segue as show detail. Also set the identifier for the Storyboard Segue as “**ShowDetailIdentifier**"

  
![201504011323.jpg](images/201504011323.jpg)

  
![201504011326.jpg](images/201504011326.jpg)

Navigate to RootViewController (TableViewController) Provide the Identifier as CellIdentifier for the Prototype Cells.

![201504011325.jpg](images/201504011325.jpg)

Right click on the Project Navigator, select New File and Choose the template as Cocoa Touch Class

![201504011331.jpg](images/201504011331.jpg)

In the next screen, select subclass as UIViewController and provide a name as SplitViewController

![201504011332.jpg](images/201504011332.jpg)

After creating the file, edit SplitViewController subclass to UISplitViewController. Then add the following line to the viewDidLoad method.

  splitViewController?.preferredDisplayMode \= .PrimaryOverlay

The above line is to keep the PrimaryViewController (TableViewController) on top of SecondaryViewController (DetailViewController). You can change this behaviour by setting other types, check the [documentation](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UISplitViewController_class/) for more details.

![201504011407.jpg](images/201504011407.jpg)

Now add the PrimaryViewController (TableViewController) by right clicking and selecting New File. Select Cocoa Touch class and in the subclass field pick UITableViewController. Provide the the name for the TableViewController ListTableViewController.

![201504011409.jpg](images/201504011409.jpg)

Set the class name for the RootViewController (TableViewController) to the newly created class, ListTableViewController.

![201504011424.jpg](images/201504011424.jpg)

Navigate to DetailViewController in the Interface builder, add a label and make it horizontally and vertically centred.

![201504011524.jpg](images/201504011524.jpg)

Then add a new IBOutlet in DetailViewController and connect the Outlet to the label in interface builder.

  @IBOutlet var numberLabel:UILabel?

  

Also add property of type Int and the value for this property will be set during the segue transition.  

  

var selectedIndex:Int = 1

  

Make changes to the viewDidLoad method, to set the value for the label and to add back button to the navigation bar.  

  

override func viewDidLoad() {

super.viewDidLoad()

numberLabel?.text \= "\\(selectedIndex)"

// add back button to the navigation bar.

if splitViewController?.respondsToSelector("displayModeButtonItem") == true {

navigationItem.leftBarButtonItem \= splitViewController?.displayModeButtonItem()

navigationItem.leftItemsSupplementBackButton \= true

}

}

  

In the ListTableViewController, add the following code that sets the datasource.  

  

  let names = \["One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten”\] (class level declaration)

  

  // MARK: - Table view data source

  

override func numberOfSectionsInTableView(tableView: UITableView) -> Int {

return 1

}

  

override func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {

return names.count

}

  

override func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {

let cell = tableView.dequeueReusableCellWithIdentifier("CellIdentifier", forIndexPath: indexPath) as UITableViewCell

  

   cell.textLabel?.text = names\[indexPath.row\]

  

return cell

}

  

Then make changes to the prepareForSegue method to navigate to DetailViewController after setting the selectedIndex property  
  

  override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {

if (segue.identifier == "ShowDetailIdentifier") {

var detail: DetailViewController

if let navigationController = segue.destinationViewController as? UINavigationController {

detail = navigationController.topViewController as DetailViewController

} else {

detail = segue.destinationViewController as DetailViewController

}

if let path = tableView.indexPathForSelectedRow() {

detail.selectedIndex = path.row + 1

}

}

}

![201504011556.jpg](images/201504011556.jpg)

Download the source from [here](https://github.com/rshankras/UISplitViewControllerExample).
