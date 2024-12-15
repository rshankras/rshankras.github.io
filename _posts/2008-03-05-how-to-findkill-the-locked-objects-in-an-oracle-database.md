---
title: "How to find/kill the locked objects in an oracle database"
date: "2008-03-05"
categories: 
  - "technical"
---

The below query can be used for determining the if any object locked in an oracle database.

> select   c.owner,  c.object\_name,  c.object\_type,  b.sid,  b.serial#,  
>    b.status, b.osuser, b.machine  
> from  
>    v$locked\_object a , v$session b, dba\_objects c  
> where  
>    b.sid = a.session\_id  
> and a.object\_id = c.object\_id;

And if you need to kill any session you can use the below query to do the same.

> alter system kill session sid,serial;
