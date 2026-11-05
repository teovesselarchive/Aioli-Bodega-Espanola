# Aioli complete menu transcription

Transcribed from all seven Fall 2026 PNGs linked on the restaurant’s official website. Every sheet was visually inspected, with the small wine and spirit text cropped and enlarged. macOS text recognition supplied a second pass on the smallest type; its output was checked against the pixels rather than accepted automatically. The existing food-only JSON was used as a starting point and corrected against the originals.

## Deliverable and schema

`menu-complete.json` is an array of **52 groups containing 343 sheet-specific entries**, plus two food options (jamón serrano on pa amb tomaquet, and two additional lamb chops).

Every group has `id`, `section`, `category`, `title`, `note`, `source`, `menu`, `canonical`, and `items`. `category` and `section` use the six interface identifiers: seasonal, lunch, dessert, drinks, wine, spirits. Lunch beverage variants are placed in lunch; after-dinner variants are placed in dessert. Main bar groups retain `canonical: true`; overlapping lunch and after-dinner groups retain `canonical: false`. This is an editorial routing aid, not an assertion that one sheet is newer.

Every item has a stable ID, name, description, and source filename. Prices are decimal strings. Wines have separate `glass` and `bottle` fields where printed, plus `vintage` and `region`. Bottle-only wines also repeat the bottle amount in `price` for compatibility. Missing or unresolved prices are null and must display “Ask your server,” not zero. Food substitutions/additions are in `options` with their own price. `source_name`, `source_price`, `printed_markers`, `transcription_note`, and `uncertainty` retain relevant source details without forcing them into the public-facing prose.

| Original sheet | Groups | Entries | Coverage |
|---|---:|---:|---|
| Chef’s seasonal selections | 1 | 12 | All specials, including both pinchitos and the risotto for two |
| Lunch page 1 | 8 | 29 | Soup/salad, bocadillo, cold/hot tapas, pasta, main courses, paellas, lunch set |
| Lunch page 2 | 5 | 31 | 15 wines, five beers/cider, 11 cocktails |
| Dessert page 1 | 3 | 19 | Nine desserts, four coffee cocktails, six café drinks |
| Dessert page 2 | 3 | 29 | Seven sherries, six port/Madeira, 16 brandies/whiskies |
| Wine page 1 | 16 | 122 | Sangría, 11 cocktails, four coffee cocktails, five beers/cider, 22 wines, 79 spirits/fortified wines |
| Wine page 2 | 16 | 101 | Complete regional bottle list: Spain 49, France 11, Italy 9, Reda selections 7, New World 25 |
| **Total** | **52** | **343** | Duplicate offerings are preserved where the sheets repeat them |

The section totals for the interface are seasonal 12, lunch 60, dessert 48, drinks 21, wine 123, spirits 79.

## Unresolved source information

Three bottle entries intentionally have no numeric display price:

- **Deobriga Selección Familiar 2018:** the tiny source price could be 56 or 58. Two independent visual readings disagreed. Both candidates are stored in `possible_source_prices`; bottle and price are null.
- **Finca Martelo Reserva 2015:** the source price could be 120 or 132. Two independent visual readings did not settle it. Both candidates are stored in metadata; bottle and price are null.
- **Viña Progreso 2022:** the printed source contains no price on this line. No price was invented or inferred from neighboring wines.

## Differences between the published sheets

The JSON retains the original variants and explains the principal conflicts in the relevant group notes.

| Offering | Main wine/bar sheet | Lunch or dessert sheet |
|---|---|---|
| Monte Pío Albariño | $13 glass / $52 bottle | Lunch: $15 / $60 |
| Clavidor Verdejo | $13 / $52; Castilla y León | Lunch: $14 / $56; Rueda |
| Trefethen Chardonnay | Vintage 2022; $15 / $62 | Lunch: vintage 2020; $15 / $62 |
| Conquilla | Brut Nature Reserva; $12 / $48 | Lunch: Brut Cava; $12 / $44 |
| Smoke It Up | $17 | Lunch: $15 |
| White Coco | $16 | Lunch: $18 |
| Café Vaquero | $13; brown sugar | Dessert: $15; demerara syrup |
| Espresso Martini | House syrup | Dessert: agave syrup |
| Jerez de la Frontera | Cold brew and house syrup | Dessert: Mast cold brew and honey syrup |
| Monkey Shoulder | $14 | Dessert: $13 |
| Laphroaig | $15, no age stated | Dessert: 10 yr, $18 |
| Glenmorangie 12 | $18 | Dessert: $16 |
| Buchanan’s Deluxe 12 | $15 | Dessert: $12 |
| Dalmore 12 | $16 | Dessert: $15 |
| Corkage per 750 ml | $25 | Lunch: $20 |

The main bar sheet also lists Glenmorangie 10 at $17; the dessert sheet instead lists Glenfarclas 10 at $14. Both are preserved. Fernando de Castilla Amontillado, Arroyuelo Fino en Rama, Vallado 10 yr Tawny, Vecchia Romagna, Pedro I, Dewar’s, and Glenlivet 12 appear on the dessert sheet and are included even though absent from the principal bar list. Lustau Palo Cortado Península appears on the principal bar list and is also included.

Lunch and main-bar cocktail descriptions differ in places beyond price. Their exact ingredient distinctions remain separate: Chambery Martini’s lemon; Rosé Negroni’s specified La Fuerza vermouth; Sailors Delight’s pineapple garnish; Puertas al Infierno’s infused tequila/syrup versus tequila/lemon-jalapeño shrub; and some citrus finishes. Do not merge these descriptions silently.

## Food notes and printed markers

- The lunch set is $24 and includes soup, choice of fish/pasta/stew, and dessert.
- All four paellas serve two and require approximately 45 minutes.
- The seasonal risotto serves two.
- Pa amb tomaquet is $6.95; the source’s “with cured jamón serrano” option is $12.95 total. The extra two lamb chops on Parrillada Mixta are explicitly an additional $17.95.
- The source prints Ensalada con Pollo as 17.9. The JSON formats this as 17.90 while retaining `source_price`.
- Sopa del Día, Bocadillo del Día, and Tartar print “A.Q.” and display “Ask us.”
- The lunch notes state 20% gratuity for parties of six or more, use of extra-virgin olive oil, gluten and raw/undercooked ingredient markers, and the foodborne-illness advisory. These notes are in `source_notes`.
- **Do not infer dietary guarantees from the source’s V/VG markers.** The seasonal Palta Rellena explicitly lists shrimp and gravlax but prints “VG.” The lunch menu describes V as “vegan items, some items can be prepared vegan,” while the marked portobello includes goat cheese. The raw markers also include dishes with aioli. Markers are retained as evidence and not converted into vegan/vegetarian filters.

## Source spelling and classification

Names are lightly normalized for accents, standard capitalization, and obvious common spelling, while business-specific wording and ingredients are retained. Examples: Mascarpone Limón Mousse retains the source spelling “Marscopone” in metadata; Colas de Bruselas retains “Colas de Brusseles”; Croquitas al Gusto is preserved as printed. Known spirit brands were checked against their producer sites when the tiny type was initially ambiguous: [Sweet Gwendoline](https://sweetgwendolinefrenchgin.co.uk/), [Mal Bien](https://www.mezcalmalbien.com/), [Stonestreet](https://www.stonestreetwhiskey.com/), and [Enelalma](https://www.enelalmatequila.com/). These checks resolved spelling, not restaurant prices.

Some source classifications appear unusual and were not “corrected” by assumption: Herradura Añejo is under Mezcal; Algueira Risco is under Ribera del Duero; Charles Martinez of Baja California appears both in Reda’s selections and under South America. The data retains both appearances with explanatory metadata. Michter’s source appears to include “Irish Rye”; its display name is conservatively “Michter’s Rye,” with the printed wording retained.

## Business-information conflicts

All menu sheets show 1800 L Street, Sacramento CA 95811, 916-447-9440, and aiolibodega.com. They show differing opening hours:

- Lunch: Monday–Saturday 11am–11pm; Sunday 3pm–10pm.
- Dessert and wine: Monday–Thursday 11am–10pm; Friday/Saturday 11am–11pm; Sunday 3pm–10pm.
- The current official webpage displays Monday–Saturday 11am–10pm; Sunday 3pm–9pm.

These differences are recorded here rather than silently replacing the website’s business hours with print-menu hours.

## Original sources

- [Seasonal menu](https://aiolibodega.com/wp-content/uploads/2026/09/aioli-chefs-choice-fall-2026-menu.png)
- [Lunch page 1](https://aiolibodega.com/wp-content/uploads/2026/09/aioli-lunch-fall-2026-menu-p1.png)
- [Lunch page 2](https://aiolibodega.com/wp-content/uploads/2026/09/aioli-lunch-fall-2026-menu-p2.png)
- [Dessert page 1](https://aiolibodega.com/wp-content/uploads/2026/09/aioli-dessert-fall-2026-menu-p1.png)
- [Dessert page 2](https://aiolibodega.com/wp-content/uploads/2026/09/aioli-dessert-fall-2026-menu-p2.png)
- [Wine page 1](https://aiolibodega.com/wp-content/uploads/2026/09/aioli-wine-fall-2026-menu-p1.png)
- [Wine page 2](https://aiolibodega.com/wp-content/uploads/2026/09/aioli-wine-fall-2026-menu-p2.png)

All originals remain unmodified. Enlargements and OCR output are inspection aids in `work/research`, not replacements for original menu images.
