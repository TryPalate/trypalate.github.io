# Palate landing page: design system

Taken from the Palate app itself (no outside references), so the site and the app feel like one product.

## Color
| Token | Dark | Light | Role |
|---|---|---|---|
| `--bg` | #0A0A0D | #F1F1F4 | page background |
| `--card` | #15151A | #FFFFFF | cards, mockups |
| `--raise` | #22222A | #E8E8EE | chips, quiet buttons |
| `--text` | #F5F5F7 | #111114 | text |
| `--muted` | #8E8E98 | #5E5E67 | secondary text (4.5:1 on bg) |
| `--line` | white 8% | black 7% | dividers |
| `--accent` | #FFB06B | #A84C0F | the one accent: primary button, "Say why.", highlights |

Item color: sections tint their glow with `--h`/`--s`, sampled from the picture being shown (album cover, artist photo, anime poster). Logo glows (#FFD166, #FF8A5B, #FF5C8A, #4FC3F7, #8E6CFF) only appear in the mark.

The page follows the system light/dark setting, like the app.

## Typography
System font stack (same as the app). Weights 400, 600, 700.
Scale: 13 / 15 / 17 / 20 / 28 / 40 / clamp(44-96) display. Display: 700, letter-spacing -0.045em, line-height 0.95. Body 17px, line-height 1.5, max 60ch.

## Spacing and shape
4px base: 4, 8, 12, 16, 24, 32, 48, 72, 120. Content width 1120px, 20px side gutter on phones.
Radius: 10 (art), 16 (chips/buttons are pills), 24 (cards), 32 (phone/story frames). One shadow: `0 30px 80px -30px rgb(0 0 0 / .6)`.

## Components
- Primary button: accent fill, dark text, pill. Hover lifts 1px, focus ring 2px text color.
- Quiet button: `--raise` fill.
- Shelf card: the app's card. Rank number, art, name, subtitle, optional "why" note.
- Art: square for albums and anime posters (anime 3:4), circle for people.

## Motion
Scroll-driven, eased toward the target every frame (no jumps). Everything turns static under `prefers-reduced-motion`.

## Imagery
Real artist photos and covers loaded live from Deezer, Apple and AniList, like the app. No stock photos, no emoji, no illustrations.
