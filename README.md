# AvatarArchive

> Fan-made media hub — The entire Avatar universe, one place.

Built by [Jeffrey Creates](https://www.youtube.com/@Jeffrey_Creates) · Vanilla HTML, CSS & JavaScript · No frameworks · No servers

---

## Pages

| File | Description |
|------|-------------|
| `index.html` | Home — world map splash, cross-series search, and hub card navigation |
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

### 🔒 Password Gate
Every page is protected before anything renders. Auth state is stored in `localStorage` so users only need to enter it once.

### ▶ Custom Video Player
Skip-intro detection, next-episode auto-advance with fill-bar countdown, per-episode progress memory, and resume-on-load. Floating pill UI with seek bar, volume, playback speed, brightness/contrast, fullscreen, and SRT captions.

### CC SRT Captions
Each episode and film fetches a `.srt` file automatically on load. The CC button toggles them with a smooth fade.

### 📺 Episode Browser
Netflix-style book selector — a pill dropdown that switches between Books — with an episode grid showing per-episode progress bars and a watched checkmark at 90%+ completion.

### 📖 PDF Comic Reader
PDF.js renders graphic novels as two-page spreads. Pages turn via buttons, keyboard, mouse drag, or touch swipe. Includes zoom, page-jump, fullscreen (with iOS fallback), and download progress.

### 🔍 Cross-Series Search
Debounced search on the home page queries all 113+ episodes across ATLA, Korra, the films, games, and merchandise — with per-series color coding.

### 🗺 World Map Splash
The home page opens with a full-screen world map animation before revealing the hub cards.

### 🎵 Ambient Sound
Optional looping audio via the Web Audio API — plays an intro cue first, then crossfades to the ambient loop. Starts at a random position each session. Volume and mute state persist in `localStorage`.

### 🎨 Themes
Four built-in themes — Dark, Parchment, Water, Earth — applied via CSS custom properties and persisted in `localStorage`. Accessible from the gear button on every page.

### ✦ Ambient Particles
Floating element symbols (air, water, earth, fire) drift across the background via Canvas 2D, using orbit, wave, and drift movement modes. Pauses when the tab is hidden.

### ▣ Continue Watching
Hub cards on the home page show a color-coded progress strip and change their CTA to "Resume" if any episodes have been started.

### ★ Star Rating
Film pages include a 5-star rating widget that persists ratings per title in `localStorage`.

### ⏱ Countdown Timer
The 2026 film page displays a live days / hours / minutes / seconds countdown to the October 9, 2026 Paramount+ premiere.

### 📲 PWA
Installable on mobile and desktop via an inline Web App Manifest and service worker registered from a Blob URL. Offline shell caching covers all HTML pages.

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

- Vanilla HTML / CSS / JS
- PDF.js
- Web Audio API
- Canvas 2D
- localStorage
- PWA / Service Worker
- Zero Frameworks
- Zero Servers

---

*Fan-made · Built with ♥ by [Jeffrey Creates](https://www.youtube.com/@Jeffrey_Creates)*
