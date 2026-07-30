---
title: Emulators & Cores
group: Emulators
order: 1
icon: 💾
desc: "How Nano runs games: RetroArch cores, standalone emulators, cores table, and BIOS."
---

Nano does not emulate games itself (other than the built-in DraStic DS emulator). Instead it hands each game to the right emulator, then brings you back to exactly where you were when you exit. This page explains how that handoff works, which core or emulator each system uses by default, and how to set up the BIOS files that some consoles need.
{: .lead }

## How launching works

When you pick a game, Nano figures out which system it belongs to and launches it in one of two ways:

- **RetroArch cores (libretro).** Most systems run inside RetroArch (`com.retroarch.aarch64`) using a small plug-in called a libretro core. One RetroArch install can run many systems by loading a different core for each.
- **Standalone emulator apps.** A few systems run in their own dedicated app instead: Nintendo 64 uses Mupen64Plus, PSP uses PPSSPP, Dreamcast uses Flycast, and Nintendo DS uses the built-in [DraStic Nano](drastic-nano.html).

Either way the experience is the same from your side. Nano launches the emulator, briefly drops its own controller input during the handoff so no stray button press leaks into your game, and remembers where you were. When you exit, you land back on the same game highlighted on the home screen.

The built-in Nintendo DS emulator has its own dedicated page. See [DraStic Nano](drastic-nano.html) for its controls and in-game options.
{: .callout .note }

RetroArch and DraStic games also support [Quick Resume](quick-resume.html): power off mid-game and boot straight back into it.
{: .callout .tip }

## Default systems and cores

Here is what each system uses out of the box, along with the game file types Nano scans for. Every value below is editable (see [changing a system's core](#change-a-systems-core-or-emulator)).

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

The "Folder" column is the subfolder name Nano scans under your ROMs directory. See [Adding games](adding-games.html) for where to drop your files, and [Game Systems](game-systems.html) to turn systems on or off.

## BIOS files (not included)

Nano does **not** ship any console BIOS or firmware files. Some systems refuse to boot without them, so you must supply your own for the consoles that need them (for example PlayStation, PS2, Dreamcast, Neo Geo, and Sega CD).

Nintendo DS is the happy exception: the built-in [DraStic Nano](drastic-nano.html) emulator has its own high-level BIOS emulation, so DS games run with no BIOS files at all.
{: .callout .tip }

BIOS files are copyrighted. Nano cannot legally include them, so you provide your own copies.
{: .callout .warn }

Where the file goes depends on which kind of emulator runs the system:

- **RetroArch cores.** Put BIOS files in RetroArch's system folder on internal storage: **Internal storage / RetroArch / system** (full path `/storage/emulated/0/RetroArch/system`). A core looks there for files by exact name. If a game will not start, open that core's information screen inside RetroArch to see the precise filenames it expects.
- **Standalone emulators.** AetherSX2 (PS2), PPSSPP, Flycast, and Mupen64Plus import their BIOS in their own settings the first time you launch them. For example, AetherSX2 asks you to import your PS2 BIOS. Just follow the emulator's own first-run prompt. (DraStic for Nintendo DS needs nothing here.)

## Change a system's core or emulator

You are never locked into the defaults above. To swap the core or standalone emulator a system uses, open the **Game Systems** editor:

1. Go to Settings, then **Game Settings**, then **Game Systems**.
2. Select the system you want to change.
3. Edit the emulator (or core), the file extensions it scans, its scan folders, and its icon.

The same editor lets you add unlimited custom systems from scratch. See [Game Systems](game-systems.html) for the full walkthrough and [Custom systems](custom-system.html) for building a brand-new one.

## RetroArch controls reminder

Inside a RetroArch game, a quick tap of the <span class="btnchip">Back</span> button opens the RetroArch menu, and holding <span class="btnchip">Back</span> exits back to the Nano home on the same game. You can also press <span class="btnchip">L3</span> + <span class="btnchip">R3</span> (click both sticks in) to open the menu, which is RetroArch's own built-in combo.

For the full list, including how to reach states, options, and input rebinding, see [RetroArch controls](controls-retroarch.html).

## Related pages

<div class="cards">
  <a class="card" href="drastic-nano.html"><span class="card-ico">🟦</span><span class="card-kicker">Emulators</span><h3>DraStic Nano</h3><p>The built-in Nintendo DS emulator.</p></a>
  <a class="card" href="game-systems.html"><span class="card-ico">🎮</span><span class="card-kicker">Games</span><h3>Game Systems</h3><p>Turn systems on, edit cores and folders.</p></a>
  <a class="card" href="controls-retroarch.html"><span class="card-ico">🕹️</span><span class="card-kicker">Controls</span><h3>RetroArch Controls</h3><p>Menu, exit, and input rebinding.</p></a>
</div>
