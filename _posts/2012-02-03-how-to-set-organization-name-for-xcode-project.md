---
title: "How to set Organization name for Xcode Project"
date: "2012-02-03"
categories: 
  - "xcode"
tags: 
  - "apple"
  - "organization"
  - "xcode"
---

When ever a new project is created in Xcode, the projects files like header and implementation files will have auto generated comment section at the top of the file. This comment section will have information such as file name, Project name, Author and Organization name.

//

// ViewController.h

// Welcome

//

// Created by Ravi Shankar on 02/02/12.

// Copyright (c) 2012 \_\_MyCompanyName\_\_. All rights reserved.

//

If you have not set the organization name then the default value substituted will be **\_MyCompanyName\_**. You can set the Organization name by the following ways.

- Setting Organization name under File Inspector

- Updating Company name for the user in Mac Address book

**File Inspector**

Select the Project in the Project Navigator, then navigate to Utilities section and click the File Inspector icon. Now navigate to Project Document section and enter the company name in field with caption as Organization.

![201202031600.jpg](images/201202031600.jpg)

Now if you add any new file to this project then the auto generated comment will have the company name as "rshankar.com".

**Address Book**

If you want to retain this organization name for all the future projects then update the company name for the user in Mac Address Book. Launch Address Book, then select the user and update the company name as shown below.

![201202031613.jpg](images/201202031613.jpg)

Now when ever a new project or new file is added in Xcode, the Organization name will be set the value provided for company name in address book.

//

// ViewController.h

// OrganizationName

//

// Created by Ravi Shankar on 03/02/12.

// Copyright (c) 2012 rshankar.com. All rights reserved.

//

Please note that any files created before this change will not get affected and you will have to manually update company name.
