---
title: "'NSInvalidUnarchiveOperationException', reason: 'Could not instantiate class named MKMapView'"
date: "2013-02-01"
categories: 
  - "develop"
  - "programming"
tags: 
  - "mapkit-framework"
  - "mkmapview"
  - "objective-c"
---

**Problem** :- Xcode project with MapView control displays the error "'NSInvalidUnarchiveOperationException', reason: 'Could not instantiate class named MKMapView'"

**Solution** :- The 'Could not instantiate class named MKMapView' error is displayed when the Xcode project with MapView control on xib does not include the MapKit library as part of the Link Libraries.

Select the Xcode project and navigate to Build Phases.

![201302010703.jpg](images/201302010703.jpg)

Click the + sign under Link Binary with Libraries and select MapKit,framework from framework and libraries to add selection window.

![201302010704.jpg](images/201302010704.jpg)

![201302010705.jpg](images/201302010705.jpg)

Now running the project should not display the NSInvalidUnarchiveOperationException.

![201302010709.jpg](images/201302010709.jpg)
