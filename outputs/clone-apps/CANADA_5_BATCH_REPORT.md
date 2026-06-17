# Canada 5 High-Price App Batch Report

Generated from `CodexPipeline/tasks/temp-clone-canada-5.md`.

| App | CAD price | Xcode project | Screenshots | Metadata |
|---|---:|---|---|---|
| RPAS Deck CA | CAD $39.99 | `/Users/ethanqifeng/Documents/加拿大APP市场调查。/outputs/clone-apps/apps/RPASDeckCA/RPASDeckCA.xcodeproj` | `/Users/ethanqifeng/Documents/加拿大APP市场调查。/outputs/clone-apps/screenshots/RPASDeckCA` | `/Users/ethanqifeng/Documents/加拿大APP市场调查。/outputs/clone-apps/metadata/RPASDeckCA/metadata_en.md` |
| ExamCards CA | CAD $24.99 | `/Users/ethanqifeng/Documents/加拿大APP市场调查。/outputs/clone-apps/apps/ExamCardsCA/ExamCardsCA.xcodeproj` | `/Users/ethanqifeng/Documents/加拿大APP市场调查。/outputs/clone-apps/screenshots/ExamCardsCA` | `/Users/ethanqifeng/Documents/加拿大APP市场调查。/outputs/clone-apps/metadata/ExamCardsCA/metadata_en.md` |
| WinterOBD CA | CAD $24.99 | `/Users/ethanqifeng/Documents/加拿大APP市场调查。/outputs/clone-apps/apps/WinterOBDCA/WinterOBDCA.xcodeproj` | `/Users/ethanqifeng/Documents/加拿大APP市场调查。/outputs/clone-apps/screenshots/WinterOBDCA` | `/Users/ethanqifeng/Documents/加拿大APP市场调查。/outputs/clone-apps/metadata/WinterOBDCA/metadata_en.md` |
| ConduitMate CA | CAD $14.99 | `/Users/ethanqifeng/Documents/加拿大APP市场调查。/outputs/clone-apps/apps/ConduitMateCA/ConduitMateCA.xcodeproj` | `/Users/ethanqifeng/Documents/加拿大APP市场调查。/outputs/clone-apps/screenshots/ConduitMateCA` | `/Users/ethanqifeng/Documents/加拿大APP市场调查。/outputs/clone-apps/metadata/ConduitMateCA/metadata_en.md` |
| TelePrompt CA | CAD $29.99 | `/Users/ethanqifeng/Documents/加拿大APP市场调查。/outputs/clone-apps/apps/TelePromptCA/TelePromptCA.xcodeproj` | `/Users/ethanqifeng/Documents/加拿大APP市场调查。/outputs/clone-apps/screenshots/TelePromptCA` | `/Users/ethanqifeng/Documents/加拿大APP市场调查。/outputs/clone-apps/metadata/TelePromptCA/metadata_en.md` |

## Shared Compliance

- Market: Canada (CA)
- Purchase model: paid upfront, no subscriptions
- UI: English/French bilingual toggles in every app
- Measurement: metric/imperial toggle included in every app, with measurement-specific wording where applicable
- Assets: 1024x1024 PNG AppIcon per app
- Privacy: `PrivacyInfo.xcprivacy` declares no tracking and no collected data
- Pages: privacy/support HTML generated under `/Users/ethanqifeng/Documents/加拿大APP市场调查。/outputs/clone-apps/pages`

## Verification

- xcodebuild: all five projects passed `xcodebuild -project ... -sdk iphonesimulator -configuration Debug CODE_SIGNING_ALLOWED=NO build` on Xcode 26.5.
- GitHub repository: https://github.com/dgzf2tdv7m-dev/canada-5-app-batch
- GitHub Pages: https://dgzf2tdv7m-dev.github.io/canada-5-app-batch/
- Pages deployment: GitHub Actions run `27701050581` completed successfully.
- curl 200 checks:
  - https://dgzf2tdv7m-dev.github.io/canada-5-app-batch/rpasdeckca/privacy.html
  - https://dgzf2tdv7m-dev.github.io/canada-5-app-batch/rpasdeckca/support.html
  - https://dgzf2tdv7m-dev.github.io/canada-5-app-batch/examcardsca/privacy.html
  - https://dgzf2tdv7m-dev.github.io/canada-5-app-batch/winterobdca/support.html
  - https://dgzf2tdv7m-dev.github.io/canada-5-app-batch/conduitmateca/privacy.html
  - https://dgzf2tdv7m-dev.github.io/canada-5-app-batch/telepromptca/support.html

## Spec and Audit Files

- `outputs/clone-apps/specs/RPAS_DECK_CA_SPEC.md`
- `outputs/clone-apps/specs/EXAMCARDS_CA_SPEC.md`
- `outputs/clone-apps/specs/WINTEROBD_CA_SPEC.md`
- `outputs/clone-apps/specs/CONDUITMATE_CA_SPEC.md`
- `outputs/clone-apps/specs/TELEPROMPT_CA_SPEC.md`
- `outputs/clone-apps/specs/VISUAL_CANADA_AUDIT.md`
