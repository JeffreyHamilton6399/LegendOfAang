# AvatarArchive

> A fan-made personal media hub for the entire Avatar universe.

Built by [Jeffrey Creates](https://www.youtube.com/@Jeffrey_Creates) — vanilla HTML, CSS, and JavaScript. No frameworks. No servers.

---

## Pages

| File | Description |
|------|-------------|
| `index.html` | Home — world map splash, search, and hub card navigation |
| `atla.html` | Avatar: The Last Airbender (2005–2008) · Books 1–3 · 61 Episodes |
| `kora.html` | The Legend of Korra (2012–2014) · Books 1–4 · 52 Episodes |
| `liveshow.html` | Netflix Live Action Series (2024) · Seasons 1–2 |
| `movie2026.html` | Aang, The Last Airbender · 2026 animated film · with countdown timer |
| `movie2010.html` | The Last Airbender · 2010 live action film |
| `books.html` | Avatar graphic novels & comics (Dark Horse) |
| `games.html` | ATLA games collection |
| `merch.html` | Official merchandise — Paramount, Netflix, Nick, Funko, and more |

---

## Features

**Password Gate**
Every page is protected by a password gate that runs before anything renders. Auth state is stored in `localStorage` so users only need to enter it once.

**Video Player**
Custom-built player across all video pages with skip-intro detection, next-episode auto-advance with a fill-bar countdown, per-episode progress memory, and resume-on-load. Controls include a floating pill UI with seek bar, volume, playback speed, brightness/contrast adjustments, fullscreen, and SRT caption support. The player hides the cursor and controls during idle playback and shows an OSD toast for keyboard shortcut feedback.

**SRT Captions**
Each episode and film fetches a `.srt` file automatically on load. The CC button toggles them on and off with a smooth fade.

**Episode Browser**
ATLA and Korra use a Netflix-style book selector — a pill dropdown that switches between Books — with an episode grid below showing per-episode progress bars and a watched checkmark at 90%+ completion.

**PDF Comic Reader**
`books.html` uses PDF.js to render graphic novels as a two-page spread. Pages turn via on-screen buttons, keyboard arrow keys, mouse drag, or touch swipe. Includes zoom controls, a page-jump input, fullscreen support (with iOS fake-fullscreen fallback), and download progress display. Last-read page is saved per book in `localStorage`.

**Cross-Series Search**
Debounced search on the home page queries all 113+ episodes across ATLA, Korra, the films, games, and merchandise. Results appear inline with per-series color coding.

**World Map Splash**
The home page opens with a full-screen world map animation before revealing the hub cards.

**Ambient Sound**
Optional looping ambient audio via the Web Audio API — plays an intro cue first, then crossfades to the ambient loop. Triggered on user gesture to comply with browser autoplay policies. Toggled from the settings panel with fade-in/fade-out. Volume and mute state are persisted in `localStorage`.

**Themes**
Four built-in themes — Dark, Parchment, Water, Earth — applied via CSS custom properties and persisted in `localStorage`. The settings panel lives in a gear button fixed to the bottom-left of every page.

**Ambient Particles**
Floating element symbols (air, water, earth, fire) drift across the background of most pages via Canvas 2D, using orbit, wave, and drift movement modes. The particle loop pauses when the tab is hidden to save CPU.

**Continue Watching**
Hub cards on the home page show a color-coded progress strip and change their CTA to "Resume" if any episodes have been started.

**Star Rating**
Film pages (2010 film, 2026 film, Netflix series) include a 5-star rating widget that persists ratings per title in `localStorage`.

**Countdown Timer**
`movie2026.html` displays a live days/hours/minutes/seconds countdown in the header to the October 9, 2026 Paramount+ premiere.

**PWA**
Installable on mobile and desktop via an inline Web App Manifest and service worker registered from a Blob URL. Offline shell caching covers all HTML pages. An install button in the settings panel triggers the native browser install prompt, or falls back to manual instructions.

---

## Keyboard Shortcuts (Video Pages)

| Key | Action |
|-----|--------|
| `Space` / `K` | Play / Pause |
| `←` / `→` | Seek ±5 seconds |
| `↑` / `↓` | Volume ±10% |
| `M` | Mute / Unmute |
| `F` | Toggle Fullscreen |
| `C` | Toggle Captions |
| `N` | Next Episode |
| `?` | Show Shortcuts |

---

## Stack

- Vanilla HTML, CSS, JavaScript — zero frameworks
- PDF.js — in-browser comic reader
- Web Audio API — ambient sound engine
- Canvas 2D — floating element particles
- `localStorage` — progress, ratings, captions, preferences, and auth
- PWA — inline service worker, offline shell caching
