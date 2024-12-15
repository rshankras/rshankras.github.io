---
title: "Add annotations and Polyline to MapView in Swift"
date: "2015-07-06"
categories: 
  - "ios"
  - "programming"
  - "swift"
  - "xcode"
---

In this article, we will see the instructions for **adding annotation to MapView, Draw Polylines and Zoom to a region in Swift**. Let us see this by adding stations to a Map for Chennai subrban trains and connect these stations using Map Overlay.

### Project Setup

Create a new project by selecting Single View Application as the project template.  

[![](/assets/images/1436156526_thumb.png)](https://rshankar.com/wp-content/uploads/2015/07/1436156526_full.png)

Enter the required information such project name, organization identifier etc.. as shown in the below screenshot. Then save the project in your desired location.  

[![](/assets/images/1436156682_thumb.png)](https://rshankar.com/wp-content/uploads/2015/07/1436156682_full.png)

### Add MapKit View

Navigate to Project navigator and select Main.storyboard file.  

[![](/assets/images/1436156799_thumb.png)](https://rshankar.com/wp-content/uploads/2015/07/1436156799_full.png)

We are not using the Auto Layout for this demo, hence disable Use Auto Layout and disable size classes using the options available as part of the File Inspector  

[![](/assets/images/1436156949_thumb.png)](https://rshankar.com/wp-content/uploads/2015/07/1436156949_full.png)

Drag and drop MapKit View from object library to the View Controller and make sure to resize the MapView to full view. Add IBOutlet in the ViewController for the MapKit and connect it to the MapKit View in the Interface builder. Also add `import MapKit` to include MapKit framework for your project.  

\[code language="swift"\]@IBOutlet weak var mapView: MKMapView! \[/code\]

Now if you do a build and run the project in iPhone 6 simulator, you should see the following on simulator.  

[![](/assets/images/1436157414_thumb.png)](https://rshankar.com/wp-content/uploads/2015/07/1436157414_full.png)

### Zoom to specified region

Add the follwing piece of code in ViewController.swift file. And call this function from ViewController’s viewDidLoad function.  

\[code language="swift"\]//MARK:- Zoom to region

func zoomToRegion() {

let location = CLLocationCoordinate2D(latitude: 13.03297, longitude: 80.26518)

let region = MKCoordinateRegionMakeWithDistance(location, 5000.0, 7000.0)

mapView.setRegion(region, animated: true) } \[/code\]

CLLocationCoordinate2D is created by specifying latitude and longitude of the zoom location. Then using MKCoordinateRegionMakeWithDistance set the distance around the speicifed location. Then this region will set as the region for the MapView. Build and run the project should show Map zooming to the speicifed region as shown below.  

[![](/assets/images/1436158801_thumb.png)](https://rshankar.com/wp-content/uploads/2015/07/1436158801_full.png)

### Add plist file to project.

All the station details such as title, latitude and longitude are stored in a plist file. You can download the plist from gitHub. Right click on the Project folder (Project navigator) and select “Add Files to <Project name>” option. And select **Copy items if needed** option while adding the file.  

[![](/assets/images/1436159062_thumb.png)](https://rshankar.com/wp-content/uploads/2015/07/1436159062_full.png)

The sample data structure of the plist file is shown below  

[![](/assets/images/1436159206_thumb.png)](https://rshankar.com/wp-content/uploads/2015/07/1436159206_full.png)

### Add place holder class Station

Create a new model class for holding the station data. This class should conform to `MKAnnotation` and `NSObject` protocol.  

\[code language="swift"\]import MapKit

class Station: NSObject, MKAnnotation { var title: String? var subtitle: String? var latitude: Double var longitude:Double

var coordinate: CLLocationCoordinate2D { return CLLocationCoordinate2D(latitude: latitude, longitude: longitude) }

init(latitude: Double, longitude: Double) { self.latitude = latitude self.longitude = longitude } }\[/code\]

This class has properties for title, subtitle, latitude, longitude and coordinate. Any mappoint should have coordinate for the adding it to the map. This property is mandatory and it is defined in MKAnnotation protocol. The initializer in the class accepts the latitide and longitude details as they are needed for creating the coordinates.

### Add annotation to MapKit

We need to iterate through the plist file and create annotation for each stations. Add the following function to ViewController.swift which does the same.

\[code language="swift"\]//MARK:- Annotations

func getMapAnnotations() -&gt; \[Station\] { var annotations:Array = \[Station\]()

//load plist file var stations: NSArray? if let path = NSBundle.mainBundle().pathForResource("stations", ofType: "plist") { stations = NSArray(contentsOfFile: path) } //iterate and create annotations if let items = stations { for item in items { let lat = item.valueForKey("lat") as! Double let long = item.valueForKey("long")as! Double let annotation = Station(latitude: lat, longitude: long) annotation.title = item.valueForKey("title") as? String annotations.append(annotation) } }

return annotations } \[/code\]

Add the following piece of code in viewDidLoad function.  

\[code language="swift"\]let annotations = getMapAnnotations() // Add mappoints to Map mapView.addAnnotations(annotations)\[/code\]

Now if you build and run the project, you should see the map with annotations. And on tapping any mappoint should display the title for that station.  

[![](/assets/images/1436160287_thumb.png)](https://rshankar.com/wp-content/uploads/2015/07/1436160287_full.png)

### Add Polyline to MapView

In order add Polyline overlay to map, we need to implement function defined in MKMapViewDelegate protocol. Add MkMapViewDelegate in the class declaration after UIViewController.

\[code language="swift"\]class ViewController: UIViewController, MKMapViewDelegate {\[/code\]

Then make sure to set the delegate property of the mapview to self so that the ViewController can implement and handle the MKMapViewDelegate functions. Add the following piece of code in viewDidLoad function after the annotations.  

\[code language="swift"\] mapView.delegate = self // Connect all the mappoints using Poly line.

var points: \[CLLocationCoordinate2D\] = \[CLLocationCoordinate2D\]()

for annotation in annotations { points.append(annotation.coordinate) } var polyline = MKPolyline(coordinates: &amp;points, count: points.count) mapView.addOverlay(polyline) \[/code\]

create a array of CLLocationCoordinate2D by iterating through annotations. Then create an instance of MKPolyline class by passing array of CLLocationCoordinate2D and count of coordinates. Finally add this polyline to mapView overlay.

Implement the **rendererForOverlay MKMapViewDelegate** function and return an insatnce of MKPolylineRenderer class  

\[code language="swift"\] //MARK:- MapViewDelegate methods

func mapView(mapView: MKMapView!, rendererForOverlay overlay: MKOverlay!) -&gt; MKOverlayRenderer! { if overlay is MKPolyline { var polylineRenderer = MKPolylineRenderer(overlay: overlay) polylineRenderer.strokeColor = UIColor.blueColor() polylineRenderer.lineWidth = 5 return polylineRenderer }

return nil } \[/code\]

Now build and run the app should display the Polyline on the Map.  

[![](/assets/images/1436161478_thumb.png)](https://rshankar.com/wp-content/uploads/2015/07/1436161478_full.png)

Download the source code from [here](https://github.com/rshankras/MapViewDemo)
