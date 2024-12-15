---
title: "Assertions supported in XCTest"
date: "2017-03-23"
categories: 
  - "develop"
  - "ios"
  - "swift"
  - "xcode"
tags: 
  - "assertions"
  - "xcode"
  - "xctest"
---

Here you can find the list of Assertions supported by XCTest and it is essential to know all these assertion if you are practicing Test Driven Development in IOS. You can get this list from XCTestAssertions.h

```
XCTFail(<#format...#>) - This unconditionally fails the test.
XCTAssertNil(<#a1#>, <#format...#>) - Failure message when object is not nil.
XCTAssertNotNil(<#a1#>, <#format...#>) - Failure message when object is nil
XCTAssertEqual(<#a1#>, <#a2#>, <#format...#>) - Failure message when expressions(a1 & a2) are not equal.
XCTAssertNotEqual(<#a1#>, <#a2#>, <#format...#>) - Failure message when expressions(a1 & a2) are equal.
XCTAssertEqualObjects(<#a1#>, <#a2#>, <#format...#>) - Failure message when objects(a1 & a2) are not equal.
XCTAssertNotEqualObjects(<#a1#>, <#a2#>, <#format...#>) - Failure message when objects(a1 & a2) are not equal.
XCTAssertEqualWithAccuracy(<#a1#>, <#a2#>, <#accuracy#>, <#format...#>) - Failure message when a1 is not equal to a2 with + or - accuracy.
XCTAssertNotEqualWithAccuracy(<#a1#>, <#a2#>, <#accuracy#>, <#format...#>) - Failure message when a1 is equal to a2 with + or - accuracy.
XCTAssertNoThrow(<#expression#>, <#format...#>) - Failure message when expression does throw exception.
XCTAssertNoThrowSpecific(<#expression#>, <#specificException#>, <#format...#>) - Failure message when expression throws specific exception.
XCTAssertNoThrowSpecificNamed(<#expression#>, <#specificException#>, <#exception_name#>, <#format...#>) - Failure message when expression throws specific class with specific name.
XCTAssertThrows(<#expression#>, <#format...#>) - Failure message when expression does not throw exception.
XCTAssertThrowsSpecific(<#expression#>, <#specificException#>, <#format...#>) - Failure message when expression does not throw specific exception.
XCTAssert(<#expression#>, <#format...#>) - Failure message when expression is false.
XCTAssertTrue(<#expression#>, <#format...#>) - Failure message when expression is false.
XCTAssertFailure(<#expression#>, <#format...#>) - Failure message when expression is true.
```
