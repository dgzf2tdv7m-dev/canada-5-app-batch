# ExamCards CA Implementation Spec

## Product Positioning

ExamCards CA is a premium iOS 26+ SwiftUI study app for Canadian learners who need polished flashcards for exams, certifications, language courses, and school review. The paid-app promise is simple: no ads, no account requirement, no subscriptions, private offline-first study with bilingual English/French UI.

Primary audiences:
- Canadian high school, college, and university students.
- Adult learners preparing for licensing, workplace, language, or citizenship-style exams.
- Parents/tutors who want a clean, local-first card tool without analytics-heavy clutter.

Core value:
- Fast card creation, spaced review, quiz modes, and progress clarity.
- English/French interface, with per-deck language labels.
- Local-first privacy, iCloud sync optional.

## Core Features

- Deck library with pinned decks, folders, search, tags, due counts, and progress rings.
- Card editor with front/back fields, hint, explanation, image attachment, accent/subject color, language label, and optional multiple-choice answers.
- Study modes: Flip Cards, Learn, Quiz, Type Answer, Cram, and Due Review.
- Lightweight spaced repetition using `new`, `learning`, `review`, and `mastered` states.
- Import/export: CSV, TSV, plain text, and shareable `.examcards` package.
- Bilingual UI: English and Canadian French. App content remains user-authored.
- iCloud sync toggle, local backup export, and device-only mode.
- Widgets/Live Activities are out of scope for v1 unless required later.

## SwiftUI App Structure

- Minimum target: iOS 26.0 and iPadOS 26.0.
- Language: Swift 6.
- UI framework: SwiftUI with NavigationSplitView for iPad and NavigationStack for iPhone.
- Persistence: SwiftData local store, optional CloudKit-backed sync.
- Localization: `Localizable.xcstrings` with `en-CA` and `fr-CA`.
- Accessibility: Dynamic Type, VoiceOver labels for card state/progress, Reduce Motion support.

Primary tabs:
- Library
- Review
- Create
- Progress
- Settings

## Core Screens

### Onboarding

Purpose: Set language, study goal, and privacy preference.

Controls:
- Language picker: English / Français.
- Daily goal stepper: 5, 10, 20, 40 cards.
- Sync choice: This Device Only / Use iCloud.
- Import sample deck button.

### Library

Purpose: Manage decks and start sessions quickly.

Elements:
- Search field.
- Filter chips: All, Due, Pinned, Recent, Mastered.
- Deck rows with title, subject color, card count, due count, progress ring, last studied date.
- Toolbar actions: import, new folder, new deck.

### Deck Detail

Purpose: Inspect a deck and choose a study action.

Elements:
- Header with deck name, subject, card count, due count, mastery percent.
- Primary action: Study Due.
- Secondary actions: Flip, Quiz, Cram, Edit.
- Card list with status badges and quick edit.

### Card Editor

Purpose: Create and refine cards with minimal friction.

Fields:
- Front
- Back
- Hint
- Explanation
- Tags
- Language
- Image
- Multiple-choice options

Actions:
- Save
- Save and Add Another
- Duplicate
- Delete

### Study Session

Purpose: Focused card review.

Interaction:
- Tap or swipe to flip.
- Grade controls: Again, Hard, Good, Easy.
- Optional typed-answer field.
- Session progress bar and remaining count.
- Pause menu with Resume Later, Restart, End Session.

### Quiz Mode

Purpose: Test recall with immediate feedback.

Question types:
- Multiple choice.
- True/false when generated from card metadata.
- Typed answer.

Results:
- Correct count.
- Missed cards.
- Retry missed.
- Add missed to Cram.

### Progress

Purpose: Show the user where effort is working.

Metrics:
- Daily goal streak.
- Cards reviewed this week.
- Mastery by deck.
- Due forecast for next 7 days.
- Weak tags.

### Settings

Purpose: Privacy, language, data, and support.

Options:
- App language.
- Daily goal.
- iCloud sync.
- Export all data.
- Import backup.
- Privacy Policy.
- Support.
- Rate ExamCards CA.

## English/French UI Strings

| Key | English `en-CA` | French `fr-CA` |
| --- | --- | --- |
| app_name | ExamCards CA | ExamCards CA |
| tab_library | Library | Bibliotheque |
| tab_review | Review | Revision |
| tab_create | Create | Creer |
| tab_progress | Progress | Progres |
| tab_settings | Settings | Reglages |
| onboarding_title | Study your way, privately. | Etudiez a votre facon, en prive. |
| onboarding_language | App Language | Langue de l'app |
| onboarding_goal | Daily Goal | Objectif quotidien |
| onboarding_sync | Sync Option | Option de synchronisation |
| device_only | This Device Only | Cet appareil seulement |
| use_icloud | Use iCloud | Utiliser iCloud |
| continue_button | Continue | Continuer |
| new_deck | New Deck | Nouveau paquet |
| import_deck | Import Deck | Importer un paquet |
| search_decks | Search decks | Rechercher des paquets |
| filter_all | All | Tous |
| filter_due | Due | A reviser |
| filter_pinned | Pinned | Epingles |
| filter_recent | Recent | Recents |
| filter_mastered | Mastered | Maitrises |
| cards_count | %d cards | %d cartes |
| due_count | %d due | %d a reviser |
| study_due | Study Due | Reviser maintenant |
| flip_cards | Flip Cards | Cartes a retourner |
| quiz | Quiz | Quiz |
| cram | Cram | Revision intensive |
| edit | Edit | Modifier |
| front | Front | Recto |
| back | Back | Verso |
| hint | Hint | Indice |
| explanation | Explanation | Explication |
| tags | Tags | Etiquettes |
| language | Language | Langue |
| add_image | Add Image | Ajouter une image |
| save | Save | Enregistrer |
| save_add | Save and Add Another | Enregistrer et ajouter |
| delete | Delete | Supprimer |
| again | Again | Encore |
| hard | Hard | Difficile |
| good | Good | Bien |
| easy | Easy | Facile |
| type_answer | Type your answer | Tapez votre reponse |
| show_answer | Show Answer | Afficher la reponse |
| correct | Correct | Correct |
| try_again | Try Again | Reessayer |
| session_complete | Session Complete | Session terminee |
| reviewed_today | Reviewed Today | Revisees aujourd'hui |
| weekly_review | Weekly Review | Revision hebdomadaire |
| weak_tags | Weak Tags | Etiquettes faibles |
| export_data | Export All Data | Exporter toutes les donnees |
| import_backup | Import Backup | Importer une sauvegarde |
| privacy_policy | Privacy Policy | Politique de confidentialite |
| support | Support | Assistance |

Note: French strings are ASCII-safe for implementation handoff. Final `fr-CA` copy may restore accents in localized resources if the project standard allows non-ASCII.

## iPhone Screenshot Scenes

1. Library Ready
   - Title: All your exam decks, organized
   - Copy: Pin key subjects, see due cards, and start reviewing in seconds.

2. Fast Card Creation
   - Title: Build cards without friction
   - Copy: Add hints, explanations, tags, images, and bilingual labels.

3. Focused Review
   - Title: Review what matters today
   - Copy: Flip, grade, and move through a clean distraction-free session.

4. Quiz Yourself
   - Title: Turn cards into practice tests
   - Copy: Multiple choice and typed answers help expose weak spots.

5. Private Progress
   - Title: Track mastery privately
   - Copy: See streaks, weak tags, and deck progress without an account.

French variants:
1. Title: Tous vos paquets d'examen
   - Copy: Epinglez les matieres importantes et commencez vite.
2. Title: Creez des cartes rapidement
   - Copy: Ajoutez indices, explications, images et etiquettes bilingues.
3. Title: Revisez ce qui compte
   - Copy: Retournez, evaluez et avancez sans distraction.
4. Title: Transformez vos cartes en quiz
   - Copy: Questions a choix et reponses tapees revelent vos lacunes.
5. Title: Suivez vos progres en prive
   - Copy: Series, etiquettes faibles et maitrise, sans compte.

## iPad Screenshot Scenes

1. Split Library
   - Title: A full study command centre
   - Copy: Browse decks, inspect progress, and launch review from one iPad layout.

2. Deck Detail Workspace
   - Title: See every card and every gap
   - Copy: Review due counts, mastery, tags, and card status side by side.

3. Card Builder
   - Title: Create richer study material
   - Copy: Use the larger canvas for explanations, images, and answer options.

4. Review Focus
   - Title: Big-screen recall practice
   - Copy: Spacious cards, clear grading, and keyboard-friendly typed answers.

5. Progress Dashboard
   - Title: Know where to study next
   - Copy: Weekly volume, weak tags, and deck mastery guide your next session.

French variants:
1. Title: Un centre d'etude complet
   - Copy: Parcourez, comparez et lancez vos revisions sur iPad.
2. Title: Chaque carte, chaque lacune
   - Copy: Voyez echeances, maitrise, etiquettes et statut cote a cote.
3. Title: Creez du contenu plus riche
   - Copy: Profitez du grand ecran pour images, explications et options.
4. Title: Pratique de rappel grand format
   - Copy: Cartes spacieuses, evaluation claire et reponses au clavier.
5. Title: Sachez quoi reviser ensuite
   - Copy: Volume, lacunes et maitrise guident la prochaine session.

## App Store Metadata

Name:
- ExamCards CA

Subtitle, <=30 characters:
- Private Exam Flashcards

Promotional Text:
- Study Canadian exam material with private, bilingual flashcards built for focused review.

Description:
ExamCards CA is a premium flashcard app for focused exam study in Canada. Build clean decks for school, licensing, language learning, workplace training, or personal review, then study with flip cards, quizzes, typed answers, and due-review sessions.

Create cards with hints, explanations, tags, images, and optional multiple-choice answers. Organize decks by subject, pin the material that matters, and use progress views to see which topics need more attention.

ExamCards CA is designed for privacy. You can study fully on device, export your data, and choose whether to use iCloud sync. There are no ads, no required account, and no subscription.

Designed for iPhone and iPad with English and French interface options.

Keywords:
- flashcards,exam,study,cards,quiz,revision,school,college,university,canada,french,english,spaced,learning,test

Category:
- Education

Price model:
- Paid upfront. No ads. No subscription for v1.

In-App Purchases:
- None for v1.

## Privacy Page Copy

Title: Privacy Policy

ExamCards CA is designed to keep your study data under your control.

What you create:
Your decks, cards, tags, images, quiz results, and progress are stored on your device. If you enable iCloud sync, Apple syncs supported app data through your iCloud account so it can appear on your devices.

No required account:
ExamCards CA does not require you to create an app account.

No advertising:
ExamCards CA does not show third-party ads and does not sell personal data.

Diagnostics:
If Apple crash diagnostics are enabled on your device, Apple may provide anonymized crash information to help improve app stability.

Data export and deletion:
You can export your study data from Settings. You can delete decks inside the app, or remove all app data by deleting ExamCards CA from your device and iCloud storage if iCloud sync was enabled.

Contact:
For privacy questions, contact support at support@example.com.

French summary:
ExamCards CA conserve vos donnees d'etude sous votre controle. L'app ne demande pas de compte, n'affiche pas de publicites et ne vend pas vos donnees personnelles. Vos cartes restent sur l'appareil, sauf si vous activez la synchronisation iCloud.

## Support Page Copy

Title: ExamCards CA Support

Need help with ExamCards CA? We can help with imports, exports, iCloud sync, deck recovery, accessibility, and general app questions.

Before contacting support:
- Check that you are using the latest App Store version.
- If sync is enabled, confirm that iCloud Drive is available on each device.
- Export a backup before making large deck changes.

Contact:
- Email: support@example.com
- Response target: 2 business days.

Please include:
- Device model.
- iOS or iPadOS version.
- App version.
- A brief description of the issue.

French summary:
Pour obtenir de l'aide, envoyez un courriel a support@example.com avec votre modele d'appareil, la version iOS ou iPadOS, la version de l'app et une courte description du probleme.

## Visual Design Tokens

Design direction:
- Premium academic utility.
- Calm, precise, trustworthy.
- Avoid childish school motifs and loud gamification.

Color tokens:
- `color.background`: `#F7F7F3`
- `color.surface`: `#FFFFFF`
- `color.surfaceAlt`: `#ECEFE8`
- `color.textPrimary`: `#1C211B`
- `color.textSecondary`: `#5B6357`
- `color.border`: `#D9DED2`
- `color.accent`: `#0E7C66`
- `color.accentPressed`: `#095E4D`
- `color.warning`: `#B66A00`
- `color.success`: `#247A3D`
- `color.error`: `#B43A32`
- `color.subjectBlue`: `#2C6FA3`
- `color.subjectRed`: `#B64C4C`
- `color.subjectGold`: `#C7922B`
- `color.subjectViolet`: `#7357A6`

Typography:
- System font: SF Pro.
- Large title: 34 pt, semibold.
- Screen title: 28 pt, semibold.
- Section title: 17 pt, semibold.
- Body: 16 pt, regular.
- Caption: 13 pt, regular.
- Monospaced answer preview: SF Mono 15 pt.

Spacing:
- `space.1`: 4
- `space.2`: 8
- `space.3`: 12
- `space.4`: 16
- `space.5`: 24
- `space.6`: 32

Radius:
- `radius.small`: 6
- `radius.medium`: 8
- `radius.large`: 12
- `radius.card`: 8

Layout:
- iPhone content margin: 16.
- iPad content margin: 24.
- Deck row height: 76.
- Study card aspect ratio: 4:3 on iPhone, 16:10 on iPad.
- Toolbar icon button: 44 x 44.

Motion:
- Card flip: 220 ms, easeInOut.
- Progress updates: 180 ms, easeOut.
- Respect Reduce Motion by switching flips to opacity transitions.

Iconography:
- Use SF Symbols.
- Deck: `rectangle.stack`
- Due review: `clock.badge.checkmark`
- Quiz: `checklist`
- Create: `plus.square`
- Progress: `chart.line.uptrend.xyaxis`
- Settings: `gearshape`
- Import: `square.and.arrow.down`
- Export: `square.and.arrow.up`

## Data Model

Deck:
- `id`
- `title`
- `subject`
- `colorToken`
- `isPinned`
- `createdAt`
- `updatedAt`
- `lastStudiedAt`

Card:
- `id`
- `deckID`
- `front`
- `back`
- `hint`
- `explanation`
- `tags`
- `languageCode`
- `imageAssetID`
- `choiceOptions`
- `correctChoiceIndex`
- `reviewState`
- `easeFactor`
- `dueAt`
- `createdAt`
- `updatedAt`

ReviewEvent:
- `id`
- `cardID`
- `deckID`
- `grade`
- `mode`
- `reviewedAt`
- `responseSeconds`

## V1 Acceptance Criteria

- User can create, edit, delete, import, export, and study decks without an account.
- All listed UI strings exist in English and French.
- iPhone and iPad layouts are native, not stretched versions of the same screen.
- Study sessions update due dates and mastery states.
- Progress dashboard reflects stored review events.
- Privacy/support pages are reachable from Settings.
- App remains functional with iCloud sync disabled.
