---
title: "Swift Demo - Add Progress Bar"
date: "2015-06-24"
categories: 
  - "ios"
  - "xcode"
tags: 
  - "gestures"
  - "uiprogressview"
---

In this short tutorial, we will see the steps required to **add UIProgressView** to a Swift IOS Project.

[![](/assets/images/1435151362_thumb.png)](https://rshankar.com/wp-content/uploads/2015/06/1435151362_full.png)

UIProgressView and UILabel showing the current progress will be added programmatically to the View Controller. Create a Single View Application and navigate to ViewController.swift file.

### Add UIProgressView and UILabel

Add the following code snippet below the class definition. This code snippet adds variables for UILabel and UIProgressView.  

```swift
var progressView: UIProgressView?
var progressLabel: UILabel?
```

Now add the following function which initialises and adds UIProgressView and UILabel to the view.  

```swift
//MARK:- Controls
func addControls() {
    // Create Progress View Control
    progressView = UIProgressView(progressViewStyle: UIProgressViewStyle.Default)
    progressView?.center = self.view.center
    view.addSubview(progressView!)

    // Add Label
    progressLabel = UILabel()
    let frame = CGRectMake(view.center.x - 25, view.center.y - 100, 100, 50)
    progressLabel?.frame = frame
    view.addSubview(progressLabel!)
}
```

ProgressView style can be set to Default or Bar type. And UILabel needs to be appear just above the ProgressView hence we added an offset from view center.

### Add GestureRecogonizers

This demo starts and resets the progress on single and double tap gesture event. The following code snippet adds single and double tap gesture recognisers to the view. This also specifies the function that needs to be called when user does a single or double tap.

```swift
func addGestures() {
    // Add Single Tap and Doube Tap Gestures
    let tap = UITapGestureRecognizer(target: self, action: "handleTap:")
    tap.numberOfTapsRequired = 1

    let doubleTap = UITapGestureRecognizer(target: self, action: "handleDoubleTap:")
    doubleTap.numberOfTapsRequired = 2

    view.addGestureRecognizer(tap)
    view.addGestureRecognizer(doubleTap)
    tap.requireGestureRecognizerToFail(doubleTap)
}
```

Now add the required functions for the gesture recogonizer events.  

```swift
// Start Progress View
func handleTap(sender: UITapGestureRecognizer) {
    if sender.state == .Ended {
        timer = NSTimer.scheduledTimerWithTimeInterval(1.0, target: self, selector: "updateProgress", userInfo: nil, repeats: true)
    }
}

//MARK:- Double Tap
// Reset Progress View
func handleDoubleTap(sender: UITapGestureRecognizer) {
    if sender.state == .Ended {
        progressView?.progress = 0.0
        progressLabel?.text = "0 %"
        timer?.invalidate()
    }
}
```

### Display Progress

The actual progress will be displayed by the following piece of code in the updateProgress function. You can change progress interval by setting appropriate value to progress property of UIProgressView.  

```swift
//MARK:- Increment Progress
func updateProgress() {
    progressView?.progress += 0.05
    let progressValue = self.progressView?.progress
    progressLabel?.text = "\(progressValue! * 100) %"
}
```

Finally we need to add the `addControls` and `addGestures` to the viewDidLoad method.

```swift
override func viewDidLoad() {
    super.viewDidLoad()
    addControls()
    addGestures()
}
```

Download source code from [here](https://github.com/rshankras/SwiftDemo) (SwiftDemo - ProgressView)
