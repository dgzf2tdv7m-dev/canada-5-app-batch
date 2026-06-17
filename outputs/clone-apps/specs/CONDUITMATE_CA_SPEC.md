# ConduitMate CA Implementation Spec

SwiftUI iOS 26+ paid app for Canadian electricians, apprentices, estimators, and site supervisors who need fast conduit fill, bend, voltage-drop, and material planning tools in English and French.

## Product Positioning

- App concept: Professional conduit and raceway field calculator for Canadian electrical work.
- Paid tier: Premium one-time purchase, no account, no ads, no subscription.
- Core promise: Fast CSA/CEC-aligned jobsite calculations with bilingual output, printable/shareable summaries, and offline use.
- Target user: Canadian electrical contractors, industrial maintenance teams, commercial apprentices, forepersons, and estimators.
- Differentiator: Canadian-first units, trade terminology, bilingual UI strings, province-aware note fields, and clean calculation reports.

## Core Features

1. Conduit fill calculator
   - Select conduit type, trade size, conductor insulation, conductor gauge, conductor count, and ambient/project notes.
   - Show fill percentage, remaining capacity, status band, and recommended next trade size.

2. Bend planner
   - Offset, saddle, kick, and 90-degree planning.
   - Inputs for offset height, bend angle, shrink, spacing, take-up, and conduit size.
   - Output marked distances and quick field diagram.

3. Voltage drop estimator
   - Single-phase and three-phase support.
   - Copper/aluminum conductor selection, load current, distance, voltage, and target max drop.
   - Suggest larger gauge when target is exceeded.

4. Material takeoff
   - Build a run list with conduit lengths, fittings, boxes, straps, couplings, conductors, labels, and notes.
   - Export summary as PDF/share sheet text.

5. Job library
   - Save jobs locally with site name, province, room/area, circuit identifier, date, and preferred language.
   - Duplicate previous runs for repeat calculations.

6. Reference tables
   - Offline conduit/conductor reference tables used by calculators.
   - Include a visible disclaimer that users must verify final work against the current Canadian Electrical Code and local authority requirements.

## Core Screens

- Home Dashboard: Recent jobs, quick calculator tiles, active language toggle, and large "New Job" action.
- New Job: Site metadata, province picker, measurement preferences, and default conductor/conduit settings.
- Conduit Fill: Main field calculator with live result card, size recommendation, and add-to-job action.
- Bend Planner: Bend type segmented control, input form, result diagram, and save/share actions.
- Voltage Drop: Circuit settings, conductor options, result comparison, and suggested gauge.
- Material Takeoff: Editable list grouped by conduit, fittings, conductors, and labels.
- Job Report: Bilingual calculation summary, warnings, notes, timestamp, and PDF/share/export actions.
- Reference: Searchable conduit and conductor tables with bookmarks.
- Settings: Language, units, default province, appearance, privacy/support links, and disclaimer acknowledgement.

## English/French UI Strings

| Key | English | French |
| --- | --- | --- |
| app.name | ConduitMate CA | ConduitMate CA |
| nav.home | Home | Accueil |
| nav.jobs | Jobs | Chantiers |
| nav.reference | Reference | Référence |
| nav.settings | Settings | Réglages |
| action.newJob | New Job | Nouveau chantier |
| action.save | Save | Enregistrer |
| action.share | Share | Partager |
| action.exportPDF | Export PDF | Exporter en PDF |
| action.addToJob | Add to Job | Ajouter au chantier |
| action.duplicate | Duplicate | Dupliquer |
| field.siteName | Site Name | Nom du site |
| field.province | Province | Province |
| field.area | Area / Room | Zone / pièce |
| field.circuitId | Circuit ID | ID du circuit |
| calc.conduitFill | Conduit Fill | Remplissage de conduit |
| calc.bendPlanner | Bend Planner | Planificateur de cintrage |
| calc.voltageDrop | Voltage Drop | Chute de tension |
| calc.materialTakeoff | Material Takeoff | Liste de matériel |
| input.conduitType | Conduit Type | Type de conduit |
| input.tradeSize | Trade Size | Dimension nominale |
| input.conductor | Conductor | Conducteur |
| input.gauge | Gauge | Calibre |
| input.quantity | Quantity | Quantité |
| input.length | Length | Longueur |
| input.current | Current | Courant |
| input.voltage | Voltage | Tension |
| result.pass | Within Limit | Dans la limite |
| result.warning | Check Required | Vérification requise |
| result.fail | Exceeds Limit | Dépasse la limite |
| result.fillPercent | Fill Percentage | Pourcentage de remplissage |
| result.remainingCapacity | Remaining Capacity | Capacité restante |
| result.recommendedSize | Recommended Size | Dimension recommandée |
| report.title | Job Report | Rapport de chantier |
| report.generated | Generated | Généré |
| disclaimer.short | Verify all results with the current Canadian Electrical Code and local authority requirements. | Vérifiez tous les résultats selon le Code canadien de l'électricité en vigueur et les exigences locales. |
| empty.jobs | No saved jobs yet | Aucun chantier enregistré |
| settings.language | Language | Langue |
| settings.units | Units | Unités |
| settings.privacy | Privacy | Confidentialité |
| settings.support | Support | Assistance |

## iPhone Screenshot Scenes

1. Title: Fast Canadian Conduit Fill  
   Copy: Live fill percentages, remaining capacity, and next-size recommendations for jobsite decisions.

2. Title: Bend Layouts Without Guesswork  
   Copy: Plan offsets, saddles, kicks, and 90s with clear marks you can take to the pipe.

3. Title: Voltage Drop in Seconds  
   Copy: Compare copper and aluminum runs, then spot when a larger conductor is the better call.

4. Title: Build a Clean Takeoff  
   Copy: Save conduit, fittings, conductors, labels, and notes into one organized job list.

5. Title: English and French Reports  
   Copy: Export bilingual job summaries for forepersons, apprentices, offices, and clients.

## iPad Screenshot Scenes

1. Title: Job Dashboard for the Whole Site  
   Copy: Review recent jobs, calculators, and saved runs from a spacious command view.

2. Title: Full-Width Conduit Fill Tables  
   Copy: Enter conductors on the left and review fill status, capacity, and recommendations on the right.

3. Title: Visual Bend Planning  
   Copy: Large diagrams make offset, saddle, and kick measurements easier to verify before bending.

4. Title: Side-by-Side Voltage Drop  
   Copy: Compare circuit assumptions and conductor options with room for detailed notes.

5. Title: Professional PDF Reports  
   Copy: Preview calculation summaries, material takeoffs, warnings, and bilingual notes before sharing.

## App Store Metadata

- Name: ConduitMate CA
- Subtitle: Canadian Conduit Tools
- Promotional text: Professional conduit fill, bend, voltage-drop, and takeoff tools built for Canadian electrical work.
- Keywords: conduit, electrician, electrical, Canada, CEC, CSA, conduit fill, bending, voltage drop, takeoff, wire, contractor, apprentice, construction, estimate
- Category: Productivity
- Secondary category: Utilities
- Age rating: 4+

### Description

ConduitMate CA is a paid professional field tool for Canadian electrical work. Calculate conduit fill, plan bends, estimate voltage drop, and build organized material takeoffs from one clean bilingual app.

Designed for electricians, apprentices, forepersons, maintenance teams, and estimators, ConduitMate CA keeps the most common conduit decisions fast and consistent on iPhone and iPad. Create a job, run calculations, save results, and export a clear report for your records.

Key features:
- Conduit fill calculator with status bands and next-size recommendations
- Bend planner for offsets, saddles, kicks, and 90-degree bends
- Voltage drop estimator for single-phase and three-phase circuits
- Material takeoff list for conduit, fittings, conductors, labels, and notes
- Local job library with duplicate and export actions
- English and French interface strings
- Offline reference tables
- PDF/share reports for job documentation

ConduitMate CA does not replace professional judgment, engineering review, inspection requirements, or the current Canadian Electrical Code. Always verify results with the latest code edition and your local authority having jurisdiction.

## Privacy Page Copy

ConduitMate CA is designed as an offline-first paid utility. The app does not require an account, does not display ads, and does not sell user data.

Data you create, including job names, calculation inputs, notes, and saved reports, is stored locally on your device unless you choose to share or export it using iOS share features. If iCloud backup is enabled for your device, Apple may include app data in your device backup according to your iCloud settings.

The app may collect anonymous crash diagnostics and basic performance information through Apple developer tools when users have enabled sharing diagnostics with developers. This information is used only to improve reliability.

ConduitMate CA does not collect precise location, contacts, payment card data, photos, microphone input, or advertising identifiers.

## Support Page Copy

Need help with ConduitMate CA?

Email support with your device model, iOS version, app version, preferred language, and a short description of the issue. For calculation questions, include the conduit type, trade size, conductor type, conductor gauge, quantities, and any job notes needed to reproduce the result.

Support topics:
- App setup and language preferences
- Saved jobs and exports
- Calculator input questions
- Report formatting
- Bug reports and correction requests
- Feature suggestions for Canadian electrical workflows

Important: Support can help explain app behavior, but it cannot provide engineering approval, inspection approval, legal advice, or site-specific code rulings. Verify final installations with the current Canadian Electrical Code and the local authority having jurisdiction.

## Visual Design Tokens

### Brand Feel

- Professional, compact, field-ready, and premium.
- Avoid playful construction clichés; use precise technical rhythm, crisp diagrams, and high-contrast status states.
- Main visual motif: conduit paths, measured bends, and quiet drafting-grid structure.

### Color

| Token | Hex | Usage |
| --- | --- | --- |
| color.background | #F7F8F4 | Main light background |
| color.surface | #FFFFFF | Forms, sheets, tables |
| color.surfaceElevated | #ECEFE8 | Secondary panels |
| color.textPrimary | #17201A | Primary text |
| color.textSecondary | #596257 | Supporting text |
| color.accent | #0E7C66 | Primary actions, active states |
| color.accentDark | #075C4B | Pressed actions |
| color.measure | #2457C5 | Diagram marks and measured distances |
| color.warning | #B7791F | Check-required status |
| color.danger | #B42318 | Exceeds-limit status |
| color.success | #218A4A | Within-limit status |
| color.separator | #D7DCD2 | Dividers and table rules |

### Typography

- Primary font: SF Pro
- Monospaced numeric font: SF Mono for measurements, percentages, gauge values, and report IDs.
- Large title: 32/38 semibold
- Screen title: 24/30 semibold
- Section title: 17/22 semibold
- Body: 16/22 regular
- Field label: 13/18 medium
- Result numeric: 34/38 semibold, monospaced digits
- Table numeric: 15/20 regular, monospaced digits

### Spacing and Layout

- Base spacing: 4 pt grid
- Screen margin iPhone: 16 pt
- Screen margin iPad: 28 pt
- Card radius: 8 pt
- Control radius: 8 pt
- Row height: 48 pt minimum
- Toolbar icon target: 44 x 44 pt
- Result cards: fixed minimum height to avoid layout shifts during live calculation.

### Components

- CalculatorInputRow: label, value field, unit suffix, validation message.
- ResultStatusBand: pass/warning/fail color band with concise action text.
- MeasurementDiagram: vector SwiftUI diagram with SF Mono labels.
- JobTile: site name, province, last edited, primary calculator used, status count.
- ReferenceTable: searchable, sortable compact table with pinned header.
- LanguageToggle: segmented English/French selector.
- ExportPreview: report sheet with PDF and share actions.

## Implementation Notes

- Platform: iOS 26+ and iPadOS 26+, SwiftUI-first.
- Persistence: SwiftData local models for Job, CalculationRun, MaterialItem, and UserPreferences.
- Localization: String Catalog with English as development language and French Canadian strings.
- Export: PDFRenderer-based report generation plus ShareLink.
- Accessibility: Dynamic Type up to Accessibility Large, VoiceOver labels for diagrams, color-independent status labels, 44 pt minimum tap targets.
- Offline behavior: All core calculators and references must work without network access.
- Safety: Every report and calculator screen should include a compact code-verification disclaimer or link to the full disclaimer.
