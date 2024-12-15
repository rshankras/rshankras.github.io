---
title: "UserForms in Word Macros and VBA"
date: "2014-10-11"
categories: 
  - "9-dec-2024"
  - "ms-office"
tags: 
  - "macros"
  - "userforms"
  - "vba-code"
  - "vba-editor"
---

We had earlier seen an example [Macro for inserting date and time](http://blogmines.com/blog/write-your-own-macro-in-word-2011-for-mac/). We will use the same example but replace MsgBox with UserForms. The users will be displayed the following form and based on the user input the date and time will be inserted in the document.

![201407021300.jpg](/assets/images/201407021300.jpg)

**Step 1**: Insert a UserForm by right clicking the Project Navigator, Click Insert then UserForm.

![201407021157.jpg](/assets/images/201407021157.jpg)

The following UserForm along with the controls for designing form will be shown.

![201407021204.jpg](/assets/images/201407021204.jpg)

**Step 2**: Now drag and drop the required controls on to the form. This form will be presented to the user asking their choice on the date and time and the alignment.

![201407021222.jpg](/assets/images/201407021222.jpg)

The form contains two frames for grouping Date and Time and Alignment choices. The corresponding option controls for Date and Time and Alignment. Then OK button to apply the changes and Cancel button to close the form without applying the user choice.

**Step 3**: Make sure to change the caption for the controls and provide the Value as True for Date and Time and Right. This is to ensure than both the choices have default values. You can set these values using the properties window.

![201407021234.jpg](/assets/images/201407021234.jpg)

**Step 4**: Add the code for the action that should occur on clicking the OK and Cancel button. Double click on the Command button to add the code for respective command controls.

**Code for OK Button**

`Private Sub CommandButton1_Click()   `

`'Create a new document`

`Documents.Add DocumentType:=wdNewBlankDocument`

`'Insert date or date and time depending upon the user input.`

`If OptionButton1.Value = True Then`

`Selection.InsertDateTime DateTimeFormat:="dddd, MMMM d, y", InsertAsField _`

`:=True`

`Else`

`Selection.InsertDateTime DateTimeFormat:="M/d/yy h:mm:ss am/pm", _`

`InsertAsField:=True`

`End If`

`'Align date based on user's choice`

`If OptionButton3.Value = True Then`

`Selection.ParagraphFormat.Alignment = wdAlignParagraphLeft`

`ElseIf OptionButton4.Value = True Then`

`Selection.ParagraphFormat.Alignment = wdAlignParagraphRight`

`Else`

`Selection.ParagraphFormat.Alignment = wdAlignParagraphCenter`

`End If`

`'Revert the alignment to left.`

`Selection.TypeParagraph`

`Selection.ParagraphFormat.Alignment = wdAlignParagraphLeft`

`‘Hide the form.   `

`UserForm1.Hide`

`End Sub`

**Code for Cancel Button**

`Private Sub CommandButton2_Click()`

`UserForm1.Hide`

`End Sub`

Now trying running the form to see the UserForm in action.  
![201407021253.jpg](/assets/images/201407021253.jpg)  
Note :- Some improvements can be done to the above example like providing proper name to OptionButtons and CommandButtons.
