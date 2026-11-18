# Prompt for Grok App Builder: RATEENA SOUND, Stage 00 chapter screens (v3)

Copy everything below the line into the App Builder.

---

You are implementing the **Stage 00 "Framing and Assumptions"** chapter screens in the **RATEENA SOUND** app. The approved design is in the attached package `RATEENA-Stage0-Chapters-v3.zip`. Treat its HTML pages, `DESIGN-SPEC.md`, screenshots, fonts, logo and banners as the **source of truth**, and reproduce them faithfully.

## Hard constraints (read first)
1. **Do not modify, overwrite, push to, or publish** the existing application or its repository (including `deepershi8-art/rateena-sound-2`) without explicit written approval from the owner. Work on a separate branch or preview, show the result, and wait for approval.
2. **Do not publish anything publicly** (prototype, preview link, store build) without explicit permission.
3. **Preserve approved designs and assets.** Do not redraw, recolour, crop, retouch or re-generate the logo or the banner images. Use the files exactly as supplied.
4. **No unnecessary libraries, external services, CDNs, analytics or web fonts.** Use only the app's existing stack. Fonts are bundled locally from `fonts/`.
5. **"RATEENA" is always written in Latin letters**, in English and Arabic alike. Never transliterate it as رتينة or anything similar. The same applies to "RATEENA SOUND".
6. **No long dashes anywhere in the app.** Never use an em dash or en dash, or a spaced hyphen as a dash, in any text, label, title, alt text or strip name. Use a comma, a full stop, a colon or a line break (Arabic: ، or a full stop). Hyphens inside words (Room-within-a-Room, world-class) are fine.

## Brand
- Background: pure black `#000000`. Gold `#C2AD90` for text on black, the logo, the active state and hairlines (`rgba(194,173,144,.25)`).
- Chapter card: warm white `#F5F2EC`. Ink `#141210`, body `#2B2722`, bronze `#8A7558` (kicker and rule), lead `#6E5C43`.
- Logo: `rateena-logo.svg`, unchanged, top-right in EN and top-left in AR.
- Fonts: Montserrat (Latin) and Noto Naskh Arabic (Arabic), both variable TTFs in `fonts/`.

## Structure
Stage 00 has **10 chapters**, each its own screen, in EN and AR (20 screens total).

| # | EN title | AR title | Strip label EN | Strip label AR | Banner |
|---|---|---|---|---|---|
| 01 | Seven O'Clock in Cairo | الساعة السابعة مساءً في القاهرة | Seven o'clock in Cairo | الساعة السابعة مساءً | final/ch01 |
| 02 | Who Is This Story For? | لمن نروي هذه الحكاية؟ | Who this story is for | لمن نروي هذه الحكاية | final/ch02 |
| 03 | What Does “World-Class” Really Mean? | ماذا يعني المستوى العالمي حقاً؟ | What world-class means | معنى المستوى العالمي | final/ch03 |
| 04 | Two Facilities, One Standard of Excellence | منشأتان، ومعيار واحد للتميّز | Two facilities, one standard | منشأتان ومعيار واحد | final/ch04 |
| 05 | The Flagship Studio: One Live Room, Three Missions | الاستوديو الرئيسي: غرفة واحدة، وثلاث مهام | The flagship | الاستوديو الرئيسي | final/ch05 |
| 06 | The Building: What Do We Need From It? | المبنى: شنو المطلوب منه؟ | The building | المبنى | final/ch06 |
| 07 | How Will We Tell This Story? | كيف بنحكي الحكاية دي؟ | How we tell the story | كيف بنحكي الحكاية | final/ch07 |
| 08 | The Road Ahead | الطريق القدامنا | The road ahead | الطريق القدامنا | final/ch08 |
| 09 | Glossary | مسرد المصطلحات الفنية | Glossary | المسرد | final/ch09 |
| 10 | The Next Step: The Size of a Room | الخطوة الجاية: حجم الغرفة | The size of a room | حجم الغرفة | final/ch10 |

The chapter texts are in `texts/` (`page-ch01..06-{en,ar}.md` and `new-ch07..10-{en,ar}.md`) and are already rendered in the HTML pages. Use them **verbatim**. Arabic pages use the owner's Sudanese Arabic, and English pages use the full English. The old chapter "What this study deliberately does not do" has been **permanently removed**; do not bring it back.

## Screen layout (top to bottom), fixed full-screen with no page scroll
1. **Header** (76 px on mobile): BACK on one side, the language switch `EN | عربي` centred, and the logo (62 px wide) on the other side. A 1 px gold hairline sits below it.
2. **Banner band**: the chapter's banner, full width and black, at its **own aspect ratio**, never cropped (`object-fit: contain`). Max height is `min(32vh, 440px)`. On ≥ 900 px the banner is centred at `width:auto` with max height `min(26vh, 360px)`. A 1 px hairline sits below it. Do **not** mirror banners in Arabic.
3. **Stage line**: a large thin "00" next to "FRAMING AND ASSUMPTIONS" / "STAGE 00 OF 08" (AR: الإطار العام والافتراضات / الجزء 00 من 08).
4. **Chapter card** (warm white, radius 14 px, fills the remaining height, **only this card scrolls**): kicker `CHAPTER 0N` (AR `الفصل 0N`), title, a 34 px bronze rule, then the body (paragraphs, h3 sub-headings, bold lead lines, lists, and the ch04 table that becomes stacked cards below 540 px). Bottom padding is 120 px.
5. **Bottom strip** (black): a meta row with `CHAPTERS` and the counter `NN / 10`, then a horizontally scrolling row of 10 fixed-width items (80 px, 88 px ≥ 600 px; gap 8 to 16 px). Each item shows the number (Montserrat 300, 15 px) above a 2-line short name. About **4 items are visible plus a peek** of the next one on a 390 px screen.

All exact sizes, paddings and the type scale are in `DESIGN-SPEC.md`; follow them.

## Behaviour
- Tapping a strip item cross-fades the card: fade out over 280 ms, then the new chapter fades in from opacity 0 to 1 over 0.4 s ease. Honour reduced-motion.
- The active item is gold at full opacity with a 1 px gold underline and is **auto-centred** in the strip. Inactive items are at 45 % opacity. Scroll snap is `x proximity` and the scrollbar is hidden.
- The counter `NN / 10` is **always LTR**, even in Arabic. Never show "10 / 07".
- The language switch keeps the same chapter.
- BACK returns to the Stage list or overview in the existing app.

## Arabic / RTL rules
- `dir="rtl"`: mirror the header, stage line, card alignment, list indents and strip order (chapter 01 starts on the right). Flip the back chevron.
- Keep Latin terms (RATEENA SOUND, Stage 01, HVAC, Foley, Live Room …) in Latin letters inside LTR-isolated spans (`unicode-bidi:isolate`), so the punctuation lands correctly.
- Arabic sizes: body 16 px with line-height 1.9, and strip labels 13 px. Use Naskh for body text, titles and labels. Numbers stay in Montserrat.

## Assets (in the package)
- `images/banners/final/` holds the 10 approved banners: `chNN.png` (1920 × 1080 master), `chNN-web.jpg` (1600 × 900), `chNN-800.jpg`, `chNN-1600.webp`, `chNN-800.webp`. All are 16 : 9. Serve WebP with a JPG fallback and `srcset` 800w/1600w. `images/banners/` keeps the owner's originals for reference only; do not use them in the app.
- `rateena-logo.svg` and `fonts/*.ttf`.
- `screenshots/Stage00-ChNN-mobile-{en,ar}.png` are the 390 × 844 @2x references for every screen.

## Banner notes
- All 10 banners already carry the authentic RATEENA logo, STAGE 00, FRAMING AND ASSUMPTIONS and the correct CHAPTER number. Use them as supplied. Do not redraw, retype or crop them.
- Banner titles are the owner's artwork wording and can differ slightly from the card titles (ch07 "HOW THIS STORY IS TOLD", ch10 "NEXT STEPS & DELIVERABLES"). That is intended.

## Deliverable
Build these screens in a **non-production branch or preview** and send screenshots of ch01 EN, ch07 AR, ch09 EN and ch10 AR at 390 × 844 for approval. Do not merge, deploy or publish until the owner approves.
