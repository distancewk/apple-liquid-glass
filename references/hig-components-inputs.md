# Apple HIG Components and Inputs for Web Decisions

## Contents

- [Use this guide](#use-this-guide)
- [Component grammar](#component-grammar)
- [Control selection](#control-selection)
- [Input parity](#input-parity)
- [State and feedback](#state-and-feedback)
- [Review checklist](#review-checklist)
- [Official sources](#official-sources)

## Use this guide

Choose the component by its job, then apply the liquid-glass renderer only when the selected component belongs to the functional control plane. A visually attractive control with the wrong semantic element, location, state, or input path is not HIG-aligned.

## Component grammar

- **Navigation:** sidebar for broad peer destinations; tab bar for top-level mode switching; back control for hierarchical return; breadcrumb only when the hierarchy genuinely needs explicit path context.
- **Contextual actions:** toolbar actions live near the current context; group related icon actions in one compact container; keep one primary/prominent action at most where attention needs a clear answer; place lower-frequency actions in an overflow/menu.
- **Presentation:** a popover/anchored menu stays tied to its source; a sheet creates temporary focus while preserving a clear dismissal; an alert warns or asks for a consequential decision, not routine confirmation.
- **Content:** lists/tables support scanning and repeated peer items; a collection/grid supports visual or heterogeneous browsing; a card represents one logical group, not merely a desire for roundness.
- **Selection and input:** use a toggle for independent boolean state; segmented control for a small mutually exclusive visible set; menu/select for a longer exclusive set; checkbox list for multiple independent selections; radio-like options only when all exclusive options need comparison; slider for an immediate continuous range.
- **Status:** progress tells what is happening; badges/counters denote a concise status; labels carry readable explanation; avoid making a decorative symbol do all the work.

## Control selection

- A button initiates an immediate action. Give it a clear verb or a widely recognized symbol, a 44 CSS px touch target on touch pages, and an immediate press state.
- Keep prominent button treatment scarce. Use style and color, not mismatched size, to distinguish the preferred action. A horizontal row of text actions can use capsules; a vertical text stack uses related rounded rectangles.
- Use icon-only actions for standard, frequently recognized concepts and provide `aria-label`/tooltip. If users could reasonably ask “what does that icon do?”, add a text label.
- A text field requests a small, specific value. Use persistent labels when a placeholder would disappear and erase context; use appropriate input types/autocomplete; use secure entry for secrets; validate early without preventing correction.
- Native HTML controls (`button`, `input`, `select`, `dialog`, `details`) are preferred where they satisfy the task. Custom div-based controls must recreate semantics, focus, keyboard, state, and pointer behavior before they are acceptable.

## Input parity

- Touch: respond on press, leave sufficient space between targets, and never require hover. Touch gesture behavior follows common expectations and has a visible alternative.
- Pointer: use hover only as a supplemental affordance; preserve the same action by click/tap. Keep pointer target and visual target aligned; anchors, menus, and drag targets make the outcome predictable.
- Keyboard: logical Tab order follows reading order; Enter/Space activates buttons; Escape dismisses a dismissible transient surface; arrow keys only navigate patterns where that behavior is expected. Preserve standard browser and platform shortcuts instead of repurposing them.
- Assistive technology: expose names, roles, states, errors, and live changes. Do not encode the page’s only instruction in motion, color, hover, or drag.

## State and feedback

Every interactive component declares idle, hover (if relevant), focus-visible, pressed, selected/on, disabled, loading, success, and error behavior as applicable. State changes keep the material DOM stable: do not replace or reorder the four required glass layers to express a state.

For direct manipulation, track the pointer continuously, make motion interruptible, and provide a visible non-gesture route. For ordinary controls, a short, immediate press response is enough; do not add springy theatrics where no physical manipulation occurred.

## Review checklist

For each control, record: `user intent → semantic element → familiar component → placement/group → label/symbol → input alternatives → focus/press/disabled/error states → reason it is or is not glass`. If any link is unknown, return to the pattern or simplify the control.

## Official sources

- [Components](https://developer.apple.com/design/human-interface-guidelines/components)
- [Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons)
- [Text fields](https://developer.apple.com/design/human-interface-guidelines/text-fields)
- [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars)
- [Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars)
- [Gestures](https://developer.apple.com/design/human-interface-guidelines/gestures)
- [Keyboards](https://developer.apple.com/design/human-interface-guidelines/keyboards)
- [Pointing devices](https://developer.apple.com/design/human-interface-guidelines/pointing-devices)
