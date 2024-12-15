---
title: "Selection Sort"
date: "2014-07-01"
categories: 
  - "develop"
  - "ios"
  - "xcode"
tags: 
  - "algorithm"
  - "selection-sort"
  - "swift"
  - "xcode"
---

Selection Sort algorithm does the same amount of comparison( **N\*(N-1)/2** ) like [bubble sort](https://rshankar.com/swift-bubble-sort/) but the number swaps (**N**) is reduced drastically. This sort algorithm traverse through all the items, picks the smallest number and swaps it with left most item. Then the step is repeated for the next smallest number until it reaches the end of the elements in array. Listed below is the code for Selection Sort and screenshot of this algorithm executed in Playground.

import UIKit

`func swapNumbers(index1 :Int,index2: Int) {`

`let temp = inputArr[index1]`

`inputArr[index1] = inputArr[index2]`

`inputArr[index2] = temp`

`}`

`   `

`var inputArr = Int[]()`

`   `

`// generate random numbers`

`for rIndex in 0..10 {`

`inputArr.append(((Int(arc4random()) % 100)))`

`}`

`   `

`inputArr`

`   `

`var minIndex: Int = 0`

`   `

`func selectionSort(inputArray :Int[]) {`

`for var index:Int = 0; index < inputArr.count-1; ++index {`

`minIndex = index`

`for (var jIndex: Int = index + 1; jIndex < inputArr.count-1; ++jIndex) {`

`if inputArr[jIndex] < inputArr[minIndex] {`

`minIndex = jIndex`

`}`

`}`

`swapNumbers(index, minIndex)`

`}`

`}`

`   `

`selectionSort(inputArr)`

`   `

`inputArr`

1. swapNumber function is used for swapping the numbers in the array for the given indexes.

3. The numbers for the input array is randomly generated using the arc4random function.  
    

5. selectionSort function is the selectionSort algorithm that starts from the first number in the array and compares it with other elements and finds smallest one (stores the index as minIndex).  
    

7. Then swaps the smallest number with the left most and repeats these steps for the next number in the array until it reaches end of array.  
    

  
![Selection Sort algorithm in Swift ](images/201407012043.jpg)
