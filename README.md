# Aioli Bodega Española

A complete restaurant demo redesign for Vessel Archive, using Aioli’s real logo, food photography, Fall 2026 menus and booking destination.

## Preview

```sh
python3 -m http.server 8080
```

Open http://localhost:8080. The repository root and `dist/` both contain the ready-to-host site. No packages, API keys, accounts or paid services are required to run it.

## Edit and build

```sh
python3 scripts/menu_data.py
python3 scripts/build.py
python3 scripts/check.py
```

- `scripts/build.py`: shared page layout and content.
- `scripts/menu_data.py`: 67 text menu entries transcribed from the current restaurant menu images.
- `styles.css`: responsive styling; `app.js`: navigation, menu filters/search, gallery.
- `assets/originals/`: unchanged source photos, logo and all seven menu sheets.
- `assets/images/`: optimized WebP images.
- `assets/fonts/`: self-hosted Bodoni Moda and DM Sans with their licenses.
- `asset-sources.json`: original asset URLs.

The build uses Python’s standard library. Image assets are already prepared; Pillow is not needed to build or serve the site. Source photos were only resized and encoded as WebP, with display cropping in CSS. No generated food photos or image enhancement is presented as real photography.

## Pages

- `/`: homepage, menu paths, introduction and visiting information.
- `/menu/`: seasonal, lunch, dessert and drinks categories; accent-insensitive search; no-results recovery; complete original menu sheets.
- `/bodega/`: all ten original photos in a keyboard-accessible gallery.
- `/visit/`: reservations, hours, directions, contact and sister venues.
- `/404.html`: custom missing-page page.

The original homepage anchors `#content`, `#aioli-menu`, `#contact-aioli` and `#aioli-contact` remain. Relative links support GitHub Pages repository subpaths. Core content, links and the complete menu are available without JavaScript.

## GitHub Pages

Destination: `teovesselarchive/Aioli-Bodega-Espanola`. Choose **Settings → Pages → Deploy from a branch → main → /(root)**. The root `index.html` and `.nojekyll` support direct branch publishing. A source ZIP can also be deployed to any static host by uploading `dist/`.

## Content notes before a production launch

This is a demo and remains `noindex,nofollow`, with indexing disallowed in `robots.txt`.

- The homepage/contact block says Monday–Saturday 11am–10pm and Sunday 3pm–9pm. The printed menus contain conflicting closing times. This demo uses the homepage hours; confirm with the restaurant before production.
- The text menu preserves the listed prices for seasonal food, lunch, dessert and lunch cocktails. Printed wine and dessert sheets contain some differing drink prices. Complete originals remain available as the reference; confirm prices with the business.
- The current source has a Lunch menu but no separate Dinner menu. This demo does not invent one.
- Reservation links go to the restaurant’s real OpenTable ID 58273, verified in the source widget and on OpenTable. No booking is completed inside the demo.
- Phone, directions and social links are real. No invented contact form, checkout, customer reviews, awards or backend.
- The original Grand Wine Bar links contained spelling errors. The sister-venue links now go to the verified official `thegrandwinebar.com` and `brasseriedumonde.com`.
- Original brand, photography and menus remain the property of their respective owners. Confirm permission before a client production launch.

See `DESIGN.md` for the visual research and design decisions, and `QA.md` for completed checks.
