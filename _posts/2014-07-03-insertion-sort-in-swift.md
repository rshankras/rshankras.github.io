---
title: "Insertion Sort"
date: "2014-07-03"
categories: 
  - "ios"
  - "mac"
  - "programming"
  - "xcode"
tags: 
  - "algorithm"
  - "insertion-sort"
  - "swift"
  - "xcode"
---

**Insertion Sort** algorithm does the following

- Keeps the sorted numbers from left to right.

- Compares the left with right and interchanges the number if left is greater than right.

Here is code snippet of **Insertion Sort in Swift**.  

```swift
var inputArr: [Int] = [Int]()

// generate random numbers 
for rIndex in 0..<10 { 
    inputArr.append(((Int(arc4random()) % 100))) 
}

func insertionSort(var array: [Int]) -> [Int] {
    for x in 1..<array.count {
        var y = x
        while y > 0 && array[y] < array[y-1] {
            let temp = array[y]
            array[y] = array[y-1]
            array[y-1] = temp
            y -= 1
        }
    }
    return array
}

var numbers = [64, 34, 25, 12, 22, 11, 90]
numbers = insertionSort(numbers)
println(numbers)
```

```swift
func insertionSort(var inputArray: [Int]) -> [Int] {
    var jIndex: Int, kIndex: Int

    for kIndex in 1..<inputArray.count {
        let temp = inputArray[kIndex]
        var jIndex = kIndex
        while (jIndex > 0 && inputArray[jIndex-1] >= temp) {
            inputArray[jIndex] = inputArray[jIndex-1]
            --jIndex
        }
        inputArray[jIndex] = temp
    }
    return inputArray
}

insertionSort(inputArr)
