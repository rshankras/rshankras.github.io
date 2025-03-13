---
title: "How to Create Test Accounts for In-App Purchases and Subscriptions"
date: "2025-03-13"
description: "Learn how to set up and use sandbox test accounts for testing in-app purchases and subscriptions in your iOS apps without real money. Step-by-step guide for app developers."
categories: 
  - "ios"
  - "app-development"
  - "swift"
  - "monetization"
tags: 
  - "in-app-purchases"
  - "subscriptions"
  - "sandbox-testing"
  - "app-store-connect"
  - "ios-development"
  - "test-accounts"
  - "app-monetization"
  - "storekit"
  - "developer-tools"
  - "app-testing"
---

Testing in-app purchases and subscriptions is a crucial step in releasing a monetized app. You don't want to use real money during development and testing, and Apple provides a simple solution - sandbox test accounts. In this post, I'll show you how to create and use these accounts to test your in-app purchases without spending real money.

## Why Use Sandbox Test Accounts?

Sandbox test accounts let you:

- Test the full purchase flow without real charges
- Verify subscription renewals (at accelerated time intervals)
- Test upgrade, downgrade, and cancellation flows
- Ensure receipt validation works correctly
- Test the restore purchases functionality

## Step 1: Create Sandbox Test Accounts in App Store Connect

To create a sandbox test account:

1. Log in to [App Store Connect](https://appstoreconnect.apple.com/)
2. Click on "Users and Access" in the sidebar
3. Select the "Sandbox" tab
4. Click on "Test Accounts"
5. Click the "+" button to add a new tester
6. Fill in the required information:
   - First Name and Last Name
   - Email Address (use an email you have access to)
   - Password (meeting Apple ID requirements)
   - Select your territory

<img src="/assets/images/sandbox-test-account-creation.jpg" alt="App Store Connect Sandbox Test Account Creation" width="600">

**Important:** Use a real email address that you own, but one that's not already associated with an Apple ID. You'll need to verify this email.

## Step 2: Configure Your Device for Testing

After creating your sandbox tester, you need to add it to your test device:

1. On your iOS device, go to **Settings**
2. Scroll down and tap on **Developer**
   - If you don't see this option, make sure you've installed your app from Xcode at least once
3. Tap on **StoreKit Testing** or **Sandbox Apple Account**
4. Tap **Add Account** and enter your sandbox account email and password

<img src="/assets/images/sandbox-account-device-setup.jpg" alt="Device Settings for Sandbox Account" width="400">

## Step 3: Test In-App Purchases with Your Sandbox Account

Now you're ready to test purchases:

1. Open your app on your test device
2. Attempt to make a purchase
3. When prompted to sign in with an Apple ID, use your sandbox account credentials
4. Complete the purchase process

The purchase will go through as if it were a real transaction, but no actual money will be charged. You'll see a confirmation showing it's a sandbox purchase.

## Common Issues and Solutions

### Sandbox Account Not Working

If your sandbox account isn't working:

- Make sure you've verified the email address
- Check that you're signed out of your regular Apple ID in the App Store
- Restart your device and try again

### "This In-App Purchase Has Already Been Bought" Error

If you see this error:

1. Open Settings → App Store
2. Sign out of your regular Apple ID
3. Try the purchase again, and it will prompt for the sandbox account

## Best Practices

1. Create multiple sandbox accounts to test different scenarios
2. Test all subscription tiers and upgrade/downgrade paths
3. Test purchase restoration functionality
4. Verify receipt validation with your server (if applicable)
5. Test cancellation flows and grace periods

## Conclusion

Setting up sandbox test accounts is essential for properly testing in-app purchases and subscriptions. This approach ensures your monetization features work correctly before your app reaches real users, preventing potential revenue loss and negative reviews.

Have you encountered any challenges when testing in-app purchases? Share your experiences in the comments below!

---

*Note: StoreKit testing configurations and sandbox behavior may change with newer iOS versions. This guide is current as of iOS 18.* 