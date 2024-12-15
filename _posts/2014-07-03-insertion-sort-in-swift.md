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

\[code language="swift"\]var inputArr:\[Int\] = \[Int\]()

// generate random numbers for rIndex in 0..&lt;10 { inputArr.append(((Int(arc4random()) % 100))) }

func insertionSort(var inputArray :\[Int\]) -&gt; \[Int\] { var jIndex:Int,kIndex:Int

for kIndex in 1.. 0 &amp;&amp; inputArray\[jIndex-1\] &gt;= temp ) { inputArray\[jIndex\] = inputArray\[jIndex-1\] --jIndex } inputArray\[jIndex\] = temp }

return inputArray }

insertionSort(inputArr)\[/code\]
