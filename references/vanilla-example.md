# Vanilla Four-Layer Fixture

## Contents

- [Purpose](#purpose)
- [Runnable fixture](#runnable-fixture)
- [Adaptation notes](#adaptation-notes)

## Purpose

This fixture is intentionally close to the reference code. It demonstrates the required SVG filter, four real layers, SVG mask rim, 2px cover blur, sharp edge, reflective inset, and readable content. It also contains a real scroll flow: the sticky `Field notes` control stays in place while varied chapter surfaces pass behind it. It is the baseline fixture for browser verification.

## Runnable fixture

Save the following as `index.html` and serve it from a local HTTP origin:

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="icon" href="data:," />
    <title>Liquid Glass</title>
    <style>
      * { box-sizing: border-box; }
      html { min-height: 100%; scroll-behavior: smooth; }
      body {
        min-height: 220vh;
        margin: 0;
        overflow-x: hidden;
        overflow-y: auto;
        font: 16px/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        color: rgba(255, 255, 255, .86);
        background:
          radial-gradient(circle at 12% 12%, #b2b79f 0 9%, transparent 30%),
          radial-gradient(circle at 88% 24%, #c7b8a7 0 8%, transparent 30%),
          radial-gradient(circle at 22% 78%, #737d75 0 10%, transparent 28%),
          linear-gradient(135deg, #30332e, #68685b 48%, #b8aa98);
      }
      button { font: inherit; }
      .liquid-filter { position: absolute; width: 0; height: 0; overflow: hidden; }
      .page-shell { width: min(92vw, 760px); margin: 0 auto; padding: 10vh 0 28vh; }
      .page-heading { max-width: 560px; margin-bottom: 28px; }
      .page-heading small { color: rgba(255, 255, 255, .58); letter-spacing: .16em; }
      .page-heading h1 { margin: 10px 0 8px; font-size: clamp(34px, 8vw, 68px); line-height: .98; font-weight: 500; letter-spacing: -.05em; }
      .page-heading p { max-width: 440px; margin: 0; color: rgba(255, 255, 255, .68); }
      .glass-toolbar {
        position: sticky;
        top: 24px;
        z-index: 10;
        display: flex;
        width: min(100%, 620px);
        min-height: 76px;
        margin: 0 auto 48px;
        overflow: hidden;
        border-radius: var(--border-radius);
      }
      .liquid_glass-wrapper {
        position: relative;
        display: flex;
        overflow: hidden;
        border-radius: var(--border-radius);
      }
      .liquid_glass-wrapper.glass-toolbar { position: sticky; }
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
        mask-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%"><rect x="0" y="0" width="100%" height="100%" rx="0" ry="0" fill="white"/></svg>'), url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%"><rect x="5" y="5" width="calc(100% - 10px)" height="calc(100% - 10px)" rx="21" ry="21" fill="white"/></svg>');
        mask-composite: exclude;
        -webkit-mask-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%"><rect x="0" y="0" width="100%" height="100%" rx="0" ry="0" fill="white"/></svg>'), url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%"><rect x="5" y="5" width="calc(100% - 10px)" height="calc(100% - 10px)" rx="21" ry="21" fill="white"/></svg>');
        -webkit-mask-composite: xor;
      }
      .liquid_glass-cover { z-index: 2; background: rgba(0, 0, 0, .12); backdrop-filter: blur(2px); -webkit-backdrop-filter: blur(2px); }
      .liquid_glass-sharp { z-index: 3; box-shadow: inset 1px 1px 0 rgba(255, 255, 255, .5), inset -1px -1px 0 rgba(255, 255, 255, .6); }
      .liquid_glass-reflect { z-index: 2; inset: 1px; box-shadow: inset 2px 2px 6px 2px rgba(255, 255, 255, .2), inset -2px -2px 4px -1px rgba(255, 255, 255, .2); }
      .liquid_glass-content { position: relative; z-index: 4; display: flex; align-items: center; gap: 16px; width: 100%; padding: 16px 22px; }
      .liquid_glass-content strong { font-size: 18px; font-weight: 600; }
      .liquid_glass-content span { margin-left: auto; color: rgba(255, 255, 255, .62); font-size: 13px; }
      .glass-action { flex: 0 0 auto; min-height: 44px; padding: 0 16px; border: 0; border-radius: 999px; color: white; background: rgba(255, 255, 255, .12); cursor: pointer; }
      .glass-action:hover { background: rgba(255, 255, 255, .2); }
      .glass-action:active { transform: translateY(1px) scale(.98); }
      .glass-action[aria-pressed="true"] { background: rgba(255, 255, 255, .28); }
      .glass-action:focus-visible { outline: 3px solid rgba(255, 255, 255, .95); outline-offset: 3px; }
      .scene-grid { display: grid; gap: 18px; }
      .scene-card { min-height: 190px; padding: 24px; border: 1px solid rgba(255, 255, 255, .2); color: rgba(255, 255, 255, .88); }
      .scene-card:nth-child(1) { width: 78%; border-radius: 34px 12px 12px 34px; background: linear-gradient(135deg, rgba(186, 192, 166, .72), rgba(85, 91, 78, .38)); }
      .scene-card:nth-child(2) { width: 58%; margin-left: auto; border-radius: 18px 42px 18px 18px; background: linear-gradient(135deg, rgba(161, 179, 157, .72), rgba(91, 99, 83, .4)); }
      .scene-card:nth-child(3) { width: 68%; border-radius: 44px 18px 18px 18px; background: linear-gradient(135deg, rgba(190, 157, 143, .72), rgba(93, 76, 68, .4)); }
      .scene-card:nth-child(4) { width: 50%; margin-left: auto; border-radius: 18px 18px 42px 18px; background: linear-gradient(135deg, rgba(147, 168, 177, .72), rgba(168, 143, 124, .42)); }
      .scene-card h2 { margin: 0 0 8px; font-size: 24px; font-weight: 500; }
      .scene-card p { max-width: 360px; margin: 0; color: rgba(255, 255, 255, .68); }
      @media (prefers-reduced-motion: reduce) { html { scroll-behavior: auto; } .glass-action:active { transform: none; } }
      html[data-glass-mode="fallback"] .liquid_glass-outer { display: none; }
      html[data-glass-mode="fallback"] .liquid_glass-wrapper { background: rgba(48, 49, 45, .9); }
      @supports not ((backdrop-filter: url(#liquid_glass_filter)) or (-webkit-backdrop-filter: url(#liquid_glass_filter))) {
        .liquid_glass-outer { display: none; }
        .liquid_glass-wrapper { background: rgba(48, 49, 45, .9); }
      }
      @media (forced-colors: active) {
        .liquid_glass-wrapper { border: 1px solid CanvasText; background: Canvas; color: CanvasText; }
        .liquid_glass-outer, .liquid_glass-cover, .liquid_glass-reflect { display: none; }
        .liquid_glass-sharp { box-shadow: none; }
      }
      @media (prefers-reduced-transparency: reduce) {
        .liquid_glass-wrapper { background: rgba(48, 49, 45, .94); }
        .liquid_glass-outer, .liquid_glass-cover { backdrop-filter: none; -webkit-backdrop-filter: none; }
      }
      @media (max-width: 560px) {
        .page-shell { width: min(88vw, 420px); padding-top: 8vh; }
        .glass-toolbar { top: 12px; min-height: 68px; margin-bottom: 34px; }
        .liquid_glass-content { padding: 12px 14px; gap: 10px; }
        .liquid_glass-content span { display: none; }
        .scene-card, .scene-card:nth-child(1), .scene-card:nth-child(2), .scene-card:nth-child(3), .scene-card:nth-child(4) { width: 100%; margin-left: 0; }
      }
    </style>
  </head>
  <body>
    <svg class="liquid-filter" style="display: none" aria-hidden="true">
      <defs>
        <filter id="liquid_glass_filter" x="0%" y="0%" width="100%" height="100%" filterUnits="objectBoundingBox">
          <feDisplacementMap scale="200" />
        </filter>
      </defs>
    </svg>

    <main class="page-shell">
      <header class="page-heading">
        <small>LIQUID GLASS / SCROLL TEST</small>
        <h1>Color keeps moving.</h1>
        <p>This is a real reading flow: the toolbar stays anchored while each changing surface passes behind it.</p>
      </header>

      <div class="liquid_glass-wrapper glass-toolbar" style="--border-radius: 26px">
        <div class="liquid_glass-outer"></div>
        <div class="liquid_glass-cover"></div>
        <div class="liquid_glass-sharp"></div>
        <div class="liquid_glass-reflect"></div>
        <div class="liquid_glass-content">
          <strong>Field notes</strong>
          <span>4 chapters · 12 min</span>
          <button class="glass-action" type="button" aria-pressed="false">Save</button>
        </div>
      </div>

      <section class="scene-grid" aria-label="Field notes chapters">
        <article class="scene-card"><h2>01 / Quiet morning</h2><p>A muted stone field establishes the first visual layer beneath the sticky control.</p></article>
        <article class="scene-card"><h2>02 / Warm current</h2><p>A restrained sage and amber surface changes the color sampled through the glass.</p></article>
        <article class="scene-card"><h2>03 / Soft signal</h2><p>A subdued clay field creates a second pass with a different edge contrast.</p></article>
        <article class="scene-card"><h2>04 / Open air</h2><p>The final blue-gray field makes the scroll-state difference easy to inspect.</p></article>
      </section>
    </main>
    <script>
      const saveButton = document.querySelector('.glass-action');
      saveButton.addEventListener('click', () => {
        const saved = saveButton.getAttribute('aria-pressed') === 'true';
        saveButton.setAttribute('aria-pressed', String(!saved));
        saveButton.textContent = saved ? 'Save' : 'Saved';
      });
    </script>
  </body>
</html>
```

## Adaptation notes

- Keep the class names and layer order stable when translating this fixture into a framework.
- Set `--border-radius` per instance rather than hard-coding shape geometry into the content.
- Keep product content at `z-index: 4` and do not place important text inside the refractive rim.
- Keep the reference filter declaration unchanged. Do not add a second displacement-map recipe to this fixture.
- Keep this fixture scrollable. Its sticky toolbar and changing chapter surfaces are part of its acceptance contract; do not restore `overflow: hidden` or replace the chapter surfaces with a test-only color strip. For a product page whose real task does not scroll, reuse the material layers but remove this synthetic flow and apply the non-scrollable preview check in `verification.md`.
- Keep the `Save` button's state change intact when adapting the fixture; it provides a minimal press/active behavior for browser verification.
- The scene cards intentionally use several muted colors to make scroll-through refraction observable; treat them as scene content, not as multiple UI accents.
- This fixture uses the `rounded` shape profile. For a pill or circle, replace both the wrapper radius and the inner SVG mask geometry as a matched pair, then verify the rim at the actual rendered size.
- If visual browser evidence shows that the rim is not readable, set `document.documentElement.dataset.glassMode = "fallback"`. This hides only `liquid_glass-outer` and keeps the cover, sharp, reflect, and content layers; record the browser engine and fallback screenshot.
