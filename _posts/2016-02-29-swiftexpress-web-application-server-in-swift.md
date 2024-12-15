---
title: "SwiftExpress - Web Application Server in Swift"
date: "2016-02-29"
categories: 
  - "ios"
  - "swift"
  - "swift-2"
tags: 
  - "swiftexpress"
  - "web-service"
---

[Swift Express](http://swiftexpress.io/) is a simple yet powerful web application written in Apple’s Swift language. This is an initiative started by [Crossload Labs](http://www.crossroadlabs.xyz/) using Play Framework and Express.js

### Installation

SwiftExpress [GitHub](https://github.com/crossroadlabs/Express) provides a well documented steps for installing the server on Mac OS X and Linux. I tried this on Mac OS X and the whole setup was completed in less 10 minutes and was able quickly run the demo API request.

### Features

Feature supported by Swift Express (Note :- re-published from SwiftExpress [GitHub](https://github.com/crossroadlabs/Express#installation) repository)

- ? Linux support with and without [Dispatch](https://swift.org/core-libraries/#libdispatch)
- 100% asynchronous (Future-based API)
- Flexible and extensible
- Full [Model-View-Controller](https://ru.wikipedia.org/wiki/Model-View-Controller) support
- Swift 2.1 and 2.2 compatible
- [Simple routing mechanism](https://github.com/crossroadlabs/Express/blob/master/doc/gettingstarted/routing.md)
- Request handlers chaining
- [Typesafe Error Handlers](https://github.com/crossroadlabs/Express/blob/master/doc/gettingstarted/errorhandling.md)
- Templeates: [Stencil](https://github.com/kylef/Stencil) and [Mustache](https://mustache.github.io/)
- Built-in [JSON](http://www.json.org/) support
- Easy creation of [RESTful](https://en.wikipedia.org/wiki/Representational_state_transfer) APIs
- Built-in [static files serving](https://github.com/crossroadlabs/Express/blob/master/doc/gettingstarted/static.md)
- Multiple contents types built-in support

### A Quick Demo

Let us see a quick demo of JSON API Service deployed on SwiftExpress and consumed by iOS App written Swift.

##### Project Creation

Make sure to [install](https://github.com/crossroadlabs/Express#installation) the required libraries before creating the project. Launch terminal window and type the following  

```plain
swift-express init APIDemo 
```

The project creation should kick start the following set of dependancies updates.  

```plain
*** No Cartfile.resolved found, updating dependencies ***
Fetching Express
*** Fetching Stencil ***
Fetching CEVHTP
*** Fetching PathToRegex ***
Fetching Regex
*** Fetching GRMustache.swift ***
Fetching TidyJSON
*** Fetching BrightFutures ***
Fetching PathKit
*** Fetching ExecutionContext ***
Fetching Result
*** Checking out CEVHTP at "0.1.0" ***
*** Checking out GRMustache.swift at "bf7d6031d7e0dd862519eaba2b36b2e11a0d25a9" ***
*** Checking out Result at "1.0.3" ***
*** Checking out ExecutionContext at "0.3.1" ***
*** Downloading Regex.framework binary at "v0.5.2: Linux support final" ***
*** Downloading Express.framework binary at "v0.3.1: OS X binary build" ***
*** Checking out PathKit at "0.6.1" ***
*** Downloading TidyJSON.framework binary at "v1.1.0: faster parser" ***
*** Downloading PathToRegex.framework binary at "v0.2.0: linux support" ***
*** Checking out Stencil at "0.5.3" ***
*** Checking out BrightFutures at "0.4.0" ***
*** xcodebuild output can be found in /var/folders/gs/586wmrks50b9xdpq1309qn9m0000gn/T/carthage-xcodebuild.hzo8CL.log ***
*** Building scheme "MustacheOSX" in Mustache.xcworkspace ***
*** Building scheme "PathKit" in PathKit.xcworkspace ***
*** Building scheme "Result-Mac" in Result.xcodeproj ***
*** Building scheme "ExecutionContext-OSX" in ExecutionContext.xcodeproj ***
*** Building scheme "BrightFutures-Mac" in BrightFutures.xcworkspace ***
*** Building scheme "Stencil" in Stencil.xcodeproj ***
ld: warning: linking against dylib not safe for use in application extensions: /Users/ravishankar/Downloads/Demo/APIDemo/Carthage/Checkouts/BrightFutures/Carthage/Build/Mac/ExecutionContext.framework/ExecutionContext
Task: "init" done.
```

Navigate to APIDemo project folder and launch APIDemo.xcodeproj  

```plain
cd APIDemo
open APIDemo.xcodeproj
```

You should see the following project structure with main.swift file.  

![](/assets/images/1456760176_thumb.png)

##### Create JSON API Call

Now edit the main.swift file and add `app.views.register(JsonView())`to enable JSON API service. This can be added below the `app.views.register(StencilViewEngine())`

Let us create a JSON Service that returns details about Marathon Runs for 2016. We should register a new API route /marathon/ and the response returned by service has been hard code as shown below. The app.get can be added above the app.listen(9999) method call.  

```swift
app.get("/marathons/") { request in 
    //compose the response as a simple dictionary
    let response = [
        ["name": "Tokyo Marathon", "date": "28/02/2016"],
        ["name": "Dong-A Seoul International Marathon", "date": "20/03/2016"],
        ["name": "Aalborg Brutal Marathon", "date": "25/03/2016"],
        ["name": "Bath Beat Marathon", "date": "02/04/2016"],
        ["name": "Freiburg Marathon", "date": "03/04/2016"],
        ["name": "Canberra Marathon", "date": "10/04/2016"],
        ["name": "NN Rotterdam Marathon", "date": "10/04/2016"],
        ["name": "Vienna City Marathon", "date": "10/04/2016"],
        ["name": "Haspa Marathon Hamburg", "date": "17/04/2016"],
        ["name": "Blackpool Marathon", "date": "24/04/2016"]
    ]
    //render disctionary as json (remember the one we've registered above?)
    return Action.render(JsonView.name, context: response)
}
```

Compiling and run the project in Xcode should show “Express was successfully launched on port 9999” in the console message. Accessing the following url should display the JSON Response as shown below.  

![](/assets/images/1456763045_thumb.png)

Now consuming this JSON service from iOS App using NSURLSession class as shown below.  

```swift
func loadData() {
    let url = NSURL(string:"http://localhost:9999/marathons")

    let request = NSURLRequest(URL: url!)

    let session = NSURLSession.sharedSession().dataTaskWithRequest(request) { (data, response, error) -> Void in

        if let error = error {
            print("Error " + (error.localizedDescription))
            return
        }

        if let data = data {
            do {
                let results = try NSJSONSerialization.JSONObjectWithData(data, options: NSJSONReadingOptions.AllowFragments) as! NSArray
                for item in results {
                    print(item)
                    self.details.append(item as! [String : String])
                }

                dispatch_async(dispatch_get_main_queue(), { () -> Void in
                    self.tableView.reloadData()
                })
            } catch (let error as NSError) {
                print("JSON error" + error.localizedDescription)
            }

        } else {
            print("No response")
            return
        }
    }
    session.resume()
}

```

Since we are running the service using http, make sure to add Allow Arbitrary Loads to “YES” (under App Transport Security Settings) in info.plist file.  

[![](/assets/images/1456765246_thumb.png)](https://rshankar.com/wp-content/uploads/2016/02/1456765246_full.png)

Looking forward to the production release of Swift Express !!!
