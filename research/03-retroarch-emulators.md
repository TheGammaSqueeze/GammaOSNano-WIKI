# Research brief: RetroArch + emulators - code-verified

## How Nano launches games

- Most systems run through **RetroArch** (`com.retroarch.aarch64`) with a libretro core (a `.so` file under `/data/data/com.retroarch.aarch64/cores/`).
- Some systems run in a **standalone emulator app** (DraStic for DS, PPSSPP for PSP, Mupen64Plus for N64, Flycast for Dreamcast). DS specifically uses the built-in DraStic Nano.
- When you launch a game, Nano hands off to the emulator, drops its own input during the transition (so no phantom button press leaks into the game), and remembers where you were so you land back on the same game when you exit.

## Default systems and cores

| System | Folder | Default core / emulator | Common extensions |
|--------|--------|-------------------------|-------------------|
| NES | nes | Nestopia (libretro) | .nes .fds .unf .unif |
| SNES | snes | Snes9x (libretro) | .smc .sfc .fig .swc |
| Game Boy | gb | Gambatte (libretro) | .gb |
| Game Boy Color | gbc | Gambatte (libretro) | .gbc .gb |
| Game Boy Advance | gba | gpSP (libretro) | .gba |
| Nintendo 64 | n64 | Mupen64Plus (standalone) | .n64 .v64 .z64 .bin .ndd |
| Nintendo DS | nds | DraStic Nano (built-in) | .nds |
| Genesis / Mega Drive | genesis | Genesis Plus GX (libretro) | .md .gen .smd .bin |
| Master System | mastersystem | Genesis Plus GX (libretro) | .sms .sg |
| Game Gear | gamegear | Genesis Plus GX (libretro) | .gg |
| PlayStation | psx | PCSX ReARMed (libretro) | .cue .pbp .chd .iso .m3u .img |
| PSP | psp | PPSSPP (standalone) | .iso .cso .pbp |
| Dreamcast | dreamcast | Flycast (standalone) | .cdi .gdi .chd .cue |
| Neo Geo Pocket | ngpc | Mednafen NGP (libretro) | .ngp .ngc .npc |
| PICO-8 | pico8 | fake08 (libretro) | .p8 .png |

Every one of these is editable in the **Game Systems** editor (change the core/emulator, extensions, scan folders, icon, and more), and you can add unlimited custom systems.

## RetroArch controls: opening the menu and exiting (GammaOS behavior - IMPORTANT)

GammaOS does NOT use a hotkey-modifier combo (like Select + X) to open the RetroArch menu. Instead it drives RetroArch with the **Back** button plus a stick combo. This is the accurate, shipped behavior (the button is the Back button specifically, not Select):

| Action | How |
|--------|-----|
| **Open the RetroArch menu** | Press the **Back** button **once** (a quick tap). GammaOS injects RetroArch's menu-toggle key (F1) for you. |
| **Open the RetroArch menu (alternative)** | Press **L3 + R3** (click both analog sticks in together). This is RetroArch's own built-in gamepad menu-toggle combo. |
| **Exit RetroArch back to the Nano home** | **Hold** the **Back** button. GammaOS injects Quit (ESC); RetroArch closes and you land back on the same game in the home. |

Mechanism (for accuracy): GammaOS maps a short Back press to KEYCODE_F1 (RetroArch's menu toggle) and a long Back hold to KEYCODE_ESCAPE (RetroArch quit) while RetroArch is foreground. The same long-hold-to-exit also works for DraStic. This is the **RetroArch Back Button Override** behavior (GammaOS Toolbox > RetroArch Back Button Override); L3 + R3 works independently as RetroArch's native combo.

Everything else inside the RetroArch menu (states, options, controls, cheats) is RetroArch's own UI - open it with a single Back press or L3+R3 and use RetroArch's on-screen menu. To rebind in-game inputs, use RetroArch's Settings > Input.

## Exiting a game back to the Nano home

- **RetroArch**: hold the Back button (injects Quit). You return to the same game highlighted on the home.
- Alternatively, from the RetroArch menu (single Back press or L3+R3) choose Quit RetroArch.
- Power-hold also raises the Nano overlay over the game; press B to dismiss, or pick another game to switch.

## Quick Resume with RetroArch

With Quick Resume on, powering off from a running libretro game primes a resume marker with the core and game name; on the next boot Nano relaunches that game. (DraStic Nano additionally restores an exact paused autosave; libretro relies on RetroArch's own save/state handling.)

## BIOS files (important - not included)

GammaOS does **not** ship any console BIOS/firmware files. You must supply your own for the systems that need them (PlayStation, PS2, Dreamcast, Neo Geo, Sega CD, some others).

- **Nintendo DS (DraStic) does NOT need a BIOS** - DraStic has built-in high-level BIOS emulation, so DS games run without any BIOS/firmware files. (Its "firmware user data" like nickname/birthday/language is just cosmetic and set inside DraStic, not an external BIOS.)
- **RetroArch cores**: put BIOS files in RetroArch's system folder on internal storage: `Internal storage / RetroArch / system` (full path `/storage/emulated/0/RetroArch/system`). Cores look there by name; a core's info screen lists the exact filenames it expects.
- **Standalone emulators** (AetherSX2/PS2, PPSSPP, Flycast, Mupen64Plus): if the console needs a BIOS, you import it in that emulator's own settings the first time you launch it (for example AetherSX2 asks you to import your PS2 BIOS). Follow that emulator's own first-run prompt.

## Where emulator options live

- **Inside the emulator** (RetroArch's own menu, or DraStic Nano's overlay) - per-core video/audio/input/state options.
- **Game Systems editor** (Settings > Game Settings > Game Systems) - which core/emulator each system uses, extensions, scan folders, icon, per-system scraper.
- **GammaOS Toolbox** - the RetroArch Back Button Override and ROM-scan options (subfolders, multi-disc .m3u grouping).
