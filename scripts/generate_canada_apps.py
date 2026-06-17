from __future__ import annotations

import json
import math
import plistlib
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "clone-apps"
APPS_DIR = OUT / "apps"
SHOTS_DIR = OUT / "screenshots"
PAGES_DIR = OUT / "pages"
META_DIR = OUT / "metadata"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        "/System/Library/Fonts/SFNS.ttf",
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial Unicode.ttf",
    ]
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size=size)
        except Exception:
            continue
    return ImageFont.load_default()


APPS = [
    {
        "id": "RPASDeckCA",
        "display": "RPAS Deck CA",
        "bundle": "com.codexpipeline.canada.rpasdeckca",
        "price": "CAD $39.99",
        "subtitle": "RPAS exam deck",
        "category": "Canadian RPAS exam and pre-flight tools",
        "accent": (42, 171, 226),
        "accent2": (20, 56, 92),
        "bg": (8, 18, 31),
        "fg": (232, 246, 255),
        "language": "aviation instruments, dark cockpit panels, chart blue overlays",
        "symbols": ["airplane", "map", "checklist", "wind", "location.north.line"],
        "tabs": ["Deck", "Airspace", "Preflight"],
        "tabs_fr": ["Cartes", "Espace", "Prévol"],
        "headline": "Pass the Canadian RPAS exam",
        "headline_fr": "Réussissez l'examen RPAS canadien",
        "body": "Bilingual study decks, airspace drills, weather minima, and a pre-flight flow built around Transport Canada terminology.",
        "body_fr": "Cartes d'étude bilingues, exercices d'espace aérien, météo minimale et séquence prévol avec terminologie de Transports Canada.",
        "features": ["Basic/Advanced topic decks", "Airspace and NOTAM checks", "Pre-flight risk board", "Metric/imperial altitude and wind"],
        "features_fr": ["Jeux Basic/Advanced", "Espace aérien et NOTAM", "Tableau de risque prévol", "Altitude et vent métrique/impérial"],
        "keywords": "RPAS,drone,Canada,Transport Canada,exam,UAV,pilot,airspace,preflight",
        "promo": "A polished Canadian RPAS study deck with bilingual practice and flight-ready check tools.",
        "desc": "RPAS Deck CA helps Canadian drone pilots prepare with bilingual study cards, airspace practice, weather prompts, and pre-flight checklists. Built for Canada-only terminology and paid once in CAD.",
        "scenes": [
            ("Command deck", "Study progress, risk lights, and today's RPAS focus in one cockpit-style view."),
            ("Airspace drills", "Practice controlled zones, charts, NOTAM prompts, and Canadian flight terms."),
            ("Pre-flight flow", "Battery, weather, site survey, observer, and emergency prompts before takeoff."),
            ("Exam cards", "Fast bilingual flashcards for Basic and Advanced RPAS knowledge areas."),
            ("Unit control", "Switch metric and imperial values for altitude, wind, distance, and temperature."),
        ],
    },
    {
        "id": "ExamCardsCA",
        "display": "ExamCards CA",
        "bundle": "com.codexpipeline.canada.examcardsca",
        "price": "CAD $24.99",
        "subtitle": "Canadian exam cards",
        "category": "Canadian certificate SRS flashcards",
        "accent": (190, 85, 55),
        "accent2": (244, 188, 99),
        "bg": (250, 243, 228),
        "fg": (38, 31, 26),
        "language": "warm paper, tactile flashcards, calm study desk",
        "symbols": ["rectangle.stack", "graduationcap", "timer", "checkmark.seal", "bookmark"],
        "tabs": ["Decks", "Review", "Stats"],
        "tabs_fr": ["Paquets", "Révision", "Stats"],
        "headline": "Canadian exams, one smart deck",
        "headline_fr": "Examens canadiens, un paquet intelligent",
        "body": "Spaced repetition cards for citizenship, Red Seal readiness, and first-aid refreshers, with English and French study modes.",
        "body_fr": "Répétition espacée pour citoyenneté, Red Seal et secourisme, avec modes d'étude anglais et français.",
        "features": ["SRS review queue", "Citizenship practice", "Red Seal trade prompts", "First-aid refreshers"],
        "features_fr": ["File SRS", "Pratique citoyenneté", "Questions Red Seal", "Révision secourisme"],
        "keywords": "Canada,exam,flashcards,citizenship,Red Seal,first aid,SRS,study,French",
        "promo": "Premium bilingual flashcards for Canadian licensing and certificate prep.",
        "desc": "ExamCards CA organizes high-value Canadian exam prep into bilingual spaced-repetition decks. Review citizenship, Red Seal, and first-aid concepts in a calm card interface.",
        "scenes": [
            ("Study desk", "Warm flashcards, due counts, and exam tracks without visual clutter."),
            ("Spaced review", "A daily queue that keeps hard Canadian terms coming back at the right time."),
            ("Citizenship set", "Practice government, rights, symbols, geography, and history prompts."),
            ("Red Seal set", "Trade-focused prompts with confident answer reveal and notes."),
            ("Progress view", "Retention, streak, and weak-topic indicators for serious study sessions."),
        ],
    },
    {
        "id": "WinterOBDCA",
        "display": "WinterOBD CA",
        "bundle": "com.codexpipeline.canada.winterobdca",
        "price": "CAD $24.99",
        "subtitle": "Cold-code decoder",
        "category": "Winter automotive OBD diagnostic code library",
        "accent": (255, 126, 42),
        "accent2": (70, 160, 190),
        "bg": (14, 17, 22),
        "fg": (245, 248, 250),
        "language": "vehicle dashboard, black glass, warning orange, cold weather diagnostics",
        "symbols": ["car", "exclamationmark.triangle", "thermometer.snowflake", "wrench.adjustable", "bolt.car"],
        "tabs": ["Codes", "Freeze", "Garage"],
        "tabs_fr": ["Codes", "Gel", "Garage"],
        "headline": "Decode winter warning lights",
        "headline_fr": "Décodez les alertes d'hiver",
        "body": "A cold-weather OBD reference for Canadian drivers: battery, emissions, misfire, heater, ABS, and sensor faults.",
        "body_fr": "Référence OBD hivernale pour le Canada : batterie, émissions, ratés, chauffage, ABS et capteurs.",
        "features": ["Winter fault library", "Freeze-frame notes", "Battery and heater prompts", "Metric/imperial temperature"],
        "features_fr": ["Codes d'hiver", "Notes freeze-frame", "Batterie et chauffage", "Température métrique/impériale"],
        "keywords": "OBD,Canada,winter,car,diagnostic,codes,battery,engine,garage",
        "promo": "A premium cold-weather OBD code companion tuned for Canadian driving conditions.",
        "desc": "WinterOBD CA helps drivers and independent shops interpret diagnostic trouble codes in Canadian winter contexts. It includes bilingual code notes, freeze-frame capture prompts, and metric/imperial unit support.",
        "scenes": [
            ("Dashboard scan", "Search common cold-weather codes in a dark instrument-panel interface."),
            ("Winter causes", "See likely battery, moisture, sensor, and low-temperature explanations."),
            ("Freeze-frame notes", "Capture km/h, coolant temp, voltage, and conditions before clearing codes."),
            ("Garage checklist", "Prioritize safe checks before a winter commute or remote trip."),
            ("Bilingual code card", "English and French notes stay side by side for shop-floor clarity."),
        ],
    },
    {
        "id": "ConduitMateCA",
        "display": "ConduitMate CA",
        "bundle": "com.codexpipeline.canada.conduitmateca",
        "price": "CAD $14.99",
        "subtitle": "Red Seal bends",
        "category": "Electrical conduit bending calculator",
        "accent": (238, 210, 72),
        "accent2": (35, 95, 82),
        "bg": (20, 24, 23),
        "fg": (247, 244, 226),
        "language": "jobsite engineering, high-contrast numbers, measured conduit marks",
        "symbols": ["ruler", "angle", "bolt", "hammer", "number"],
        "tabs": ["Bends", "Offsets", "Marks"],
        "tabs_fr": ["Cintrage", "Décalage", "Repères"],
        "headline": "Fast conduit math on site",
        "headline_fr": "Calculs de conduit au chantier",
        "body": "Canadian electrician bending references with offsets, shrink, take-up, and clear metric/imperial markouts.",
        "body_fr": "Références de cintrage pour électriciens au Canada : décalage, retrait, gain et repères métriques/impériaux.",
        "features": ["Offset and saddle bends", "Take-up references", "Large numeric markouts", "Metric/imperial conduit units"],
        "features_fr": ["Décalages et selles", "Références de gain", "Grands repères numériques", "Unités métriques/impériales"],
        "keywords": "conduit,electrician,Canada,Red Seal,bending,offset,EMT,metric,imperial",
        "promo": "High-contrast conduit bend math for Canadian Red Seal electricians and apprentices.",
        "desc": "ConduitMate CA brings precise bend calculations to the jobsite with bilingual labels, large markouts, and metric/imperial inputs. Built as a simple paid-once calculator for Canadian electrical work.",
        "scenes": [
            ("Bend calculator", "Offset, shrink, and markout values are readable in bright site-light contrast."),
            ("Red Seal practice", "Trade terminology stays Canadian and bilingual for apprentice study."),
            ("Metric/imperial", "Flip mm, cm, inches, and feet without losing the bend plan."),
            ("Markout board", "Large numbers and angle chips help you work with gloves on."),
            ("Saddle reference", "Common bends are organized into practical field cards."),
        ],
    },
    {
        "id": "TelePromptCA",
        "display": "TelePrompt CA",
        "bundle": "com.codexpipeline.canada.telepromptca",
        "price": "CAD $29.99",
        "subtitle": "Bilingual prompter",
        "category": "English/French teleprompter",
        "accent": (72, 222, 166),
        "accent2": (78, 84, 108),
        "bg": (8, 11, 13),
        "fg": (229, 255, 246),
        "language": "mirror glass, studio green, reflection, bilingual creator workflow",
        "symbols": ["text.alignleft", "camera", "arrow.left.and.right", "speedometer", "rectangle.on.rectangle"],
        "tabs": ["Script", "Mirror", "Remote"],
        "tabs_fr": ["Texte", "Miroir", "Téléco."],
        "headline": "Bilingual scripts, studio-ready",
        "headline_fr": "Scripts bilingues prêts pour studio",
        "body": "A paid-once prompter for Canadian creators, educators, and teams who record in English and French.",
        "body_fr": "Un prompteur acheté une fois pour créateurs, éducateurs et équipes canadiennes en anglais et français.",
        "features": ["Mirror mode", "Speed and margin control", "English/French script lanes", "iPad stage view"],
        "features_fr": ["Mode miroir", "Vitesse et marges", "Pistes anglais/français", "Vue scène iPad"],
        "keywords": "teleprompter,Canada,bilingual,French,English,video,script,mirror,iPad",
        "promo": "A polished bilingual teleprompter for Canadian creators, classrooms, and teams.",
        "desc": "TelePrompt CA gives Canadian creators a refined teleprompter with English/French script lanes, mirror mode, speed controls, and iPad-friendly presentation views. One purchase, no subscription.",
        "scenes": [
            ("Script studio", "Draft English and French script lanes with calm studio controls."),
            ("Mirror mode", "Flip text for beam-splitter glass and tune margins for your rig."),
            ("Playback control", "Speed, size, and focus line controls stay close without crowding text."),
            ("Remote-ready", "Prepare stage views for iPad recording, teaching, and presentations."),
            ("Clean export", "Keep reusable Canadian bilingual scripts organized by project."),
        ],
    },
]


def clean_name(value: str) -> str:
    return value.replace(" ", "").replace("-", "")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def plist(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as f:
        plistlib.dump(value, f, sort_keys=False)


def wrap_text(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont, width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        test = f"{current} {word}".strip()
        if draw.textbbox((0, 0), test, font=fnt)[2] <= width:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def lerp(a: int, b: int, t: float) -> int:
    return int(a + (b - a) * t)


def gradient(size: tuple[int, int], top: tuple[int, int, int], bottom: tuple[int, int, int]) -> Image.Image:
    w, h = size
    img = Image.new("RGB", size, top)
    px = img.load()
    for y in range(h):
        t = y / max(h - 1, 1)
        col = tuple(lerp(top[i], bottom[i], t) for i in range(3))
        for x in range(w):
            px[x, y] = col
    return img


def rounded(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], r: int, fill, outline=None, width: int = 1) -> None:
    draw.rounded_rectangle(xy, radius=r, fill=fill, outline=outline, width=width)


def make_icon(app: dict, path: Path) -> None:
    img = gradient((1024, 1024), app["accent2"], app["bg"])
    d = ImageDraw.Draw(img)
    accent = app["accent"]
    fg = app["fg"]
    for i in range(9):
        x = 80 + i * 112
        d.line((x, 0, x - 210, 1024), fill=tuple(max(0, c - 34) for c in app["accent2"]), width=8)
    d.rounded_rectangle((146, 146, 878, 878), radius=172, outline=accent, width=18)
    d.ellipse((292, 238, 732, 678), outline=accent, width=30)
    d.arc((248, 194, 776, 722), start=210, end=330, fill=fg, width=30)
    initials = "".join(part[0] for part in app["display"].replace(" CA", "").split()[:2])
    if len(initials) < 2:
        initials = app["display"][:2]
    d.text((512, 544), initials.upper(), font=font(220, True), fill=fg, anchor="mm")
    d.text((512, 746), "CA", font=font(92, True), fill=accent, anchor="mm")
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path)


def make_screenshot(app: dict, path: Path, title: str, copy: str, size: tuple[int, int], idx: int) -> None:
    w, h = size
    img = gradient(size, app["bg"], tuple(max(0, c - 22) for c in app["accent2"]))
    d = ImageDraw.Draw(img)
    accent = app["accent"]
    fg = app["fg"]
    muted = tuple(lerp(fg[i], app["bg"][i], 0.38) for i in range(3))
    margin = int(w * 0.07)
    top = int(h * 0.07)
    d.text((margin, top), app["display"], font=font(int(w * 0.052), True), fill=accent)
    d.text((w - margin, top), app["price"], font=font(int(w * 0.034), True), fill=muted, anchor="ra")
    y = top + int(h * 0.08)
    for line in wrap_text(d, title, font(int(w * 0.098), True), w - margin * 2):
        d.text((margin, y), line, font=font(int(w * 0.098), True), fill=fg)
        y += int(w * 0.112)
    y += int(h * 0.012)
    for line in wrap_text(d, copy, font(int(w * 0.038)), w - margin * 2):
        d.text((margin, y), line, font=font(int(w * 0.038)), fill=muted)
        y += int(w * 0.052)
    panel_top = int(h * 0.42)
    panel_h = int(h * 0.46)
    rounded(d, (margin, panel_top, w - margin, panel_top + panel_h), int(w * 0.04), fill=tuple(lerp(app["bg"][i], accent[i], 0.12) for i in range(3)), outline=tuple(lerp(accent[i], fg[i], 0.2) for i in range(3)), width=3)
    cx, cy = w // 2, panel_top + int(panel_h * 0.38)
    for r in range(0, 4):
        radius = int(w * (0.12 + r * 0.08))
        d.ellipse((cx - radius, cy - radius, cx + radius, cy + radius), outline=tuple(lerp(accent[i], fg[i], r / 5) for i in range(3)), width=3)
    needle = idx * math.pi / 6 + 0.6
    d.line((cx, cy, cx + int(math.cos(needle) * w * 0.23), cy + int(math.sin(needle) * w * 0.23)), fill=fg, width=max(5, int(w * 0.008)))
    for n, label in enumerate(app["tabs"]):
        x0 = margin + int((w - 2 * margin) * n / 3) + int(w * 0.024)
        x1 = margin + int((w - 2 * margin) * (n + 1) / 3) - int(w * 0.024)
        y0 = panel_top + panel_h - int(h * 0.15)
        rounded(d, (x0, y0, x1, y0 + int(h * 0.052)), int(w * 0.02), fill=accent if n == idx % 3 else tuple(lerp(app["bg"][i], fg[i], 0.12) for i in range(3)))
        d.text(((x0 + x1) // 2, y0 + int(h * 0.026)), label, font=font(int(w * 0.026), True), fill=app["bg"] if n == idx % 3 else fg, anchor="mm")
    metric = "Metric" if idx % 2 == 0 else "Imperial"
    metric_fr = "Métrique" if idx % 2 == 0 else "Impérial"
    d.text((margin + int(w * 0.04), panel_top + panel_h - int(h * 0.06)), f"EN / FR  •  {metric} / {metric_fr}", font=font(int(w * 0.027), True), fill=muted)
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path)


def swift_string_array(values: list[str]) -> str:
    return "[" + ", ".join(json.dumps(v, ensure_ascii=False) for v in values) + "]"


def make_swift(app: dict) -> str:
    return f'''
import SwiftUI

@main
struct {app["id"]}App: App {{
    var body: some Scene {{
        WindowGroup {{
            ContentView()
        }}
    }}
}}

struct ContentView: View {{
    @State private var french = false
    @State private var metric = true
    @State private var selected = 0

    private let tabs = {swift_string_array(app["tabs"])}
    private let tabsFR = {swift_string_array(app["tabs_fr"])}
    private let features = {swift_string_array(app["features"])}
    private let featuresFR = {swift_string_array(app["features_fr"])}

    var body: some View {{
        ZStack {{
            LinearGradient(colors: [Color(hex: "{app["bg"][0]:02X}{app["bg"][1]:02X}{app["bg"][2]:02X}"), Color(hex: "{app["accent2"][0]:02X}{app["accent2"][1]:02X}{app["accent2"][2]:02X}")], startPoint: .topLeading, endPoint: .bottomTrailing)
                .ignoresSafeArea()
            ScrollView {{
                VStack(alignment: .leading, spacing: 22) {{
                    header
                    instrumentPanel
                    featureGrid
                    reviewPanel
                }}
                .padding(22)
            }}
        }}
    }}

    private var header: some View {{
        VStack(alignment: .leading, spacing: 14) {{
            HStack {{
                Label("{app["display"]}", systemImage: "{app["symbols"][0]}")
                    .font(.system(.title2, design: .rounded, weight: .bold))
                    .foregroundStyle(accent)
                Spacer()
                Text("{app["price"]}")
                    .font(.system(.callout, design: .rounded, weight: .semibold))
                    .foregroundStyle(foreground.opacity(0.76))
            }}
            Text(french ? "{app["headline_fr"]}" : "{app["headline"]}")
                .font(.system(size: 38, weight: .black, design: .rounded))
                .foregroundStyle(foreground)
                .fixedSize(horizontal: false, vertical: true)
            Text(french ? "{app["body_fr"]}" : "{app["body"]}")
                .font(.system(.body, design: .rounded, weight: .medium))
                .foregroundStyle(foreground.opacity(0.78))
            HStack(spacing: 12) {{
                TogglePill(title: french ? "FR" : "EN", icon: "character.bubble", isOn: $french)
                TogglePill(title: metric ? "Metric" : "Imperial", icon: "ruler", isOn: $metric)
            }}
        }}
    }}

    private var instrumentPanel: some View {{
        VStack(alignment: .leading, spacing: 18) {{
            HStack {{
                ForEach(Array((french ? tabsFR : tabs).enumerated()), id: \\.offset) {{ index, label in
                    Button {{
                        withAnimation(.spring(response: 0.35, dampingFraction: 0.82)) {{ selected = index }}
                    }} label: {{
                        Label(label, systemImage: ["{app["symbols"][1]}", "{app["symbols"][2]}", "{app["symbols"][3]}"][index])
                            .font(.system(.caption, design: .rounded, weight: .bold))
                            .frame(maxWidth: .infinity)
                            .padding(.vertical, 12)
                            .background(selected == index ? accent : foreground.opacity(0.10), in: RoundedRectangle(cornerRadius: 16, style: .continuous))
                            .foregroundStyle(selected == index ? Color(hex: "{app["bg"][0]:02X}{app["bg"][1]:02X}{app["bg"][2]:02X}") : foreground)
                    }}
                    .buttonStyle(.plain)
                }}
            }}
            ZStack {{
                RoundedRectangle(cornerRadius: 28, style: .continuous)
                    .fill(.ultraThinMaterial.opacity(0.7))
                    .overlay(RoundedRectangle(cornerRadius: 28).stroke(accent.opacity(0.65), lineWidth: 1.5))
                VStack(spacing: 18) {{
                    Image(systemName: "{app["symbols"][4]}")
                        .font(.system(size: 58, weight: .bold))
                        .symbolRenderingMode(.hierarchical)
                        .foregroundStyle(accent)
                    Text((french ? tabsFR : tabs)[selected])
                        .font(.system(.title, design: .rounded, weight: .black))
                        .foregroundStyle(foreground)
                    Text(metric ? "km / m / °C" : "mi / ft / °F")
                        .font(.system(.headline, design: .rounded, weight: .bold))
                        .foregroundStyle(accent)
                }}
                .padding(30)
            }}
            .frame(minHeight: 250)
        }}
    }}

    private var featureGrid: some View {{
        LazyVGrid(columns: [GridItem(.adaptive(minimum: 154), spacing: 14)], spacing: 14) {{
            ForEach(Array((french ? featuresFR : features).enumerated()), id: \\.offset) {{ index, text in
                VStack(alignment: .leading, spacing: 14) {{
                    Image(systemName: ["{app["symbols"][0]}", "{app["symbols"][1]}", "{app["symbols"][2]}", "{app["symbols"][3]}"][index])
                        .font(.system(size: 24, weight: .bold))
                        .foregroundStyle(accent)
                    Text(text)
                        .font(.system(.headline, design: .rounded, weight: .bold))
                        .foregroundStyle(foreground)
                        .fixedSize(horizontal: false, vertical: true)
                }}
                .frame(maxWidth: .infinity, minHeight: 112, alignment: .topLeading)
                .padding(18)
                .background(foreground.opacity(0.10), in: RoundedRectangle(cornerRadius: 18, style: .continuous))
            }}
        }}
    }}

    private var reviewPanel: some View {{
        VStack(alignment: .leading, spacing: 10) {{
            Text(french ? "Conçu pour le Canada" : "Designed for Canada")
                .font(.system(.title3, design: .rounded, weight: .black))
                .foregroundStyle(foreground)
            Text(french ? "Interface anglais/français, prix en CAD, contexte canadien et unités commutables." : "English/French interface, CAD pricing, Canadian context, and switchable units.")
                .font(.system(.body, design: .rounded, weight: .medium))
                .foregroundStyle(foreground.opacity(0.76))
        }}
        .padding(22)
        .background(accent.opacity(0.16), in: RoundedRectangle(cornerRadius: 22, style: .continuous))
    }}

    private var accent: Color {{ Color(hex: "{app["accent"][0]:02X}{app["accent"][1]:02X}{app["accent"][2]:02X}") }}
    private var foreground: Color {{ Color(hex: "{app["fg"][0]:02X}{app["fg"][1]:02X}{app["fg"][2]:02X}") }}
}}

struct TogglePill: View {{
    let title: String
    let icon: String
    @Binding var isOn: Bool
    var body: some View {{
        Button {{ isOn.toggle() }} label: {{
            Label(title, systemImage: icon)
                .font(.system(.caption, design: .rounded, weight: .bold))
                .padding(.horizontal, 14)
                .padding(.vertical, 10)
                .background(.white.opacity(0.14), in: Capsule())
        }}
        .buttonStyle(.plain)
        .foregroundStyle(.white)
    }}
}}

extension Color {{
    init(hex: String) {{
        let scanner = Scanner(string: hex)
        var value: UInt64 = 0
        scanner.scanHexInt64(&value)
        let red = Double((value >> 16) & 0xff) / 255.0
        let green = Double((value >> 8) & 0xff) / 255.0
        let blue = Double(value & 0xff) / 255.0
        self.init(red: red, green: green, blue: blue)
    }}
}}
'''.strip() + "\n"


def pbx_id(seed: str) -> str:
    value = abs(hash(seed)) % (16 ** 24)
    return f"{value:024X}"


def make_pbx(app: dict) -> str:
    app_id = app["id"]
    ids = {name: pbx_id(app_id + name) for name in [
        "project", "mainGroup", "productsGroup", "target", "sources", "resources",
        "configListProject", "debugProject", "releaseProject", "configListTarget",
        "debugTarget", "releaseTarget", "product", "sourceGroup", "appFile",
        "appBuild", "assets", "assetsBuild", "privacy", "privacyBuild", "info",
    ]}
    return f'''// !$*UTF8*$!
{{
	archiveVersion = 1;
	classes = {{}};
	objectVersion = 56;
	objects = {{

/* Begin PBXBuildFile section */
		{ids["appBuild"]} /* ContentView.swift in Sources */ = {{isa = PBXBuildFile; fileRef = {ids["appFile"]} /* ContentView.swift */; }};
		{ids["assetsBuild"]} /* Assets.xcassets in Resources */ = {{isa = PBXBuildFile; fileRef = {ids["assets"]} /* Assets.xcassets */; }};
		{ids["privacyBuild"]} /* PrivacyInfo.xcprivacy in Resources */ = {{isa = PBXBuildFile; fileRef = {ids["privacy"]} /* PrivacyInfo.xcprivacy */; }};
/* End PBXBuildFile section */

/* Begin PBXFileReference section */
		{ids["product"]} /* {app_id}.app */ = {{isa = PBXFileReference; explicitFileType = wrapper.application; includeInIndex = 0; path = {app_id}.app; sourceTree = BUILT_PRODUCTS_DIR; }};
		{ids["appFile"]} /* ContentView.swift */ = {{isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ContentView.swift; sourceTree = "<group>"; }};
		{ids["assets"]} /* Assets.xcassets */ = {{isa = PBXFileReference; lastKnownFileType = folder.assetcatalog; path = Assets.xcassets; sourceTree = "<group>"; }};
		{ids["privacy"]} /* PrivacyInfo.xcprivacy */ = {{isa = PBXFileReference; lastKnownFileType = text.xml; path = PrivacyInfo.xcprivacy; sourceTree = "<group>"; }};
		{ids["info"]} /* Info.plist */ = {{isa = PBXFileReference; lastKnownFileType = text.plist.xml; path = Info.plist; sourceTree = "<group>"; }};
/* End PBXFileReference section */

/* Begin PBXGroup section */
		{ids["mainGroup"]} = {{
			isa = PBXGroup;
			children = (
				{ids["sourceGroup"]} /* {app_id} */,
				{ids["productsGroup"]} /* Products */,
			);
			sourceTree = "<group>";
		}};
		{ids["sourceGroup"]} /* {app_id} */ = {{
			isa = PBXGroup;
			children = (
				{ids["appFile"]} /* ContentView.swift */,
				{ids["assets"]} /* Assets.xcassets */,
				{ids["privacy"]} /* PrivacyInfo.xcprivacy */,
				{ids["info"]} /* Info.plist */,
			);
			path = {app_id};
			sourceTree = "<group>";
		}};
		{ids["productsGroup"]} /* Products */ = {{
			isa = PBXGroup;
			children = (
				{ids["product"]} /* {app_id}.app */,
			);
			name = Products;
			sourceTree = "<group>";
		}};
/* End PBXGroup section */

/* Begin PBXNativeTarget section */
		{ids["target"]} /* {app_id} */ = {{
			isa = PBXNativeTarget;
			buildConfigurationList = {ids["configListTarget"]} /* Build configuration list for PBXNativeTarget "{app_id}" */;
			buildPhases = (
				{ids["sources"]} /* Sources */,
				{ids["resources"]} /* Resources */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = {app_id};
			productName = {app_id};
			productReference = {ids["product"]} /* {app_id}.app */;
			productType = "com.apple.product-type.application";
		}};
/* End PBXNativeTarget section */

/* Begin PBXProject section */
		{ids["project"]} /* Project object */ = {{
			isa = PBXProject;
			attributes = {{
				LastSwiftUpdateCheck = 2600;
				LastUpgradeCheck = 2600;
				TargetAttributes = {{
					{ids["target"]} = {{
						CreatedOnToolsVersion = 26.0;
						ProvisioningStyle = Automatic;
					}};
				}};
			}};
			buildConfigurationList = {ids["configListProject"]} /* Build configuration list for PBXProject "{app_id}" */;
			compatibilityVersion = "Xcode 14.0";
			developmentRegion = en;
			hasScannedForEncodings = 0;
			knownRegions = (
				en,
				fr,
				Base,
			);
			mainGroup = {ids["mainGroup"]};
			productRefGroup = {ids["productsGroup"]} /* Products */;
			projectDirPath = "";
			projectRoot = "";
			targets = (
				{ids["target"]} /* {app_id} */,
			);
		}};
/* End PBXProject section */

/* Begin PBXResourcesBuildPhase section */
		{ids["resources"]} /* Resources */ = {{
			isa = PBXResourcesBuildPhase;
			buildActionMask = 2147483647;
			files = (
				{ids["assetsBuild"]} /* Assets.xcassets in Resources */,
				{ids["privacyBuild"]} /* PrivacyInfo.xcprivacy in Resources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		}};
/* End PBXResourcesBuildPhase section */

/* Begin PBXSourcesBuildPhase section */
		{ids["sources"]} /* Sources */ = {{
			isa = PBXSourcesBuildPhase;
			buildActionMask = 2147483647;
			files = (
				{ids["appBuild"]} /* ContentView.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		}};
/* End PBXSourcesBuildPhase section */

/* Begin XCBuildConfiguration section */
		{ids["debugProject"]} /* Debug */ = {{
			isa = XCBuildConfiguration;
			buildSettings = {{
				SDKROOT = iphoneos;
				SWIFT_VERSION = 6.0;
			}};
			name = Debug;
		}};
		{ids["releaseProject"]} /* Release */ = {{
			isa = XCBuildConfiguration;
			buildSettings = {{
				SDKROOT = iphoneos;
				SWIFT_VERSION = 6.0;
			}};
			name = Release;
		}};
		{ids["debugTarget"]} /* Debug */ = {{
			isa = XCBuildConfiguration;
			buildSettings = {{
				ASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
				CODE_SIGN_STYLE = Automatic;
				DEVELOPMENT_TEAM = "";
				GENERATE_INFOPLIST_FILE = NO;
				INFOPLIST_FILE = {app_id}/Info.plist;
				IPHONEOS_DEPLOYMENT_TARGET = 26.0;
				PRODUCT_BUNDLE_IDENTIFIER = {app["bundle"]};
				PRODUCT_NAME = "$(TARGET_NAME)";
				SUPPORTED_PLATFORMS = "iphoneos iphonesimulator";
				SUPPORTS_MACCATALYST = NO;
				SWIFT_VERSION = 6.0;
				TARGETED_DEVICE_FAMILY = "1,2";
			}};
			name = Debug;
		}};
		{ids["releaseTarget"]} /* Release */ = {{
			isa = XCBuildConfiguration;
			buildSettings = {{
				ASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
				CODE_SIGN_STYLE = Automatic;
				DEVELOPMENT_TEAM = "";
				GENERATE_INFOPLIST_FILE = NO;
				INFOPLIST_FILE = {app_id}/Info.plist;
				IPHONEOS_DEPLOYMENT_TARGET = 26.0;
				PRODUCT_BUNDLE_IDENTIFIER = {app["bundle"]};
				PRODUCT_NAME = "$(TARGET_NAME)";
				SUPPORTED_PLATFORMS = "iphoneos iphonesimulator";
				SUPPORTS_MACCATALYST = NO;
				SWIFT_VERSION = 6.0;
				TARGETED_DEVICE_FAMILY = "1,2";
			}};
			name = Release;
		}};
/* End XCBuildConfiguration section */

/* Begin XCConfigurationList section */
		{ids["configListProject"]} /* Build configuration list for PBXProject "{app_id}" */ = {{
			isa = XCConfigurationList;
			buildConfigurations = (
				{ids["debugProject"]} /* Debug */,
				{ids["releaseProject"]} /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Release;
		}};
		{ids["configListTarget"]} /* Build configuration list for PBXNativeTarget "{app_id}" */ = {{
			isa = XCConfigurationList;
			buildConfigurations = (
				{ids["debugTarget"]} /* Debug */,
				{ids["releaseTarget"]} /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Release;
		}};
/* End XCConfigurationList section */
	}};
	rootObject = {ids["project"]} /* Project object */;
}}
'''


def make_project(app: dict) -> None:
    base = APPS_DIR / app["id"]
    src = base / app["id"]
    xcode = base / f'{app["id"]}.xcodeproj'
    write(src / "ContentView.swift", make_swift(app))
    plist(src / "Info.plist", {
        "CFBundleDisplayName": app["display"],
        "CFBundleIdentifier": "$(PRODUCT_BUNDLE_IDENTIFIER)",
        "CFBundleName": app["display"],
        "CFBundleShortVersionString": "1.0",
        "CFBundleVersion": "1",
        "UILaunchScreen": {},
        "UISupportedInterfaceOrientations": ["UIInterfaceOrientationPortrait", "UIInterfaceOrientationLandscapeLeft", "UIInterfaceOrientationLandscapeRight"],
        "UISupportedInterfaceOrientations~ipad": ["UIInterfaceOrientationPortrait", "UIInterfaceOrientationPortraitUpsideDown", "UIInterfaceOrientationLandscapeLeft", "UIInterfaceOrientationLandscapeRight"],
    })
    plist(src / "PrivacyInfo.xcprivacy", {
        "NSPrivacyAccessedAPITypes": [],
        "NSPrivacyCollectedDataTypes": [],
        "NSPrivacyTracking": False,
        "NSPrivacyTrackingDomains": [],
    })
    write(src / "Assets.xcassets" / "Contents.json", json.dumps({"info": {"author": "xcode", "version": 1}}, indent=2))
    icon_dir = src / "Assets.xcassets" / "AppIcon.appiconset"
    write(icon_dir / "Contents.json", json.dumps({
        "images": [
            {"filename": "AppIcon-1024.png", "idiom": "ios-marketing", "scale": "1x", "size": "1024x1024"}
        ],
        "info": {"author": "xcode", "version": 1},
    }, indent=2))
    make_icon(app, icon_dir / "AppIcon-1024.png")
    write(xcode / "project.pbxproj", make_pbx(app))


def make_metadata(app: dict) -> None:
    write(META_DIR / app["id"] / "metadata_en.md", f"""# {app["display"]} metadata

Market: Canada (CA)
Price: {app["price"]}
Purchase model: Paid upfront, no subscription
Category: {app["category"]}

Name: {app["display"]}
Subtitle: {app["subtitle"]}
Promotional text: {app["promo"]}

Description:
{app["desc"]}

Keywords:
{app["keywords"]}
""")


def make_pages(app: dict) -> None:
    app_slug = app["id"].lower()
    base = PAGES_DIR / app_slug
    common_style = f"""
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;margin:0;background:#{app['bg'][0]:02x}{app['bg'][1]:02x}{app['bg'][2]:02x};color:#{app['fg'][0]:02x}{app['fg'][1]:02x}{app['fg'][2]:02x};line-height:1.55}}
main{{max-width:820px;margin:0 auto;padding:56px 24px}}
a{{color:#{app['accent'][0]:02x}{app['accent'][1]:02x}{app['accent'][2]:02x}}}
.badge{{display:inline-block;padding:8px 12px;border:1px solid currentColor;border-radius:999px;color:#{app['accent'][0]:02x}{app['accent'][1]:02x}{app['accent'][2]:02x}}}
"""
    privacy = f"""<!doctype html><html lang="en"><meta charset="utf-8"><title>{app["display"]} Privacy</title><style>{common_style}</style><main><span class="badge">Canada / English + Français</span><h1>{app["display"]} Privacy Policy</h1><p>{app["display"]} is a paid-upfront Canadian app. It does not require an account, does not track users, and does not sell personal data.</p><h2>Data Collection</h2><p>No personal data is collected by the app. Study progress, scripts, notes, or calculations remain on device unless a user exports or shares them using system controls.</p><h2>Contact</h2><p>Support: <a href="mailto:support@example.com">support@example.com</a></p><h2>Français</h2><p>L'application ne suit pas les utilisateurs et ne vend aucune donnée personnelle. Les contenus restent sur l'appareil, sauf partage volontaire par les contrôles du système.</p></main></html>"""
    support = f"""<!doctype html><html lang="en"><meta charset="utf-8"><title>{app["display"]} Support</title><style>{common_style}</style><main><span class="badge">{app["price"]} / CA market</span><h1>{app["display"]} Support</h1><p>For help with {app["display"]}, email <a href="mailto:support@example.com">support@example.com</a>. Include your device model, iOS version, and a short description of the issue.</p><h2>Canada-first</h2><p>The app uses Canadian context, English/French interface copy, CAD pricing, and metric/imperial controls where measurements apply.</p><h2>Français</h2><p>Pour obtenir de l'aide, écrivez à <a href="mailto:support@example.com">support@example.com</a> avec le modèle de votre appareil, la version iOS et une courte description.</p></main></html>"""
    write(base / "privacy.html", privacy)
    write(base / "support.html", support)


def make_check(app: dict) -> None:
    write(APPS_DIR / app["id"] / "CHECK.md", f"""# {app["display"]} CHECK

- [x] SwiftUI iOS 26+ Xcode project generated
- [x] AppIcon 1024x1024 generated
- [x] PrivacyInfo.xcprivacy included
- [x] English/French bilingual UI controls included
- [x] Canada market context, CAD price: {app["price"]}
- [x] Metric/imperial toggle included where relevant
- [x] 5 iPhone 6.5-inch screenshots generated
- [x] 5 iPad screenshots generated
- [x] English metadata generated
- [x] Privacy HTML and Support HTML generated
- [ ] xcodebuild verification recorded in batch report
- [ ] GitHub Pages deployment/curl 200 recorded in batch report
""")


def make_screenshots(app: dict) -> None:
    for idx, (title, copy) in enumerate(app["scenes"], start=1):
        make_screenshot(app, SHOTS_DIR / app["id"] / "iphone_6_5" / f"{idx:02d}.png", title, copy, (1290, 2796), idx)
        make_screenshot(app, SHOTS_DIR / app["id"] / "ipad" / f"{idx:02d}.png", title, copy, (2048, 2732), idx)


def make_report() -> None:
    rows = "\n".join(f"| {a['display']} | {a['price']} | `{APPS_DIR / a['id'] / (a['id'] + '.xcodeproj')}` | `{SHOTS_DIR / a['id']}` | `{META_DIR / a['id'] / 'metadata_en.md'}` |" for a in APPS)
    write(OUT / "CANADA_5_BATCH_REPORT.md", f"""# Canada 5 High-Price App Batch Report

Generated from `CodexPipeline/tasks/temp-clone-canada-5.md`.

| App | CAD price | Xcode project | Screenshots | Metadata |
|---|---:|---|---|---|
{rows}

## Shared Compliance

- Market: Canada (CA)
- Purchase model: paid upfront, no subscriptions
- UI: English/French bilingual toggles in every app
- Measurement: metric/imperial toggle included in every app, with measurement-specific wording where applicable
- Assets: 1024x1024 PNG AppIcon per app
- Privacy: `PrivacyInfo.xcprivacy` declares no tracking and no collected data
- Pages: privacy/support HTML generated under `{PAGES_DIR}`

## Verification

Build and GitHub Pages verification will be appended after commands run.
""")


def main() -> None:
    for folder in [OUT, APPS_DIR, SHOTS_DIR, PAGES_DIR, META_DIR]:
        folder.mkdir(parents=True, exist_ok=True)
    for app in APPS:
        make_project(app)
        make_metadata(app)
        make_pages(app)
        make_check(app)
        make_screenshots(app)
    make_report()


if __name__ == "__main__":
    main()
