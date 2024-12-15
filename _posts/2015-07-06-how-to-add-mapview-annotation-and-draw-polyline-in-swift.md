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

```swift
@IBOutlet weak var mapView: MKMapView!
```

Now if you do a build and run the project in iPhone 6 simulator, you should see the following on simulator.  

[![](/assets/images/1436157414_thumb.png)](https://rshankar.com/wp-content/uploads/2015/07/1436157414_full.png)

### Zoom to specified region

Add the follwing piece of code in ViewController.swift file. And call this function from ViewController’s viewDidLoad function.  

```swift
//MARK:- Zoom to region
func zoomToRegion() {
    let location = CLLocationCoordinate2D(latitude: 13.0827, longitude: 80.2707)
    let region = MKCoordinateRegionMakeWithDistance(location, 1000.0, 1000.0)
    mapView.setRegion(region, animated: true)
}
```

CLLocationCoordinate2D is created by specifying latitude and longitude of the zoom location. Then using MKCoordinateRegionMakeWithDistance set the distance around the speicifed location. Then this region will set as the region for the MapView. Build and run the project should show Map zooming to the speicifed region as shown below.  

[![](/assets/images/1436158801_thumb.png)](https://rshankar.com/wp-content/uploads/2015/07/1436158801_full.png)

### Add plist file to project.

All the station details such as title, latitude and longitude are stored in a plist file. You can download the plist from gitHub. Right click on the Project folder (Project navigator) and select “Add Files to <Project name>” option. And select **Copy items if needed** option while adding the file.  

[![](/assets/images/1436159062_thumb.png)](https://rshankar.com/wp-content/uploads/2015/07/1436159062_full.png)

The sample data structure of the plist file is shown below  

[![](/assets/images/1436159206_thumb.png)](https://rshankar.com/wp-content/uploads/2015/07/1436159206_full.png)

### Add place holder class Station

Create a new model class for holding the station data. This class should conform to `MKAnnotation` and `NSObject` protocol.  

```swift
import MapKit
import UIKit

class MapPoint: NSObject, MKAnnotation {
    var coordinate: CLLocationCoordinate2D
    var title: String?
    var subtitle: String?
    
    init(coordinate: CLLocationCoordinate2D, title: String, subtitle: String) {
        self.coordinate = coordinate
        self.title = title
        self.subtitle = subtitle
    }
}
```

This class has properties for title, subtitle, latitude, longitude and coordinate. Any mappoint should have coordinate for the adding it to the map. This property is mandatory and it is defined in MKAnnotation protocol. The initializer in the class accepts the latitide and longitude details as they are needed for creating the coordinates.

### Add annotation to MapKit

We need to iterate through the plist file and create annotation for each stations. Add the following function to ViewController.swift which does the same.

```swift
//MARK:- Annotations
func getMapAnnotations() -> [MapPoint] {
    var annotations = [MapPoint]()
    
    // Chennai Central
    let chennaiCentral = MapPoint(coordinate: CLLocationCoordinate2D(latitude: 13.0827, longitude: 80.2707), title: "Chennai Central", subtitle: "Railway Station")
    annotations.append(chennaiCentral)
    
    // Chennai Egmore
    let chennaiEgmore = MapPoint(coordinate: CLLocationCoordinate2D(latitude: 13.0732, longitude: 80.2610), title: "Chennai Egmore", subtitle: "Railway Station")
    annotations.append(chennaiEgmore)
    
    return annotations
}
```

Add the following piece of code in viewDidLoad function.  

```swift
let annotations = getMapAnnotations()
// Add mappoints to Map
mapView.addAnnotations(annotations)
```

Now if you build and run the project, you should see the map with annotations. And on tapping any mappoint should display the title for that station.  

[![](/assets/images/1436160287_thumb.png)](https://rshankar.com/wp-content/uploads/2015/07/1436160287_full.png)

### Add Polyline to MapView

In order add Polyline overlay to map, we need to implement function defined in MKMapViewDelegate protocol. Add MkMapViewDelegate in the class declaration after UIViewController.

```swift
class ViewController: UIViewController, MKMapViewDelegate {
```

Then make sure to set the delegate property of the mapview to self so that the ViewController can implement and handle the MKMapViewDelegate functions. Add the following piece of code in viewDidLoad function after the annotations.  

```swift
mapView.delegate = self
// Connect all the mappoints using Poly line.
let coordinates = annotations.map({ $0.coordinate })
let polyLine = MKPolyline(coordinates: &coordinates, count: coordinates.count)
mapView.addOverlay(polyLine)
```

create a array of CLLocationCoordinate2D by iterating through annotations. Then create an instance of MKPolyline class by passing array of CLLocationCoordinate2D and count of coordinates. Finally add this polyline to mapView overlay.

Implement the **rendererForOverlay MKMapViewDelegate** function and return an insatnce of MKPolylineRenderer class  

```swift
//MARK:- MapViewDelegate methods
func mapView(mapView: MKMapView!, rendererForOverlay overlay: MKOverlay!) -> MKOverlayRenderer! {
    if overlay is MKPolyline {
        let polylineRenderer = MKPolylineRenderer(overlay: overlay)
        polylineRenderer.strokeColor = UIColor.blueColor()
        polylineRenderer.lineWidth = 4
        return polylineRenderer
    }
    return nil
}
```

Now build and run the app should display the Polyline on the Map.  

[![](/assets/images/1436161478_thumb.png)](https://rshankar.com/wp-content/uploads/2015/07/1436161478_full.png)

Download the source code from [here](https://github.com/rshankras/MapViewDemo)
