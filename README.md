# Aioli Bodega Española

Vessel Archive’s restaurant redesign: a bold Spanish bodega identity and a complete, functioning food and drinks menu. Uses Aioli’s real logo, food/room photography, seven Fall 2026 menu sheets and verified OpenTable destination.

## Run locally

```sh
python3 -m http.server 8080
```

Open http://localhost:8080. Both the repository root and dist contain the ready-to-host site. No packages, accounts, API keys or paid services are needed.

## Edit and build

Edit data/menu.json for menu content, scripts/build.py for page structure/content, styles.css for the visual system and app.js for interactions. Then:

```sh
python3 scripts/menu_data.py
python3 scripts/build.py
python3 scripts/check.py
```

menu_data.py validates the data; it does not overwrite it. build.py uses Python’s standard library. Image assets are already prepared; Pillow is unnecessary for building or serving.

## Pages and interactions

- Home: original Aioli masthead/ceramic composition, real dishes, six menu paths and visiting information.
- Menu: 343 sheet-specific entries in 52 groups, six primary sections, two food options, live accent-insensitive search, category narrowing, glass/bottle prices, by-the-glass filter, clear/empty states, URL category links print selection and a persistent mobile Menu sections control.
- Bodega: all ten original photos, keyboard-accessible gallery, previous/next, Escape and focus restoration.
- Visit: real OpenTable booking link, hours, telephone, directions and sister venues.
- Custom 404 page.

Starting a fresh search searches all sections. Select a category afterwards to narrow results. The full menu remains HTML-readable without JavaScript, and the original sheets remain available. Original anchors #content, #aioli-menu, #contact-aioli and #aioli-contact are retained. Relative links support a GitHub Pages repository path.

## Assets and hosting

assets/originals contains unchanged source photos, logo and all seven menus. assets/images contains responsive WebP versions; cropping is done in CSS. assets/fonts contains locally served Bricolage Grotesque, Barlow Condensed, Bodoni Moda and DM Sans with licenses. asset-sources.json records original URLs. No generated food photography is used.

GitHub: teovesselarchive/Aioli-Bodega-Espanola. The root index.html and .nojekyll support branch hosting. dist can be uploaded to any static host. The ZIP includes portable source and the generated website.

## Content notes

The demo remains noindex/nofollow and robots.txt disallows indexing. Restaurant confirmation is needed for three unclear/missing wine prices and differences between printed hours and the homepage. The site displays Ask your server for those prices and uses the official homepage’s hours. Lunch/bar and dessert/bar versions retain their respective printed prices and descriptions. No separate dinner menu was supplied; none is invented. No dietary guarantees are inferred from contradictory source markers.

OpenTable restaurant ID 58273 was verified against the live source widget and booking destination. Reservations happen on OpenTable; this demo does not submit a booking. Phone, directions, social and sister-venue links are real. No invented contact form, checkout, testimonials, awards or backend. Original materials remain their owners’ property.

See DESIGN.md, QA.md, docs/award-research.md and docs/menu-transcription.md for rationale, checks and source discrepancies.
