---
title: "Case study: seven years as the mobile engineer for a sailing software company"
layout: single
permalink: /work/club-operations/
author_profile: true
toc: true
toc_sticky: true
description: "How a small paid pilot became seven years as lead iOS developer for Club Operations: the Sailor apps, 18,500+ installs, the race system used by more Australian sailing clubs than any other, and a clean handover after the company's sale."
keywords: "iOS case study, sailing app, Sailor app, lead iOS developer, mobile product, remote team, app handover, Club Operations"
---

- **Client:** Club Operations, Australia: sailing results and club management software. Acquired by Northstar Technologies in 2023
- **My role:** Lead iOS Developer and Product Manager (Mobile Apps). First employee
- **Apps:** Sailor (for sailors), Sailing Official (for race officers) and Sailing Club, on iOS and Android, plus white-label versions
- **Engagement:** a small paid pilot in Jan 2016, full time from Aug 2016 to Jul 2023, then a handover contract with Northstar until Feb 2024

## The starting point

Club Operations was a small, owner-led business. The owner knew the sport and had built the web system that clubs used to run their racing. What the business needed next was mobile apps for three very different users (sailors, race officers and club administrators), and someone to own that engineering for the long term.

It started on Upwork with a small paid pilot. A second small project followed, and a few months later I joined full time as the company's first employee.

## What I built and owned

- **The iOS apps:** Sailor, Sailing Official and Sailing Club, with a shared Swift framework underneath all three so fixes and features reached every app at once.
- **Android:** I took over Android from a contractor, built two of the Android apps myself, then hired an Android developer and reviewed all of their work before each release.
- **Product:** I turned the owner's knowledge of how clubs and race officers work into requirements the team could build from, and ran testing for every release.
- **The team:** a three-person remote team in Chennai covering iOS, Android and the .NET backend. I ran sprints and daily stand-ups, moved the team to Git and pull requests, and handled the App Store releases.

## Features clubs relied on

- **Race entry and sign-on from the phone.** During 2020, sailors signed on and off for races from their own phones and race officers saw each boat's status live, with no shared paper sheet.
- **Swipe-to-finish.** Race officers record finishes with a swipe on the committee boat's iPad. One officer finished a fleet of 55+ boats in a single race; at one regatta with three events running at once, results were out within about 30 seconds of the last finisher.
- **No passwords.** Phone-number verification, so members and officials never had to remember a password.
- **Payments.** I led the choice of Stripe for online race entry and ran its QA and release.
- **White-label apps** for other sailing classes, built as separate targets from the same code. Laser 2020 reached 2,500+ monthly users during the Laser World Championships.

## Engineering stories

- **A crash nobody could reproduce.** Some users crashed on launch and no one could make it happen. I traced it to phones set to 24-hour time (a date-parsing problem), confirmed it on a device and shipped a fix.
- **Built for bad signal.** Sailors and officials use the apps at the water's edge. I tested all three apps with no network and with poor network, found that the connection check didn't handle a weak signal, and fixed it, then had the Android app put through the same tests.
- **Reproduce first, then fix.** When a sign-on problem appeared on Android, I argued for reproducing it before rolling back, because the older version might have had the same bug. We found the real cause and fixed forward.

## Results

- **18,500+ installs** of Sailor across iOS and Android by February 2023, with a peak of **2,700+ monthly active users**.
- **By December 2022, more Australian sailing clubs used Sailor than any other race system**: 62 clubs by March 2023.
- Seven years of regular releases, with the owner free to focus on clubs and the product while the mobile engineering was handled.

## A clean handover

When Northstar Technologies acquired the business in 2023, I ran the product demos for the buyer and trained the new team on the whole system: the apps, payments, race setup and releases. I then supported the product under Northstar until February 2024, and added biometric login to their ClubNow iOS app.

## What this means for your product

- **Ownership:** one engineer who takes responsibility for your mobile product, not just a list of tickets.
- **Learning your domain:** I learn how your users actually work and turn it into requirements and software.
- **Continuity:** I stay for years, and when it's time, I leave a product that another team can take over.

The apps are on the App Store: [Sailor](https://apps.apple.com/au/app/sailor/id1094179490), [Sailing Official](https://apps.apple.com/au/app/sailing-official/id1207760372) and [Sailing Club](https://apps.apple.com/au/app/sailing-club/id1207760571).

<a class="svc-btn svc-btn--primary" href="/services/">Have a product that needs an engineer like this? Let's talk →</a>
