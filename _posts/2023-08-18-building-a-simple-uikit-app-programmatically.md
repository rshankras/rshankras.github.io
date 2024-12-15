---
title: "Building a Simple UIKit App Programmatically"
date: "2023-08-18"
categories: 
  - "swift"
  - "uikit"
---

In this tutorial, we'll build a simple app called "QuickTabs" using UIKit, featuring a tab bar controller and a settings screen. This approach gives you more control over your app's structure and is great for working in teams. Let's get started!

## Prerequisites

- Xcode installed on your Mac

- Basic knowledge of Swift and iOS development

## Step 1: Project Setup

1. Open Xcode and create a new iOS app project.

3. Choose "App" as the template.

5. Name your project "QuickTabs".

7. In the interface dropdown, select "Storyboard" (we'll remove it later).

9. Click "Create".

## Step 2: Remove Storyboard

1. Delete the `Main.storyboard` file from your project.

3. In your project settings, go to the "Info" tab.

5. Delete the "Main storyboard file base name" entry.

7. In the "Deployment Info" section, clear the "Main Interface" field.

9. Delete the Scene Delegate and Application Scene Manifest property under Info file as we are not using Scene Delegate or support for Multiple Windows.

## Step 3: Set Up the App Delegate

Replace the contents of `AppDelegate.swift` with the following code:

```swift
import UIKit

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

    var window: UIWindow?

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        window = UIWindow(frame: UIScreen.main.bounds)
        window?.makeKeyAndVisible()

        let tabBarController = UITabBarController()

        let homeVC = HomeViewController()
        homeVC.tabBarItem = UITabBarItem(title: "Home", image: UIImage(systemName: "house"), tag: 0)

        let settingsVC = SettingsViewController()
        settingsVC.tabBarItem = UITabBarItem(title: "Settings", image: UIImage(systemName: "gear"), tag: 1)

        tabBarController.viewControllers = [homeVC, settingsVC]

        window?.rootViewController = tabBarController

        return true
    }
}
```

This sets up our app's main window and creates a tab bar controller with two tabs: Home and Settings.

## Step 4: Create the Home View Controller

Create a new file called `HomeViewController.swift` and add the following code:

```swift
import UIKit

class HomeViewController: UIViewController {

    private let welcomeLabel: UILabel = {
        let label = UILabel()
        label.text = "Welcome to SuperApp!"
        label.font = UIFont.systemFont(ofSize: 24, weight: .bold)
        label.textAlignment = .center
        label.translatesAutoresizingMaskIntoConstraints = false
        return label
    }()

    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .white
        setupUI()
    }

    private func setupUI() {
        view.addSubview(welcomeLabel)

        NSLayoutConstraint.activate([
            welcomeLabel.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            welcomeLabel.centerYAnchor.constraint(equalTo: view.centerYAnchor)
        ])
    }
}
```

This creates a simple home screen with a welcome message.

## Step 5: Create the Settings View Controller

Create another new file called `SettingsViewController.swift` and add the following code:

```swift
import UIKit

class SettingsViewController: UIViewController {

    private let settingsLabel: UILabel = {
        let label = UILabel()
        label.text = "Settings"
        label.font = UIFont.systemFont(ofSize: 24, weight: .bold)
        label.textAlignment = .center
        label.translatesAutoresizingMaskIntoConstraints = false
        return label
    }()

    private let darkModeSwitch: UISwitch = {
        let switch_ = UISwitch()
        switch_.translatesAutoresizingMaskIntoConstraints = false
        return switch_
    }()

    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .white
        setupUI()
    }

    private func setupUI() {
        view.addSubview(settingsLabel)
        view.addSubview(darkModeSwitch)

        NSLayoutConstraint.activate([
            settingsLabel.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            settingsLabel.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 20),

            darkModeSwitch.topAnchor.constraint(equalTo: settingsLabel.bottomAnchor, constant: 20),
            darkModeSwitch.centerXAnchor.constraint(equalTo: view.centerXAnchor)
        ])

        darkModeSwitch.addTarget(self, action: #selector(darkModeSwitchValueChanged), for: .valueChanged)
    }

    @objc private func darkModeSwitchValueChanged() {
        if darkModeSwitch.isOn {
            view.backgroundColor = .darkGray
            settingsLabel.textColor = .white
        } else {
            view.backgroundColor = .white
            settingsLabel.textColor = .black
        }
    }
}
```

This creates a settings screen with a switch to toggle dark mode.

## Step 6: Build and Run

You should now be able to build and run your app. You'll see a tab bar with two options: Home and Settings. The Home tab will show your welcome message, and the Settings tab will have a switch to toggle dark mode.

## Conclusion

Congratulations! You've built a simple iOS app programmatically using UIKit. This project has introduced you to several important concepts:

1. Setting up an app without a storyboard

3. Using UITabBarController for navigation

5. Creating view controllers programmatically

7. Using Auto Layout for UI design

9. Implementing basic user interactions
