# Apple HIG Visual Grammar

## Contents

- [How to use this reference](#how-to-use-this-reference)
- [What the HIG information architecture teaches](#what-the-hig-information-architecture-teaches)
- [Foundational design logic](#foundational-design-logic)
- [HIG coverage and routing](#hig-coverage-and-routing)
- [Three visual planes](#three-visual-planes)
- [Foundation boundary](#foundation-boundary)
- [Component and shape grammar](#component-and-shape-grammar)
- [Flow boundary](#flow-boundary)
- [Case-study reading: Landmarks](#case-study-reading-landmarks)
- [Case-study reading: App Privacy](#case-study-reading-app-privacy)
- [Research sources](#research-sources)

## How to use this reference

Read this before writing the page brief for any Apple-like page. Use it to choose the page's information hierarchy, visual planes, component family, and interaction model. It is a decision guide, not a screenshot-copying recipe: preserve the user's product, brand, and content while applying the underlying grammar.

When a page depends on a specialized pattern or technology — for example, onboarding, data entry, navigation, Sign in with Apple, Maps, or privacy permissions — follow the relevant official HIG page linked below before inventing a custom pattern. Do not claim that a generic web page is a native Apple app, copy Apple trademarks, or reuse Apple assets without the applicable license.

## What the HIG information architecture teaches

The HIG groups decisions in a deliberate order. Use the same order when designing a page:

| HIG area | What it decides for a web page |
| --- | --- |
| Getting started | Product purpose, platform fit, hierarchy, harmony, and consistency |
| Foundations | Accessibility, color, material, layout, typography, imagery, writing, privacy, localization |
| Patterns | The user task and recovery path: searching, entering data, feedback, onboarding, settings, sharing, modality, undo |
| Components | Familiar visual containers and controls: toolbars, sidebars, menus, search, sheets, buttons, lists, status |
| Inputs | Touch, pointer, keyboard, gesture, voice, and assistive alternatives |
| Technologies | Product-specific constraints from services like Maps, Sign in with Apple, Apple Pay, HealthKit, Siri, and Wallet |

The implication is important: decide the task and content first, choose a familiar pattern and component second, then choose material, color, typography, and motion. Do not begin with glass, gradients, or a gallery of cards.

## Foundational design logic

Use Apple’s design principles as an active tradeoff tool:

- **Purpose** — state the person’s job in one sentence and make the common path visible immediately.
- **Agency** — expose status, provide a way out of flows, and make recovery or undo easy when an action can fail.
- **Responsibility** — request only necessary data and permissions, explain why, and make privacy implications understandable before commitment.
- **Familiarity** — use established labels, icons, placement, and behavior; elements that look alike must act alike.
- **Flexibility** — preserve context across viewport, input method, locale, text size, light/dark appearance, and accessibility preferences.
- **Simplicity** — remove nonessential content, but add explanation when it reduces uncertainty. Simplicity is not empty space for its own sake.
- **Craft** — align details precisely, keep movement and feedback responsive, and test after resizing or changing content.
- **Delight** — let a sense of calm, confidence, or energy emerge from the above decisions instead of adding decoration after the fact.

The current HIG expresses the visual layer through **hierarchy, harmony, and consistency**. Hierarchy separates controls from content. Harmony uses related proportions and concentric geometry. Consistency keeps the same conventions meaningful across windows and devices.

## HIG coverage and routing

This reference supplies the shared visual grammar. To retain the HIG’s full decision structure without turning this file into a copied manual, use the focused guides below:

| HIG area | Read when | Operational guide |
| --- | --- | --- |
| Foundations | Every page | [Foundations](hig-foundations.md) |
| Patterns | The page has a user flow beyond simple browsing | [Patterns](hig-patterns.md) |
| Components and Inputs | The page introduces a control, navigation, field, selection, or interaction | [Components and inputs](hig-components-inputs.md) |
| Technologies | The page surfaces a service, device capability, AI, payment, or sensitive data | [Technologies](hig-technologies.md) |

This routing is intentionally broad: a login page reads Foundations, Patterns, and Components/Inputs; a media browse page reads Foundations and Components/Inputs; a location-aware AI assistant reads all four. In every case, the specific liquid-glass renderer remains the single material implementation defined in `SKILL.md`.

## Three visual planes

Map every visible element to one of three planes before styling it:

1. **Content plane** — the person’s actual work, media, article, map, list, or form. Keep it direct and readable. Use ordinary backgrounds or standard materials for grouping.
2. **Standard-material plane** — a quiet content grouping surface, such as a privacy card or settings group. It separates related information without pretending to be a floating control.
3. **Liquid Glass control plane** — navigation, toolbars, tab bars, floating actions, and active transient controls. It floats over content, lets meaningful content or color appear beneath it, and exists to make actions distinct.

The control plane is not a universal card treatment. Keep it sparse, neutral by default, and above real content. Apple’s native system offers regular and clear glass variants; this skill deliberately has one fixed SVG four-layer renderer. Apply the native distinction by choosing *where* that renderer belongs: place it over rich content when its translucency can be read, and use an ordinary/standard surface or quieten the scene when text would become illegible. Do not create a second CSS glass renderer to imitate a native variant. Let content extend beneath a sidebar, toolbar, or tab bar so the floating relationship is visible.

## Foundation boundary

Color, typography, writing, iconography, imagery, adaptation, and accessibility are owned by [Foundations](hig-foundations.md). This guide uses their outcomes when it chooses planes, shape, grouping, and examples; it does not restate their rules.

## Component and shape grammar

Choose a shape because of the component and context, not because one radius feels fashionable:

| Situation | Apple-like choice |
| --- | --- |
| One icon-only action floating over content | Circular glass control with a familiar symbol |
| Related icon actions in one small toolbar group | One shared capsule/rounded material container; avoid drawing a separate circle around every icon |
| Standalone text or icon-plus-text action | Capsule when isolated or in a horizontal row |
| Text actions stacked vertically | Rounded rectangles with equal heights and clear spacing |
| Primary toolbar action | One tinted/prominent control on the trailing side; other actions stay neutral |
| Content grouping, settings, privacy explanation | Standard material or neutral rounded box, with generous padding and no nested card maze |
| Modal task | Sheet or alert only when focus or confirmation is genuinely needed; preserve the parent context and provide dismissal |

### Control topology and concentric geometry

Choose the *topology* before the radius: first decide whether people are acting on one independent target, several independent peer targets, or several contextually related actions that form one command group. Shape then reveals that relationship.

| Topology | Correct construction | Do not do this |
| --- | --- | --- |
| One independent icon action | One circular control | Put it inside a decorative second circle or a needless group shell |
| One independent text or icon-plus-text action | One capsule, especially when it floats alone | Use a rounded card merely because the label is long |
| Independent peer text actions in a horizontal row | Separate capsules are acceptable when each is a separately scannable action | Pretend that unrelated actions are one menu by drawing a shared shell |
| Contextually related actions, such as toolbar commands, an edit menu, or tab destinations | One shared glass vessel with contiguous hit regions; use spacing or subtle separators to distinguish items | Give every item a complete glass wrapper, rim, and pill border |
| Selected, hovered, or pressed member of a group | A local state surface *inside the clipped group*; it follows the group’s outer contour only at a group edge | Add a second standalone capsule, doubled rim, or a conflicting shadow around the member |
| Vertical action stack | Equal-height rounded rectangles with clear gaps; use a shared group only when the actions genuinely behave as one compact control | Turn every stacked row into a full-height capsule or a nested-card maze |

The edit-menu pattern is therefore not a row of pills. Its outer vessel says “these commands belong to this selection”; its members are contiguous targets; a temporary inner highlight says “this member is focused, pressed, or selected.” A destructive command stays last and receives its destructive treatment from semantic color and label, not from a different container shape.

Use **concentric geometry** for every visible inset. If a child surface is inset from a rounded parent by the same distance on every edge, derive the child radius from the parent rather than choosing a fashionable second number:

```text
child radius ≈ max(0, parent radius − uniform inset)
```

This is a practical CSS approximation, not a replacement for Apple’s concentric-shape APIs. For a capsule, the outer radius is half its height. An inset highlight should preferably be clipped by that same capsule; if it needs its own visible edge, use the corresponding reduced radius and verify it at the rendered size. `border-radius: inherit` alone is not concentric after an inset. For a circle, keep equal width and height. This is why a grouped menu can look rounder at its outside edges while its interior remains calm and almost rectangular. Do not use this formula to invent arbitrary nested cards — it applies only when the inset is a real child surface.

For a custom web toolbar, use one `liquid_glass-wrapper` for the group and keep the ordinary semantic buttons in its `liquid_glass-content`; do not nest a four-layer glass wrapper inside each button:

```html
<div class="liquid_glass-wrapper" data-glass-shape="pill" style="--border-radius: 999px">
  <div class="liquid_glass-outer"></div><div class="liquid_glass-cover"></div>
  <div class="liquid_glass-sharp"></div><div class="liquid_glass-reflect"></div>
  <div class="liquid_glass-content" role="toolbar" aria-label="编辑操作">
    <button class="group-action">剪切</button>
    <button class="group-action">复制</button>
    <button class="group-action">粘贴</button>
    <button class="group-action destructive">删除</button>
    <button class="group-action more" aria-label="更多编辑操作">…</button>
  </div>
</div>
```

This markup expresses a command group, not a literal native edit-menu replacement. When an actual menu is needed, use the platform-appropriate menu semantics and keyboard behavior; do not make a persistent toolbar look like a context menu just to obtain its shape.

Use component placement as part of its meaning:

- Sidebars are leading-edge navigation for broad peer areas and need sufficient space. They float above extended content; they are not opaque columns pasted beside it.
- Toolbars group navigation on the leading edge, context/title in the center or leading area, and important actions — including at most one primary action — on the trailing edge. Move lower-priority commands into More/overflow rather than crowding the bar.
- A bottom tab bar is for switching top-level areas, not for page-local commands. Search may be a dedicated, visibly distinct tab or an appropriate toolbar action when it is central to the task.
- A card should represent one logical group. Use padding, alignment, and a short descriptive heading before adding nested cards or decorative borders.

## Flow boundary

Task flows, input alternatives, and capability-specific trust decisions are owned by [Patterns](hig-patterns.md), [Components and inputs](hig-components-inputs.md), and [Technologies](hig-technologies.md). Read the applicable guide before turning this visual grammar into a page.

## Case-study reading: Landmarks

The Mount Fuji Landmarks image demonstrates the HIG layout and Liquid Glass guidance rather than a generic translucent dashboard.

- The mountain image is primary content and carries the saturated color. The article body switches to an ordinary, quiet reading surface; it does not remain inside glass.
- The leading sidebar is a navigation plane. It floats above a blurred, mirrored extension of the adjacent photo, making its separation visible without creating an empty opaque column.
- The top controls are functional chrome: a separate circular Back action at the leading edge, a compact shared action group on the trailing edge, and a distinct circular Info control. Shapes express grouping, not decoration.
- Symbols and navigation labels use a restrained tint while the photo provides the expressive palette. The UI does not compete with the media by tinting every element.
- Image, sidebar, and toolbar remain spatially related as the layout changes: content stays in focus while controls hover above it.

Use this composition when the product has genuinely rich media or a map. Do not add a photo merely to justify a glass sidebar.

## Case-study reading: App Privacy

The App Privacy image demonstrates how Apple makes complex disclosure feel calm and legible on a phone.

- The page begins with a clear title and a concise explanation. Dark, bold hierarchy names the topic; secondary body text is neutral gray; the policy link and the one acquisition action use blue as the action tint.
- Each white rounded card is a standard content grouping, not a glass panel. It has one purpose, a centered semantic symbol, a brief heading, supporting copy, and a scannable two-column list.
- Black category icons add shape-based recognition alongside text; color is not the only signal. Generous padding and repeated alignment make dense disclosure scan as small groups instead of a wall of paragraphs.
- The top Back action is icon-only and circular because it is a single navigation control. The blue Get control is a distinct capsule because it is one prominent text action. The bottom navigation is a shared floating glass group; Search is separated because it has a separate top-level role.
- The page trusts whitespace and type contrast. It does not use gradients, ornamental shadows, or multiple accent colors to manufacture importance.

Use this composition for disclosures, settings, account details, and structured information. Keep cards small relative to the view and avoid nesting cards inside cards.

## Research sources

This synthesis is based on the current official Apple Human Interface Guidelines and the visual examples the user supplied:

- [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines)
- [Design principles](https://developer.apple.com/design/human-interface-guidelines/design-principles)
- [Layout](https://developer.apple.com/design/human-interface-guidelines/layout)
- [Materials](https://developer.apple.com/design/human-interface-guidelines/materials)
- [Adopting Liquid Glass](https://developer.apple.com/documentation/TechnologyOverviews/adopting-liquid-glass)
- [Color](https://developer.apple.com/design/human-interface-guidelines/color)
- [Typography](https://developer.apple.com/design/human-interface-guidelines/typography)
- [Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons)
- [Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars)
- [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars)
- [Menus](https://developer.apple.com/design/human-interface-guidelines/menus)
- [Privacy](https://developer.apple.com/design/human-interface-guidelines/privacy)
- [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)
- [Inputs and gestures](https://developer.apple.com/design/human-interface-guidelines/gestures)
