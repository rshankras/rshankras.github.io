---
title: "Privacy Policy - Claudit"
layout: single
permalink: /claudit/privacy/
author_profile: false
---

*Last updated: January 15, 2026*

## Our Commitment to Privacy

Claudit is designed with privacy as a core principle. Your usage data belongs to you and stays on your Mac. This policy explains what information we collect (spoiler: almost nothing) and how we handle your data.

## Information We Collect

### Zero External Data Collection
- **No analytics**: We don't use any analytics services
- **No telemetry**: No usage data is sent anywhere
- **No accounts**: No registration or sign-in required
- **No cloud sync**: The app works entirely on your local machine

## Data Storage

### Your Data Stays Local
- All usage tracking data is stored locally on your Mac using SwiftData
- Token counts, costs, and project usage are stored only on your device
- Your activity data never leaves your computer
- We have no ability to access your data

### What Gets Stored Locally
- Token counts (input, output, cache read/write) from Claude Code session files
- Calculated API costs based on token usage
- Project paths and usage statistics
- Cache efficiency metrics
- Model usage breakdown (Opus, Sonnet, Haiku)
- App preferences and settings

### How Data is Collected
Claudit reads local session files from `~/.claude/projects/*/[session].jsonl` that Claude Code creates during normal operation. These files contain token usage data that Claudit parses to calculate costs.

## Data We Don't Collect

Claudit does NOT track, access, or store:
- Session contents, prompts, or conversations
- Code you write or files you edit
- Personal identification information
- Location data
- Network traffic (except optional Anthropic API quota checks)
- Any data on external servers
- Browsing history or other app usage

## Permissions

Claudit requires these permissions to function:

- **File System Access**: To read Claude Code session files (`~/.claude/projects/`) for token counting
- **Keychain Access**: To securely store your optional Anthropic API key

These permissions are used exclusively for local data processing on your device. No data is transmitted externally except for the optional quota API call described below.

## Anthropic API Usage (Optional)

Claudit can optionally fetch quota information from the Anthropic API to display your current usage limits.

**This is entirely optional and requires you to provide an API key.**

If you choose to enable quota tracking:
- Your API key is stored securely in macOS Keychain (never in plain text)
- Only the Anthropic quota endpoint is called (`https://api.anthropic.com/v1/usage`)
- No usage data is sent to Anthropic—only a request for your current quota status
- Quota data is fetched every 5 minutes and displayed in the menu bar
- You can remove your API key anytime in Settings

## Data Export and Deletion

### Export Your Data
Claudit includes built-in CSV export for all your data:
- **Daily Usage**: Export costs, tokens, and usage by day
- **Project Costs**: Export spending breakdown by project
- **Summary Report**: Export overall statistics

Access export options from the Dashboard toolbar. All exports are saved locally to a location you choose.

### Delete Your Data
- Use "Reset All Data" in Settings to permanently delete all usage history
- Uninstalling the app removes all associated data from your Mac
- Deleting the cache file above also removes all stored data

To completely remove all Claudit data:
```bash
rm -rf ~/Library/Application\ Support/Claudit/
```

## Third-Party Services

Claudit does not integrate with any third-party services except:
- **Anthropic API** (optional, only for quota checking as described above)

We do NOT use:
- Analytics platforms (no Google Analytics, Mixpanel, etc.)
- Crash reporting services (no Sentry, Crashlytics, etc.)
- Cloud storage services
- Social features or sharing
- Advertising networks

## Children's Privacy

Claudit is not directed at children under 13. We do not knowingly collect information from children. Since no data is collected or transmitted, this is not a concern for our app.

## Changes to This Policy

We may update this privacy policy from time to time to reflect changes in the app or legal requirements. Any changes will be posted on this page with an updated revision date.

Significant changes will be communicated through:
- An update to this page with a new "Last updated" date
- Release notes in app updates

## International Users

Claudit is available worldwide. Since all data stays on your local Mac and is never transmitted to servers, international data transfer regulations (like GDPR) are not applicable. Your data never crosses borders because it never leaves your computer.

## Your Rights

Since all data is stored locally on your Mac:
- **Access**: You have full access to all your data at all times
- **Correction**: You can delete and recalculate data using the "Reset" feature
- **Deletion**: You can delete all data instantly via Settings or by uninstalling
- **Portability**: Your data is stored in standard SwiftData format on your device

## Security

We take security seriously:
- **Keychain Storage**: API keys stored using macOS Keychain (industry-standard)
- **No Plain Text Secrets**: No sensitive data stored in plain text
- **Local-Only**: No network transmission of usage data means no interception risk
- **No Server Vulnerabilities**: Since there are no servers, there's no risk of server breaches
- **Open Source Philosophy**: While not currently open source, the app's local-first architecture is transparent

## Contact Us

If you have questions about this privacy policy or Claudit's data practices:

**Email**: [ravi@rshankar.com](mailto:ravi@rshankar.com)

We typically respond within 24-48 hours.

## Summary (TL;DR)

- ✅ All data stays on your Mac
- ✅ No analytics or tracking
- ✅ No accounts or cloud sync
- ✅ API key in Keychain (optional)
- ✅ Delete data anytime
- ✅ No third-party services (except optional Anthropic quota API)
- ✅ You own your data completely

---

**Claudit respects your privacy because your data never leaves your Mac.**
