---
title: "A trick to flip a column upside down in Excel"
date: "2016-02-17"
categories: 
  - "excel"
  - "excel-2007"
  - "excel-2010"
  - "excel-2013"
  - "ms-office"
  - "not-programming"
---

Excel users can [sort a column](http://blogmines.com/blog/how-to-sort-columns-with-date-values-in-excel-2010/) using the Sort feature available as part of Sort & Filter menu. But what if you want to flip a column upside down. Let us see this with an example column having some text values as shown below.

[![](/assets/images/1455691643_thumb.png)](http://blogmines.com/blog/wp-content/uploads/2016/02/1455691643_full.png)

We will not be able to apply sort feature directly on this column to flip the data instead we can add a dummy column and use that for sorting the text values.

**Step 1**: Insert a new column before the existing column. **Step 2**: Now use [Auto Fill](http://blogmines.com/blog/how-to-disable-auto-fill-feature-in-excel-2010/) feature to fill the temp with numbers as shown below

[![](/assets/images/1455693039_thumb.png)](http://blogmines.com/blog/wp-content/uploads/2016/02/1455693039_full.png)

**Step 3**: Now you can use the Sort feature on column1 and make sure to sort by descending order. Also include the column2 in Sort sleection list.

[![](/assets/images/1455693169_thumb.png)](http://blogmines.com/blog/wp-content/uploads/2016/02/1455693169_full.png)

**Step 4**: Once the columns are sorted, delete the temp column with numbers.

[![](/assets/images/1455693409_thumb.png)](http://blogmines.com/blog/wp-content/uploads/2016/02/1455693409_full.png)
