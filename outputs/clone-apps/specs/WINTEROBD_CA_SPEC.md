# WinterOBD CA Implementation Spec

## Product Summary

WinterOBD CA is a paid SwiftUI iOS 26+ vehicle diagnostics app for Canadian drivers who want clear OBD-II health checks, winter readiness guidance, freeze-risk alerts, and bilingual English/French reporting. The app should feel trustworthy, practical, and premium, with no subscriptions, ads, account creation, or cloud dependency.

Primary value:
- Read and explain OBD-II trouble codes in plain English and French.
- Track cold-weather vehicle health signals before long winter drives.
- Save inspection-ready reports for mechanics, buyers, and fleet logs.
- Provide Canada-focused maintenance prompts for battery, coolant, emissions readiness, and cold-start issues.

Target customer:
- Canadian car owners, used-car shoppers, rural commuters, rideshare drivers, small fleet owners, and DIY mechanics.

Platform:
- iPhone and iPad.
- iOS/iPadOS 26+.
- SwiftUI, SwiftData, Charts, PDFKit, CoreBluetooth for BLE OBD-II adapters.
- Paid upfront app. No IAP required.

## Core Screens And Features

### 1. Garage
- Vehicle cards with year, make, model, VIN nickname, odometer, province, fuel type, and last scan status.
- Quick actions: Scan, Winter Check, Reports, Settings.
- Vehicle health summary: Engine, emissions readiness, battery, coolant, last code count.
- Empty state encourages adding a vehicle or pairing an OBD-II adapter.

### 2. OBD Pairing
- BLE adapter discovery with signal strength and trusted-device labeling.
- Guided connection states: Searching, Connecting, Initializing ECU, Ready, Failed.
- Adapter compatibility tips for ELM327-style BLE devices.
- Offline demo mode with sample data for App Store review and onboarding.

### 3. Live Scan
- Real-time diagnostic scan with progress rings for ECU modules.
- Trouble code list with severity, system, freeze-frame availability, and bilingual explanations.
- Readiness monitors: catalyst, EVAP, oxygen sensor, misfire, fuel system.
- Actions: Clear codes, Save report, Export PDF, Share with mechanic.
- Safety copy: clearing codes may reset readiness monitors.

### 4. Winter Check
- Canada-specific cold-weather readiness score.
- Battery voltage and crank confidence indicator.
- Coolant temperature and warm-up trend.
- Intake air temperature, engine load, idle stability, and short-trip warning.
- Checklist: battery age, winter tires, block heater, washer fluid, coolant mix, emergency kit.
- Province-aware seasonal reminders without legal claims.

### 5. Code Detail
- Plain-language explanation, likely causes, urgency, symptoms, what to check first, and mechanic notes.
- English/French toggle per code.
- Freeze-frame snapshot: RPM, speed, coolant temperature, load, fuel trim, voltage.
- Mark as resolved, add note, attach photo, rescan after repair.

### 6. Reports
- Timeline of scans and winter checks by vehicle.
- PDF report builder with vehicle info, scan result, codes, readiness, freeze-frame, notes, and timestamp.
- Share sheet export.
- Local-only searchable archive.

### 7. Settings
- Language: English, French, System.
- Units: Celsius/km, Fahrenheit/miles optional.
- Province/territory selection.
- Adapter management.
- Privacy, support, legal notices, diagnostic disclaimer.

## UI String Set

### Global
| Key | English | French |
|---|---|---|
| app_name | WinterOBD CA | WinterOBD CA |
| scan_now | Scan Now | Scanner |
| winter_check | Winter Check | Controle hivernal |
| garage | Garage | Garage |
| reports | Reports | Rapports |
| settings | Settings | Reglages |
| cancel | Cancel | Annuler |
| save | Save | Enregistrer |
| done | Done | Termine |
| share | Share | Partager |
| export_pdf | Export PDF | Exporter le PDF |
| connected | Connected | Connecte |
| disconnected | Disconnected | Deconnecte |
| no_vehicle | No vehicle selected | Aucun vehicule selectionne |

### Garage
| Key | English | French |
|---|---|---|
| add_vehicle | Add Vehicle | Ajouter un vehicule |
| last_scan | Last scan | Dernier scan |
| no_codes | No active codes | Aucun code actif |
| codes_found | Codes found | Codes trouves |
| readiness_ready | Ready for inspection | Pret pour l'inspection |
| readiness_pending | Readiness pending | Preparation en attente |

### Pairing
| Key | English | French |
|---|---|---|
| find_adapter | Find OBD-II Adapter | Trouver l'adaptateur OBD-II |
| searching | Searching nearby adapters... | Recherche des adaptateurs proches... |
| initializing | Initializing vehicle link... | Initialisation du lien vehicule... |
| connection_failed | Connection failed | Connexion echouee |
| retry_connection | Retry Connection | Reessayer la connexion |
| demo_mode | Use Demo Mode | Utiliser le mode demo |

### Scan
| Key | English | French |
|---|---|---|
| live_scan | Live Scan | Scan en direct |
| scanning_modules | Scanning modules | Scan des modules |
| trouble_codes | Trouble Codes | Codes d'anomalie |
| clear_codes | Clear Codes | Effacer les codes |
| save_report | Save Report | Enregistrer le rapport |
| severity_low | Low | Faible |
| severity_medium | Medium | Moyen |
| severity_high | High | Eleve |
| freeze_frame | Freeze Frame | Donnees figees |

### Winter
| Key | English | French |
|---|---|---|
| winter_score | Winter Readiness | Preparation hivernale |
| battery_health | Battery Health | Etat de la batterie |
| coolant_temp | Coolant Temperature | Temperature du liquide |
| cold_start | Cold Start | Demarrage a froid |
| short_trip_warning | Short trips may prevent full warm-up. | Les courts trajets peuvent empecher le rechauffement complet. |
| check_block_heater | Check block heater cable | Verifier le cable du chauffe-moteur |
| washer_fluid | Winter washer fluid | Lave-glace d'hiver |

### Disclaimers
| Key | English | French |
|---|---|---|
| diagnostic_disclaimer | WinterOBD CA provides diagnostic guidance, not professional repair advice. Always consult a qualified technician before driving with a serious warning. | WinterOBD CA fournit des indications diagnostiques, pas des conseils de reparation professionnels. Consultez toujours un technicien qualifie avant de conduire avec une alerte serieuse. |
| clear_warning | Clearing codes can reset inspection readiness monitors. | Effacer les codes peut reinitialiser les moniteurs de preparation a l'inspection. |

## iPhone Screenshot Scenes

1. Garage Overview  
   Title: Your Winter-Ready Garage  
   Copy: Track every vehicle, last scan, active codes, and cold-weather readiness in one clean view.

2. Live OBD-II Scan  
   Title: Decode Engine Warnings Fast  
   Copy: Read trouble codes, freeze-frame data, and readiness monitors with clear bilingual explanations.

3. Winter Check  
   Title: Built For Canadian Cold  
   Copy: Review battery voltage, coolant temperature, warm-up behavior, and winter maintenance prompts.

4. Code Detail  
   Title: Know What To Check First  
   Copy: See severity, likely causes, symptoms, and mechanic-ready notes before you book a repair.

5. PDF Reports  
   Title: Share A Clean Report  
   Copy: Export local scan history as a polished PDF for mechanics, buyers, or fleet records.

## iPad Screenshot Scenes

1. Split Garage Dashboard  
   Title: A Bigger View Of Vehicle Health  
   Copy: Browse your garage, scan history, and vehicle status with a spacious iPad layout.

2. Scan Command Center  
   Title: Live Diagnostics, Clearly Organized  
   Copy: Monitor modules, trouble codes, readiness, and freeze-frame values side by side.

3. Winter Readiness Board  
   Title: Cold-Weather Signals At A Glance  
   Copy: Compare battery, coolant, idle, and checklist items before winter travel.

4. Report Workspace  
   Title: Review Before You Share  
   Copy: Inspect scan details, notes, and vehicle data before exporting a mechanic-ready PDF.

5. Bilingual Code Library  
   Title: English And French Built In  
   Copy: Switch languages instantly for code explanations, repair notes, and saved reports.

## App Store Metadata

Name:
WinterOBD CA

Subtitle:
Canadian OBD Winter Scan

Promotional Text:
Scan OBD-II codes, check winter readiness, and export bilingual vehicle reports. Built for Canadian drivers and cold-weather maintenance.

Description:
WinterOBD CA is a premium OBD-II diagnostics app built for Canadian drivers. Connect a compatible BLE OBD-II adapter, scan your vehicle, understand trouble codes in plain English or French, and save clean reports for mechanics, buyers, or fleet records.

Designed for winter driving, the app highlights cold-weather signals such as battery voltage, coolant temperature, idle stability, warm-up behavior, and readiness monitors. Add vehicles to your garage, keep a local scan history, and review seasonal maintenance prompts before long drives or deep cold.

Features:
- OBD-II trouble code scanning with clear explanations
- English and French interface strings
- Winter readiness score for Canadian conditions
- Battery, coolant, idle, and warm-up checks
- Emissions readiness monitor summary
- Freeze-frame data when available
- Local scan history by vehicle
- PDF report export and sharing
- Demo mode for learning without an adapter
- No ads, no account, no subscription

WinterOBD CA provides diagnostic guidance and vehicle health organization. It does not replace professional repair advice. Always consult a qualified technician before driving with a serious warning or making repair decisions.

Keywords:
OBD,OBD2,OBD-II,car scanner,auto diagnostic,check engine,winter car,battery,Canada,mechanic,vehicle,scanner,ELM327,French,garage

Category:
Utilities

Age Rating:
4+

In-App Purchases:
None

Price Model:
Paid upfront

## Privacy Page Copy

WinterOBD CA is designed as a local-first vehicle diagnostics app.

We do not require an account. We do not sell personal data. We do not include third-party advertising. Vehicle profiles, scan history, diagnostic notes, and saved reports are stored locally on your device unless you choose to export or share them.

Bluetooth is used to connect to compatible OBD-II adapters. The app may read vehicle diagnostic values such as trouble codes, readiness monitor status, sensor values, and freeze-frame data. This information is used only to display diagnostics and create reports inside the app.

If crash reporting or analytics are added in a future build, they must be opt-in, anonymized, and disclosed in App Store privacy nutrition labels.

French summary:
WinterOBD CA fonctionne d'abord en local. Aucun compte n'est requis, aucune donnee personnelle n'est vendue et aucune publicite tierce n'est incluse. Les profils de vehicules, l'historique des scans et les rapports restent sur votre appareil sauf si vous choisissez de les exporter ou de les partager.

## Support Page Copy

Need help with WinterOBD CA?

Before contacting support:
- Confirm your OBD-II adapter supports Bluetooth Low Energy.
- Make sure the adapter is fully seated in the vehicle's OBD-II port.
- Turn the ignition to ON or start the engine when scanning.
- Try Demo Mode to confirm the app interface is working.
- If a scan fails, disconnect the adapter, wait 10 seconds, and reconnect.

Support email:
support@winterobd.ca

Please include:
- iPhone or iPad model
- iOS/iPadOS version
- Adapter brand/model
- Vehicle year, make, and model
- A brief description of the issue

French support intro:
Besoin d'aide avec WinterOBD CA? Verifiez que votre adaptateur OBD-II prend en charge Bluetooth Low Energy, que le contact du vehicule est active et que l'adaptateur est bien branche. Incluez le modele de votre appareil, la version iOS/iPadOS, le modele de l'adaptateur et le vehicule concerne dans votre message.

## Visual Design Tokens

### Color
```swift
enum WinterOBDColor {
    static let frostWhite = Color(hex: "F7FAFC")
    static let iceBlue = Color(hex: "D9ECF7")
    static let arcticCyan = Color(hex: "4FB3D9")
    static let northernGreen = Color(hex: "2F8F83")
    static let warningAmber = Color(hex: "F5A524")
    static let alertRed = Color(hex: "D84A4A")
    static let graphite = Color(hex: "1F2933")
    static let slate = Color(hex: "52616B")
    static let panel = Color(hex: "FFFFFF")
    static let panelAlt = Color(hex: "EEF4F7")
}
```

### Typography
- Large title: SF Pro Rounded, 34, semibold
- Screen title: SF Pro, 28, semibold
- Section title: SF Pro, 17, semibold
- Body: SF Pro, 16, regular
- Caption: SF Pro, 12, medium
- Diagnostic code: SF Mono, 15, semibold
- Sensor value: SF Mono, 22, semibold

### Layout
- Base spacing: 4 pt grid.
- Screen padding iPhone: 20 pt.
- Screen padding iPad: 32 pt.
- Card radius: 8 pt.
- Control radius: 8 pt.
- Divider opacity: 12%.
- Minimum tap target: 44 x 44 pt.
- iPad preferred layout: NavigationSplitView with garage/sidebar, detail, and inspector/report column where useful.

### Components
- HealthGauge: circular score with color thresholds.
- VehicleCard: compact vehicle summary with status chips.
- CodeRow: code, severity, system, short explanation.
- SensorTile: icon, label, live value, trend arrow.
- ReadinessGrid: monitor status cells.
- ChecklistRow: toggle, seasonal label, optional due date.
- ReportPreview: paginated PDF thumbnail with export actions.

### Icon Style
- Use SF Symbols with rounded line icons.
- Primary icons: car.side, stethoscope, snowflake, battery.100percent, thermometer.medium, doc.richtext, bluetooth, exclamationmark.triangle.
- Avoid novelty illustrations; diagnostic UI should feel precise and durable.

## Data Model Sketch

Vehicle:
- id
- displayName
- year
- make
- model
- vinOptional
- province
- odometerKm
- fuelType
- createdAt
- updatedAt

ScanSession:
- id
- vehicleId
- startedAt
- completedAt
- adapterName
- codes
- readiness
- freezeFrames
- sensorSnapshot
- notes
- reportURL

TroubleCode:
- code
- system
- severity
- englishTitle
- frenchTitle
- englishExplanation
- frenchExplanation
- likelyCauses
- symptoms
- firstChecks
- resolvedAt

WinterCheck:
- id
- vehicleId
- date
- readinessScore
- batteryVoltage
- coolantTempC
- intakeTempC
- idleRpm
- warmupMinutes
- checklistItems

## Implementation Notes

- Keep all diagnostic data local with SwiftData.
- Provide seeded demo data for App Store review and empty-state exploration.
- Treat OBD communication as an injectable service so simulator builds can use mock scan data.
- Make language override app-local and independent of system language.
- Use MeasurementFormatter for temperature and distance, but default Canadian configuration to Celsius and kilometres.
- PDF reports should include both English and French headers when bilingual export is enabled.
- Do not make medical, legal, or regulatory guarantees about emissions inspections. Use readiness language only.
- Clearing codes must require confirmation and explain readiness reset impact.
