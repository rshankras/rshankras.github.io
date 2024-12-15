---
title: "Test Driven Development in iOS - Beginners tutorial - Part 1"
date: "2014-04-13"
categories: 
  - "ios"
  - "iphone-4s"
  - "xcode"
tags: 
  - "assertions"
  - "ios-2"
  - "tdd"
  - "xcode"
  - "xctest"
---

This is a beginner tutorial on TDD in iOS, explained with an example app that adds two numbers. Let us see try to use some [XCTest assertions supported in iOS](https://rshankar.com/assertions-supported-in-xctest/) in this project.

Create a New iOS project select the template as Empty Application

![201404132059.jpg](/assets/images/201404132059.jpg)

Enter the required details in Choose options for your new project screen.

![201404132104.jpg](/assets/images/201404132104.jpg)

Step 3: Then specify the folder to save this project.

![201404132106.jpg](/assets/images/201404132106.jpg)

The project navigator screen will have two targets, one for app and add another for XCTest framework. The folder that ends with “Tests” will contain the default XCTest file .

Lets use the class AddingTwoNumbersTests.m for testing the application logic. Open AddingTwoNumbersTests.m and delete default testExample method.

![201404132127.jpg](/assets/images/201404132127.jpg)

Create a failing method that tests for existence of new “RSAddition” class that is going to have method for adding two numbers.

![201404132155.jpg](/assets/images/201404132155.jpg)  

You should notice the errors displayed in the above screenshot after adding testAdditionClassExists. To fix these error, create a new class named RSAddition subclass of NSObject and add the class to both the targets. Then import the Addition.h in “AddingTwoNumbersTests.m”.

![201404132152.jpg](/assets/images/201404132152.jpg)

![201404132153.jpg](/assets/images/201404132153.jpg)

Now the tests should pass when it gets executed. You should notice the green tick mark before the class and method and shown in the below screenshot.

![201404132158.jpg](/assets/images/201404132158.jpg)

Now add the following method to do a simple addition of 2+2.

\-(void)testAddTwoPlusTwo {

RSAddition \*addition = \[\[RSAddition alloc\] init\];

NSInteger result = \[addition addNumberOne:2 withNumberTwo:2\];

XCTAssertEqual(result, 4, @"Addition of 2 + 2 is 4");

}

RSAddition class needs to have a new method addNumberOne: withNumberTwo: Add the method definition in RSAddition.h interface file.

\-(NSInteger)addNumberOne:(NSInteger) firstNumber withNumberTwo:(NSInteger) secondNumber;

Then add the following method to RSAddition.m implementation file. Let us hardcode the result “4” for time being to pass this test.

\-(NSInteger)addNumberOne:(NSInteger) firstNumber withNumberTwo:(NSInteger) secondNumber {

return 4;

}

  
Now the test should get executed successfully.  
![201404132209.jpg](/assets/images/201404132209.jpg)  
Let us add another test to fix the hardcoding problem. This time we will add two different numbers 2 and 7. But before adding the test method, we need to refactor the existing code in the test file. The below code is used by both the test methods and this is the best candidate to be placed under setup method.  

  RSAddition \*addition = \[\[RSAddition alloc\] init\];

  

The changed code should look as shown in the below screenshot.  

![201404132223.jpg](/assets/images/201404132223.jpg)  

Adding the below method should fail as the addition method is hardcoded to return value as 4. 

  

\-(void)testAddTwoPlusSeven {

NSInteger result = \[addition addNumberOne:2 withNumberTwo:7\];

XCTAssertEqual(result, 9, @"Addition of 2 + 7 is 9");

}

  
![201404132226.jpg](/assets/images/201404132226.jpg)

  

Now edit the addition method to fix this problem. It requires just a one line change and now the test should pass.

![201404132229.jpg](/assets/images/201404132229.jpg)

  

![201404132231.jpg](/assets/images/201404132231.jpg)

  

The next tutorial will cover the steps for adding the view controller and required fields for adding two numbers using the above added application logic class.

  

Download source code from [here](https://github.com/rshankras/AddingTwoNumbers-Part1).
