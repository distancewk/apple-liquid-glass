# Vanilla Four-Layer Fixture

## Contents

- [Purpose](#purpose)
- [Runnable fixture](#runnable-fixture)
- [Adaptation notes](#adaptation-notes)

## Purpose

This fixture is intentionally close to the reference code. It demonstrates the required SVG filter, four real layers, SVG mask rim, 2px cover blur, sharp edge, reflective inset, and readable content. It is the baseline fixture for browser verification.

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
      html, body { min-height: 100%; margin: 0; }
      body {
        min-height: 100vh;
        overflow: hidden;
        font: 16px/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        color: rgba(255, 255, 255, .86);
        background:
          radial-gradient(circle at 15% 20%, #8db5df, transparent 32%),
          radial-gradient(circle at 85% 30%, #efc4ba, transparent 34%),
          linear-gradient(135deg, #5d83b5, #a7a6c9 58%, #d8b3b3);
      }
      button { font: inherit; }
      .liquid-filter { position: absolute; width: 0; height: 0; overflow: hidden; }
      .liquid_glass-wrapper {
        position: relative;
        display: flex;
        width: min(80vw, 520px);
        min-height: 120px;
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
        mask-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%"><rect x="0" y="0" width="100%" height="100%" rx="0" ry="0" fill="white"/></svg>'), url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%"><rect x="5" y="5" width="calc(100% - 10px)" height="calc(100% - 10px)" rx="21" ry="21" fill="white"/></svg>');
        mask-composite: exclude;
        -webkit-mask-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%"><rect x="0" y="0" width="100%" height="100%" rx="0" ry="0" fill="white"/></svg>'), url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%"><rect x="5" y="5" width="calc(100% - 10px)" height="calc(100% - 10px)" rx="21" ry="21" fill="white"/></svg>');
        -webkit-mask-composite: xor;
      }
      .liquid_glass-cover { z-index: 2; background: rgba(0, 0, 0, .12); backdrop-filter: blur(2px); -webkit-backdrop-filter: blur(2px); }
      .liquid_glass-sharp { z-index: 3; box-shadow: inset 1px 1px 0 rgba(255, 255, 255, .5), inset -1px -1px 0 rgba(255, 255, 255, .6); }
      .liquid_glass-reflect { z-index: 2; inset: 1px; box-shadow: inset 2px 2px 6px 2px rgba(255, 255, 255, .2), inset -2px -2px 4px -1px rgba(255, 255, 255, .2); }
      .liquid_glass-content { position: relative; z-index: 4; display: grid; align-content: center; gap: 5px; width: 100%; padding: 24px 30px; }
      .liquid_glass-content small { color: rgba(255, 255, 255, .58); letter-spacing: .16em; }
      .liquid_glass-content strong { font-size: 28px; font-weight: 500; }
      @media (forced-colors: active) {
        .liquid_glass-wrapper { border: 1px solid CanvasText; background: Canvas; color: CanvasText; }
        .liquid_glass-outer, .liquid_glass-cover, .liquid_glass-reflect { display: none; }
        .liquid_glass-sharp { box-shadow: none; }
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

    <main class="liquid_glass-wrapper" style="--border-radius: 26px">
      <div class="liquid_glass-outer"></div>
      <div class="liquid_glass-cover"></div>
      <div class="liquid_glass-sharp"></div>
      <div class="liquid_glass-reflect"></div>
      <div class="liquid_glass-content">
        <small>LIQUID GLASS / FOUR LAYERS</small>
        <strong>Rain on glass</strong>
        <span>The edge bends the background; the center stays readable.</span>
      </div>
    </main>
  </body>
</html>
```

## Adaptation notes

- Keep the class names and layer order stable when translating this fixture into a framework.
- Set `--border-radius` per instance rather than hard-coding shape geometry into the content.
- Keep product content at `z-index: 4` and do not place important text inside the refractive rim.
- If the SVG filter URL is unavailable, hide only `liquid_glass-outer` and keep the cover, sharp, reflect, and content layers.
