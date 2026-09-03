---
name: apple-liquid-glass
description: Independently plan and implement focused Apple-like web pages with the reference liquid glass material from shuding/liquid-glass: restrained content-first design plus a hidden SVG displacement filter, four stacked surface layers, SVG edge masks, 2px cover blur, sharp rim lighting, and reflective inset shadows.
---

# Apple Liquid Glass Design

Use the reference implementation as the material contract. The page can have any product-specific layout, but every glass surface must use this four-layer SVG/CSS construction.

This skill is self-contained for a new HTML/CSS/JS page: do not require another design skill to choose the page direction or implement the material. If no framework or project is supplied, use the vanilla fixture in [references/vanilla-example.md](references/vanilla-example.md) as the starting point and serve it from a local HTTP origin for browser verification.

Before designing a new Apple-like page, start with the routing, three-plane, and component-shape sections in [references/apple-hig.md](references/apple-hig.md), plus the use/boundary, layout/material, color/icons, and accessibility sections in [references/hig-foundations.md](references/hig-foundations.md). They translate the current official HIG information architecture and the studied Landmarks and App Privacy examples into web decisions for hierarchy, planes, color, imagery, type, writing, iconography, accessibility, and recovery. Load the remaining sections only when the page task makes them relevant, then load the task-specific HIG guide before choosing a pattern or component:

- For a flow involving sign-in, search, onboarding, settings, forms, permissions, feedback, errors, help, account management, destructive actions, or undo, read [references/hig-patterns.md](references/hig-patterns.md).
- For navigation, actions, selections, lists, collections, fields, menus, alerts, sheets, toolbars, sidebars, tabs, status, or keyboard/pointer/touch behavior, read [references/hig-components-inputs.md](references/hig-components-inputs.md).
- For an Apple service or capability such as generative AI, machine learning, Maps, payments, Health, Home, media, Siri/Shortcuts, widgets, or App Clips, read [references/hig-technologies.md](references/hig-technologies.md) before making a product promise or control.

These are operational syntheses, not screenshot-copying recipes: preserve the user’s product, brand, and content while applying the underlying grammar. Do not copy Apple screenshots, assets, trademarks, or fixed pixels.

## Rule precedence and overrides

Resolve conflicts in this order:

1. **Accessibility and operability** — preserve legibility, keyboard and touch operation, reduced-motion/transparency support, and meaningful fallback behavior.
2. **Explicit product or brand direction** — honor a user-requested palette, typography, composition, or art direction when it does not break accessibility or the material contract.
3. **Material contract** — preserve the SVG filter, four real layers, matching masks, `rgba(0, 0, 0, 0.12)` cover, and `blur(2px)` reference behavior unless target-browser evidence requires the documented readable fallback.
4. **Apple visual baseline** — apply content-first hierarchy, functional glass, semantic color, concise writing, and platform-aware adaptation.
5. **Anti-AI defaults** — remove unrequested decorative patterns that add atmosphere without meaning.

The Apple and Anti-AI rules are visual defaults, not a ban on expressive design. An explicit request can override them; it cannot justify an inaccessible interface or a broken liquid-glass material.

## Default Apple visual baseline

Use [Foundations](references/hig-foundations.md) as the sole owner of foundation rules and [Apple HIG Visual Grammar](references/apple-hig.md) as the sole owner of visual planes, shape/grouping, and studied examples. The default is content-first hierarchy, functional glass, a neutral semantic palette with one dominant accent, familiar controls, and purposeful motion. Explicit product direction can be more expressive when it remains accessible and respects the material contract.

### Anti-AI visual gate

Reject unrequested decoration that does not clarify the task: blue-purple neon, gratuitous glow, floating ornaments, **unjustified repeated glass pills**, card walls, invented slogans, or color with no semantic job. Separate capsules remain valid for genuinely independent horizontal actions; a contextual command group must share one vessel. This gate is applied in the preview audit in [references/verification.md](references/verification.md).

### Palette decision gate

For every non-neutral color, record `role → token → light/dark/contrast behavior → non-color cue`. Use one dominant accent by default; scene color is content rather than interface tint. The detailed color rules live in [references/hig-foundations.md](references/hig-foundations.md).

## Apple HIG visual grammar

After identifying the page’s purpose and likely controls, classify the task with the routing table in [references/apple-hig.md](references/apple-hig.md), then read each applicable guide before the page brief is finalized. Use semantic HTML and browser-accessible controls to express HIG intent; do not claim literal native-platform behavior or imitate unavailable system surfaces.

## Page phase: purpose + behavior

Before writing markup or CSS, produce the following page brief: define the product purpose, information hierarchy, background scene, interaction behavior, typography, and accessibility. Keep the page-specific style independent from the material implementation.

```text
Purpose: the one job this page must accomplish
Audience and context: who uses it, when, and on what device
Visual direction: tone, palette, texture, composition, and one memorable anchor
Content hierarchy: primary, secondary, supporting, and action content
Material map: each glass surface, its role, radius, weight, and background detail
Plane map: which elements are content, standard material, and Liquid Glass controls
Component grammar: familiar pattern/component, independent target or shared command group, outer shape, local state surface, and placement rationale
Interaction class: discrete control or direct-manipulation control
Interaction state map: only the applicable idle, hover, press, focus, selected, disabled, loading, error, drag, and release states
Motion model: immediate feedback, spring/transition choice, interruption, spatial origin
Typography: platform font, display/body scale, weight, tracking, and leading
Accessibility: reduced motion, reduced transparency, high contrast, focus, touch targets
Platform adaptation: viewport, safe area, locale/RTL, text scaling, input modes
Writing: action labels, capitalization, field hints, error recovery
Color semantics: role of each non-neutral color and light/dark/contrast behavior
HIG route: the selected Foundation, Pattern, Component/Input, and Technology references
Acceptance criteria: design checks and material checks
```

Apply these page rules before entering the material implementation:

1. **Purpose and simplicity** — remove elements that do not support the primary job. Put the common path first; keep advanced options secondary.
2. **Direction and differentiation** — choose a page-specific visual direction from the content and context. The Apple visual baseline above remains the default; vary palette, density, composition, and geometry only when the product reason is explicit. The liquid glass material remains the shared constant.
3. **Agency and familiarity** — use recognizable labels, predictable placement, visible escape/undo paths, and controls next to the thing they affect.
   - Decide control topology before styling: an independent action may use its own circle or capsule; a contextual command group gets one shared vessel with contiguous members and local internal state treatment. Follow the concentric-geometry rules in [Apple HIG Visual Grammar](references/apple-hig.md); do not solve grouping by multiplying glass wrappers.
4. **Immediate response** — provide press feedback on pointer-down. For direct manipulation, update continuously with the pointer instead of waiting for release.
5. **Interruptible motion** — gesture-driven animation must be redirectable at any time. Animate from the current presented value, carry release velocity into the next motion, and use critically damped springs by default. Use bounce only when momentum created it.
6. **Spatial consistency** — enter and exit along related paths, anchor popovers/sheets to their trigger, and keep the source-to-result relationship visible.
7. **Material hierarchy** — use glass as a floating functional layer over meaningful background content. Give structural surfaces more weight, interactive controls clearer contrast, and avoid stacking multiple light translucent surfaces where legibility collapses.
8. **Typography and accessibility** — start with a platform/system font, tune tracking and leading by text size, and plan reduced motion, reduced transparency, high contrast, keyboard focus, and touch hit areas before implementation.
9. **Anti-pattern review** — before showing the preview, check the anti-AI visual gate and palette decision gate. A technically correct glass surface is not acceptable if the surrounding page still reads as generic AI-generated sci-fi UI.
10. **HIG review** — verify each control and flow against the selected HIG route before styling; do not derive a new component from a screenshot.

## Composition diversity

Keep the material contract stable while allowing the page composition to respond to its subject:

- Do not make every content module a full-width rounded rectangle or horizontal bar.
- For multiple cases, vary at least three of these axes: primary layout, module silhouette, control silhouette, spacing density, background treatment, and information rhythm.
- Choose shapes from the content: media can use staggered album cards, weather can use circles or tall forecast cards, and productivity can use compact tiles or asymmetric markers. Shape changes must clarify hierarchy, not add decoration without a job.
- A scrollable flow should contain real content behind the glass control. Use a queue, timeline, task rhythm, or another meaningful product structure instead of adding a test-only transparency section.
- Check the smallest supported viewport after varying widths and offsets; responsive rules must collapse asymmetric compositions into readable single-column content.

## Primary composition examples

When the requested page matches one of these contexts, inspect the corresponding runnable example for composition and material placement only. Do not copy its product copy, palette, or layout into an unrelated product.

- [Music player](examples/04-music-player.html): immersive media content with one fixed bottom transport surface.
- [Creative workbench](examples/05-workbench.html): an asymmetric, non-card canvas with one shared top command vessel.
- [Team chat](examples/06-chat.html): ordinary scrolling message content with one fixed bottom composer surface.

Together they demonstrate the intended boundary: liquid glass is a small functional control plane over changing content, not a default material for every module.

## Progressive delivery and approval gate

Choose the delivery mode before implementation:

| Mode | Use when | Stop condition |
| --- | --- | --- |
| `preview` (default) | The user asks to design, explore, or assess a page without explicitly requesting full completion | Build one representative slice and wait for approval or revision feedback |
| `full` | The user explicitly asks to complete the page, implement all named screens, or proceed past preview | Build the preview-quality slice first, then continue into full implementation without a separate approval pause |
| `iterate` | The user gives feedback on an existing preview or page | Change only the requested material, topology, layout, or behavior variable and show the revised evidence |

Do not infer `full` merely because the user asks for “a page”; use `preview` until they explicitly state that they want the complete implementation. A later explicit request to continue changes the current delivery mode to `full`.

Use the mode to control the two-phase workflow and avoid spending tokens on an unapproved direction:

1. **Preview phase** — write the page brief, then implement one high-fidelity representative slice. It must use the final SVG filter, all four material layers, a real detailed background, one meaningful glass control, and the relevant interaction behavior; for a scrollable page, this includes scroll-through behavior. Use minimal product copy and a small amount of content; reduce quantity, never material fidelity.
2. **Approval gate** — in `preview` mode, show the running preview or a browser screenshot and state exactly what the user should judge: translucency, changing background through the surface, rim displacement, 3D thickness, hierarchy, and interaction response. Stop there until the user explicitly approves or requests a revision. In `full` mode, capture the same evidence but continue after recording it.
3. **Expansion phase** — after approval in `preview` mode, or immediately after recording preview evidence in `full` mode, extend the slice into the complete page and then create additional cases. Reuse the approved material contract and tokens, but choose each page's composition from its content.

Treat feedback as local iteration: change only the preview's relevant material, topology, shape, or layout variable, then show the preview again. Do not generate the full page set while a material or direction decision is still unresolved. A preview is a reduced-content version of the final implementation, not a throwaway mock or a separate renderer.

First classify every interactive surface. Do not add drag physics to an ordinary button merely to satisfy a state table.

| Interaction class | Required states and behavior |
| --- | --- |
| Discrete control: button, link, field, menu item, tab | Idle; hover only when available; immediate press; persistent focus; selected/on, disabled, loading, success, or error only when the component has that state; keep its action semantic and keyboard-operable |
| Direct-manipulation control: draggable card, slider, sheet, canvas object | All relevant discrete states, plus drag with pointer capture and 1:1 tracking; on release, continue from the presented value and hand off velocity only if momentum continues |
| Any control under accessibility preferences | Keep meaning and operation while reducing motion or material intensity; never make a gesture, color, or hover state the only route |

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

## SVG displacement fundamentals

The refractive principle is pixel displacement, not blur alone. `feDisplacementMap` uses one image as the filtered source and another as the displacement map:

- `in` identifies the image being displaced;
- `in2` identifies the displacement map;
- `scale` controls displacement amplitude, with `0` meaning no displacement;
- `xChannelSelector` chooses the `in2` channel used for the x axis;
- `yChannelSelector` chooses the `in2` channel used for the y axis.

Use one reference mode: preserve the exact `shuding/liquid-glass` declaration, including `<feDisplacementMap scale="200" />`. A declared filter is not proof of visible refraction. Do not relabel the default `SourceGraphic` inputs as a repair, and do not introduce a second displacement-map design to force an effect in a browser where the reference does not render visibly.

If browser evidence shows no readable rim displacement, record the engine and select the readable fallback state described below. The reference material remains the only normal renderer; the fallback communicates the same hierarchy without making a false refraction claim.

## Browser capability preflight

Before building the preview, test the exact reference fixture in the target browser or the closest available target engine, over a detailed contrasting scene. Record:

```text
engine and version → viewport → reference rim visibly displaced? → selected mode: reference | fallback
```

`CSS.supports`, a parsed `backdrop-filter` declaration, and a nonempty computed style prove syntax only. They do not prove that the browser renders the reference filter or the mask composite visibly. If the rim is not readable, select `data-glass-mode="fallback"` before composing the page, keep the same component topology and four-layer DOM, and describe the result as a readable translucent fallback rather than refraction. If a testing tool cannot emulate a user preference, record that gap instead of claiming the preference was verified.

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

Start with these values. Keep the material invariants unchanged by default; adapt page colors, typography, layout, control states, and fallback presentation when platform, brand, background content, or accessibility requires it. Never change those adaptations into a second glass renderer.

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

## Backdrop topology and shape contract

The visual effect depends on the scene graph, not only on declarations. Put the detailed scene below the glass surface and keep the path between them transparent. Do not place an opaque parent or an unrelated filtered/transformed/paint-contained ancestor between the surface and the scene; inspect stacking contexts when the backdrop appears flat. Keep the glass surface itself above the content it is meant to sample, and keep interactive content in its `z-index: 4` layer.

Use one of three supported shape profiles so the inner rim mask matches the visible geometry:

- `rounded` — the reference 26px rectangular mask;
- `pill` — a capsule mask whose inner radius is half the surface height;
- `circle` — a circular mask with equal width and height.

For `pill` and `circle`, provide a matching SVG mask or a mask geometry generated from the same size variables. Do not reuse the reference `rx="21" ry="21"` geometry for a different shape and call the edge optically correct. If a project needs arbitrary radii, verify the edge mask at that actual size before shipping.

The reference mask can be adapted without changing the material layers by selecting a shape-specific second mask. Use the same selector for `mask-image` and `-webkit-mask-image`:

```css
/* rounded: keep the reference mask from the baseline */
[data-glass-shape="pill"] .liquid_glass-outer {
  mask-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%"><rect width="100%" height="100%" fill="white"/></svg>'), url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%"><rect x="5" y="5" width="calc(100% - 10px)" height="calc(100% - 10px)" rx="50%" ry="50%" fill="white"/></svg>');
  mask-composite: exclude;
  -webkit-mask-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%"><rect width="100%" height="100%" fill="white"/></svg>'), url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%"><rect x="5" y="5" width="calc(100% - 10px)" height="calc(100% - 10px)" rx="50%" ry="50%" fill="white"/></svg>');
  -webkit-mask-composite: xor;
}

[data-glass-shape="circle"] .liquid_glass-outer {
  mask-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%"><rect width="100%" height="100%" rx="50%" ry="50%" fill="white"/></svg>'), url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%"><rect x="5" y="5" width="calc(100% - 10px)" height="calc(100% - 10px)" rx="50%" ry="50%" fill="white"/></svg>');
  mask-composite: exclude;
  -webkit-mask-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%"><rect width="100%" height="100%" rx="50%" ry="50%" fill="white"/></svg>'), url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%"><rect x="5" y="5" width="calc(100% - 10px)" height="calc(100% - 10px)" rx="50%" ry="50%" fill="white"/></svg>');
  -webkit-mask-composite: xor;
}
```

Mark each non-rounded wrapper explicitly, for example `data-glass-shape="pill"` or `data-glass-shape="circle"`, and use equal width and height for circles. If the target browser does not honor percentage radii inside the data URL, keep the wrapper in the rounded profile or move the mask to an inline SVG whose geometry is updated with the measured size; do not silently accept a visibly broken rim.

For a scrollable page, the baseline topology is:

```text
page scene with varied color/image blocks
  → normal-flow content
  → sticky or anchored glass control above that content
  → content passes behind the control during scroll
```

Avoid `overflow: hidden` on the page or the relevant scroll container unless another explicitly tested scroll container owns the interaction. Avoid clipping, transforms, or containment on ancestors that prevent the intended scene from reaching the backdrop sampling area.

## Transparency as the default behavior

Make translucency observable in a real product flow, not only in an isolated material demo:

1. Put primary glass buttons and controls over meaningful visual content so the background color is visibly readable through the semi-transparent surface.
2. On a scrollable page, make at least one meaningful glass control sticky or otherwise anchored while the page content passes behind it. The content behind the control must contain contrasting colors, images, or surfaces so the color seen through the control changes during scrolling.
3. Keep the reference cover values as the starting point: `rgba(0, 0, 0, 0.12)` with `blur(2px)`. Do not replace the effect with an opaque button fill.
4. Treat this as part of the page's real interaction model. A separate test-only transparency section does not satisfy the default behavior.

## Design-to-material sequence

1. Inspect the target page, framework, browser target, existing interaction model, and delivery mode.
2. Run the browser capability preflight and select reference or fallback mode before composition.
3. Write the page brief before choosing components.
4. Build the representative preview slice described in [Progressive delivery and approval gate](#progressive-delivery-and-approval-gate).
5. Add the detailed background scene, single SVG filter definition, and four layers in the exact order above.
6. Keep content and focus states above the layers and readable against the cover.
7. Implement only the interaction class each control needs: immediate response for discrete controls; direct manipulation, interruption, and velocity handoff only when dragging exists.
8. Verify the preview in a real browser. In `preview` mode, stop at the approval gate; in `full` mode, record the same evidence and continue.
9. During final expansion, repeat the material and responsive checks. For scrollable pages, capture the same glass control at two scroll positions and confirm its sampled background changes; if the rim displacement is not visible, capture and record the readable fallback before accepting the result.

## Single-effect rule

This skill has one material implementation: the four real layers above, backed by the shared SVG displacement filter. Keep layout, content, icons, and interactions separate from the material. Do not introduce another glass renderer or replace the four layers with a generic blur or pseudo-element-only approximation.

## Fallback and accessibility

Keep the component operable when SVG-backed `backdrop-filter` is unavailable:

```css
html[data-glass-mode="fallback"] .liquid_glass-outer {
  display: none;
}

html[data-glass-mode="fallback"] .liquid_glass-wrapper {
  background: rgba(48, 49, 45, 0.9);
}

@supports not ((backdrop-filter: url(#liquid_glass_filter)) or (-webkit-backdrop-filter: url(#liquid_glass_filter))) {
  .liquid_glass-outer { display: none; }
  .liquid_glass-wrapper { background: rgba(48, 49, 45, 0.9); }
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
  .liquid_glass-wrapper { background: rgba(48, 49, 45, 0.94); }
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

Use `prefers-reduced-motion` to disable continuous motion. The static four-layer material may remain when it is not animated. Keep text, controls, and keyboard focus in the content layer; translucency is not a substitute for contrast. `@supports` detects unsupported syntax only; choose `data-glass-mode="fallback"` after target-browser visual verification when the reference filter is declared but the rim is not visibly rendered.

## Performance boundary

Treat backdrop filtering and SVG displacement as compositing work. Avoid nested glass surfaces, keep the number of simultaneously visible surfaces small (as a starting budget: no more than 8 on desktop and 4 on mobile), and do not animate large filter regions continuously. If the page exceeds that budget, reduce surfaces or switch nonessential surfaces to the solid fallback on small or low-power devices.

## Verification checklist

Before handoff, verify all of the following in a real browser:

### Delivery state

- The selected delivery mode is recorded. If it is `preview`, only the representative slice has been generated until the user approves; if it is `full`, the explicit request to complete is recorded.
- The preview uses the same SVG filter, four-layer DOM, mask strategy, fallback, and interaction model intended for the final page.
- Full-page expansion and additional cases were started only after preview approval or an explicit `full` request.

### Design acceptance

- The page has a stated purpose and a clear common path; every visible element supports that purpose.
- The visual direction is coherent and has one intentional memorable anchor.
- Interactive controls respond on press, and gesture-driven motion can be interrupted and redirected.
- Enter/exit paths and trigger-to-surface relationships are spatially consistent.
- Material weight communicates hierarchy without stacking translucent surfaces into an unreadable pile.
- Typography, focus, reduced motion, reduced transparency, and high-contrast states remain usable.

### Material acceptance

- The background remains visible through the wrapper and contains enough detail to reveal the rim.
- The backdrop topology is valid: the intended scene is below the surface, the surface is partially transparent, and no ancestor blocks sampling.
- The selected reference/fallback mode is backed by target-browser visual evidence, not only by CSS support or computed-style output.
- The DOM contains one shared `#liquid_glass_filter` and four layer nodes per glass wrapper.
- Computed style for `liquid_glass-outer` contains `url(#liquid_glass_filter)`.
- `liquid_glass-cover` uses `rgba(0, 0, 0, 0.12)` and `blur(2px)`.
- `liquid_glass-sharp` and `liquid_glass-reflect` produce visible rim and thickness cues.
- Content stays above the layers and remains readable.
- Focus, active, responsive, reduced-motion, forced-colors, and filter-unavailable states remain operable.
- For scrollable pages, the same meaningful glass control shows different background color/detail at two scroll positions.
- If reference-mode displacement is not visible, the page selects `data-glass-mode="fallback"` and records the browser engine and evidence.
- The visible glass surface stays within the performance boundary or documents why it exceeds it.
- The build/type check passes and the browser console has no errors.
- Capture a screenshot at desktop and the smallest supported viewport.

### Final Apple Conformance Review

Run the single authoritative review in [references/verification.md](references/verification.md) after the complete page and after the last visual change. Record `PASS` or `FAIL` there; do not report completion while any item is failed or unverified.

For the exact reference markup and a runnable fixture, read [references/vanilla-example.md](references/vanilla-example.md). For browser acceptance checks and final review, read [references/verification.md](references/verification.md).
