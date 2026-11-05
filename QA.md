# Verification — second design

Checked November 4, 2026.

- Four primary pages checked at 320, 390, 768, 1024 and 1440px: no document horizontal overflow. One h1 per page. The full 343-item selection also has no overflow at 320px. All loaded source images resolved. The closed lightbox intentionally has an empty image until opened.
- Desktop/mobile visual review of the full homepage and menu. Increased menu reading sizes; corrected the ceramic crop inside the O; strengthened contrast over the grill photograph and focus indicators on colored sections.
- All 343 HTML menu entries match the validated data. All 52 groups have source-sheet mappings; all item IDs are unique. Seven original menu sheets retained. Both food options render with their correct total/additional pricing.
- Category, search and wine filtering tested in the browser: wine 123 selections; by-the-glass 15; paella search returns four lunch paellas; impossible query shows empty state; reset restores 343 selections. Search includes group titles, ingredients, grape, region and vintage and ignores accents. Direct category hashes work.
- A persistent mobile Menu sections control returns directly from long lists to the category controls. Mobile navigation opens, Escape closes it and focus returns to the Menu button. Gallery next changes 1/10 to 2/10; ArrowLeft returns to 1/10; Escape closes the dialog and restores focus to the originating link. No console errors in the tested browser session.
- Static checks pass: 133 local references across five pages, no duplicate IDs, original menu files present, noindex metadata and root/dist HTML/CSS/JS/data parity. Browser JavaScript loaded and ran without parse errors. Core content and links are in HTML without JavaScript; controls hide in the no-script fallback.
- Print stylesheet preserves the current selection and removes site navigation. Reduced-motion CSS disables animation/transitions and smooth scrolling. No automated accessibility certification or performance score is claimed.
- Responsive WebP variants, explicit image dimensions, eager hero and lazy lower-page images, self-hosted fonts. No trackers or external runtime dependencies.
- OpenTable destination remains restaurant ID 58273, verified in the first pass. No reservation submitted.

Source limitations are explicit in docs/menu-transcription.md: three prices absent or illegible display Ask your server; menu-specific price/ingredient variants are preserved; homepage opening times are used where print sheets disagree. Dietary labels are not inferred from inconsistent source markers.
