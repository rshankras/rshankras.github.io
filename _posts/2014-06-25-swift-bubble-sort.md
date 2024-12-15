---
title: "Bubble Sort"
date: "2014-06-25"
categories: 
  - "apple"
  - "ios"
  - "programming"
  - "xcode"
tags: 
  - "apple"
  - "swift"
  - "untitled"
  - "xcode"
---

The best way to practice a new language is to write more programs using that language. Here is a Bubble Sort program written in [Swift Programming language](https://rshankar.com/swift-quick-reference/).

Data to be sorted = {12, 56, 32, 23, 67, 87, 45, 23,10, 11}

**Bubble Sort**

Bubble Sort is performed by comparing two number starting from the left and swapping the greater number to the right. And then moves one position to right until end.

**Bubble Sort in Swift**

This has a function named swapNumbers for swapping the values of array for the given two indexes. Then the **for loop** that compares the two numbers starting from left to right and uses swapNumbers function to swap the values if the left is greater than right.  

var inputArr = \[12,56,32,23,67,87,45,23,10,11\]

  

func swapNumbers(index1 :Int,index2: Int) {

let temp = inputArr\[index1\]

inputArr\[index1\] = inputArr\[index2\]

inputArr\[index2\] = temp

}

  

for var index: Int = inputArr.count\-1; index > 1; --index {

for var jIndex: Int = 0; jIndex < index; ++jIndex {

if inputArr\[jIndex\] > inputArr\[jIndex + 1\] {

swapNumbers(jIndex, jIndex+1)

}

}

}

  

inputArr

  

Here is the Swift code tested in [Playground](https://rshankar.com/xcode-6-and-playground/), you can see the sorted results in the sidebar  

  

![Bubble Sort in Swift Programming language](images/201406251741.jpg)
