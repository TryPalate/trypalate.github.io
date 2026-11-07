# Palate landing page: design system

The site and the app share one look: warm paper, ink, and one soft accent. The colourful glow (the logo's five colours) appears only in the hero, the final call to action and the logo mark, so it stays special.

## Color
| Token | Light | Dark | Role |
|---|---|---|---|
| `--bg` | #F6F3EE | #100E0C | page (warm paper / warm black) |
| `--card` | #FFFFFF | #1B1916 | cards, mockups |
| `--raise` | #ECE6DE | #26231F | quiet fills (search box, meters) |
| `--text` | #1C1915 | #F3EEE7 | text and the primary button |
| `--muted` | #6E675E | #A49C92 | secondary text |
| `--faint` | #A59D92 | #6F685F | rank numbers, captions |
| `--line` | ink 9% | white 8% | hairlines |
| `--accent` | #B65A33 | #EFA27A | emphasis only: italic words in headlines, #1, step numbers, the score |

Glow colours (hero aurora, final CTA, logo): #FFD166, #FF8A5B, #FF5C8A, #4FC3F7, #8E6CFF, always heavily blurred and at 35–55% opacity. A light film grain sits over the page so the gradients never band.

Contrast rule: one dark ink button per screen. Everything else is a text link or a hairline.

## Typography
- Display and titles: **Instrument Serif** 400 (roman + italic), self-hosted in `fonts/`. Headlines pair a roman phrase with an *italic accent phrase*.
- Text and UI: **Geist** 400/500/600, self-hosted.
- Scale: 12.5 (eyebrows, uppercase, +0.14em) / 15 / 17 / 19 / 30 (card titles) / clamp(42–80) section titles / clamp(54–122) hero.
- Eyebrows: italic serif number + uppercase label + short hairline ("01 PICK A TOPIC ——").

## Spacing and shape
4px base. Sections clamp(96–168px) vertical padding. Content width 1160px, 20–24px gutters.
Radius: 10 (art), 999 (buttons, chips), 20–22 (cards), 34 (story frame), 6 (polaroids).
Shadows: layered and warm (`--shadow`), never grey-blue.

## Motion
- Hero: five polaroids fan out under the headline and bob gently; scrolling pins the stage and the polaroids fly into the rows of a shelf card, turning into round photos. Mouse parallax on desktop.
- Headlines: each word rises out of its own line (`.split`).
- Sections: fade + rise + un-blur on entry (`.rv`). The taste-match score counts up.
- Everything static under `prefers-reduced-motion` (hero shows the fan, no pinning).

## Imagery
Real artist photos, covers and posters loaded live (Deezer, Apple, AniList, Wikipedia), as in the app. No stock photos, no emoji, no illustrations.
