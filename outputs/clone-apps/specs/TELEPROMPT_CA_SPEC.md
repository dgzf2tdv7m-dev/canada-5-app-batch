# TelePrompt CA - SwiftUI iOS 26+ Implementation Spec

## Product Positioning

TelePrompt CA is a premium bilingual teleprompter for Canadian creators, executives, educators, journalists, podcasters, legal professionals, and public speakers. It should feel like a reliable studio tool: fast script setup, calm reading controls, precise pacing, and exportable rehearsal notes without subscriptions or cloud dependence.

Paid app promise: one purchase, private scripts, polished prompting on iPhone and iPad.

Primary languages: English and French. Default language follows system locale, with an in-app override.

## Core Screens

1. Library
   - Script list with search, tags, language filter, last practiced date, and estimated read time.
   - Quick actions: New Script, Import, Paste, Scan Text, Start Prompt.
   - Empty state focused on creation, not onboarding marketing.

2. Script Editor
   - Rich plain-text editor optimized for speeches.
   - Controls for title, language, tags, target duration, section breaks, speaker notes, and cue markers.
   - Word count, estimated duration, and pace indicator.
   - Import from Files, clipboard, plain text, PDF text extraction where feasible, and camera OCR if supported.

3. Prompt Stage
   - Full-screen teleprompter with adjustable speed, font size, margins, line height, mirror mode, countdown, and focus guide.
   - Tap zones: left slow down, right speed up, center play/pause.
   - Remote-ready controls via keyboard shortcuts and external display support where feasible.
   - Orientation support: portrait, landscape, iPad split screen.

4. Rehearsal
   - Timed practice sessions with actual duration, words per minute, pauses, and take notes.
   - Compare target vs actual pacing.
   - Save rehearsal history per script.

5. Settings
   - Appearance, default prompt style, language, privacy, export options, storage management, support, and legal.
   - No account requirement.

## Core Features

- Offline-first local script storage using SwiftData.
- Bilingual English/French UI.
- Script folders/tags for speeches, video, podcast, class, courtroom, client, and personal.
- Adjustable prompting speed from very slow to fast, represented as WPM and slider value.
- Mirror mode for beam-splitter rigs.
- Focus line, dim surrounding text, optional safe-area margins.
- Countdown timer and elapsed/remaining time.
- Rehearsal analytics: target time, actual time, average WPM, completion percentage.
- iCloud Drive import/export through system document picker only; no proprietary cloud sync required.
- Export as TXT, PDF rehearsal sheet, and share sheet text.
- Accessibility: Dynamic Type-friendly controls, VoiceOver labels, high contrast mode, reduced motion support, keyboard shortcuts.
- Paid-app polish: no ads, no trackers, no account wall.

## Navigation Model

- iPhone: `NavigationStack` Library -> Editor -> Prompt Stage / Rehearsal.
- iPad: `NavigationSplitView` with Library sidebar, script detail/editor, and modal/full-screen Prompt Stage.
- Prompt Stage should use a separate immersive route with hidden chrome and gesture-first controls.

## English UI Strings

- App name: TelePrompt CA
- New Script
- Import Script
- Paste Text
- Start Prompt
- Rehearse
- Edit Script
- Mirror Mode
- Focus Line
- Countdown
- Speed
- Font Size
- Margins
- Line Height
- Estimated Time
- Target Time
- Actual Time
- Words Per Minute
- Save Take
- Practice History
- Export
- Share Script
- No Scripts Yet
- Create your first script or import text from Files.
- Scripts stay on this device unless you choose to share or export them.
- Language
- English
- French
- System Default
- Support
- Privacy
- Restore Purchase

## French UI Strings

- Nom de l'app : TelePrompt CA
- Nouveau texte
- Importer un texte
- Coller le texte
- Lancer le prompteur
- Repeter
- Modifier le texte
- Mode miroir
- Ligne de focus
- Compte a rebours
- Vitesse
- Taille du texte
- Marges
- Interligne
- Duree estimee
- Duree cible
- Duree reelle
- Mots par minute
- Enregistrer la prise
- Historique des repetitions
- Exporter
- Partager le texte
- Aucun texte
- Creez votre premier texte ou importez du contenu depuis Fichiers.
- Vos textes restent sur cet appareil sauf si vous choisissez de les partager ou de les exporter.
- Langue
- Anglais
- Francais
- Reglage du systeme
- Assistance
- Confidentialite
- Restaurer l'achat

Note: Use proper localized strings with accents in `Localizable.xcstrings`; ASCII here is intentional for broad tooling safety.

## iPhone Screenshot Scenes

1. Title: Your Scripts, Ready Fast
   - Copy: Draft, import, tag, and launch speeches from one clean library.

2. Title: Write With Timing Built In
   - Copy: See word count, target duration, and reading pace while you edit.

3. Title: A Studio Prompting View
   - Copy: Adjust speed, size, margins, focus line, and mirror mode in seconds.

4. Title: Practice Before You Record
   - Copy: Track actual time, words per minute, and saved rehearsal takes.

5. Title: Private By Design
   - Copy: No accounts, no ads, no tracking. Your scripts stay with you.

## iPad Screenshot Scenes

1. Title: A Full Teleprompter Desk
   - Copy: Browse scripts, edit details, and prepare your next take on a wider canvas.

2. Title: Spacious Script Editing
   - Copy: Organize long speeches with notes, sections, tags, and target timing.

3. Title: Landscape Prompting
   - Copy: Run a clean, readable prompter view for studio, classroom, and stage setups.

4. Title: Rehearsal History
   - Copy: Compare takes and refine your delivery before the final recording.

5. Title: Built For Canadian Workflows
   - Copy: English and French controls for creators, teams, educators, and speakers.

## App Store Metadata

Name:
TelePrompt CA

Subtitle, <= 30 chars:
Bilingual Teleprompter

Promotional Text:
A private, paid teleprompter for Canadian creators and speakers. Write, rehearse, mirror, and present scripts in English or French without ads, accounts, or tracking.

Description:
TelePrompt CA turns your iPhone or iPad into a focused bilingual teleprompter for speeches, videos, podcasts, lessons, presentations, and client work.

Write or import a script, set your target duration, then start a clean prompting view with adjustable speed, font size, margins, line height, countdown, focus line, and mirror mode. Rehearsal tools help you compare your target time with your actual delivery so you can tighten every take before recording or presenting.

TelePrompt CA is built for privacy and speed. Scripts are stored locally on your device unless you choose to export or share them. There are no ads, no account requirements, and no tracking.

Features:
- English and French interface
- Full-screen teleprompter for iPhone and iPad
- Mirror mode for prompter rigs
- Adjustable speed, text size, margins, and line height
- Countdown and elapsed time
- Script library with tags and search
- Target duration and estimated reading time
- Rehearsal history with actual time and WPM
- Import, export, and share scripts
- Offline-first private storage

TelePrompt CA is a one-time paid app for people who want a polished prompting tool without subscriptions or distractions.

Keywords:
teleprompter,prompter,script,speech,video,podcast,rehearsal,mirror,creator,presentation,Canada,French,English

Category:
Productivity

Secondary Category:
Photo & Video

Age Rating:
4+

## Privacy Page Copy

TelePrompt CA is designed to keep your scripts private.

We do not require an account. We do not show ads. We do not use third-party tracking SDKs. Your scripts, notes, tags, and rehearsal history are stored locally on your device unless you choose to share, export, or import files through Apple system services.

If you use system features such as Files, Share Sheet, document import, or camera-based text capture, those actions are handled through Apple-provided frameworks and your selected destinations.

Data stored by the app:
- Script titles and body text
- Tags, language choice, and formatting preferences
- Rehearsal timing history
- App settings

Data not collected by us:
- Personal identity
- Contact information
- Precise location
- Browsing history
- Advertising identifiers
- Analytics for tracking across apps or websites

To delete app data, delete individual scripts in the app or remove TelePrompt CA from your device.

## Support Page Copy

Need help with TelePrompt CA?

Common fixes:
- If text scrolls too quickly, lower Speed or set a longer Target Time.
- If the prompter looks reversed, turn Mirror Mode off unless you are using a reflective teleprompter rig.
- If the text is hard to read, increase Font Size, Line Height, or Margins.
- If imported text looks unusual, paste it into a new script as plain text and reformat section breaks.

Contact support:
Email: support@example.com

When contacting support, include your device model, iOS or iPadOS version, app version, and a short description of the issue. Do not send private scripts unless you intentionally choose to share them.

## Visual Design Tokens

Design direction:
Quiet Canadian studio utility. Clear contrast, professional typography, calm controls, no decorative clutter.

Color tokens:
- `color.background`: `#F7F8F6`
- `color.surface`: `#FFFFFF`
- `color.surfaceMuted`: `#EEF1EE`
- `color.textPrimary`: `#151816`
- `color.textSecondary`: `#59615B`
- `color.accent`: `#C9282D`
- `color.accentDark`: `#8F1D22`
- `color.blueUtility`: `#1E5B8F`
- `color.success`: `#2F7D4F`
- `color.warning`: `#B66A00`
- `color.border`: `#D8DDD8`
- `color.promptBlack`: `#050505`
- `color.promptWhite`: `#F7F7F2`

Typography:
- Use SF Pro for UI.
- Prompt text defaults to SF Pro Rounded or system serif option, user selectable.
- Library title: 28 semibold.
- Section title: 17 semibold.
- Body: 15 regular.
- Utility labels: 12 medium.
- Prompt text default: 42 regular on iPhone, 56 regular on iPad.

Spacing:
- Base grid: 4.
- Screen margin iPhone: 16.
- Screen margin iPad: 24.
- Control gap: 8.
- Panel gap: 16.
- Toolbar height: 52.
- Minimum touch target: 44.

Shape:
- Small radius: 6.
- Card/list radius: 8.
- Prompt controls radius: 8.
- Avoid large pill-heavy styling except for segmented controls.

Motion:
- Use subtle spring for panel presentation.
- Prompt scrolling must be linear and stable.
- Respect Reduce Motion by disabling animated transitions except essential scroll movement.

Iconography:
- Use SF Symbols or lucide-equivalent where available:
  - plus, doc, square.and.arrow.down, play.fill, pause.fill, speedometer, textformat.size, arrow.left.and.right, timer, line.3.horizontal.decrease, magnifyingglass, tag, gearshape.

## Implementation Notes

- Minimum target: iOS 26, iPadOS 26.
- Architecture: SwiftUI + SwiftData + Observation.
- Localization: `Localizable.xcstrings` for English and French.
- Data models:
  - `Script`: id, title, body, language, tags, createdAt, updatedAt, targetDurationSeconds, promptStyleId.
  - `PromptStyle`: id, fontSize, lineHeight, margins, speedWPM, mirrorMode, focusLineEnabled, theme.
  - `RehearsalTake`: id, scriptId, startedAt, actualDurationSeconds, averageWPM, completionPercent, notes.
- Prompt engine:
  - Use a deterministic timer or display-linked scroll model.
  - Convert WPM to points-per-second using measured text layout height and total estimated reading time.
  - Persist last used prompt style per script.
- Testing priorities:
  - Localization completeness.
  - Prompt scroll accuracy at multiple font sizes.
  - Mirror mode transform and safe-area behavior.
  - iPad split view and landscape prompting.
  - SwiftData migration with sample scripts.

## Non-Goals For V1

- Social posting integrations.
- Cloud account system.
- AI script writing.
- Video recording inside the app.
- Team collaboration.
- Subscription gating.
