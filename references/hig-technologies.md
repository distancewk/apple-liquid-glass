# Apple HIG Technology Boundaries for Web Pages

## Contents

- [Use this guide](#use-this-guide)
- [Universal rules](#universal-rules)
- [Intelligence and automation](#intelligence-and-automation)
- [Identity, payments, and private data](#identity-payments-and-private-data)
- [Contextual capabilities](#contextual-capabilities)
- [Technology acceptance](#technology-acceptance)
- [Official sources](#official-sources)

## Use this guide

Read this only when a page exposes a product capability rather than ordinary interface behavior. The purpose is to prevent a visually Apple-like page from making an untruthful promise about AI, identity, payments, health, location, media, automation, or system integration.

## Universal rules

- State the value, data source, and user control before asking for data or commitment.
- Request the smallest useful scope at the moment of need; offer a refusal, retry, or manual alternative where the core task can still continue.
- Separate generated, inferred, estimated, or delayed information from confirmed user data. Give people a way to inspect, correct, or opt out when an automated result affects them.
- Use actual platform branding, buttons, claims, and entitlements only when the product has them. A web demo may describe an integration prospectively but must not impersonate a system surface.

## Intelligence and automation

- Machine-learning or generative features explain what they do, distinguish suggestion from decision, and preserve user agency for important outcomes.
- Surface source/attribution, uncertainty, correction, and feedback when they help people calibrate trust. Avoid proactive automation that makes consequential changes without a clear, reversible control.
- Keep an ordinary route through the task if an intelligent feature is complementary. If intelligence is critical, communicate fallback, loading, failure, and limits rather than simulating certainty.

## Identity, payments, and private data

- Authentication names the real available method and provides account recovery. Do not imply device biometrics, passkeys, or Sign in with Apple without a supported integration.
- Payments make price, currency, items, recurring terms, and commitment clear before confirmation. Never style an ordinary action as Apple Pay or use protected marks without authorization.
- Health, location, contacts, camera, microphone, and similar data flows minimize scope, give a timely rationale, and preserve a meaningful denial state. Do not collect data merely to personalize visual atmosphere.

## Contextual capabilities

- Maps, media, Home, workouts, games, and other contextual surfaces keep content primary, make current state obvious, and offer a safe recovery when a device/service is unavailable.
- Siri, Shortcuts, widgets, App Clips, and notifications represent a focused task that can be understood without opening the full product. A web page may offer an equivalent shortcut, but should not imitate system placement or imply unavailable background execution.
- Spatial/immersive ideas translate to web only when the product actually needs depth and motion. Protect comfort: minimize peripheral motion, avoid head-locked metaphors, and provide an ordinary 2D path.

## Technology acceptance

Before preview, record: capability; whether it is real, mocked, or future; user benefit; data/permission scope; user control and cancellation; fallback; error/retry state; required legal/brand review. If these cannot be written plainly, remove the capability from the page brief.

## Official sources

- [Technologies](https://developer.apple.com/design/human-interface-guidelines/technologies)
- [Machine learning](https://developer.apple.com/design/human-interface-guidelines/machine-learning)
- [Generative AI](https://developer.apple.com/design/human-interface-guidelines/generative-ai)
- [Privacy](https://developer.apple.com/design/human-interface-guidelines/privacy)
- [Managing accounts](https://developer.apple.com/design/human-interface-guidelines/managing-accounts)
- [Apple Pay](https://developer.apple.com/design/human-interface-guidelines/apple-pay)
