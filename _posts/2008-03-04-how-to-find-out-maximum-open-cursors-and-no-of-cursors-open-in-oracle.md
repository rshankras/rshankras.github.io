---
title: "How to find out maximum open cursors and no of cursors open in Oracle"
date: "2008-03-04"
categories: 
  - "technical"
---

The **maximum number of open cursors** in an **oracle** database can be determined by the following query

**select name, value  
from v$parameter  
where name like 'open-cursors'**

the value for **open\_cursors** parameter refers to maximum number of open cursors allowed.

The below query can be used to determine number of open cursors for the current session.

**SELECT  
sid,user\_name, COUNT(\*) "Cursors per session"  
FROM v$open\_cursor  
GROUP BY sid,user\_name**
