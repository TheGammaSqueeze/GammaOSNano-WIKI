---
title: FAQ and Troubleshooting
group: Help
order: 1
icon: ❓
desc: Common questions and quick fixes.
---

Quick answers to the questions handheld owners ask most. If your question is not here, the linked pages go into more depth.
{: .lead }

### How do I change the screen brightness?

Hold <kbd>Select</kbd> and press <kbd>Vol +</kbd> to brighten or <kbd>Vol -</kbd> to dim. This works everywhere, in the menus and inside games.

You can also set brightness under **Settings > Display Settings > Brightness**, or from the [Quick Menu](settings-reference.html#quick-menu) (hold <span class="btnchip">Power</span>).

### How do I open the RetroArch menu or exit a game?

Inside a RetroArch game, GammaOS drives everything from the <span class="btnchip">Back</span> button:

- **Tap <span class="btnchip">Back</span> once** to open the RetroArch menu.
- **Hold <span class="btnchip">Back</span>** to exit back to the Nano home. You land back on the same game.
- **<span class="btnchip">L3</span> + <span class="btnchip">R3</span>** (click both sticks in) also opens the RetroArch menu.

This is the RetroArch Back Button Override. Full details are on the [RetroArch Controls](controls-retroarch.html) page.

### How do I exit a DS (DraStic) game?

Hold the <span class="btnchip">Back</span> button. The same hold-to-exit that quits RetroArch also quits DraStic Nano and returns you to the home. See [DraStic Nano](drastic-nano.html) for more.

### My games do not show up

Work through this checklist:

1. Put your ROMs in the right per-system folder, for example `/sdcard/ROMs/nes/` for NES or `/sdcard/ROMs/snes/` for SNES. SD card, internal storage, and USB all work.
2. Go to **Settings > Game Settings > Rescan Games**.
3. Check the system is enabled in **Settings > Game Settings > Game Systems** (each system has an On/Off toggle).
4. Make sure your file types match the system's **Extensions** list. For example, SNES expects `.smc`, `.sfc`, `.fig`, or `.swc`.

If your games are inside subfolders, turn on **Scan ROM Subfolders** in the [GammaOS Toolbox](gammaos-toolbox.html), then rescan. See [Adding Games](adding-games.html) for the full guide.

### A game will not launch

The most common causes:

- **Missing BIOS.** GammaOS does not ship console BIOS or firmware files. Systems like PlayStation, PS2, Dreamcast, and Neo Geo need you to supply your own. For RetroArch cores, put BIOS files in `Internal storage / RetroArch / system`. Standalone emulators (AetherSX2, PPSSPP, Flycast) each have their own first-run BIOS import step. Nintendo DS games are the exception and need no BIOS.
- **Wrong core or package.** Check the **Emulator** set for that system in the [Game Systems](game-systems.html) editor.
- **Wrong extension.** The game's file type must be in that system's **Extensions** list.

Games that need a BIOS will not launch until you add the correct BIOS files.
{: .callout .warn }

See [Emulators](emulators.html) for which core or app each system uses.

### How do I add an emulator or system that is not in the list?

Open **Settings > Game Settings > Game Systems** and choose **Add New System...** at the bottom. You can point a new system at any RetroArch core or standalone emulator app, set its extensions, folders, and icon. The full walkthrough is on the [Custom System](custom-system.html) page.

### My games have no boxart

Run the scraper: **Settings > Game Settings > Boxart Scraper**, then **Scrape All Systems**. You can also scrape a single game from its [Options menu](context-menus.html) with **Scrape This Game**. Art downloads in the background while you are idle. Full guide on the [Boxart](boxart.html) page.

### How do I switch home themes?

Go to **Settings > Theme Settings > Home Theme** and pick **GammaOS XMB**, **DSi Menu**, or **Minima**. Applying restarts the home so the new look takes effect right away. See [Themes](themes.html) for what each one looks like.

### The screen is too dark or a shader broke the display

Hold <span class="btnchip">Power</span> + <span class="btnchip">Select</span> together. This disables the system display shader, which is the escape hatch when a shader (like the CRT Shader) makes the screen unreadable. Then adjust or turn off the shader in the [GammaOS Toolbox](gammaos-toolbox.html).

For a screen that is simply dim, hold <kbd>Select</kbd> + <kbd>Vol +</kbd> to brighten it.

### The home screen is frozen

Force a restart of the home:

- **Hold <span class="btnchip">Back</span> for 10 seconds**, or
- **Hold the Guide / Mode button for 10 seconds**.

Either one restarts a frozen or dead home screen.

### More help

- [OS Controls](controls-os.html) and [RetroArch Controls](controls-retroarch.html)
- [Adding Games](adding-games.html), [Game Systems](game-systems.html), and [Custom System](custom-system.html)
- [Boxart](boxart.html) and [Emulators](emulators.html)
- [Settings Reference](settings-reference.html) and [GammaOS Toolbox](gammaos-toolbox.html)
