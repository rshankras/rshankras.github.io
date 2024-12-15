---
title: "Turn on/off Wifi using Keyboard shortcut"
date: "2021-06-06"
categories: 
  - "automator"
  - "mac"
  - "tips"
tags: 
  - "automator"
  - "keyboard-shortcut"
  - "mac"
---

Mac users can turn on/off Wifi using option available as part of the Menu bar.

<figure>

![](/assets/images/image.png)

<figcaption>

Wifi Menu bar option

</figcaption>

</figure>

**Add quick action in Automator app**

Launch Automator app on your mac and choose Quick Action.

<figure>

![](/assets/images/image-1-1024x743.png)

<figcaption>

Automator - Quick Action

</figcaption>

</figure>

Choose action as "Run Shell Script" then set Workflow receives to "no input" and set it to run for for any application and select an image for your action.

![](/assets/images/image-2-1024x382.png)

Then under the run script window add the following script.

```shell
set_wifi_on_or_off() {
  networksetup -getairportpower en${n} | grep ": ${1}";
  if test $? -eq 0;
  then
    echo WiFi interface found: en${n};
    eval "networksetup -setairportpower en${n} ${2}"
    return 0;
  fi
  return 1;
}

for n in $(seq 0 10);
do
  if set_wifi_on_or_off "On" "off"; then break; fi;
  if set_wifi_on_or_off "Off" "on"; then break; fi;
done
```

![](/assets/images/image-3-1024x870.png)

You can test the above script using "Run" option and check if Wifi settings turned On or Off based on the current state. Save this quick action by providing a name as "Wifi"

**Assign a keyboard shortcut for quick action**

Launch Keyboard preferences using System preferences and navigate to Shortcuts tab.

<figure>

![](/assets/images/image-4-1024x925.png)

<figcaption>

Keyboard Preferences

</figcaption>

</figure>

The newly added Wifi quick action will be available under Services. Now assign a keyboard shortcut for this action.

![](/assets/images/image-5-1024x311.png)

Note :- Make sure to select 3 letters or more keyboard combination for your shortcut. Sometimes other apps might be using the same set of key combination and this would prevent launching the Automator action.

[References](https://apple.stackexchange.com/questions/194368/turn-wifi-off-on-with-a-single-key)
