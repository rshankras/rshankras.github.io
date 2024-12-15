---
title: "Add path variable in MacOS for flutter"
date: "2021-03-26"
categories: 
  - "android-2"
  - "ios"
tags: 
  - "flutter"
  - "macos"
  - "terminal"
---

Flutter commands can be executed from macOS terminal app after adding the path variable to installation of flutter directory on the local machine. You can set Path variable temporarily by executing the following command in the Terminal app or within the Terminal window inside Visual Studio Code

```
export PATH="$PATH:`pwd`[FLUTTER_INSTALLATION_DIRECTORY]/bin"
```

where `FLUTTER_INSTALLATION_DIRECTORY` represents the installtion of flutter SDK on your local macOS

**Setting PATH variable permanently**

Mac users having Catlina OS and above can follow the below mentioned steps for setting the PATH variable permanently.

```
Launch Terminal App.

type touch ~/.zshrc and press enter

type vi ~/.zshrc

add export PATH = $PATH[FLUTTER_INSTALLATION_DIRECTORY]/bin

save the changes.

Reload the changes by typing ~/.zshrc
```

Now you should be able to run all flutter commands using terminal app.
