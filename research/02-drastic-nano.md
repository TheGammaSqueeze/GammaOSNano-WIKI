# Research brief: DraStic Nano (Nintendo DS) - code-verified

## What it is

DraStic Nano is an in-process Nintendo DS emulator built into GammaOS Nano. It embeds the DraStic native core directly (no separate Android app UI), so it launches from the Nano home and boots fast. It shares the same save data and preferences file with the stock DraStic app (`com.dsemu.drastic`), so settings carry over both ways. The prefs live at `/data/user/0/com.dsemu.drastic/shared_prefs/_Dra$t1c_Pref$_.xml`.

Nintendo DS games (`.nds`) launch through DraStic Nano automatically from the Game menu.

## In-game controls

DS buttons map to the pad's face/D-pad/shoulder buttons and Start/Select 1:1 (Up/Down/Left/Right, A, B, X, Y, L, R, Start, Select). The bottom (touch) screen is driven by the touch panel, or by a virtual touch cursor.

| Input | Action |
|-------|--------|
| **Short BACK/Select press** (tap) | Open / close the in-game overlay menu (game pauses while it is open) |
| **Long BACK press** (hold ~1.5 s) | Exit the game, return to the Nano home |
| **Long Power hold** | Graceful power-off (auto-saves first) |
| Touch panel | Acts as the DS stylus on the bottom screen |
| Virtual touch cursor (toggle) | D-Pad / left stick moves a cursor over the bottom screen; A taps/holds the stylus |

## In-game overlay menu (short BACK press)

The overlay is organized in sections:

**Save States** - save/load slots 0-8, an Auto-Load toggle, and Restart Game.

**Video**
- Shader / video filter (Linear by default; a picker of .dfx shaders)
- Screen Layout: Auto / Side by Side (horizontal) / Stacked (vertical) / Single Screen
- Layout Preset (picture-in-picture and other presets)
- PiP Opacity (100/80/60/40%) and PiP Corner (which corner the inset sits in)
- Screen Scaling (Stretch / None / integer), Screen Gap (0/8/16/25%), Swap Screens
- Display Rotation (0/90/180/270)
- Hi-res 3D (default On) - doubles internal 3D render resolution
- Threaded 3D (default On) - multi-threaded rasterizer
- Disable Edge Marking (default On)
- Frame Sync (default Off) - phase-locks the two panels on dual-screen devices
- Frameskip (type + value)
- Performance Mode (Max / Stock / Powersave)
- Restart-to-apply for options that need it

**Audio**
- Volume (0-10, live)
- Audio Latency (0-4, applies on next launch)

**Controls** - rebind DS buttons, analog stick modes, touch-cursor toggle, portrait control rotation.

**Cheats** - enable/disable per-game cheats and add custom cheats (stored per game code).

**Achievements** - RetroAchievements login, unlock list, leaderboards (uses the bottom panel on dual-screen devices).

## Recommended defaults (already set by GammaOS on dual-screen devices)

Frame Sync On, Hi-res 3D On, Threaded 3D On, Disable Edge Marking On. These are applied non-destructively.

## Firmware / DS user data

Firmware Language, Colour/theme, Birthday, and Nickname are read at launch from the prefs file. They are **not** editable in the in-game overlay - to change them, open the stock DraStic app once, set them there, then relaunch. Defaults: Language English, Nickname "Dr Drastic", birthday June 6.

## Quick Resume

With Quick Resume enabled (default On, toggled on the Nano home via L1/R1 or the setting), powering off or rebooting while in a DS game force-saves to DraStic's reserved autosave slot (slot 9) and, on the next boot, relaunches straight back into the paused game with no load screen. There is a crash guard: a truncated or too-small autosave is quarantined and the game boots fresh instead of loading a corrupt state. Quick Resume is skipped for RetroAchievements hardcore mode (which requires a fresh boot).

## Where DS options live (summary)

- **In-game overlay** (short BACK) - most video/audio/cheat/control settings, live.
- **Nano home** - Quick Resume on/off.
- **Stock DraStic app** - firmware user data (language, nickname, birthday, colour), full keymaps.
- All of it round-trips through the shared prefs XML, so both the built-in emulator and the stock app stay in sync.
