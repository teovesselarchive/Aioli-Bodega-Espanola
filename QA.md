# Verification

Checked November 4, 2026.

- Home, menu, gallery and visit pages checked in the browser at widths 320, 390, 768, 1024 and 1440px: no document overflow or broken loaded images.
- Desktop and mobile visual review, followed by a single batch of refinements: cleared the hero caption from the wine-photo inset and removed photo captions that collided with the large display lettering.
- All homepage images verified loaded before saving final desktop and mobile previews.
- Menu search for “paella” returns exactly four lunch paellas; nonsense query produces the empty state; reset restores all 67 items. Category filters and direct category links checked.
- Mobile menu opens, closes with Escape, and returns focus to the Menu button.
- Gallery next control advances to the next photo; Escape closes the dialog and restores focus to the originating photo link. Ten original photos remain available. Photo links also open images without JavaScript.
- OpenTable reservation link verified in the browser as “Reservation at Aioli Bodega Espanola”, restaurant ID 58273. No reservation submitted.
- 136 local references checked across all five generated pages, all seven original menu sheets present, root/dist HTML and CSS/JS parity verified.
- Browser error log contained no errors.
- Contrast ratios calculated from the actual palette; visible focus, keyboard controls and reduced-motion overrides reviewed. No automated accessibility certification or Lighthouse performance score is claimed.
- Responsive WebP image variants, explicit image dimensions, eager hero imagery and lazy below-fold images; locally served typefaces.

Known source-content issues requiring restaurant confirmation before production: printed-menu closing times and some drink prices disagree with other source sheets. The homepage hours and lunch cocktail prices are used; originals are preserved for review.
