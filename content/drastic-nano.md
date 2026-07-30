---
title: DraStic Nano
group: Emulators
order: 2
icon: 🟦
desc: "The built-in Nintendo DS emulator and all its in-game options."
---

DraStic Nano is the Nintendo DS emulator built right into GammaOS Nano. It runs your DS games straight from the Game menu with a fast boot and a friendly in-game overlay. This page is the complete reference: how it launches, its controls, and every option in the overlay menu.
{: .lead }

## What DraStic Nano is

DraStic Nano embeds the DraStic DS core directly inside Nano, so there is no separate app to open and games boot quickly. It shares the same save data and preferences file with the stock DraStic app (`com.dsemu.drastic`), so any settings you change in one carry over to the other, both ways.

Nintendo DS games (`.nds` files) launch through DraStic Nano automatically from the Game menu. There is nothing to select or configure to make this happen.

DraStic Nano shares its saves and preferences with the stock DraStic app, so your progress and settings stay in sync between them.
{: .callout .note }

## No BIOS needed

Good news: DraStic does **not** need a BIOS. It has its own built-in high-level BIOS emulation, so Nintendo DS games run straight away with no BIOS or firmware files to find or copy. This is unlike PlayStation, PS2, or Dreamcast, which do need you to supply a BIOS (see [Emulators](emulators.html#bios-files-not-included)).

The only "firmware" DraStic has is cosmetic DS user data (nickname, birthday, favourite colour, and menu language). It is optional, and you set it inside the stock DraStic app, not with any BIOS file.
{: .callout .tip }

## In-game controls

The DS face buttons, D-pad, shoulder buttons, and Start/Select map to your handheld one to one (Up, Down, Left, Right, A, B, X, Y, L, R, Start, Select). The DS bottom (touch) screen is driven by your touch panel, or by a virtual touch cursor if your device has no touchscreen.

| Input | Action |
|-------|--------|
| Short <span class="btnchip">Back</span> / <span class="btnchip">Select</span> tap | Open or close the in-game overlay menu (the game pauses while it is open) |
| Long <span class="btnchip">Back</span> hold (about 1.5 s) | Exit the game and return to the Nano home |
| Long <span class="btnchip">Power</span> hold | Graceful power-off (auto-saves first) |
| Touch panel | Acts as the DS stylus on the bottom screen |
| Virtual touch cursor (toggle) | D-pad or left stick moves a cursor over the bottom screen; <span class="btnchip">A</span> taps or holds the stylus |

For the full controls breakdown, see [DraStic controls](controls-drastic.html).

## The in-game overlay menu

Give the <span class="btnchip">Back</span> button a short tap to open the overlay. The game pauses while it is open, and tapping <span class="btnchip">Back</span> again closes it and resumes play. The overlay is organized into sections, covered below.

### Save States

- Save and load slots **0 to 8**.
- **Auto-Load** toggle, so a game can pick up from your last state automatically.
- **Restart Game**.

### Video

This is the largest section. Options that need it are marked to restart before they take effect.

| Option | Choices / notes |
|--------|-----------------|
| Shader / video filter | Linear by default; a picker of `.dfx` shaders |
| Screen Layout | Auto, Side by Side (horizontal), Stacked (vertical), or Single Screen |
| Layout Preset | Picture-in-picture and other presets |
| PiP Opacity | 100%, 80%, 60%, or 40% |
| PiP Corner | Which corner the inset sits in |
| Screen Scaling | Stretch, None, or integer |
| Screen Gap | 0%, 8%, 16%, or 25% |
| Swap Screens | Swap top and bottom |
| Display Rotation | 0, 90, 180, or 270 |
| Hi-res 3D | Default **On**; doubles the internal 3D render resolution |
| Threaded 3D | Default **On**; multi-threaded rasterizer |
| Disable Edge Marking | Default **On** |
| Frame Sync | Default **Off**; phase-locks the two panels on dual-screen devices |
| Frameskip | Type plus value |
| Performance Mode | Max, Stock, or Powersave |

### Audio

- **Volume**, 0 to 10, applies live.
- **Audio Latency**, 0 to 4, applies on the next launch.

### Controls

Rebind DS buttons, choose analog stick modes, toggle the virtual touch cursor, and set portrait control rotation.

### Cheats

Enable or disable per-game cheats, and add your own custom cheats. Cheats are stored per game code, so they follow the right game.

### Achievements

RetroAchievements login, your unlock list, and leaderboards. On dual-screen devices this uses the bottom panel.

## Recommended defaults

On dual-screen devices GammaOS already sets sensible defaults for you, applied without overwriting your own choices:

| Option | Default |
|--------|---------|
| Frame Sync | On |
| Hi-res 3D | On |
| Threaded 3D | On |
| Disable Edge Marking | On |

## Firmware and DS user data

Your DS firmware personalization (Firmware Language, colour and theme, birthday, and nickname) is read at launch from the shared preferences file. These are **not** editable in the in-game overlay.

To change them, open the stock DraStic app once, set them there, then relaunch your game from Nano. The stock app is also where you set the full keymaps.

| Setting | Default |
|---------|---------|
| Language | English |
| Nickname | Dr Drastic |
| Birthday | June 6 |

## Quick Resume

With Quick Resume enabled (default **On**, toggled on the Nano home with <span class="btnchip">R1</span> or in the setting), powering off or rebooting while in a DS game force-saves to DraStic's reserved autosave slot (slot 9). On the next boot, Nano relaunches straight back into your paused game with no load screen.

There is a built-in crash guard: if an autosave is truncated or too small, it is quarantined and the game boots fresh instead of loading a corrupt state.

Quick Resume is skipped for RetroAchievements hardcore mode, which requires a fresh boot.
{: .callout .note }

DraStic has the most seamless Quick Resume of any emulator on Nano. For the full picture, including how it works for RetroArch, see the [Quick Resume](quick-resume.html) page.

## Where DS options live

| Where | What you set |
|-------|--------------|
| In-game overlay (short <span class="btnchip">Back</span>) | Most video, audio, cheat, and control settings, live |
| Nano home | Quick Resume on or off |
| Stock DraStic app | Firmware user data (language, nickname, birthday, colour) and full keymaps |

All of it round-trips through the shared preferences file, so the built-in emulator and the stock app always stay in sync.

## Related pages

<div class="cards">
  <a class="card" href="controls-drastic.html"><span class="card-ico">🕹️</span><span class="card-kicker">Controls</span><h3>DraStic Controls</h3><p>Every button in a DS game.</p></a>
  <a class="card" href="emulators.html"><span class="card-ico">💾</span><span class="card-kicker">Emulators</span><h3>Emulators & Cores</h3><p>How Nano runs every other system.</p></a>
  <a class="card" href="adding-games.html"><span class="card-ico">📂</span><span class="card-kicker">Games</span><h3>Adding Games</h3><p>Where to put your DS ROMs.</p></a>
</div>
