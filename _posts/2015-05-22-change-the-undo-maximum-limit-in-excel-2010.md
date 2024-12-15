---
title: "Change undo limit in Excel 2013 and Excel 2010"
date: "2015-05-22"
categories: 
  - "excel"
  - "excel-2010"
  - "excel-2013"
  - "not-programming"
  - "office-2010"
tags: 
  - "change-limit"
  - "excel-2010"
  - "maximum"
  - "undo-history"
  - "undo-limit"
---

[![Undo](/assets/images/Undo_thumb.jpg "Undo")](http://blogmines.com/blog/wp-content/uploads/2011/07/Undo.jpg)

As per the [Excel Specifications and limits](http://office.microsoft.com/en-us/excel-help/excel-specifications-and-limits-HP010073849.aspx#BMworksheetworkbook) the maximum limit for **undo** in Excel 2010 is set to 100. In the previous version of Excel this was set to 16. The **maximum limit** value is fixed but you can **increase** or **decrease** this limit by modify registry settings.

> Please Note:- Changing Registry Settings is not recommended and do this with at most caution while trying these changes.

To change the **undo maximum limit**, Open Windows Registry Editor and then navigate to the following path

**HKEY\_CURRENT\_USER –> Software –> Microsoft –> Office –> 14.0->Excel->Options**

Create a new DWORD value with the key name as **UndoHistory**

[![image](/assets/images/image_thumb230.png "image")](http://blogmines.com/blog/wp-content/uploads/2011/07/image230.png)

Then modify **UndoHistory** by setting the Base as **Decimal** and value as 16. Click the OK button to save the changes.

[![image](/assets/images/image_thumb231.png "image")](http://blogmines.com/blog/wp-content/uploads/2011/07/image231.png)

This would decrease the number of undo same as the previous of Excel. You can also **increase** the **undo limit** from 100 to 200 for Excel 2010 by changing the above created Windows Registry key.
