---
title: "CoreData tutorial in Swift 5 using NSFetchedResultsController"
date: "2019-12-25"
categories: 
  - "develop"
  - "ios"
  - "iphone-4s"
  - "programming"
  - "swift"
  - "xcode"
tags: 
  - "coredata"
  - "delegation"
  - "nsfetchedresultcontoller"
  - "swift"
  - "tutorials"
  - "uitableview"
  - "user-interface"
  - "xcode"
---

Let us see an example TaskManager app using **CoreData written in Swift Programming language**. This app provides the following functionality

- Allow users to enter new task

- Update existing task

- delete task

![TaskManager using CoreData](/assets/images/201407121029.jpg)![201407121030.jpg](/assets/images/201407121030.jpg)

You can download source code for this project from [Github](https://github.com/rshankras/Swift-Demo/tree/master/TaskManager). If you are familiar with user interface then move on to the Core Data implementation in Swift section

Create a new File -> New -> Project and select template Single View Application

![201407121032.jpg](/assets/images/201407121032.jpg)

Enter Product Name, Language as Swift and select "**Use Core Data**" for the new Project.

![201407121037.jpg](/assets/images/201407121037.jpg)

### User Interface Implementation

#### Add new TableViewController for managing tasks

Delete ViewController.swift and Add new view controller which will be used for displaying the list of tasks.

![201407121059.jpg](/assets/images/201407121059.jpg)

Right click on the Project and select New File

![201407121101.jpg](/assets/images/201407121101.jpg)

Choose the template as Cocoa Touch under iOS -> Source

![201407121103.jpg](/assets/images/201407121103.jpg)

Enter name of the file as TaskManagerViewController with Subclass as UITableViewController and **Language as Swift**.

![201407121104.jpg](/assets/images/201407121104.jpg)

#### Add new UITableViewController to the Storyboard

Navigate to Main.storyboard, delete the ViewController and add new TableViewController to the Storyboard

![201407121108.jpg](/assets/images/201407121108.jpg)

Embed this TableViewController inside a navigation controller. You can do this by clicking Editor menu -> Embed In -> Navigation Controller.

![201407121110.jpg](/assets/images/201407121110.jpg)

Navigate to Storyboard file and select Table View Controller. Click Identity Inspector and set the Class to the TaskManagerViewController.

#### Add button to the navigation bar

Users can navigate to new task screen by tapping the button on the TaskManager. Drag and drop the button bar item to the navigation bar.

![201407121116.jpg](/assets/images/201407121116.jpg)

In the attributes inspector, set the identifier for button bar item as Add. Also enter title as “Task Manager” in the navigation bar.

####   
**Add View Controller for entering task detail**

Now to enter task detail, let us add new View Controller. From the Objects library, drag and drop View Controller on to storyboard. Then drag and drop a navigation item to this View Controller. Add a Done bar button item for saving the changes, Cancel bar button item for dismissing the screen. Also provide a title for the screen as Task Detail.

![201407121138.jpg](/assets/images/201407121138.jpg)

Then add a textfield to the View Controller to enter details about the task.

![201407121540.jpg](/assets/images/201407121540.jpg)

Now to connect the Task Manager screen to Task Detail screen, select the Add button in Task Manager screen, hold the control button and make a connection to the Task Detail screen. Select type of **Action Segue as Show**.  

![201407121125.jpg](/assets/images/201407121125.jpg)![201407121127.jpg](/assets/images/201407121127.jpg)

Select each View Controller and Click on the **Resolve Auto Layout** Issues option and pick **Reset to Suggested Constraints**. This would ensure that the controls alignment and display remains same in different screen sizes.

![201407121557.jpg](/assets/images/201407121557.jpg)

#### Add View Controller Class

Right click on the Project, select New File from menu list.

![201407130919.jpg](/assets/images/201407130919.jpg)

Select Cocoa Touch Class as template.

![201407130920.jpg](/assets/images/201407130920.jpg)

Enter the Class name as TaskDetailViewController, Subclass of UIViewController and Language as Swift.

![201407130921.jpg](/assets/images/201407130921.jpg)

Navigate to Storyboard file and select Task Detail View Controller. Click Identity Inspector and set the Class to the TaskDetailViiewController.

![201407141329.jpg](/assets/images/201407141329.jpg)

Now let us add the function required for dismissing the View Controller. This gets called when user taps done and cancel buttons. Navigate to TaskDetailViewController.swift file and add the following functions.

```
    
   @IBAction func done(sender: AnyObject) {
        if task != nil {
            editTask()
        } else {
            createTask()
        }
        dismissViewController()
    }
    
    @IBAction func cancel(sender: AnyObject) {
         dismissViewController()
    }
    
    // MARK:- Dismiss ViewControllers
    
    func dismissViewController() {
        navigationController?.popViewController(animated: true)
    }

```

Connect the IBActions with the corresponding done and cancel buttons

![201407130930.jpg](/assets/images/201407130930.jpg)

Try to compile and run the app on the Simulator. You should see the following Task Manager screen and tapping + sign should display the Task Detail screen with TextField, Cancel and Done button.

![201407130933.jpg](/assets/images/201407130933.jpg)![201407130935.jpg](/assets/images/201407130935.jpg)

When you tap the Cancel or Done button should take you to the Task Manager screen.

#### **Create IBOutlet element for UITextField Element**

Add the following piece of code after the Class TaskDetailViewController: UIViewController  

```
@IBOutlet var txtDesc: UITextField!
```

Now use the connection inspector to connect the IBOutlet variable to the textfield on the User Interface.

### **Core Data Implementation**

Click Show Project Navigator and select CoreData model file (ending with extension .xcdatamodelid)

![201407121042.jpg](/assets/images/201407121042.jpg)

Click Add Entity option available at the bottom of Xcode Editor window.

![201407121045.jpg](/assets/images/201407121045.jpg)

Then enter the name of the entity as Tasks.

![201407121047.jpg](/assets/images/201407121047.jpg)

Click Add Attribute then enter name as desc and choose the type as String. This attribute will be used for storing the task detail information.

![201407121049.jpg](/assets/images/201407121049.jpg)

Now to generate the CoreData mapping class, click Editor and select **Create NSManagedObject Subclass**.

![201407121051.jpg](/assets/images/201407121051.jpg)

Select the data models and click Next

![201407121052.jpg](/assets/images/201407121052.jpg)

Then select entities and in this example it is Tasks

![201407121053.jpg](/assets/images/201407121053.jpg)

Make sure to select **Language for NSManagedObject class as Swift**. Click Create to the create new class.

![201407121055.jpg](/assets/images/201407121055.jpg)

Click Yes to to configure an Objective-C birding header for the Swift class.

![201407121056.jpg](/assets/images/201407121056.jpg)

This should create a new class called Tasks.swfit with variable for corresponding attribute defined in Entities

### Write code to save new task details

Add the following line at the top of TaskDetailViewController class  

```
  let managedObjectContext = (UIApplication.shared.delegate as! AppDelegate).managedObjectContext
```

The above line defines a variable to store the ManagedObjectContext. In order to save the task information entered in the UITextField, add the following code to TaskDetailViewController.swift. Then call this function in the @IBAction done.  

```
   func createTask() {
        let entityDescripition = NSEntityDescription.entity(forEntityName: "Tasks", in: managedObjectContext)
        let task = Tasks(entity: entityDescripition!, insertInto: managedObjectContext)
        task.desc = txtDesc.text!
        do {
            try managedObjectContext.save()
        } catch _ {
        }
    }

```

```
@IBAction func done(sender: AnyObject) {
	createTask()
	dismissViewController()
}

```

The createTask function uses the Tasks Entity class and ManagedObjectContext class to save the information entered in the text field in to SQLite using CoreData.

Now if you try to run this app in Xcode simulator, you should be able to enter the details in textfield and save the task. But there is no way to see the saved tasks.

### Write code to retrieve information from SQLite using NSFetchedResultsController

We will be using [NSFetchedResultsController](https://developer.apple.com/library/prerelease/ios/documentation/CoreData/Reference/NSFetchedResultsController_Class/index.html#//apple_ref/occ/instm/NSFetchedResultsController/objectAtIndexPath:) to retrieve and manage information returned from Core Data. Write the following code after the class declaration of TaskManagerViewController class  

```
 let managedObjectContext = (UIApplication.shared.delegate as! AppDelegate).managedObjectContext
    
var fetchedResultController: NSFetchedResultsController = NSFetchedResultsController<NSFetchRequestResult>()
    
```

![201407141923.jpg](/assets/images/201407141923.jpg)

You might see the above error message “Use of undeclared type ’NSFetchedResultsContoller”. This can be fixed by importing CoreData module and making your class a delegate of NSFetchedResultsControllerDelegate.  

```
import CoreData

class TaskManagerViewController: UITableViewController, NSFetchedResultsControllerDelegate {
```

Then add the following function to populate fetchedResultController.

```
  
    func getFetchedResultController() -> NSFetchedResultsController<NSFetchRequestResult> {
        fetchedResultController = NSFetchedResultsController(fetchRequest: taskFetchRequest(),  managedObjectContext: managedObjectContext, sectionNameKeyPath: nil, cacheName: nil)
        return fetchedResultController
    }
      

```

Update the ViewDidLoad method of TableViewController to populate fetchedResultController variable and set the delegate to self and call the function to retrieve the results.  

```
override func viewDidLoad() {
        super.viewDidLoad()

       fetchedResultController = getFetchedResultController()
        fetchedResultController.delegate = self
        do {
            try fetchedResultController.performFetch()
        } catch _ {
        }
    }

```

### Implement the TableView related functions to display the data

Navigate to Main.storyoard then to TaskManagerViewController and set Identifier for Prototype Cells as “Cell"

![201407142004.jpg](/assets/images/201407142004.jpg)

Add the following functions required for population of rows in tableView and to refresh the tableView when content is changed.

And for refreshing the tableview content add the following piece of code snippet.

```
  func controllerDidChangeContent(_ controller: NSFetchedResultsController<NSFetchRequestResult>) {          tableView.reloadData()
    }

```

Swift uses namespaces for classes, so the downcast of NSManagedObject class to Tasks class will work only when you append the module name with the class for Entity

```
  let task = fetchedResultController.object(at: indexPath as IndexPath) as! Tasks
```

Navigate to TaskManager.xcdatamodeld, select Tasks under Entities and using the Data Model Inspector append Module name i.e TaskManager with the class.

`![201407142038.jpg](/assets/images/201407142038.jpg)`

Now you should be able to see the data added via TaskDetailScreen in the TaskManager Screen.

![201407142059.jpg](/assets/images/201407142059.jpg)

###   
**Implementation of deleting rows from tableView and CoreData entity**  

Copy and paste the following code to provide the users with the option to delete the rows.

```
 override func tableView(_ tableView: UITableView, commit editingStyle: UITableViewCell.EditingStyle, forRowAt indexPath: IndexPath) {
        let managedObject:NSManagedObject = fetchedResultController.object(at: indexPath as IndexPath) as! NSManagedObject
        managedObjectContext.delete(managedObject)
        do {
            try managedObjectContext.save()
        } catch _ {
        }
    }
```

![201407142116.jpg](/assets/images/201407142116.jpg)

###   
**Implementation of editing task details**

Now let us see how to edit a task in the TaskManager screen. We will re-use the same TaskDetail screen for editing the task information. First let create segue from UITableViewCell to TaskDetailViewController. You can do this by holding the Control key and drag and drop the connection to TaskDetailViewController.

![201407142127.jpg](/assets/images/201407142127.jpg)

Make sure to set the Segue identifier as edit using Attributes Inspector

![201407142128.jpg](/assets/images/201407142128.jpg)

Add the following piece of code in TaskManagerViewController to populate the task detail for the edited row.  

```
      override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if segue.identifier == "edit" {
            let cell = sender as! UITableViewCell
            let indexPath = tableView.indexPath(for: cell)
            let taskController:TaskDetailViewController = segue.destination as! TaskDetailViewController
            let task:Tasks = fetchedResultController.object(at: indexPath!) as! Tasks
            taskController.task = task
        }
    }
    

```

Navigate to TaskDetailViewController and variable which used to pass the task details across the ViewControllers  

```
var task: Task? = nil
```

In viewDidLoad fund, populate the textField with the task details for edit operation i.e task is not nil

```
 override func viewDidLoad() {
        super.viewDidLoad()
     if task != nil {
            txtDesc.text = task?.desc
        }
    }
```

Then add a new function to save the edited task. Also modify the done function to handle create and edit task functionality

```
func editTask() {
       task?.desc = txtDesc.text!
        do {
            try managedObjectContext.save()
        } catch _ {
        }
    }

```

```
@IBAction func done(sender: AnyObject) {
        if task != nil {
            editTask()
        } else {
            createTask()
        }
        dismissViewController()
    }

```

Now when you run the app in Xcode simulator, you should be able to edit the task.

  
The final piece of code left is to add background colour to the navigation bar for both the controllers. Click AppDelegate.swift file and add the following function. Then call this function from the didFinishLaunchingWithOptions.

```
    func setupAppearance() {
        let navigationBarAppearance = UINavigationBar.appearance()
        navigationBarAppearance.barTintColor = UIColor(red: 51.0/255.0, green: 104.0/255.0, blue: 121.0/255.0, alpha: 1.0)
        navigationBarAppearance.tintColor = UIColor.white
        navigationBarAppearance.titleTextAttributes = [NSAttributedString.Key.foregroundColor:UIColor.white]
    }


```

Running the app on the iOS simulator should change the appearance for the navigation bar.

![201407142233.jpg](/assets/images/201407142233.jpg)

Hope you found this beginner tutorial useful. Please use the comments section to share your thoughts and suggestion

Download the source code for this tutorial from [GitHub](https://github.com/rshankras/Swift-Demo/tree/master/TaskManager)
