---
title: Adding Games
group: Games
order: 1
icon: 📥
desc: Where to put ROMs and how to scan them into your library.
---

Getting your games into GammaOS Nano is simple: copy your ROM files into the right folders, then run a scan. This page shows you exactly where each system's files go and how to bring them into your library.
{: .lead }

## The one rule: per-system folders

Nano finds your games by looking in a folder named for each system. Put each game in the folder that matches its console.

The base folder is `ROMs` at the top of your storage. Inside it, make one folder per system using the short folder name from the table below. For example:

- Put NES games in `/sdcard/ROMs/nes/`
- Put SNES games in `/sdcard/ROMs/snes/`
- Put Game Boy Advance games in `/sdcard/ROMs/gba/`

SD card, internal storage, and USB all work, so use whichever you like. Nano scans them all.

You do not have to unzip anything special or rename your files, as long as the file extension matches what the system expects (see the table).

## Systems, folders, and file types

Here are the systems Nano knows out of the box, the folder each one uses, and the file extensions it looks for.

| System | Folder | File types |
|--------|--------|------------|
| NES | `nes` | .nes .fds .unf .unif |
| SNES | `snes` | .smc .sfc .fig .swc |
| Game Boy | `gb` | .gb |
| Game Boy Color | `gbc` | .gbc .gb |
| Game Boy Advance | `gba` | .gba |
| Nintendo 64 | `n64` | .n64 .v64 .z64 .bin .ndd |
| Nintendo DS | `nds` | .nds |
| Genesis / Mega Drive | `genesis` | .md .gen .smd .bin |
| Master System | `mastersystem` | .sms .sg |
| Game Gear | `gamegear` | .gg |
| PlayStation | `psx` | .cue .pbp .chd .iso .m3u .img |
| PSP | `psp` | .iso .cso .pbp |
| Dreamcast | `dreamcast` | .cdi .gdi .chd .cue |
| Neo Geo Pocket | `ngpc` | .ngp .ngc .npc |
| PICO-8 | `pico8` | .p8 .png |

Every system here can be changed, and you can add your own. See [Game Systems](game-systems.html) to edit any of these, and [Add a Custom System](custom-system.html) to create a new one.

## Scanning your games in

Once your files are in place, tell Nano to look for them:

1. Open the **Settings** category on the home screen.
2. Go to **Game Settings**.
3. Choose **Rescan Games**.

Nano scans every system folder and adds anything new to your library. Your games appear under the **Game** category, grouped by system.

![XMB game list showing per-system counts](assets/img/shots/xmb_home.png)

Run **Rescan Games** any time you add more files. It is safe to run as often as you like.

## Multi-disc games (.m3u)

Some games span several discs (common on PlayStation). Instead of showing every disc as a separate entry, Nano can group a multi-disc game into a single library item using an `.m3u` playlist file that lists the disc files.

This grouping is a switch you turn on in the toolbox: **Settings > GammaOS Toolbox > Group Multi-Disc (.m3u)**. With it on, a game with an `.m3u` file shows up once, and the emulator can switch discs on its own. See [GammaOS Toolbox](gammaos-toolbox.html) for the full list of scan options.

## Games tucked away in subfolders

If you keep your games sorted into subfolders inside a system folder (for example `ROMs/snes/USA/` and `ROMs/snes/Japan/`), turn on **Settings > GammaOS Toolbox > Scan ROM Subfolders** so Nano looks inside those subfolders too. Without it, only files directly in the system folder are scanned.

## A note on BIOS files

GammaOS Nano does not include any console BIOS or firmware files. Systems like PlayStation, PS2, and Dreamcast need you to supply your own BIOS before games will run, and each emulator has its own place to put it. (Nintendo DS is the exception: the built-in DraStic emulator needs no BIOS.)
{: .callout .warn }

For the full picture of which systems need a BIOS and where each one goes, see [Emulators](emulators.html).

## Next steps

- Turn systems on or off and change how they run in [Game Systems](game-systems.html).
- Add a console Nano does not list yet in [Add a Custom System](custom-system.html).
- Download cover art for your library in [Boxart & Metadata](boxart.html).
