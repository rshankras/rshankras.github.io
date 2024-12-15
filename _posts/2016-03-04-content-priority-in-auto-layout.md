---
title: "Content Priority in Auto Layout"
date: "2016-03-04"
categories: 
  - "auto-layout"
  - "xcode"
tags: 
  - "compression-resistance"
  - "content-hugging"
---

Auto Layout brings in lots of good features to ease the life of an iOS developer when designing User Interfaces. In this example, we will see how to use **Content Priorities** such as **Content Hugging** and **Comrpession Resistance**.

I have created a project with Single View Template and dispayed Size Classes as we are going to focus only on iPhone family.  

![](/assets/images/1457021327_thumb.png)

Drag and drop two labels adjacent to each other.  

![](/assets/images/1457066527_thumb.png)

Add Leading Space and Vertical Space constraints for Label A. Similarly add Vertical Space and Trailing Space constraints for Label B

\[embed height="315" width="560"\]http://www.youtube.com/embed/DT4fqn61eXI\[/embed\]

### Constraints for Label A

![](/assets/images/1457066719_thumb.png)

### Constraints for Label B

![](/assets/images/1457066743_thumb.png)

Click the Update Frames option under the Resolve AutoLayout Issues menu. This should align the frames to reflect the constraints changes.  

![](/assets/images/1457066957_thumb.png)

Change the background colour of Labels to Yellow and Green respectively. This would help us to identity the growth of each labels. Now add the Horizontal Spacing constraint between these two labels and set constant to 5. 

[![](/assets/images/1457068314_thumb.png)](https://rshankar.com/wp-content/uploads/2016/03/1457068314_full.png)

Now Label B has grown and covered the space between both labels. Please note that this would be in random nature some times even Label A can fill up the space between these labels. And in this article, we will see how to control this behaviour. You will also notice the warning message that “2 views are horizontally ambitguous”. This is because Auto Layout does not know which label should grow and shrink in size.  

[![](/assets/images/1457068770_thumb.png)](https://rshankar.com/wp-content/uploads/2016/03/1457068770_full.png)

### Content Compression Resistance Priority

Let us change the text for Label in left hand side as "Content Hugging". Simialrly enter the text for right hand side label as "Compression Resistance". Then Update Frames to refelect the Intrinsic Content Size changes. You will notice that the Compression Resistance has a truncated trail.  

[![](/assets/images/1457068818_thumb.png)](https://rshankar.com/wp-content/uploads/2016/03/1457068818_full.png)

If you want to this label to resist shrinking its size then set the **Content Compression Resistance Priority** (Under Size Inspector) to value higher than the label on left hand side.  

[![](/assets/images/1457069271_thumb.png)](https://rshankar.com/wp-content/uploads/2016/03/1457069271_full.png)

After changing the value from 750 to 751, you will notice the warning messages “Frame will be different at run time”. Now Updating the Frames for All Views in Container shoud reflect as shown in the below screenshot.  

[![](/assets/images/1457069533_thumb.png)](file://localhost//Users/ravishankar/Library/Caches/com.blogo.Blogo.nonmas/1457069533_full-1.png)

### Content Hugging Priority

Now Content Hugging label is partially hidden and it cannot grow horizontally as right hand side label has a higher compression resistance priority. Let us set the number of lines for this lable to 0 (which means it can grow based on the content size). This should again result in “Content Priority Ambiguity” error. This time we can fix this by telling Auto Layout that the label on left hand side has least resistance for growth. Select the label on left hand side, navigate to Size Inspector and set the Content Hugging Priority to lower than right hand side label i.e from 251 to 250. 

[![](/assets/images/1457070194_thumb.png)](https://rshankar.com/wp-content/uploads/2016/03/1457070194_full.png)

Click Update Frames to resolve the warning message “Frame for Content Hugging will be different at run time”. The Content Hugging label in shown in two lines.  

[![](/assets/images/1457070368_thumb.png)](https://rshankar.com/wp-content/uploads/2016/03/1457070368_full.png)

If you need any assistance in Auto Layout, check out our new [iOS 9 Auto Layout Tutorials 50% Off](https://rshankar.com/courses/autolayoutyt5/).
