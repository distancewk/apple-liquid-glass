# Verification Playbook

## Contents

- [Static checks](#static-checks)
- [DOM and CSS checks](#dom-and-css-checks)
- [Browser checks](#browser-checks)
- [Fallback and accessibility](#fallback-and-accessibility)
- [Evidence](#evidence)

## Static checks

Run the dependency-free validator from the skill directory:

```bash
python3 scripts/validate_skill.py .
python3 scripts/extract_html_example.py \
  --source references/vanilla-example.md \
  --output /tmp/liquid-glass/index.html
```

Run the project's type check and build when the page is part of a project. The extracted fixture must contain the four real layer classes and the SVG filter definition.

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

## Design acceptance

Before checking CSS, confirm the page has:

- a one-sentence purpose and a clear common path;
- one coherent visual direction and one intentional memorable anchor;
- a content hierarchy that distinguishes primary, secondary, supporting, and action content;
- explicit idle, hover, press, focus, drag, release, disabled, and reduced-motion behavior where applicable;
- spatially consistent transitions that remain interruptible;
- readable typography, focus indicators, touch targets, and reduced-transparency/high-contrast behavior.

## Material acceptance

Confirm the DOM and computed styles satisfy the four-layer contract before judging polish:

- one `#liquid_glass_filter` definition is present;
- every wrapper has exactly one outer, cover, sharp, and reflect layer;
- the content layer is above the material layers;
- the background contains visible detail behind the wrapper.

## Browser checks

Use Playwright CLI or the project's existing browser tool from a local HTTP origin:

1. Load the page and confirm there are no console errors.
2. Capture a desktop screenshot with a detailed background behind the wrapper.
3. Resize to the smallest supported viewport and capture a mobile screenshot.
4. Hover, focus, activate, and keyboard-tab through interactive glass controls.
5. Click any product interaction and confirm it changes state without removing or reordering the four layers.
6. Emulate reduced motion, reduced transparency, and high contrast; confirm content remains operable.
7. Disable or bypass SVG-backed `backdrop-filter` and confirm the solid/translucent fallback remains readable.

Do not use the presence of a CSS declaration as proof that a browser visually applied the SVG filter. Compare the screenshot and computed style.

## Fallback and accessibility

The fallback ladder for this skill is:

```text
four-layer SVG-backed surface
→ four-layer surface with outer SVG layer hidden
→ solid Canvas/CanvasText surface in forced colors
```

The cover, sharp, reflect, and content layers should remain present in the normal fallback. The fallback must preserve focus visibility and readable text. `prefers-reduced-motion` disables continuous animation only; it does not remove the static material.

## Evidence

Keep one screenshot for the normal reference path and one for the fallback path, recording browser engine and viewport. Report SVG filter URL behavior as browser-dependent when it differs across engines.
