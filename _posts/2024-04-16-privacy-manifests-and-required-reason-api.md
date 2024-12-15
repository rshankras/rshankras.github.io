---
title: "Privacy Manifests and Required Reason API"
date: "2024-04-16"
categories: 
  - "ios"
  - "swift"
  - "xcode"
---

Most of the iOS developers might have received an email about "Privacy Manifest" issues from Apple when submitting an app for review.

"We noticed one or more issues with a recent submission for App Store review **ITMS-91053: Missing API declaration**, **TMS-91064: Invalid tracking information** etc.

1. NSPrivacyAccessedAPICategoryFileTimestamp

3. NSPrivacyAccessedAPICategoryUserDefaults

5. NSPrivacyAccessedAPICategorySystemBootTime

7. NSPrivacyAccessedAPICategoryDiskSpace

You must include a NSPrivacyAccessedAPITypes array in your app’s privacy manifest to provide approved reasons for these APIs used by your app’s code."

**Reason for this issues**

As we know that Apple is quite strict about users privacy. There is a term called finger print where you can uniquely identify the user by using combination of certain API's. And apple wants to prevent this identification, Hence they want the developers to give a reason for using any of the API's listed under [here](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_use_of_required_reason_api) in their app or the third party APIs. Now it is for each developer to give the reason for using the API by adding PrivacyInfo for their app and each third party API have to provide a similar PrivacyInfo for their APIs.

The PrivacyInfo needs to added for your app as well as for the third party frameworks like Firebase that is being used in your app. The third party framework will be handled by the respective third parties. Already Firebase has added the required information.

After adding the Privacy manifest and adding it as part of your build Target, you can ensure that it is available as part of of you build by using "Generating Privacy Report" option as part of your build archives. Just make sure the details you have added is available as part of the report.

![](/assets/images/Screenshot-2024-04-16-at-2.08.26 PM-1024x312.png)

WeMakeApps has got a cool tool that will generate the Privacy Manifest for your app. You can check this out [here](https://wemakeapps.net/manifest-maker). Also in [this](https://forums.developer.apple.com/forums/thread/749306) forum thread you can get the complete list of Privacy Manifest. Update the ones needed for your app and delete the other items.
