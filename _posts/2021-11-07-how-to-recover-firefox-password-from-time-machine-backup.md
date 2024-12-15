---
title: "How to recover Firefox password from Time Machine backup"
date: "2021-11-07"
categories: 
  - "firefox"
  - "mac"
  - "not-programming"
  - "tips"
tags: 
  - "recover-passwords"
---

Here are steps to **recover Firefox passwords** from **Time Machine backup** on Mac.

1. Open Time Machine and navigate to the backup data from which you want to retrieve the Firefox passwords
2. Make sure [hidden files and folders](https://rshankar.com/show-hidden-files-and-folders-on-mac/) option is enabled on your Mac.
3. Navigate to Users -> <UserName> -> Library
4. Under Library navigate to **Application Support** followed **Firefox** folder.
5. Under Firefox navigate to **Profiles** and open the folder ending with default-release.
6. Copy **key4.db** and **logins.json**.
7. Copy the above two files to Profiles folder under Users/<UserName>/Library/Application Support/Firefox/...default-release/Profiles. Before copying make sure to take a backup of existing key4.db and logins.json files.

Now all your saved usernames and passwords for Firefox will be available on your Mac.
