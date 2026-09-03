# Strict Apple Profile

## Contents

- [Purpose](#purpose)
- [Interface foundation](#interface-foundation)
- [Content color boundary](#content-color-boundary)
- [Type, layout, and controls](#type-layout-and-controls)
- [Strict review](#strict-review)

## Purpose

Use this profile for every page made with `apple-liquid-glass`. It converts the HIG's principles into a deliberately narrow web baseline. The result should read as a calm Apple-like product interface, not as a themed landing page or an "Apple-inspired" experiment.

## Interface foundation

- Build the interface from neutral background levels, neutral label hierarchy, separators, and one application tint.
- Declare semantic CSS variables for background, elevated surface, primary and secondary label, separator, tint, link, selection, and required statuses. Define light, dark, and increased-contrast values before styling components.
- Use the application tint only for the current primary action, links, selection, or a single active control. Status colors represent real success, warning, or destructive state and include text or an icon.
- Keep Liquid Glass neutral. Its apparent color comes from content underneath; never recolor the cover or use colored glass as atmosphere.
- No decorative gradient, glow, noise texture, or color field belongs to the interface plane. If it does not represent actual user-visible content, remove it.

## Content color boundary

Expressive color is permitted only inside named content assets: supplied photography, map imagery, album artwork, an actual chart, or a meaningful content category. Give the asset a clear content role and keep controls, labels, and surrounding surfaces neutral.

Do not fabricate abstract CSS artwork, rainbow panels, or multi-color notes merely to make translucency visible. For a scroll-through test, use meaningful media, map, document, or data content that naturally varies beneath the anchored control.

## Type, layout, and controls

- Use the system font stack. Build hierarchy from readable sizes, weights, leading, alignment, and whitespace; a display-style headline is not a default anchor.
- Make the primary task readable in the first view. Prefer a concise page title and task context over a slogan or oversized statement.
- Use ordinary white/neutral groups for content. Let one logical group have one purpose; avoid decorative shadows and nested card structures.
- Use familiar control topology: a circular isolated icon action, one shared vessel for related commands, an appropriate text capsule for one prominent action, and a quiet local selected state inside a group.
- Keep toolbars compact, place a maximum of one prominent primary action, and move secondary commands to a standard menu or secondary view.

## Strict review

Mark the page `FAIL` and repair it if any answer is true:

- Does the interface use more than one non-status application tint?
- Does an interface color lack one of the allowed semantic roles?
- Is a gradient, glow, illustration, color field, or oversized display type present only to create atmosphere?
- Does a colorful asset tint nearby UI or compete with the task controls?
- Would the page still look like the same product if its content artwork were removed? If not, the interface is relying on decoration rather than hierarchy.
- Does a case differ from another case by its UI palette or typography rather than its task and composition?

Only pass after the answers are all `no`, the material review passes, and light, dark, increased-contrast, reduced-transparency, and narrow-viewport behavior are verified or explicitly recorded as unverified.
