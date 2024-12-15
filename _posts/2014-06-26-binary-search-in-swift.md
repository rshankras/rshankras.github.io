---
title: "Binary search"
date: "2014-06-26"
categories: 
  - "apple"
  - "develop"
  - "ios"
  - "programming"
  - "xcode"
tags: 
  - "apple"
  - "binary-search"
  - "bubble-sort"
  - "swift"
  - "xcode"
---

After a [simple bubble sort algorithm](https://rshankar.com/swift-bubble-sort/) (not the most efficient sorting algorithm), let us try to implement **Binary search in Swift Programming Language**. Binary search algorithm can be applied only on sorted arrays. So let us first generate random numbers and store them in an array. Then call the bubble sort function to sort the numbers by passing the array to the function.

`import Cocoa`

`   `

`func swapNumbers(index1 :Int,index2: Int) {`

`let temp = inputArr[index1]`

`inputArr[index1] = inputArr[index2]`

`inputArr[index2] = temp`

`}`

`   `

`func bubbleSort(inputArray :Int[]) {`

`for var index: Int = inputArr.count-1; index > 1; --index {`

`for var jIndex: Int = 0; jIndex < index; ++jIndex {`

`if inputArr[jIndex] > inputArr[jIndex + 1] {`

`swapNumbers(jIndex, jIndex+1)`

`}`

`}`

`}`

`}`

`   `

`var inputArr = Int[]()`

`   `

`// generate random numbers`

`for rIndex in 0..10 {`

`inputArr.append(((Int(arc4random()) % 100)))`

`}`

`   `

`//call bubblesort function to sort the numbers in array`

`bubbleSort(inputArr)`

`   `

`inputArr`

**Steps for Binary search algorithm**

- Set lower index to 0 and upper index to total count of elements

- Set the current index to the median of lower and upper index

- Repeat these checks in a infinite while loop.

- Check if passed number is equal to number returned by current index. If it matches then return the current index.

- If the lower index is greater than upper index, it means the search item does not exist in the array. Hence return the array's total elements.

- If current index is greater than the search item then decrease the upper index

- if current index is less than the search item then increase the lower index.

`func findItem(searchItem :Int) -> Int{`

`var lowerIndex = 0;`

`var upperIndex = inputArr.count - 1`

`   `

`while (true) {`

`var currentIndex = (lowerIndex + upperIndex)/2`

`if(inputArr[currentIndex] == searchItem) {`

`return currentIndex`

`} else if (lowerIndex > upperIndex) {`

`return inputArr.count`

`} else {`

`if (inputArr[currentIndex] > searchItem) {`

`upperIndex = currentIndex - 1`

`} else {`

`lowerIndex = currentIndex + 1`

`}`

`}`

`}`

`}`

`   `

`findItem(78)`
