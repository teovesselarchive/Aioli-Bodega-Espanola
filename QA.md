# Verification — Aioli interior direction

Checked November 5, 2026.

- Home, menu, bodega and visit pages checked at 320, 390, 768, 1024 and 1440px: no horizontal document overflow or broken loaded images. The complete 343-item menu also fits at 320px.
- Reviewed desktop and mobile composition against the actual Sacramento interior research. Checked plum/amber contrast, clay-section text, copper photo frames, mosaic border and the original courtyard crop. Adjusted the phone hero spacing to keep its menu action clear of the fixed reservation bar.
- New courtyard original preserved at 1024×681; responsive 480/960/1024 WebP variants generated without upscaling. All other originals remain. The gallery now has eleven real restaurant photos. First photo is the patio; Next advances 1/11 to 2/11; Escape closes the dialog. Existing keyboard navigation and focus restoration remain in place.
- Menu behavior checked in browser: wine by the glass returns 15 selections; paella search returns four; clearing restores all 343. Menu data and all printed-sheet variants are unchanged. Both food options remain visible. Three unclear/missing bottle prices still say Ask your server.
- Calculated contrast: dark text on amber action 6.30:1; secondary text on paper 4.87:1; paper on plum 8.44:1; copper link text on paper 4.98:1. Clay-section body text was darkened to meet 4.5:1. Large plum headings on clay exceed 3:1. Visible focus and reduced-motion overrides remain.
- Static verification passes: 135 local references across five pages, no duplicate IDs, seven original menu sheets, root/dist HTML/CSS/JS/data parity. The decorative mosaic SVG exists and renders through CSS. Browser console contained no errors in the checked session.
- All homepage images were loaded before final desktop/mobile screenshots. Locally served licensed fonts and responsive photos; no new external runtime dependencies.
- Existing menu-section jump, mobile navigation, print selection and OpenTable restaurant ID 58273 remain. No reservation submitted.

The image library includes older original photography; upload dates are documented and no current photo shoot is claimed. Source-price/hour discrepancies are detailed in docs/menu-transcription.md. No automated accessibility certification or performance score is claimed.
