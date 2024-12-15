---
title: "Provisioning iPhone 4S for deploying and testing Apps"
date: "2012-03-31"
categories: 
  - "develop"
  - "ios"
tags: 
  - "apple"
  - "testing"
  - "deploying"
  - "iphone"
  - "provisioning"
---

Listed below are detail steps for provisioning iPhone 4S for deploying and testing Apps. The steps have been broadly classified in to the following topics.

- Requesting Development Certificate

- Submit Certificate in iOS Provisioning Portal  
    

- Installing Certificate  
    

- Registering Device to Provisioning Portal  
    

**Requesting Development Certificate**  

Requesting development certificate requires you to generate a Certificate Signing Request (CSR). The CSR can be generated using the KeyChain app available as part of the Mac OS. You can quickly launch keychain using spotlight search. Apart from generating the CSR, the Keychain app also generates the public and private key.

![201203311214.jpg](images/201203311214.jpg)

Select Keychain Access preferences from the menu list and navigate to Certificates tab.

![201203311227.jpg](images/201203311227.jpg)

**Turn off the Online Certificate Status Protocol** (OCSP).

![201203311229.jpg](images/201203311229.jpg)

Now to request Certificate, click the **Keychain Access** menu, select Request a certificate from a Certificate Authority under the Certificate Assistant.

![201203311244.jpg](images/201203311244.jpg)

In the Certificate Assistant window, enter your email address, name and mark the radio option with caption as Saved to disk also the check box with label as Let me specify key pair information.

  
![201203311250.jpg](images/201203311250.jpg)

Save the generated certificate to your desktop.

![201203311318.jpg](images/201203311318.jpg)

Then for the Key Pair information, select Key Size as **2048** bits and Algorithm as **RSA**.

![201203311319.jpg](images/201203311319.jpg)

On clicking the continue button will display the following confirmation message.

![201203311439.jpg](images/201203311439.jpg)

The login section under Keychain Access would display the generated Public key and Private key.

![201203311440.jpg](images/201203311440.jpg)

**Submitting Request in Provisioning Portal**

Login to the members account with your Apple user id and password. Click the **iOS Provisioning Portal** link available under Developer Program Resources section.

![201203311444.jpg](images/201203311444.jpg)

In the Provisioning Portal, navigate to Certificates section and click the Request Certificate button under Development.

![201203311443.jpg](images/201203311443.jpg)

This would display a screen with option to submit the CSR.

  
![201203311446.jpg](images/201203311446.jpg)

Choose the required CSR and click the Submit button. After submitting the status would initially be displayed as **Pending issuance** and later a download link would appear.

![201203311447.jpg](images/201203311447.jpg)

  
![201203311448.jpg](images/201203311448.jpg)

Now install the WWDR certificate and iOS developer Certificate on your Mac system

  
![201203311449.jpg](images/201203311449.jpg)

  
![201203311450.jpg](images/201203311450.jpg)

You can verify the installation of certificates by navigating to My Certificates in Keychain Access App.

  
![201203311451.jpg](images/201203311451.jpg)

**Registering Device to Provisioning Portal**

You can use Xcode for registering the Device ID and this process also create the App ID. Launch Xcode, click the Window menu option and select Organizer from the menu list.

![201203311454.jpg](images/201203311454.jpg)

This would display the list of available Devices that have been connected to the Mac system,

![201203311455.jpg](images/201203311455.jpg)

When the device is connected, a green status light will be displayed. Now select iPhone 4S and click the Use for Development button. If your Device and Mac system are out of sync with the iOS SDK then you will get the message to keep both of them in sync.

  
![201203311501.jpg](images/201203311501.jpg)

Once the device and Mac system are in sync, you can add the device to Provisioning Portal by right clicking on the device and selecting **Add Device to Provisioning Portal**.

![201203311503.jpg](images/201203311503.jpg)

Xcode will request permission for accessing your Keychain, click Always Allow button and sign-in with your Apple Developer Account credentials. Also allow code sign to sign using your key in keychain.

![201203311506.jpg](images/201203311506.jpg)

Now you can test your app on iPhone 4S by selecting the device from Active Scheme list.

![201203311508.jpg](images/201203311508.jpg)
