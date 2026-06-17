import SwiftUI

@main
struct RPASDeckCAApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}

struct ContentView: View {
    @State private var french = false
    @State private var metric = true
    @State private var selected = 0

    private let tabs = ["Deck", "Airspace", "Preflight"]
    private let tabsFR = ["Cartes", "Espace", "Prévol"]
    private let features = ["Basic/Advanced topic decks", "Airspace and NOTAM checks", "Pre-flight risk board", "Metric/imperial altitude and wind"]
    private let featuresFR = ["Jeux Basic/Advanced", "Espace aérien et NOTAM", "Tableau de risque prévol", "Altitude et vent métrique/impérial"]

    var body: some View {
        ZStack {
            LinearGradient(colors: [Color(hex: "08121F"), Color(hex: "14385C")], startPoint: .topLeading, endPoint: .bottomTrailing)
                .ignoresSafeArea()
            ScrollView {
                VStack(alignment: .leading, spacing: 22) {
                    header
                    instrumentPanel
                    featureGrid
                    reviewPanel
                }
                .padding(22)
            }
        }
    }

    private var header: some View {
        VStack(alignment: .leading, spacing: 14) {
            HStack {
                Label("RPAS Deck CA", systemImage: "airplane")
                    .font(.system(.title2, design: .rounded, weight: .bold))
                    .foregroundStyle(accent)
                Spacer()
                Text("CAD $39.99")
                    .font(.system(.callout, design: .rounded, weight: .semibold))
                    .foregroundStyle(foreground.opacity(0.76))
            }
            Text(french ? "Réussissez l'examen RPAS canadien" : "Pass the Canadian RPAS exam")
                .font(.system(size: 38, weight: .black, design: .rounded))
                .foregroundStyle(foreground)
                .fixedSize(horizontal: false, vertical: true)
            Text(french ? "Cartes d'étude bilingues, exercices d'espace aérien, météo minimale et séquence prévol avec terminologie de Transports Canada." : "Bilingual study decks, airspace drills, weather minima, and a pre-flight flow built around Transport Canada terminology.")
                .font(.system(.body, design: .rounded, weight: .medium))
                .foregroundStyle(foreground.opacity(0.78))
            HStack(spacing: 12) {
                TogglePill(title: french ? "FR" : "EN", icon: "character.bubble", isOn: $french)
                TogglePill(title: metric ? "Metric" : "Imperial", icon: "ruler", isOn: $metric)
            }
        }
    }

    private var instrumentPanel: some View {
        VStack(alignment: .leading, spacing: 18) {
            HStack {
                ForEach(Array((french ? tabsFR : tabs).enumerated()), id: \.offset) { index, label in
                    Button {
                        withAnimation(.spring(response: 0.35, dampingFraction: 0.82)) { selected = index }
                    } label: {
                        Label(label, systemImage: ["map", "checklist", "wind"][index])
                            .font(.system(.caption, design: .rounded, weight: .bold))
                            .frame(maxWidth: .infinity)
                            .padding(.vertical, 12)
                            .background(selected == index ? accent : foreground.opacity(0.10), in: RoundedRectangle(cornerRadius: 16, style: .continuous))
                            .foregroundStyle(selected == index ? Color(hex: "08121F") : foreground)
                    }
                    .buttonStyle(.plain)
                }
            }
            ZStack {
                RoundedRectangle(cornerRadius: 28, style: .continuous)
                    .fill(.ultraThinMaterial.opacity(0.7))
                    .overlay(RoundedRectangle(cornerRadius: 28).stroke(accent.opacity(0.65), lineWidth: 1.5))
                VStack(spacing: 18) {
                    Image(systemName: "location.north.line")
                        .font(.system(size: 58, weight: .bold))
                        .symbolRenderingMode(.hierarchical)
                        .foregroundStyle(accent)
                    Text((french ? tabsFR : tabs)[selected])
                        .font(.system(.title, design: .rounded, weight: .black))
                        .foregroundStyle(foreground)
                    Text(metric ? "km / m / °C" : "mi / ft / °F")
                        .font(.system(.headline, design: .rounded, weight: .bold))
                        .foregroundStyle(accent)
                }
                .padding(30)
            }
            .frame(minHeight: 250)
        }
    }

    private var featureGrid: some View {
        LazyVGrid(columns: [GridItem(.adaptive(minimum: 154), spacing: 14)], spacing: 14) {
            ForEach(Array((french ? featuresFR : features).enumerated()), id: \.offset) { index, text in
                VStack(alignment: .leading, spacing: 14) {
                    Image(systemName: ["airplane", "map", "checklist", "wind"][index])
                        .font(.system(size: 24, weight: .bold))
                        .foregroundStyle(accent)
                    Text(text)
                        .font(.system(.headline, design: .rounded, weight: .bold))
                        .foregroundStyle(foreground)
                        .fixedSize(horizontal: false, vertical: true)
                }
                .frame(maxWidth: .infinity, minHeight: 112, alignment: .topLeading)
                .padding(18)
                .background(foreground.opacity(0.10), in: RoundedRectangle(cornerRadius: 18, style: .continuous))
            }
        }
    }

    private var reviewPanel: some View {
        VStack(alignment: .leading, spacing: 10) {
            Text(french ? "Conçu pour le Canada" : "Designed for Canada")
                .font(.system(.title3, design: .rounded, weight: .black))
                .foregroundStyle(foreground)
            Text(french ? "Interface anglais/français, prix en CAD, contexte canadien et unités commutables." : "English/French interface, CAD pricing, Canadian context, and switchable units.")
                .font(.system(.body, design: .rounded, weight: .medium))
                .foregroundStyle(foreground.opacity(0.76))
        }
        .padding(22)
        .background(accent.opacity(0.16), in: RoundedRectangle(cornerRadius: 22, style: .continuous))
    }

    private var accent: Color { Color(hex: "2AABE2") }
    private var foreground: Color { Color(hex: "E8F6FF") }
}

struct TogglePill: View {
    let title: String
    let icon: String
    @Binding var isOn: Bool
    var body: some View {
        Button { isOn.toggle() } label: {
            Label(title, systemImage: icon)
                .font(.system(.caption, design: .rounded, weight: .bold))
                .padding(.horizontal, 14)
                .padding(.vertical, 10)
                .background(.white.opacity(0.14), in: Capsule())
        }
        .buttonStyle(.plain)
        .foregroundStyle(.white)
    }
}

extension Color {
    init(hex: String) {
        let scanner = Scanner(string: hex)
        var value: UInt64 = 0
        scanner.scanHexInt64(&value)
        let red = Double((value >> 16) & 0xff) / 255.0
        let green = Double((value >> 8) & 0xff) / 255.0
        let blue = Double(value & 0xff) / 255.0
        self.init(red: red, green: green, blue: blue)
    }
}
