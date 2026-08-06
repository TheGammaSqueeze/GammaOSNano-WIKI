---
title: Quick Menu
group: Settings
order: 0
icon: ⚡
desc: The fast-access overlay for brightness, performance, shaders, USB, and power.
---

The Quick Menu is your fast lane to the settings you reach for most: brightness, performance mode, shaders, USB mode, and power options. You can open it from the home, and you can raise it right over a running game without quitting.
{: .lead }

![The Quick Menu on the XMB home](assets/img/shots/xmb_quickmenu.png)

## Opening the Quick Menu

- **On the home**, the Quick Menu is the far-left category (the power-icon column). Move to it like any other category.
- **Over a running game or app**, hold <span class="btnchip">Power</span> to raise the Nano overlay, which opens straight on the Quick Menu. Press <span class="btnchip">B</span> or hold <span class="btnchip">Power</span> again to drop back into your game. See [the in-game overlay](controls-os.html#the-in-game-overlay).
- Holding <span class="btnchip">Power</span> on the home jumps directly to the Quick Menu's Power submenu.

## What is in it

| Item | What it does |
|------|--------------|
| **Resume Audio Player** | Jumps back to the now-playing screen (shown only while music is playing) |
| **Screen Brightness** | An inline slider; move <span class="btnchip">Left</span> / <span class="btnchip">Right</span> to adjust |
| **Performance Mode** | Normal, Max Performance, or Power Saver CPU/GPU profile |
| **Quick Settings** | A page of toggle tiles (see below) |
| **System Settings** | Opens the full Android Settings app |
| **Global Shaders** | Turns the system display shader on or off and tunes it (see below) |
| **Notifications** | Shows active system notifications; dismiss the focused one |
| **USB Settings** | Switch the USB mode: Charging only, MTP, PTP, or RNDIS (USB Ethernet) |
| **Close Current App** | Force-stops the foreground app and returns you home |
| **Kill Background Apps** | Force-stops background apps, sparing the one in front |
| **Kill All Apps** | Force-stops all third-party apps |
| **Screen Orientation** | Force an app's orientation (shown only over a running app); the choice is remembered per app and persists between Nano and normal Android |
| **Quick Resume** | Toggles [Quick Resume](quick-resume.html) on or off |
| **Power** | A submenu: Restart, Power Off, Recovery, Safe Mode, Boot Android |

![More Quick Menu items: USB, Close Apps, Quick Resume](assets/img/shots/xmb_quickmenu2.png)

## Performance Mode

Three profiles trade battery for speed:

- **Normal** scales up and down with load (the everyday default).
- **Max Performance** holds high clocks for the most demanding games.
- **Power Saver** keeps clocks low for light emulation and long sessions.

## Global Shaders

The Global Shaders item applies a system-wide display shader over everything on screen. Pick a preset and tune it:

- **Off** turns shaders off.
- **CRT** adds scanlines (adjust Scanline Size and Scanline Strength).
- **LCD3x** and **LCD** emulate an LCD grid.
- **Blur Fill** fills the empty sides of a non-fullscreen image (with a Resolution and Orientation control).
- **Custom Shader** loads your own preset, with Resolution Scale and Scanline Density controls.

If a shader ever makes the screen unreadable, hold <span class="btnchip">Power</span> + <span class="btnchip">Select</span> to disable it instantly. See [Controls](controls-os.html#system-shortcuts).
{: .callout .tip }

## Quick Settings tiles

The Quick Settings page is a grid of one-tap toggles, including Wi-Fi, Bluetooth, Performance Mode, Global Shaders, GammaRGB, GammaEQ, Screen Map, Deep Sleep Mode, External as Primary, Immersive Mode, ABXY Swap, D-Pad/Analog Swap, Global Sensitivity, Analog Calibration, and stick inversion. Tap one to flip it.

## USB Settings

Switch how the device appears when plugged into a computer:

- **Charging only** (default): no data connection.
- **MTP**: browse the device's files as media storage.
- **PTP**: transfer photos.
- **RNDIS**: share the device's connection as USB Ethernet.

For a simpler two-way choice, **Settings > USB & Docking** offers **File Transfer (MTP)** and **Charge Only**, which is the quickest way to move files to a PC without ADB. See the [Settings Reference](settings-reference.html#system-settings).

To silence the launcher's UI navigation sounds, use the **Navigation Sounds** toggle in **Settings > Sound Settings** (the boot jingle still plays).

## Where to go next

- [Controls](controls-os.html) for the in-game overlay and system shortcuts.
- [Settings Reference](settings-reference.html) for the full Settings tree.
- [GammaOS Toolbox](gammaos-toolbox.html) for the deeper system tweaks.
