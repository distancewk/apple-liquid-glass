# Apple HIG Foundations for Web Decisions

## Contents

- [Use and boundary](#use-and-boundary)
- [Purpose, agency, responsibility](#purpose-agency-responsibility)
- [Layout and material](#layout-and-material)
- [Color and icons](#color-and-icons)
- [Type, writing, language, and imagery](#type-writing-language-and-imagery)
- [Accessibility baseline](#accessibility-baseline)
- [Foundation acceptance](#foundation-acceptance)
- [Official sources](#official-sources)

## Use and boundary

Read this whole guide for every page made with this skill. It condenses the HIG foundation topics into choices an HTML/CSS/JS page can actually make. It does not turn a web page into an Apple-native app and it does not license Apple assets or branding.

The operative order is: purpose → content and task → layout → familiar controls → material → decoration. Liquid Glass is the fixed implementation for the chosen control plane; it never decides the product’s purpose.

## Purpose, agency, responsibility

- **Purpose:** write one user job, show its common path without a tutorial, and use secondary views or disclosure for infrequent detail.
- **Agency:** expose state, avoid traps, offer Cancel/Back/Undo where a person might reasonably reverse a choice, and never make a transient timer the only way to act.
- **Responsibility:** minimize data collection and permissions; say what is requested, why it is needed now, and what happens if it is declined. Do not present privacy, biometric, location, or AI claims as visual decoration.
- **Familiarity and consistency:** a control’s label, symbol, location, and outcome agree across the page. Prefer established browser and Apple-like patterns over a novel gesture or ambiguous metaphor.
- **Flexibility:** preserve the same task in a narrow viewport, large text, RTL language, keyboard-only use, high contrast, reduced transparency, and reduced motion.

## Layout and material

- Group related information with spacing, alignment, quiet surfaces, and separators, while keeping content separate from controls.
- Give essential information room and place it in reading order. Do not crowd the initial view with secondary controls or use a hero slogan to postpone the task.
- Let meaningful backgrounds, artwork, and scrollable content extend beneath the functional control plane. Respect browser safe-area insets, readable margins, viewport changes, and text reflow.
- Use the three planes: content; standard-material grouping; and Liquid Glass controls. A standard group is quiet and readable; glass floats to organize navigation or an immediate action.
- Use concentric related radii for nested shapes. Let an isolated action be circular or capsule-shaped; let a group share one surrounding surface rather than multiplying glass containers.
- Treat the background underneath glass as part of its legibility contract. At the resting scroll position, do not place similarly colored content directly behind control labels; use a scroll-edge treatment, a quieter scene, or stronger material separation when content moves beneath a control.

## Color and icons

### Color

- Start from named roles — background levels, label hierarchy, separator, tint, link, selection, and status — then supply light, dark, and increased-contrast values. Prefer semantic CSS custom properties over scattered hex values.
- One restrained tint can identify action, links, selection, and brand continuity. Use status hue only for actual status, and pair it with text, symbols, or state change.
- Do not use the same color for unrelated meanings, hard-code an Apple system color as a permanent value, or make color the sole indication of focus, error, or interactivity.
- Keep the liquid-glass cover neutral. Scene content may color the glass naturally; chromatic UI treatment still needs a named semantic job.
- On glass, prefer monochrome labels and symbols that can adapt to the underlying scene. If a primary action needs color, tint that single action’s background rather than tinting its label or several neighboring controls. Do not make every toolbar action colorful.
- Treat light, dark, and increased-contrast appearances as designed states, not inverted screenshots: dark surfaces generally recede while elevated surfaces separate foreground work; check icons, imagery, and text independently because a light-mode asset may disappear in dark mode.

### Icons

- An interface icon expresses one familiar concept with simplified geometry. Keep one coherent family, consistent visual weight, stroke/filled treatment, optical size, and perspective.
- Prefer a conventional symbol when it communicates the action directly. Add text when an icon alone is ambiguous; every icon-only control needs an accessible name and a visible focus/press state.
- Treat app icons as product-brand assets, not interface chrome. Do not use an app-style illustrated tile as a substitute for a clear action icon.

## Type, writing, language, and imagery

- Use a system font by default. Build hierarchy through size, weight, line height, contrast, spacing, and order; avoid thin functional text and hard-coded heights that clip at larger text sizes.
- Write concise, active, descriptive labels. Prefer `Save`, `Continue`, and `Learn about privacy` to slogans, vague `Click here`, or cute phrases. Keep related labels grammatical and consistently capitalized.
- Design for long strings and RTL: use logical CSS properties, mirror directional icons only when their meaning is directional, and do not encode reading order in absolute positioning.
- Let photography, maps, and artwork carry expressive color when they are actual content. Put extended reading or dense information on a quiet plane; do not place low-contrast text directly on busy media.

## Accessibility baseline

- Make information perceivable through more than color: pair state color with text, shape, icon, position, or announcement.
- Support text zoom and responsive reflow without clipped controls, hidden labels, or horizontal page scrolling. Maintain reading and focus order in the DOM.
- Provide visible keyboard focus, semantic names/roles/states, native controls whenever possible, and a comfortable pointer/touch target (44 CSS px for touch-oriented pages unless product context dictates more).
- Keep custom motion optional and comprehensible: respect reduced motion with fades/static state; respect reduced transparency and contrast preferences with more opaque, higher-separation surfaces.
- Do not make touch gestures exclusive. A visible control and keyboard/pointer path must achieve the core action.

## Foundation acceptance

Before preview, answer: Is the user’s task visible in reading order? Is every non-neutral color semantic and adaptive? Are icons familiar and named? Does the hierarchy survive large text, a narrow viewport, dark mode, RTL, high contrast, and reduced transparency? Does each glass surface belong to the functional control plane?

## Official sources

- [Design principles](https://developer.apple.com/design/human-interface-guidelines/design-principles)
- [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)
- [Layout](https://developer.apple.com/design/human-interface-guidelines/layout)
- [Materials](https://developer.apple.com/design/human-interface-guidelines/materials)
- [Color](https://developer.apple.com/design/human-interface-guidelines/color)
- [Dark Mode](https://developer.apple.com/design/human-interface-guidelines/dark-mode)
- [Icons](https://developer.apple.com/design/human-interface-guidelines/icons)
- [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols)
- [Typography](https://developer.apple.com/design/human-interface-guidelines/typography)
- [Writing](https://developer.apple.com/design/human-interface-guidelines/writing)
