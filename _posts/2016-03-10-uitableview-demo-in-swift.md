---
title: "UITableView Demo in Swift"
date: "2016-03-10"
categories: 
  - "ios"
  - "swift"
---

In this tutorial, we will see some of the common UITableView operations such as **Adding**, **Updating**, **Deleting** and **Moving** records using Swift.

Let us start with a TableView placed over a ViewController instead of using UITableViewController. By this way you will learn lot more about the functionality of UITableView. Add a new file and select Cocoa Touch Class as a template for the new file.

![](/assets/images/1433848175_thumb.png)

In “Choose options for your new file” screen, enter the class name as TableViewDemoController with subclass as UIViewController. Then save the new file under your preferred location.

![](/assets/images/1433848643_thumb.png)

### User Interface

Navigate to Main.stotyboard then drag and drop a ViewController from Object Libray to Storyboard. Select the ViewController and click Show Identity Inspection and enter the class name as “TableViewDemoController"

![](/assets/images/1433848794_thumb.png)

Drag and drop Table View from object library to the View Controlller and make sure Table View is aligned properly. Now place a Table View Cell from object library on top of the TableView.

![](/assets/images/1433849140_thumb.png)

Set the identifier for Prototype cell to “CellIdentifier” using Show Identity Inspector.

![](/assets/images/1433849502_thumb.png)

Now select the tableview in the Document Outline pane and click Connection Inspector under Utilies pane. Connect the dataSource and delegate Outlets to the TableViewDemoController (yellow color circle on top View Controller)

![](/assets/images/1433849850_thumb.png)

### Display Data

In this demo, we will be seeing how to display list of Socia Media icons. Here are the steps to load those icons in TableView.

First create a Struct that would act as a place holder for holding the name and image file name. Right click on the Project, select New File. In template screen, choose Swift file and provide name as SocialMedia and save the file.

![](/assets/images/1433852507_thumb.png)

Edit SocialMedia.swift and add the following code snippet. Apart name and imageName property, this also has computed property that returms UIImage based upon the image file name.

```
import UIKit

struct SocialMedia {

    var name:String
    var imageName:String
    var image: UIImage {
        get {
            return UIImage(named: imageName)!
        }
    }

}
```

Now Drag and drop social icon images from folder to Xcode project (download images from gitHub repoistory). Navigate TableViewDemoController.swift and add the following code snippet.

```
var data:[SocialMedia] = [SocialMedia]()

//MARK:- Populate data   

    func loadData() -&amp;gt; [SocialMedia] {

        data.append(SocialMedia(name:"Evernote",imageName:"evernote"))
        data.append(SocialMedia(name:"Facebook",imageName:"facebook"))
        data.append(SocialMedia(name:"GitHub",imageName:"github"))
        data.append(SocialMedia(name:"Google",imageName:"google"))
        data.append(SocialMedia(name:"LinkedIn",imageName:"linkedin"))
        data.append(SocialMedia(name:"Paypal",imageName:"paypal"))
        data.append(SocialMedia(name:"Pinterest",imageName:"pinterest"))
        data.append(SocialMedia(name:"Twitter",imageName:"twitter"))
        data.append(SocialMedia(name:"Vimeo",imageName:"vimeo"))
        data.append(SocialMedia(name:"YouTube",imageName:"youtube"))

        return data
    }
```

We have declared an array called data which will hold all the SocialMedia icon related information. The function loadData is used for adding all the social media images. Now call this function in the viewDidLoad method.

```
override func viewDidLoad() {
	super.viewDidLoad()
	 // call loaddata
	 loadData()
 }
```

In order display data, ViewController needs to conform UITableViewDataSource protocol. Add UITableViewDataSource to the class declaration next to UIViewController.

```
class TableViewDemoController: UIViewController, UITableViewDataSource {
```

Then implement the following methods in TableViewDemoController class, these required methods when a class conforms to UITableViewDataSource protocol.

```
extension TableViewDemoController: UITableViewDataSource {

    // MARK:- TabvleView dataSource methods

    func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -&amp;gt; Int {
        return data.count
    }

    func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -&amp;gt; UITableViewCell {

        let cell = tableView.dequeueReusableCellWithIdentifier(IDENTIFIER,
            forIndexPath: indexPath)

        let socialMedia = data[indexPath.row]

        cell.textLabel?.text = socialMedia.name

        cell.imageView?.image = socialMedia.image

        return cell
    }
}
```

Finally we need to create IBOutlet for tableView and connect with tableView control in Storyboard.

```
@IBOutlet var tableView: UITableView!
```

![](/assets/images/1433855020_thumb1.png)

Now you should be able to build and run the project. This should show list all Social Media icons as shown below

![](/assets/images/1433855991_thumb1.png)

### Customize UITableView

In order the customize the tableview, the TableViewDemoController class needs to conform to UITableViewDelegate protocol. Let us say you want to increase the height of tableview rows. Then implement the function heightForRowAtIndexPath to return the height for each row.

```
func tableView(tableView: UITableView, heightForRowAtIndexPath indexPath: NSIndexPath) -&amp;gt; CGFloat {
	return 60.0
}
```

Build and run the project should show the difference in height.

### Add and Update row

Navigate to Main.storyboard and add a new View Controller to Interface builder. This View Controller will be used for capturing name of the icon when adding a new row.

![](/assets/images/1433909247_thumb.png)

This View Controller has a text field to accept the name of the Social Media icon, Done button to save the entered informatiom and Cancel button to cancel the operation. Make sure to create Unwind segue for Done and Cancel button by Control drag and drop each button to Exit icon on the View Controller. Also provide the identifer for the Unwind segue as addAction and cancelAction.

![](/assets/images/1433909748_thumb.png)

Navigate to TableViewDemoController and add Bar Button Item to the left hand side. Set the Identifier of Bar Button Item to Add.

![](/assets/images/1433910221_thumb.png)

Now Control + Drag from the Add button to DetailViewController and select Segue as Push with identifier as “addAction". Similarly to allow users to edit the existing row, Control + Drag TableView prototype cell to DetailViewController and set identifier for the Push segue as “editAction”.

Add a new Cocoa Touch Class file to the existing project with Sub class as UIViewController and name of the file as DetailViewController. Set this file as the class name in the Identity Inspector of DetailViewController in Interface builder.

Update the DetailViewController.swift and replace the existing code with the following lines of code.

```
import UIKit

class DetailViewController: UIViewController {

    var socialMedia: SocialMedia?

    @IBOutlet var textFeild:UITextField?

    override func viewDidLoad() {
        super.viewDidLoad()

        if let name = socialMedia?.name {
            textFeild?.text = name
        }
    }

    // MARK:- PrepareForSegue

    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {

        let name = textFeild?.text
        if var _ = socialMedia {
            self.socialMedia?.name = name!
        } else {
            socialMedia = SocialMedia(name:name!,imageName:"unknown")
        }
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

}
```

We have declared two variables socialMedia and index which will be populated when user taps an esitsing row in the TableView. Also you should find a IBOutlet for UITextField, make sure to connect this with TextField in the Interface Builder.

In the viewDidLoad function, if the user is editing an existing row then the textfield is updated with that value. The prepareForSegue method is called when the user taps Done or Cancel button. And based on the action, a new social media icon is added or an existing row is updated.

Navigate back to TableViewDemoController and implement the following function that will be called on cancel or done operation in DetailViewController.

```
//MARK:- Cancel and Done

    @IBAction func cancel(segue:UIStoryboardSegue) {
        // do nothing
    }

    @IBAction func done(segue:UIStoryboardSegue) {

        let detailViewController = segue.sourceViewController as!
        DetailViewController

        let socialMedia = detailViewController.socialMedia

        if let selectedIndex = index {
            data[selectedIndex] = socialMedia!
        } else {
            data.append(socialMedia!)
        }
        tableView.reloadData()
    }
```

### Delete and Move row

Delete operation can be added by implementing the following function in TableViewDemoController.

```
func tableView(tableView: UITableView, commitEditingStyle editingStyle: UITableViewCellEditingStyle, forRowAtIndexPath indexPath: NSIndexPath) {
	  switch editingStyle {
		case .Delete:
		// remove the deleted item from the model
	 	data.removeAtIndex(indexPath.row)
 		// remove the deleted item from the `UITableView`
		self.tableView.deleteRowsAtIndexPaths([indexPath], withRowAnimation: .Fade)
	   	default:
		 return
   	}
}
```

This would allow users to swipe and delete a row in TableView. The function checks whether the editing style is Delete, then the row is removed from the array as well from the TableView display.

In order to allow users to move the rows, the tableView editing property needs to be set to true. Add another Bar Button Item, this time to the right of TableViewDemoController and provide the caption as Edit. Then connect this button with the following IBAction function.

```
//MARK:- Editing toggle
```

This button acts as a toggle switch to enable or disable tableview edit operation. Now add the following function required for Move operation.

```
//MARK:- TableViewCell Move row methods
	func tableView(tableView: UITableView, canMoveRowAtIndexPath indexPath: NSIndexPath) -&amp;gt; Bool {
     	return true
    }
```

Function canMoveRowAtIndexPath needs to return true and in moveRowAtIndexPath function, the tableView row data gets removed from the original index and inserted in to the new position.

![](/assets/images/1433915244_thumb.png)

Now the user can tap and hold the move option then drag and drop it to the desired position. When the tableview editing is set to true, it also provides delete button apart from the move operation.

Download the source code from [here](https://github.com/rshankras/TableViewDemo).

Social Media icons credit to [Sebastiano Guerriero](https://dribbble.com/Sebastiano_Guerriero)
