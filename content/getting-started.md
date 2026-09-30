---
title: Getting Started
group: Get Started
order: 2
icon: 🚀
desc: First boot, connecting Wi-Fi, adding your first games.
---

This page walks you through your very first minutes with GammaOS Nano: finishing the quick setup, getting online, adding your first games, and switching to the theme you like best. It only takes a few minutes, and you do not need to be technical.
{: .lead }

Have not flashed GammaOS onto your device yet? Start with [Installing GammaOS](installing-flashing.html), then come back here.
{: .callout .note }

## First boot: the setup

The first time your handheld starts, GammaOS Nano runs a short setup to get you going. It covers the basics, including connecting to Wi-Fi so your device knows the date, time, and can reach online features. Follow the on-screen prompts and confirm each step.

If you would rather skip Wi-Fi for now, you can. You can always connect later from Settings, and the steps below show you how.

Once the system configuration is done, the wizard finishes by itself: a short countdown shows on screen and then it moves on without you, so there is no need to guess which button to press.

A few things are worth knowing about a fresh install:

- **Bluetooth starts off.** The setup has no Bluetooth step. When you want to pair a controller or headphones, turn Bluetooth on from the Quick Menu (hold <span class="btnchip">Power</span>) or the Bluetooth and Accessories screen. It stays off until you turn it on. See [Connectivity](network.html).
- **Quick Resume starts off.** Every boot starts at the home. If you would like the handheld to drop straight back into the game you were playing, turn on **Settings > Game Settings > Quick Resume** (also in the Quick Menu). See [Quick Resume](quick-resume.html).
- **You choose where the home opens.** **Settings > Theme Settings > Startup Menu** lets the home open on any category, or straight into one game system such as your Nintendo DS list.

## Finding your way around

Everything lives under a small set of categories on the home screen. Move sideways to change category and up or down to move through the items. To open the settings, go to the **Settings** category and pick the option you want.

New to the controls? The [Controls cheat sheet](controls-os.html) lists every button. On most handhelds you confirm with <span class="btnchip">A</span>, go back with <span class="btnchip">B</span>, and open an item's Options menu with <span class="btnchip">X</span>.

## Connecting to Wi-Fi

You can connect (or reconnect) any time:

1. Open the **Settings** category.
2. Go to **Network Settings**.
3. Choose **Internet Connection Settings**.
4. Pick your network name from the list.
5. Enter your Wi-Fi password with the on-screen keyboard, then confirm.

Once connected, the top bar shows your Wi-Fi signal. You can check the link with **Internet Connection Test** in the same menu. For more, including Bluetooth pairing and network shares, see [Connectivity](network.html).

## Adding your first games

Adding games is simple: you place your ROM files into a folder named for each system, then tell Nano to rescan.

1. Copy your ROMs into per-system folders on your storage. For example, put NES games in `/sdcard/ROMs/nes/` and SNES games in `/sdcard/ROMs/snes/`.
2. You can use internal storage, an SD card, or a USB drive.
3. Back in Nano, open **Settings > Game Settings > Rescan Games**.
4. Your games appear under their systems in the **Game** category.

Not sure how to copy files across? Connect over USB (File Transfer / MTP), use [ADB Explorer](https://github.com/Alex4SSB/ADB-Explorer), or a [network share](network-shares.html). On devices that boot from the SD card, do not read the card on a PC; see [transferring files](faq.html).

If a system does not show up yet, make sure it is turned on in Settings > Game Settings > Game Systems. For the full walkthrough, folder tips, and multi-disc games, see [Adding Games](adding-games.html) and [Game Systems](game-systems.html).

GammaOS Nano does not include any console BIOS files, and some systems need one to run. You supply your own BIOS files and place them where the emulator expects. See [Emulators](emulators.html) for details.
{: .callout .tip }

## Switching themes

GammaOS Nano has four home themes, and switching is instant:

1. Open **Settings > Theme Settings > Home Theme**.
2. Choose **GammaOS XMB**, **DSi Menu**, **Minima**, or **Custom / ES-DE**.

The home switches to your chosen look straight away. **Custom / ES-DE** runs EmulationStation-DE theme sets, with the Slate theme preinstalled and a built-in downloader for more; see [ES-DE Themes](esde-themes.html). You can also change the accent colour, set a wallpaper, and more from Theme Settings. See [Home Themes](themes.html) for the full tour.

## Where to next

- Learn the layout in [What Is GammaOS Nano?](what-is-nano.html)
- Master every button in the [Controls cheat sheet](controls-os.html)
- Dive into your library with [Adding Games](adding-games.html)
- Explore every option in the [Settings Reference](settings-reference.html)
