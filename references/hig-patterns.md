# Apple HIG Patterns for Web Flows

## Contents

- [Use this guide](#use-this-guide)
- [Navigation and discovery](#navigation-and-discovery)
- [Entry, identity, and permissions](#entry-identity-and-permissions)
- [Feedback, recovery, and state](#feedback-recovery-and-state)
- [Preferences, help, sharing, and files](#preferences-help-sharing-and-files)
- [Pattern choice table](#pattern-choice-table)
- [Official sources](#official-sources)

## Use this guide

Read the sections matching the page’s user task before composition. A pattern defines the sequence, information, and recovery path; components merely render its individual steps. Never create an onboarding, alert, account wall, or permission prompt just to make a page look more app-like.

## Navigation and discovery

- Choose navigation from the information architecture: tabs switch peer top-level areas; a sidebar navigates broad peer areas; a back control returns within a hierarchy; a toolbar holds contextual actions; a sheet focuses a temporary task.
- Give search one discoverable home. Make its scope clear, retain query context, offer useful suggestions/filters only when they aid retrieval, and give a `No results` state that explains the outcome and preserves/corrects the query.
- Onboarding is optional, brief, and interactive. Teach a task in context or through a contextual tip; let people skip it and find help again later. Do not make launch screens explain system behavior.

## Entry, identity, and permissions

- Ask for an account only when core value requires it. Let people inspect useful content first when possible, explain the account benefit plainly, and prefer a supported, trustworthy authentication path such as passkeys or an actual Sign in with Apple integration.
- A sign-in button identifies its real method (`Continue with passkey`, `Sign In with Face ID` only when available). Never call an app password a device passcode, never prefill passwords, and provide direct recovery/help.
- Ask for permission at the moment its related feature is invoked, not indiscriminately at launch. Explain the precise benefit before system consent, request the minimum scope, allow refusal, and show a useful path when access is denied.
- A web mockup must not claim native biometric, system-account, or permission behavior it cannot provide. Label a demo/placeholder truthfully or omit the control.

## Feedback, recovery, and state

- Put ordinary status near the item it describes. Use inline validation as soon as it can prevent a mistake; pair the message with the field and an actionable correction.
- Match interruption to consequence: quiet progress/status for routine events; inline message for reversible/correctable problems; confirmation for a rare, consequential irreversible action; alert/modal only when a decision cannot safely wait.
- Offer Undo for a logical sequence of reversible edits, name the affected operation when helpful, and visibly show the result after undo/redo. Do not use an irreversible error dialog where an undo affordance would preserve agency.
- Loading preserves structure, names what is happening when duration is material, and never replaces a task with an endless animated ornament. Empty states say what is absent and the next useful action.

## Preferences, help, sharing, and files

- Choose defaults that serve most people. Keep global preferences few, stable, and discoverable; put task-specific adjustments next to the task rather than exiling them to Settings.
- Help is context-sensitive and close to the point of uncertainty. Do not add an opaque question-mark action if a short label, hint, or inline explanation would solve the problem directly.
- Share the user’s selected content with an explicit title/preview and a familiar share action. Don’t surprise people by exporting extra private data.
- File/media flows use standard-looking selection, upload, progress, failure, and retry states. Support drag/drop and paste where they are natural, while keeping an explicit picker/action alternative.

## Pattern choice table

| If the user needs to… | Start with this pattern | Must be visible |
| --- | --- | --- |
| Find known content | Search | scope, query, results, empty/recovery state |
| Learn a new capability | Contextual tip/onboarding | task benefit, Skip/exit, later help path |
| Create or sign in to an account | Account management | why account matters, actual method, recovery |
| Provide sensitive or structured data | Data entry | labels, required/optional state, validation, next action |
| Grant protected access | Permission | feature benefit, timing, refusal/fallback |
| Wait, succeed, fail, or recover | Feedback | state, cause, next action, accessible cue |
| Change a reversible result | Undo/redo | affected operation, visible result, repeatability |
| Change global behavior | Settings | useful default, limited options, stable location |
| Commit or abandon a focused subtask | Modal/sheet | context, Cancel/dismiss, clear commit action |

## Official sources

- [Onboarding](https://developer.apple.com/design/human-interface-guidelines/onboarding)
- [Entering data](https://developer.apple.com/design/human-interface-guidelines/entering-data)
- [Managing accounts](https://developer.apple.com/design/human-interface-guidelines/managing-accounts)
- [Privacy and requesting permission](https://developer.apple.com/design/human-interface-guidelines/privacy)
- [Feedback](https://developer.apple.com/design/human-interface-guidelines/feedback)
- [Undo and redo](https://developer.apple.com/design/human-interface-guidelines/undo-and-redo)
- [Settings](https://developer.apple.com/design/human-interface-guidelines/settings)
- [Search fields](https://developer.apple.com/design/human-interface-guidelines/search-fields)
