---
name: liquid-glass
description: Plan Apple-inspired interfaces and implement their surfaces with the reference liquid glass style from shuding/liquid-glass: a hidden SVG displacement filter, four stacked surface layers, SVG edge masks, a 2px cover blur, sharp rim lighting, and reflective inset shadows.
---

# Liquid Glass Design

Use the reference implementation as the material contract. The page can have any product-specific layout, but every glass surface must use this four-layer SVG/CSS construction.

## Design phase: visual direction + Apple behavior

Before writing markup or CSS, produce the following design brief. This is where the skill borrows selectively from frontend-design: define a coherent visual direction, a memorable anchor, atmosphere, composition, typography, and production quality. Prefer restraint and system typography when that better serves the product; do not add novelty for its own sake.

```text
Purpose: the one job this page must accomplish
Audience and context: who uses it, when, and on what device
Visual direction: tone, palette, texture, composition, and one memorable anchor
Content hierarchy: primary, secondary, supporting, and action content
Material map: each glass surface, its role, radius, weight, and background detail
Interaction state map: idle, hover, press, focus, drag, release, disabled
Motion model: immediate feedback, spring/transition choice, interruption, spatial origin
Typography: platform font, display/body scale, weight, tracking, and leading
Accessibility: reduced motion, reduced transparency, high contrast, focus, touch targets
Acceptance criteria: design checks and material checks
```

Apply these design rules before entering the material implementation:

1. **Purpose and simplicity** — remove elements that do not support the primary job. Put the common path first; keep advanced options secondary.
2. **Direction and differentiation** — choose one coherent visual direction and one detail the user will remember. Use atmosphere, asymmetry, texture, or a strong typographic moment only when it supports the product.
3. **Agency and familiarity** — use recognizable labels, predictable placement, visible escape/undo paths, and controls next to the thing they affect.
4. **Immediate response** — provide press feedback on pointer-down. For direct manipulation, update continuously with the pointer instead of waiting for release.
5. **Interruptible motion** — gesture-driven animation must be redirectable at any time. Animate from the current presented value, carry release velocity into the next motion, and use critically damped springs by default. Use bounce only when momentum created it.
6. **Spatial consistency** — enter and exit along related paths, anchor popovers/sheets to their trigger, and keep the source-to-result relationship visible.
7. **Material hierarchy** — use glass as a floating functional layer over meaningful background content. Give structural surfaces more weight, interactive controls clearer contrast, and avoid stacking multiple light translucent surfaces where legibility collapses.
8. **Typography and accessibility** — start with a platform/system font, tune tracking and leading by text size, and plan reduced motion, reduced transparency, high contrast, keyboard focus, and touch hit areas before implementation.

For each interactive surface, define the state behavior explicitly:

| State | Required behavior |
| --- | --- |
| Idle | Clear hierarchy and no gratuitous motion |
| Hover | Small, causal affordance change only when hover exists |
| Press | Immediate visual response on pointer-down |
| Focus | Persistent, high-contrast keyboard indicator |
| Drag | 1:1 tracking with pointer capture when dragging |
| Release | Continue from the current value and hand off velocity when motion continues |
| Reduced motion/transparency | Keep meaning and operation while reducing movement/material intensity |

## Default material contract

The reference look is produced by four separate layers, in this order:

1. `liquid_glass-outer` — samples and displaces the background with the SVG filter, then uses two SVG masks to leave a narrow refractive rim.
2. `liquid_glass-cover` — adds the dark translucent body and only `blur(2px)`.
3. `liquid_glass-sharp` — adds the crisp one-pixel white edge.
4. `liquid_glass-reflect` — adds the inset directional highlight and darker inner edge.

Keep content in a separate layer at `z-index: 4`. The surface is the composition of these layers; it is not one `backdrop-filter` declaration.

## Required SVG definition

Place this definition once in the document, before any glass wrappers. Keep the filter ID and scale aligned with the reference code:

```html
<svg style="display: none" aria-hidden="true">
  <defs>
    <filter id="liquid_glass_filter" x="0%" y="0%" width="100%" height="100%" filterUnits="objectBoundingBox">
      <feDisplacementMap scale="200" />
    </filter>
  </defs>
</svg>
```

This is an SVG filter resource, not an image decoration. CSS must reference it with `url(#liquid_glass_filter)`.

## Required wrapper structure

Every glass component uses the same wrapper and layer order. Set `--border-radius` per shape:

```html
<div class="liquid_glass-wrapper" style="--border-radius: 26px">
  <div class="liquid_glass-outer"></div>
  <div class="liquid_glass-cover"></div>
  <div class="liquid_glass-sharp"></div>
  <div class="liquid_glass-reflect"></div>

  <div class="liquid_glass-content">
    <!-- text, controls, icons, or media -->
  </div>
</div>
```

Do not reorder the layers. Do not collapse them into pseudo-elements when the reference structure can be used directly.

## Required CSS baseline

Start with these values. Adjust only the wrapper size, radius, content spacing, and page background unless a contrast or accessibility requirement demands a change.

```css
.liquid_glass-wrapper {
  position: relative;
  display: flex;
  overflow: hidden;
  border-radius: var(--border-radius);
}

.liquid_glass-outer,
.liquid_glass-cover,
.liquid_glass-sharp,
.liquid_glass-reflect {
  position: absolute;
  inset: 0;
  border-radius: var(--border-radius);
  pointer-events: none;
}

.liquid_glass-outer {
  z-index: 0;
  backdrop-filter: url(#liquid_glass_filter);
  -webkit-backdrop-filter: url(#liquid_glass_filter);
  mask-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%"><rect x="0" y="0" width="100%" height="100%" rx="0" ry="0" fill="white"/></svg>'),
    url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%"><rect x="5" y="5" width="calc(100% - 10px)" height="calc(100% - 10px)" rx="21" ry="21" fill="white"/></svg>');
  mask-composite: exclude;
  -webkit-mask-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%"><rect x="0" y="0" width="100%" height="100%" rx="0" ry="0" fill="white"/></svg>'),
    url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%"><rect x="5" y="5" width="calc(100% - 10px)" height="calc(100% - 10px)" rx="21" ry="21" fill="white"/></svg>');
  -webkit-mask-composite: xor;
}

.liquid_glass-cover {
  z-index: 2;
  background: rgba(0, 0, 0, 0.12);
  backdrop-filter: blur(2px);
  -webkit-backdrop-filter: blur(2px);
}

.liquid_glass-sharp {
  z-index: 3;
  box-shadow:
    inset 1px 1px 0 rgba(255, 255, 255, 0.5),
    inset -1px -1px 0 rgba(255, 255, 255, 0.6);
}

.liquid_glass-reflect {
  z-index: 2;
  inset: 1px;
  box-shadow:
    inset 2px 2px 6px 2px rgba(255, 255, 255, 0.2),
    inset -2px -2px 4px -1px rgba(255, 255, 255, 0.2);
}

.liquid_glass-content {
  position: relative;
  z-index: 4;
}
```

The background behind the wrapper must contain visible spatial detail: an image, gradient field, contour lines, color blocks, or another readable scene. A flat solid background cannot demonstrate the refractive rim.

## Design-to-material sequence

1. Inspect the target page, framework, browser target, and existing interaction model.
2. Write the Apple-inspired design brief before choosing components.
3. Create a detailed background scene before creating the glass wrapper.
4. Add the single SVG filter definition.
5. Add the four layers in the exact order above for every glass surface.
6. Keep content and focus states above the layers and readable against the cover.
7. Implement interaction outside the material layers: immediate feedback, direct manipulation, interruptible motion, and spatially consistent transitions.
8. Add the fallback and verify both the design behavior and the material behavior in a real browser.

## Single-effect rule

This skill has one material implementation: the four real layers above, backed by the shared SVG displacement filter. Keep layout, content, icons, and interactions separate from the material. Do not introduce another glass renderer or replace the four layers with a generic blur or pseudo-element-only approximation.

## Fallback and accessibility

Keep the component operable when SVG-backed `backdrop-filter` is unavailable:

```css
@supports not ((backdrop-filter: url(#liquid_glass_filter)) or (-webkit-backdrop-filter: url(#liquid_glass_filter))) {
  .liquid_glass-outer { display: none; }
  .liquid_glass-wrapper { background: rgba(30, 45, 75, 0.88); }
}

@media (forced-colors: active) {
  .liquid_glass-wrapper {
    border: 1px solid CanvasText;
    background: Canvas;
    color: CanvasText;
  }
  .liquid_glass-outer,
  .liquid_glass-cover,
  .liquid_glass-reflect { display: none; }
  .liquid_glass-sharp { box-shadow: none; }
}

@media (prefers-reduced-transparency: reduce) {
  .liquid_glass-wrapper { background: rgba(30, 45, 75, 0.92); }
  .liquid_glass-outer,
  .liquid_glass-cover {
    backdrop-filter: none;
    -webkit-backdrop-filter: none;
  }
}

@media (prefers-contrast: more) {
  .liquid_glass-wrapper { border: 2px solid currentColor; }
}
```

Use `prefers-reduced-motion` to disable continuous motion. The static four-layer material may remain when it is not animated. Keep text, controls, and keyboard focus in the content layer; translucency is not a substitute for contrast.

## Verification checklist

Before handoff, verify all of the following in a real browser:

### Design acceptance

- The page has a stated purpose and a clear common path; every visible element supports that purpose.
- The visual direction is coherent and has one intentional memorable anchor.
- Interactive controls respond on press, and gesture-driven motion can be interrupted and redirected.
- Enter/exit paths and trigger-to-surface relationships are spatially consistent.
- Material weight communicates hierarchy without stacking translucent surfaces into an unreadable pile.
- Typography, focus, reduced motion, reduced transparency, and high-contrast states remain usable.

### Material acceptance

- The background remains visible through the wrapper and contains enough detail to reveal the rim.
- The DOM contains one shared `#liquid_glass_filter` and four layer nodes per glass wrapper.
- Computed style for `liquid_glass-outer` contains `url(#liquid_glass_filter)`.
- `liquid_glass-cover` uses `rgba(0, 0, 0, 0.12)` and `blur(2px)`.
- `liquid_glass-sharp` and `liquid_glass-reflect` produce visible rim and thickness cues.
- Content stays above the layers and remains readable.
- Focus, active, responsive, reduced-motion, forced-colors, and filter-unavailable states remain operable.
- The build/type check passes and the browser console has no errors.
- Capture a screenshot at desktop and the smallest supported viewport.

For the exact reference markup and a runnable fixture, read [references/vanilla-example.md](references/vanilla-example.md). For browser acceptance checks, read [references/verification.md](references/verification.md).
