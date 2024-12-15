---
title: "Upload missing dSYMs to see crashes"
date: "2019-10-17"
categories: 
  - "crash"
  - "dsyms"
  - "firebase"
---

If you are using Firebase Crasyltics in your app and if bitcode is enabled then you might see this message

“Upload missing dSYMs to see crashes” when trying to view reported crash in Firebase Crashlytics. In order the see the stack trace, you can try uploading the dSYMs files.

**Compress .dSYMs files.**

- Launch Xcode Organizer.  
    
- Select the App on the Right hand side and navigate to the version which caused the crash.
- Right click on the version and select Show in Finder.

![](/assets/images/Show-Finder.png)

- Right click the archive file and select "Show Package Contents”.
- Copy all the dSYMs files to another location.
- Compress the file and upload the compress file to Firebase to see see the stack trace.

**iTunesConnect  
**  
Another option is to download dSYMs files from iTunes Connect.

Select your App -> Activity section -> Select the Version -> Download dSYSM
