---
title: "Haptic Feedback in Wellness Apps: Calm, Rhythm‑Aware Experiences on Apple Watch"
date: "2025-08-10"
description: "How we designed haptics in ChantFlow to guide practice without screens: real WatchKit code (WKHapticType), pacing choices, toggles, and best practices."
categories:
  - "watchos"
  - "ios"
  - "design"
  - "accessibility"
tags:
  - "haptics"
  - "WKHapticType"
  - "Apple Watch"
  - "wellness-apps"
  - "SwiftUI"
keywords: "Apple Watch haptics, WKHapticType examples, watchOS haptic feedback, wellness app design, meditation app haptics, tactile UX, accessibility"
image: "/assets/images/app-icons/chantflow-icon.png"
excerpt_separator: <!--more-->
toc: true
---

If you’ve ever felt a gentle tap on your wrist nudging you along—that’s the quiet power of haptics. In wellness apps, haptic feedback turns stillness into guided, meaningful practice.

In [ChantFlow — Daily Om Practice](https://www.rshankar.com/chantflow/) for Apple Watch ([App Store](https://apps.apple.com/us/app/chantflow-daily-om-practice/id6633438828)), we use haptics to mirror moving a mala bead, celebrate milestones, and keep you in flow—eyes up, mind calm. Below is exactly how we implemented it, with real code, pacing choices, and practical tips you can reuse.<!--more-->

## What haptics are (and why they matter)

- Tiny, tactile cues delivered through Apple Watch
- Help you stay present without looking at the screen
- Discreet, accessible, and ideal for meditation/chanting

On watchOS, we trigger haptics with `WKInterfaceDevice.current().play(_:)` using `WKHapticType` such as `.start`, `.stop`, `.directionUp`, `.success`, and `.notification`.

## How ChantFlow uses haptics

- Start cue: a confident start tap with a subtle follow‑up to ground the session
- Every chant: a light tap (`.directionUp`) to simulate moving a bead
- Milestones: a stronger cue every 27 chants (quarter‑mala) via `.notification`
- Goal celebration: a joyful pattern at 108 (success‑success‑lift)
- End cue: a clean stop haptic at session end
- User control: a simple toggle lets you turn haptics on/off anytime

## Real code: haptic triggers

```swift
// Haptic Feedback (Simple System Sounds)
private func triggerMalaHaptic() {
    guard settings?.hapticFeedbackEnabled == true else { return }
    let progress = getTodayProgress()
    WKInterfaceDevice.current().play(.directionUp) // per‑chant tap

    // quarter‑mala milestone (every 27)
    if progress.current % 27 == 0 && progress.current > 0 {
        DispatchQueue.main.asyncAfter(deadline: .now() + 0.1) {
            WKInterfaceDevice.current().play(.notification)
        }
    }
}

private func triggerPracticeStartHaptic() {
    WKInterfaceDevice.current().play(.start)
    DispatchQueue.main.asyncAfter(deadline: .now() + 0.1) {
        WKInterfaceDevice.current().play(.directionUp)
    }
}

private func triggerPracticeEndHaptic() {
    WKInterfaceDevice.current().play(.stop)
}

func triggerGoalCompletedHaptic() {
    WKInterfaceDevice.current().play(.success)
    DispatchQueue.main.asyncAfter(deadline: .now() + 0.2) {
        WKInterfaceDevice.current().play(.success)
    }
    DispatchQueue.main.asyncAfter(deadline: .now() + 0.4) {
        WKInterfaceDevice.current().play(.directionUp)
    }
}
```

## Real code: user toggle in Settings

```swift
Section {
    Toggle("Haptic Feedback", isOn: Binding(
        get: { dataManager.settings?.hapticFeedbackEnabled ?? true },
        set: { newValue in
            dataManager.settings?.hapticFeedbackEnabled = newValue
            try? dataManager.modelContext.save()
        }
    ))
    .tint(.orange)
}
```

## Timing and rhythm

- Keep it subtle: light tap for each chant; stronger cues only at meaningful moments
- Don’t overwhelm: milestones are spaced (every 27) with tiny delays (0.1–0.4s) to avoid overlap
- Stay in flow: non‑blocking, async calls so UI remains smooth
- Match the pace: cadence aligns with user rhythm without being intrusive

## Accessibility benefits

- Screen‑free guidance: practice with eyes closed and full confidence
- Sensory‑friendly: global toggle respects sensitivity and neurodiversity
- Quiet by design: tactile cues work in silent spaces—no sound needed
- Distinct patterns: start, progress, milestone, and success cues feel different

## Best practices we recommend

- Use consistent patterns for start, progress, milestones, success, and end
- Respect user control with a global toggle
- Keep cues brief; avoid “haptic fatigue”
- Layer meaning with timing (light for progress, stronger for milestones)
- Test with different wrist sensitivity levels and in real practice sessions

## Wrap‑up

Thoughtful haptics make wellness experiences feel personal, calm, and intuitive. In ChantFlow, a simple tap keeps your practice moving—no screens, no noise, just presence.

Building for Apple Watch? Treat haptics as your silent guide. Subtle, respectful, rhythm‑aware patterns can lift your app from “useful” to “felt.”

### Learn more
- ChantFlow page: [https://www.rshankar.com/chantflow/](https://www.rshankar.com/chantflow/)
- Download on the App Store: [https://apps.apple.com/us/app/chantflow-daily-om-practice/id6633438828](https://apps.apple.com/us/app/chantflow-daily-om-practice/id6633438828)
