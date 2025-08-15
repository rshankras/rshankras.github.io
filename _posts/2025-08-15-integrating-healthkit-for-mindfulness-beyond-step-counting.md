---
title: "Integrating HealthKit for Mindfulness: Beyond Step Counting"
date: "2025-08-15"
description: "How ChantFlow uses HealthKit to reflect calm through Mindful Minutes, heart rate, and HRV (experimental) — with simple Swift snippets you can reuse."
categories:
  - "watchos"
  - "healthkit"
  - "accessibility"
  - "design"
tags:
  - "HealthKit"
  - "Apple Watch"
  - "mindfulness"
  - "HRV"
  - "Swift"
keywords: "HealthKit mindful minutes, Apple Watch heart rate HRV, watchOS HealthKit example, mindfulness app HealthKit, HRV SDNN, HKWorkoutSession mind and body"
image: "/assets/images/app-icons/chantflow-icon.png"
excerpt_separator: <!--more-->
toc: true
---

Chanting helps you feel calm. Now ChantFlow helps you see it, too. We’ve added gentle HealthKit integration so your Apple Watch can reflect what your body experiences during practice — without turning your wrist into a spreadsheet. See the app here: [ChantFlow](https://www.rshankar.com/chantflow/) and on the App Store: [ChantFlow — Daily Om Practice](https://apps.apple.com/us/app/chantflow-daily-om-practice/id6633438828).<!--more-->

## What’s new
- **Heart rate insights**: See your BPM during and after sessions — today and across the week.
- **Mindful Minutes in Health**: Your sessions are logged to Apple Health as Mindfulness.
- **HRV (experimental)**: Heart Rate Variability appears after a session when conditions are right.
- **Simple Health Insights screen**: Big, readable numbers. Built for quick glances.

## Why this matters
- **Feel it, then see it**: A calm heart rate trend is a gentle nudge to keep going.
- **HRV as a signal, not a score**: It can reflect resilience. We show it when it’s reliable.

## How it works (plain English)
- When you chant, the app quietly starts a health session.
- We read heart rate during the session, summarize after.
- HRV usually becomes available after ending the session and needs 3–5+ minutes of stillness and good sensor contact.
- Your Mindful Minutes are saved to Apple Health (with your permission).

## Tiny code you can use

### Request Health permissions (read HR/HRV, write Mindfulness + Workout)
```swift
import HealthKit

let healthStore = HKHealthStore()

func requestHealthPermissions(completion: @escaping (Bool) -> Void) {
    let toShare: Set = [
        HKObjectType.categoryType(forIdentifier: .mindfulSession)!,
        HKObjectType.workoutType()
    ]
    let toRead: Set = [
        HKObjectType.quantityType(forIdentifier: .heartRate)!,
        HKObjectType.quantityType(forIdentifier: .heartRateVariabilitySDNN)!
    ]
    healthStore.requestAuthorization(toShare: toShare, read: toRead) { ok, _ in
        completion(ok)
    }
}
```

### Log a Mindfulness session to Apple Health
```swift
import HealthKit

func saveMindfulMinutes(start: Date, end: Date, completion: @escaping (Bool) -> Void) {
    let mindful = HKObjectType.categoryType(forIdentifier: .mindfulSession)!
    let sample = HKCategorySample(type: mindful, value: 0, start: start, end: end)
    HKHealthStore().save(sample) { ok, _ in
        completion(ok)
    }
}
```

### (Optional) Start a lightweight workout for live heart rate on watchOS
```swift
import HealthKit

final class LiveHRSession: NSObject, HKWorkoutSessionDelegate {
    private let store = HKHealthStore()
    private var session: HKWorkoutSession?
    private var builder: HKLiveWorkoutBuilder?

    func start() throws {
        let cfg = HKWorkoutConfiguration()
        cfg.activityType = .mindAndBody
        cfg.locationType = .unknown
        let session = try HKWorkoutSession(healthStore: store, configuration: cfg)
        let builder = session.associatedWorkoutBuilder()
        builder.dataSource = HKLiveWorkoutDataSource(healthStore: store, workoutConfiguration: cfg)
        self.session = session
        self.builder = builder
        session.delegate = self
        session.startActivity(with: Date())
        builder.beginCollection(withStart: Date()) { _, _ in }
    }

    func stop(completion: @escaping () -> Void) {
        builder?.endCollection(withEnd: Date()) { _, _ in
            self.session?.end()
            self.builder?.finishWorkout { _, _ in completion() }
        }
    }

    func workoutSession(_ workoutSession: HKWorkoutSession, didChangeTo toState: HKWorkoutSessionState, from fromState: HKWorkoutSessionState, date: Date) {}
    func workoutSession(_ workoutSession: HKWorkoutSession, didFailWithError error: Error) {}
}
```

## Privacy, always
- **You’re in control**: Permissions are requested clearly during onboarding (new users) or at launch (existing users).
- **Minimal data**: We read only what’s needed. We don’t write HRV to Health. We don’t sell or share your data.
- **On‑device first**: Data is handled with care for speed and privacy.

## Accessibility and design
- Big text, clean layout, VoiceOver‑friendly.
- Built for short sessions and quick checks, not deep dives.

## HRV: set the right expectation
- HRV is **experimental**. It often appears after you end a session, and only with steady, still wear for several minutes. Heart rate will show up almost every time — HRV will show up some of the time. That’s normal.

## Tips for better readings
- Wear the watch snugly, above the wrist bone.
- Keep your wrist still during the session.
- Aim for at least 5 minutes if you’re hoping to see HRV.

## What’s next
- Gentle trends over weeks and months.
- Clear, friendly insights like “Your average heart rate during chanting dropped this week.”
- Continued focus on privacy and accessibility.

Start a session, breathe, and take a peek at your Health Insights afterward. Calm feels good — and now you can see it, too.

---

Status: Wrote a complete blog post in simple language, added three concise Swift snippets (permissions, mindful logging, live HR), and clearly labeled HRV as experimental.
