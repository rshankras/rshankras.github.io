---
title: "Expense Split - A Journey from Old to New"
date: "2023-09-09"
categories: 
  - "app-reviews"
  - "expense-split"
---

I recently decided to give my hobby app - [Expense Split](https://apps.apple.com/in/app/expensesplit/id1041478586?platform=iphone) a complete makeover. The objective was not just to update its look but also to improve its architecture and add new features. In this blog post, I will walk you through the entire process, comparing old screenshots with new ones to highlight the changes.

1\. A fresh new look

2\. Core Data modifications with migration

3\. Transition to SwiftUI

4\. Implement MVVM architecture

5\. Localisation support

6\. UI and Unit Testing

7\. Analytics Integration

8\. In-app purchases

9\. User feedback collection via Google Sheet

##  **A Fresh New Look**

The first thing you will notice is that is the Updated UI. I wanted to make the app visually appealing, minimalistic but keeping the user experience intuitive.

**Before**

![](/assets/images/Screenshot-1-2-473x1024.png)

![](/assets/images/Screenshot-2-2-473x1024.png)

![](/assets/images/Simulator-Screen-Shot-iPhone-12-Pro-Max-2021-04-20-at-06.07.13-473x1024.png)

**After**

![](/assets/images/Groups-472x1024.png)

![](/assets/images/AddNewExpense-copy-472x1024.png)

![](/assets/images/BalanceDetail-472x1024.png)

## **Core Data Modifications with Migration**

The app initially used a somewhat cluttered Core Data model with multiple entities that had overlapping responsibilities. The helper methods for interacting with Core Data were also scattered and inconsistent.

I reduced the number of entities by merging some that had overlapping functionalities. I also refactored the Core Data helper methods to make them more efficient and easier to manage. Importantly, I implemented data migration to ensure that existing users wouldn't lose any data during this transition.

## **Transition to SwiftUI**

The app was originally built using UIKit/Storyboard, which was functional but a bit outdated. Switching to SwiftUI allowed me to create a more modern and interactive UI with less code.

## Implementing MVVM Architecture

The app initially used MVC, which made it challenging to manage as the codebase grew. I switched to MVVM architecture to separate the business logic from the view, making the code easier to manage and test.

## Localisation Support

I added localisation support to make the app accessible to a global audience. Now, the app automatically adapts to the language settings of the user's device. Supported language are English, French, Japanese, German, Russian, Chinese, Hindi and Tamil. SwiftUI makes life easy for reading strings from the localisation file.

## UI and Unit Testing

I implemented both UI and Unit tests to ensure that the app works as expected under various conditions. While I haven't yet achieved 100% code coverage, the exercise was incredibly educational. I learned about various testing jargons like "mocks," "stubs," and "test suites," and how they can be applied to improve the app's reliability and maintainability.

## Analytics Integration

I integrated analytics to track user behaviour, which will help in future updates.

I'm tracking several key metrics to understand user engagement and feature usage:

**User Onboarding Completion**: To see how many users successfully complete the onboarding process.

**Migration Completion for Old Users**: To ensure that users who are updating the app experience a smooth transition.

**CSV Export Attempts**: To gauge the usage of the app's export feature.

**Number of Expenses Created**: To understand how actively the app's core functionality is being used.

## In-App Purchases

To monetise the app, I implemented in-app purchases, allowing users to buy premium features. Now the data export to CSV is available as an In-app purcahse.

## User Feedback via Google Sheet

I added an option for users to provide feedback directly through a form that populates a Google Sheet. This makes it easier to collect and analyse user opinions for future improvements.

## Conclusion

Revamping my hobby app was a rewarding experience. Not only did it get a visual upgrade, but it also gave exposure to analytics integration, Unit and UI testing, refactoring etc. Hope this post gives you some insights and inspiration for your own app development journey.

You can check out the [Easy Split App](https://apps.apple.com/in/app/expensesplit/id1041478586?platform=iphone)
