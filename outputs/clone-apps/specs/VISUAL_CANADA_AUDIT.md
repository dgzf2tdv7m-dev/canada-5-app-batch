# Visual + Canada Compliance Audit Checklist

Scope: Canada 5 high-price app batch. This checklist covers visual polish and Canada-only compliance expectations for all five apps. It is intentionally limited to audit/spec guidance and does not require touching implementation directories.

## Five-App Signoff Matrix

| Audit area | App 1 | App 2 | App 3 | App 4 | App 5 |
| --- | --- | --- | --- | --- | --- |
| English/French bilingual UI complete | TBD | TBD | TBD | TBD | TBD |
| Canada-only content and examples | TBD | TBD | TBD | TBD | TBD |
| No US/UK regulation references | TBD | TBD | TBD | TBD | TBD |
| Metric/imperial handling reviewed | TBD | TBD | TBD | TBD | TBD |
| High-price visual polish approved | TBD | TBD | TBD | TBD | TBD |
| Required outputs present | TBD | TBD | TBD | TBD | TBD |
| App Store privacy/support expectations met | TBD | TBD | TBD | TBD | TBD |

## 1. English/French Bilingual UI

- Every user-facing screen has English and Canadian French copy, including onboarding, paywalls, empty states, errors, confirmation messages, settings, account flows, notifications, and legal/support links.
- Language switching is visible, persistent, and reversible without account deletion or app reinstall.
- French text is not machine-literal where product trust matters. Review tone for Canadian French usage, especially billing, health, finance, identity, legal, and customer support language.
- Layouts are tested with longer French strings. Buttons, segmented controls, tabs, cards, form labels, and modals must not clip, overlap, or shrink into illegibility.
- App Store metadata expectations are covered in both languages where submitted: app name/subtitle if localized, description, screenshots, keywords, privacy/support URLs, promotional text, and in-app purchase names.
- Screenshots and preview flows include bilingual evidence or separate English/French localized assets.

## 2. Canada-Only Context

- Currency appears as CAD or Canadian dollars where prices, budgets, plans, taxes, payouts, invoices, or comparisons are shown.
- Examples use Canadian locations, addresses, provinces/territories, postal codes, phone formats, public holidays, and local terminology where relevant.
- Any regional choices include provinces and territories, not US states or UK counties.
- Date, time, and number formats are appropriate for Canadian audiences and localization mode. Avoid hardcoding US-only formats when the UI can infer locale.
- Maps, region filters, service availability, shipping, tax, climate, healthcare, insurance, education, employment, and public-sector references must be Canada-specific.
- Remove or rewrite references to US/UK regulators, laws, programs, taxes, benefits, agencies, or compliance schemes unless the app explicitly explains them as foreign context. For this batch, default expectation is no US/UK regulation references.

## 3. Metric/Imperial Handling

- Use metric by default for Canadian context where applicable: kilometres, metres, centimetres, kilograms, grams, litres, Celsius, kPa, square metres, hectares.
- Provide imperial equivalents only where a Canadian user would reasonably expect them, such as height, weight, real estate area, construction, some automotive contexts, recipes, or legacy user preference.
- Unit labels are explicit. Avoid ambiguous abbreviations where safety, finance, health, travel, or purchasing decisions depend on precision.
- Conversion behavior is consistent across onboarding, profile settings, calculators, charts, exports, and notifications.
- Forms validate both accepted unit systems when a toggle is offered, and preserve the user's selected unit preference.
- Charts and comparisons label axes and tooltips with units in both English and French localization.

## 4. High-Price Visual Polish

- First impression supports a premium price point: confident hierarchy, restrained density, deliberate spacing, crisp imagery, polished icons, and no generic template feel.
- Typography is consistent across screen classes. Headings, labels, numeric data, helper text, and legal text have clear roles and sufficient contrast.
- Primary actions are visually decisive and consistent. Destructive, secondary, and disabled states are unmistakable.
- Paywall or purchase screens clearly communicate value without visual clutter, dark-pattern pressure, misleading countdowns, or hidden renewal terms.
- Core workflows feel finished: loading states, skeletons, empty states, success states, error recovery, offline states, and permission-denied states are designed, not left as defaults.
- Premium screens avoid low-effort signals: mismatched icon styles, uneven radii, inconsistent shadows, muddy gradients, cramped cards, stock-like imagery, placeholder copy, or unlocalized screenshots.
- Accessibility polish is visible: dynamic type tolerance, contrast, tap targets, focus order, reduced-motion handling, and screen reader labels for icon-only controls.
- Mobile layouts are verified on small and large iPhone sizes. No text or controls should overlap safe areas, tab bars, keyboard areas, modals, or system permission sheets.

## 5. Required Outputs

For each of the five apps, confirm the delivery package includes:

- App-specific product summary for the Canadian market.
- English and French UI/copy coverage notes.
- Visual audit screenshots or screen list covering onboarding, main workflow, settings, paywall/purchase, errors/empty states, and support/privacy access.
- Canada localization notes, including currency, region, unit, and regulatory/context review.
- Privacy/support readiness notes for App Store submission.
- Open issues list with severity, owner, and expected fix location.
- Final pass/fail recommendation for launch-readiness in Canada.

## 6. App Store Privacy and Support Expectations

- Privacy policy URL is present, reachable, and appropriate for Canadian users.
- Support URL is present, reachable, and offers a real path to help in English and French or clearly states support language coverage.
- App Privacy nutrition label data matches actual collection, tracking, third-party SDKs, analytics, crash reporting, ads, account data, purchase data, location, contacts, health, finance, and user-generated content behavior.
- Permission prompts are contextual, concise, bilingual where app-controlled copy appears, and aligned with the feature that needs access.
- Account deletion is available in-app when account creation is supported, including explanation of data deletion/retention where relevant.
- Subscriptions and in-app purchases clearly show CAD pricing, billing period, renewal behavior, cancellation path, trial terms, and what remains available without purchase.
- Contact, complaint, and data-rights language avoids US/UK-only references. For Canada, review privacy language against Canadian expectations and applicable provincial context without citing irrelevant foreign regimes.
- Age rating, content warnings, medical/financial/legal disclaimers, and user-generated content moderation disclosures match the actual app behavior.

## 7. Red-Flag Items

Do not approve an app until these are resolved:

- English-only UI in any core path.
- French UI that clips, overlaps, or blocks purchase/account completion.
- Prices shown in USD, GBP, or unlabeled dollars.
- US states, ZIP codes, IRS/FDA/FTC/HIPAA/CCPA, UK GDPR/ICO/HMRC/NHS, or other non-Canada references presented as local requirements.
- Missing privacy policy or support URL.
- Paywall lacking renewal, trial, or cancellation clarity.
- Screenshots that show non-Canadian geography, currency, regulation, or store metadata for the Canada build.
- Default template visuals on premium purchase-critical screens.

## 8. Auditor Notes Template

Use one block per app:

```text
App:
Audit date:
Auditor:

Bilingual UI:
Canada-only context:
Metric/imperial:
Visual polish:
Required outputs:
Privacy/support:

Blocking issues:
Non-blocking issues:
Launch recommendation: Pass / Conditional pass / Fail
```
