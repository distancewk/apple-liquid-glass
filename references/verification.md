# Verification Playbook

## Contents

- [Static checks](#static-checks)
- [Browser capability preflight](#browser-capability-preflight)
- [Preview gate](#preview-gate)
- [DOM and CSS checks](#dom-and-css-checks)
- [Browser checks](#browser-checks)
- [Fallback and accessibility](#fallback-and-accessibility)
- [Evidence](#evidence)

## Static checks

Static checks prove that the reusable contract is present. They do **not** prove that a target browser rendered refraction, that background changes are visible, or that a produced page follows the component grammar. Treat this as Level 1 only.

Run the dependency-free validator from the skill directory:

```bash
python3 scripts/validate_skill.py .
python3 scripts/extract_html_example.py \
  --source references/vanilla-example.md \
  --output /tmp/apple-liquid-glass/index.html
```

Run the project's type check and build when the page is part of a project. The extracted fixture must contain the four real layer classes and the SVG filter definition.

The bundled fixture is also a scroll test. The dependency-free validator must reject it if it loses its long page, `overflow-y: auto`, sticky glass control, real button, or reduced-transparency fallback.

## Browser capability preflight

Before designing the page, serve the unchanged fixture from a local HTTP origin in the target browser or closest target engine. Place it over the supplied detailed scene and record:

```text
engine/version · viewport · outer filter declaration · visible rim displacement · selected mode (reference/fallback)
```

Use the browser screenshot to decide the selected mode. A successful `CSS.supports` query or computed `backdropFilter` value is structural evidence only. If the reference rim is not visually readable, set `data-glass-mode="fallback"` before page composition and retain evidence of the readable fallback.

## Preview gate

Record the selected delivery mode before generating: `preview` is the default; `full` requires an explicit user request to complete the page or all named screens; `iterate` revises only an existing preview or page. In every mode, verify one representative slice in a browser. The slice must be structurally identical to the intended final implementation and must demonstrate the detailed background, four material layers, translucent control, the preflight-selected material mode, and at least one applicable interaction state. For a scrollable page, it must also demonstrate scroll-through color change. For a non-scrollable page, verify translucency and resting-state legibility against its meaningful static scene; do not add synthetic scrolling solely for this test. Keep copy and content count small.

In `preview` mode, show the preview or its screenshot and ask the user to judge the material and direction. Stop there until the user explicitly approves or requests a revision. In `full` mode, record the same evidence and continue; in `iterate` mode, change only the relevant variable and repeat the preview. Do not treat silence, a local build pass, or an internal visual check as approval to expand.

After approval in `preview` mode — or directly in `full` mode — reuse the preview material contract and expand the page; then create additional cases with content-specific compositions. Record the selected mode, approval/revision decision when applicable, and browser evidence.

Resolve preview conflicts in this order: accessibility and operability, the strict Apple profile, the liquid-glass material contract, then named product content. A conflicting brand or art direction requires an explicit decision to leave this skill's strict profile; do not blend it into the preview.

Apply the Foundation and HIG visual-grammar guides during the preview. The preview must have a clear task, semantic color, functional glass, readable resting state, familiar controls, and no unrequested decorative atmosphere. Record the evidence rather than duplicating the foundation rules here.

## DOM and CSS checks

For every glass wrapper, assert:

```js
document.querySelectorAll('.liquid_glass-wrapper').length > 0
document.querySelectorAll('.liquid_glass-outer').length === wrapperCount
document.querySelectorAll('.liquid_glass-cover').length === wrapperCount
document.querySelectorAll('.liquid_glass-sharp').length === wrapperCount
document.querySelectorAll('.liquid_glass-reflect').length === wrapperCount
document.querySelector('#liquid_glass_filter')
```

Also assert:

- `getComputedStyle(outer).backdropFilter` contains `url("#liquid_glass_filter")` or the equivalent URL serialization;
- the cover has `background: rgba(0, 0, 0, 0.12)` and `backdrop-filter: blur(2px)`;
- the sharp layer has the two one-pixel inset highlights;
- the reflect layer has the two directional inset shadows;
- content is above the four layers at `z-index: 4`.
- the SVG contains the reference `feDisplacementMap` with `scale="200"`;
- the reference filter is defined once before wrappers;
- the intended background is not hidden behind an opaque wrapper or ancestor;
- the selected shape profile has a matching inner mask; do not use the rounded-reference mask for a pill or circle;

## Design acceptance

Before checking CSS, confirm the page has:

- a one-sentence purpose and a clear common path;
- one coherent strict Apple foundation and a task-relevant content anchor only when the product has one;
- a content hierarchy that distinguishes primary, secondary, supporting, and action content;
- explicit idle, hover, press, focus, drag, release, disabled, and reduced-motion behavior where applicable;
- spatially consistent transitions that remain interruptible;
- readable typography, focus indicators, touch targets, and reduced-transparency/high-contrast behavior.
- a content-first composition with no unearned marketing copy or decorative AI-style atmosphere;
- a stated semantic job for every non-neutral color, limited to `accent`, `link`, `selection`, `status`, or `content asset`; one application tint and only necessary status colors; light/dark/increased-contrast variants are defined;
- Apple-style color roles are used consistently: neutral system-like surfaces and labels, a restrained app tint, status colors only for status, and scene colors kept separate from interface accents;
- glass reserved for functional hierarchy rather than applied indiscriminately to every module.
- content and controls are visibly separated, with structural glass used only to carry or organize a functional layer, never as content decoration;
- the first/resting view remains readable before any scrolling or interaction changes the backdrop;
- custom colors have light, dark, and increased-contrast behavior, and no state relies on color alone;
- custom buttons provide a visible press state and touch targets are at least 44 CSS px where touch input is expected;
- labels use concise verbs and errors explain how to recover next to the affected field;
- nested rounded surfaces use related, concentric geometry instead of arbitrary corner radii.

Record the following page-level audit answers before preview approval: primary task, primary action, reason for each glass surface, semantic role of each non-neutral color, resting-state legibility, rejected decoration, adaptation behavior for small screens, large text, dark mode, high contrast, reduced transparency, RTL, and long text, plus the HIG route (Foundations and every selected Pattern, Component/Input, and Technology guide). For a page involving data, identity, permissions, automation, or a consequential action, also record the data/commitment boundary, user control, recovery, and fallback. A preview with missing answers or an unclear primary action is not ready for approval.

## Final Apple Conformance Review

Run this review after the complete page is implemented and after the last visual change, not only before the preview. Record `PASS` or `FAIL` for every item. A page is not complete while any item is `FAIL` or unverified.

- The primary task, common path, hierarchy, and action labels are clear without decorative marketing copy.
- Every non-neutral color has a semantic role and an explicit light/dark/increased-contrast treatment; one restrained app tint is used consistently and status colors are reserved for status.
- Yellow, blue, red, green, orange, teal, purple, and other hues are justified by action, link, brand, selection, status, or scene content rather than screenshot decoration.
- Liquid Glass is limited to functional hierarchy, uses the neutral reference cover, and is not multiplied or chromatically tinted to create atmosphere.
- Content, standard-material groups, and Liquid Glass controls occupy distinct visual planes; media extends beneath floating chrome only when it is meaningful product content.
- Button shape, placement, and grouping match the role: isolated icon actions are circular, related actions share a compact group, text actions use an appropriate capsule or rounded rectangle, and there is no blanket pill treatment.
- For every compact command group, there is exactly one outer material vessel; members have contiguous hit regions, and hover/pressed/selected treatment is a local surface clipped within that vessel rather than a nested glass pill. Independent horizontal actions may remain separate only when they are genuinely independent targets.
- Rounded insets are geometrically related to their containers: a uniform inset reduces the parent radius by the inset amount, capsules retain half-height end radii, and circles remain square in layout. No arbitrary radius is introduced merely to decorate a child.
- Toolbars, sidebars, tab bars, cards, search, modality, and input/recovery follow the familiar HIG pattern for the page’s task rather than a screenshot-derived approximation.
- The page brief names the HIG route used; every task-specific control is traceable to a familiar pattern/component and every technology claim states whether it is real, mock, or future behavior.
- Account, permission, payment, sensitive-data, automated, destructive, and failure paths clearly explain what will happen, retain user control, and offer the relevant cancellation, correction, retry, or undo path.
- Typography, contrast, focus, press feedback, touch targets, and non-color status cues remain usable.
- Light/dark appearance, high contrast, forced colors, reduced transparency, reduced motion, small screens, long text, locale, and RTL remain usable.
- The strict profile passes: no unclassified UI color, decorative gradient/glow/texture, floating ornament, unjustified repeated glass pill, rounded-card wall, invented slogan, or display-style hierarchy that competes with the task. Separate pills remain acceptable for truly independent peer actions.

If any item fails, fix the smallest relevant variable, repeat the browser and screenshot checks, and update the record. Explicit product or brand direction may override the Apple visual defaults only when it remains accessible and preserves the material contract.

## Composition acceptance

When reviewing more than one page or case:

- the pages do not reuse the same full-width bar or rounded-card silhouette for every major module;
- each case has a distinct primary composition and at least one distinct content shape or control shape;
- the shape variation follows the content hierarchy and remains readable on the smallest supported viewport;
- the cases retain one neutral interface palette and type system; variation comes from task, content silhouette, and control topology rather than an alternate visual theme;
- scrollable content is a real product flow, not a standalone material test area.

## Material acceptance

Confirm the DOM and computed styles satisfy the four-layer contract before judging polish:

- one `#liquid_glass_filter` definition is present;
- every wrapper has exactly one outer, cover, sharp, and reflect layer;
- the content layer is above the material layers;
- the background contains visible detail behind the wrapper.
- the surface remains partially transparent; no opaque fill covers the sampled backdrop;
- the glass is not nested inside an unrelated filtered, transformed, or paint-contained ancestor that changes the intended backdrop topology;

## Transparency acceptance

Check the behavior that makes the material readable:

- at least one primary glass control sits over meaningful visual content and reveals its color through the semi-transparent surface;
- on a scrollable page, a meaningful glass control is sticky or anchored while content passes behind it;
- the content passing behind that control has enough color or image variation for the visible color through the control to change as the page scrolls;
- no opaque button fill or isolated demo section is being used as a substitute for this behavior.

## Browser checks

This is Level 2: observable behavior. Use Playwright CLI or the project's existing browser tool from a local HTTP origin. Do not report the page verified if only Level 1 ran:

1. Load the page and confirm there are no console errors.
2. Capture a desktop screenshot with a detailed background behind the wrapper.
3. Resize to the smallest supported viewport and capture a mobile screenshot.
4. Hover, focus, activate, and keyboard-tab through interactive glass controls.
5. Click any product interaction and confirm it changes state without removing or reordering the four layers.
6. Emulate reduced motion, reduced transparency, and high contrast when the selected tool supports each preference; confirm content remains operable. If a preference cannot be emulated, record it as unverified rather than passing it by assumption.
7. Disable or bypass SVG-backed `backdrop-filter` and confirm the solid/translucent fallback remains readable.
8. On the scroll fixture, capture the same sticky control at scroll positions `0` and a later position where a different color block is behind it. Compare a central sample and an edge sample; both must change enough to show that content passes behind the control, while the control's text remains stable.
9. If the edge does not show spatial displacement in reference mode, set `data-glass-mode="fallback"`, capture the readable fallback, and record the browser engine and evidence.

Do not use the presence of a CSS declaration as proof that a browser visually applied the SVG filter. Compare the screenshot and computed style.

### Minimal browser probe

Run this in the page context after the first render, then repeat after scrolling:

```js
const glass = document.querySelector('.liquid_glass-wrapper');
const outer = glass.querySelector('.liquid_glass-outer');
const cover = glass.querySelector('.liquid_glass-cover');
const before = getComputedStyle(outer).backdropFilter;
const coverStyle = getComputedStyle(cover);
const rect = glass.getBoundingClientRect();
const center = { x: Math.round(rect.left + rect.width / 2), y: Math.round(rect.top + rect.height / 2) };
console.table({
  filter: before,
  coverBackground: coverStyle.backgroundColor,
  coverFilter: coverStyle.backdropFilter,
  center,
  scrollY: window.scrollY,
});
```

The probe is evidence only when paired with screenshots from two scroll positions. Computed style can confirm the declaration, but cannot confirm visible pixel displacement.

## Fallback and accessibility

The fallback ladder for this skill is:

```text
four-layer SVG-backed surface
→ four-layer surface with outer SVG layer hidden
→ solid Canvas/CanvasText surface in forced colors
```

The cover, sharp, reflect, and content layers should remain present in the normal fallback. Use `data-glass-mode="fallback"` when visual browser evidence shows that the declared reference filter has no readable rim; `@supports` alone is insufficient to make that decision. The fallback must preserve focus visibility and readable text. `prefers-reduced-motion` disables continuous animation only; it does not remove the static material.

## Evidence

Keep one screenshot for the normal reference path and one for the fallback path, recording browser engine and viewport. Report SVG filter URL behavior as browser-dependent when it differs across engines.

For scroll transparency, keep two normal-path screenshots with the same viewport and control position but different scroll positions. Record the sampled scene behind the control, the chosen displacement mode, and whether the rim visibly bends that scene.
