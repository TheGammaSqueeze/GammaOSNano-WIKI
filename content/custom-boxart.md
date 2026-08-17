---
title: Custom Boxart and Backup
group: Games
order: 6
icon: 🖼️
desc: Add your own cover art in bulk, back it up, and manage it from a PC, with the GammaOS Boxart Tool or by hand.
---

The [Boxart Scraper](boxart.html) and the per-game **Set Boxart** option cover most needs, but sometimes you want to manage covers in bulk: drop in your own art from a computer, fix a whole system at once, or back up every cover you have collected. This page shows how, end to end, with a ready-made tool and the full on-device format if you would rather do it by hand.
{: .lead }

## The quick ways, inside Nano

If you only need one or two covers, you do not need any of this. Inside Nano you can:

- Run the **Boxart Scraper** (Settings > Game Settings > Boxart Scraper) to fetch art automatically.
- Highlight a game, press the Options button, and choose **Set Boxart** to use any image from your Photos.

Both are covered on the [Boxart and Metadata](boxart.html) page. The rest of this page is for managing covers **in bulk or from a PC**.

## The GammaOS Boxart Tool

The easiest way to manage your covers from a computer is the **GammaOS Boxart Tool**, a small cross-platform app (Windows, macOS, Linux) that talks to your device over ADB. It has a desktop window and a command line, and it writes to the same place Nano does, so anything you set shows up in the XMB, DSi and Minima themes.

Get it here: **[github.com/TheGammaSqueeze/GammaOS-BoxartTool](https://github.com/TheGammaSqueeze/GammaOS-BoxartTool)**

### What you need

- Your handheld connected over USB with **USB debugging** turned on (Settings has a Developer Options entry, and desktop mode exposes the full Android settings).
- **Root ADB.** The cover cache lives in a protected system folder, so the tool runs `adb root` for you. This works on the standard GammaOS builds.
- **Python 3.8 or newer** on your computer, plus the `adb` command from Android platform-tools. Pillow is optional and only makes the previews nicer (`pip install pillow`).

### Install

```bash
pip install .
# or run it without installing:
python3 gammaos-boxart.py --gui
```

### The desktop app

Launch `gammaos-boxart-gui`. It connects to your device, lists your games (the ones that already have a cover are starred), and previews the selected cover.

![The GammaOS Boxart Tool desktop app](assets/img/shots/boxart_tool_gui.png)

From here you can:

- **Set / Replace Cover** pick any image; the tool pushes it and restarts Nano so it appears right away.
- **Save Current Cover As** pull an existing cover back to your PC.
- **Remove Cover** delete a custom cover and fall back to the generic icon.
- **Bulk Import** and **Bulk Export** manage the whole library in one go.

### The command line

Every action is also a command, which is handy for scripting or batching.

![The GammaOS Boxart Tool command line](assets/img/shots/boxart_tool_cli.png)

```bash
gammaos-boxart list                         # every game, boxart marked
gammaos-boxart set nes/Spacegulls.nes cover.png       # add or replace a cover
gammaos-boxart get nes/Spacegulls.nes -o out.png      # pull a cover to your PC
gammaos-boxart remove nes/Spacegulls.nes              # remove a custom cover
gammaos-boxart export ./my-covers                     # back up every cover (+ manifest)
gammaos-boxart import ./my-covers                     # bulk import a folder of covers
```

A game can be named by its full device path (`/storage/emulated/0/ROMs/nes/Game.nes`) or the short `system/file` form (`nes/Game.nes`).

### Bulk backup and restore

`export` writes every cover into a folder as `system/GameName.png`, plus a `boxart_manifest.json`, so you have a tidy, portable backup. `import` reads that folder back: with the manifest it restores each cover to the exact game, and without one it matches images to games by filename (`Spacegulls.png` finds `Spacegulls.nes`). This is the fast way to move your covers to a new device or a fresh install.

Here is a set of tool-added covers rendering on the device, in the XMB theme:

![Custom boxart on the device](assets/img/shots/boxart_device.png)

## How boxart is stored

If you would rather understand the format or edit it by hand, here is exactly how Nano keeps cover art. Everything lives in a protected folder:

```
/data/system/nano_scrape/
    index.json        the manifest (version 2)
    names.json        per-game title overrides (version 1)
    <key>.box.png     a game's cover image
    <key>.fan.jpg     a game's fan art
```

`<key>` is the game's ROM path run through a 64-bit **FNV-1a** hash, written as 16 lowercase hex digits. It is only a filename convention: Nano loads a cover from the path stored in the manifest, so what really matters is the `index.json` entry.

### index.json

`index.json` is an object with a `version` and an `items` array. Each item ties one ROM to its art and metadata. Only non-empty fields are written.

```json
{
  "version": 2,
  "items": [
    {
      "rom": "/data/media/0/ROMs/nes/Spacegulls.nes",
      "box": "/data/system/nano_scrape/5cbf8efabe804c89.box.png",
      "scraper": "manual",
      "when": 1786974787,
      "title": "Spacegulls"
    }
  ]
}
```

| Field | Meaning |
|-------|---------|
| `rom` | The full ROM path. Nano matches it across the `/storage/emulated/0`, `/data/media/0`, `/sdcard` and `/storage/self/primary` views, so any of those prefixes works. |
| `box` | Absolute path to the cover image. This is what Nano actually loads. |
| `fan` | Absolute path to fan art (optional). |
| `title` | The displayed name (optional). |
| `scraper` | Where it came from; use `manual` for your own art. |
| `when` | Unix timestamp. |
| `desc`, `genre`, `players`, `rating`, `date`, `dev`, `pub` | Optional scraped metadata. |

`names.json` is the same shape with `{ "rom", "name" }` items and just renames a game.

Nano reads `index.json` once at startup, so after any change you must restart Nano for it to show. It also refuses to save over an `index.json` it cannot read, so a bad edit will not wipe your library, but you should still keep a backup (use `export`).
{: .callout .note }

## Doing it by hand

If you want to skip the tool, the same result is a few ADB commands (root, as above):

```bash
adb root
# 1. copy your image into the cache under the game's hash-named file
adb push mycover.png /data/local/tmp/c.png
adb shell 'cp /data/local/tmp/c.png /data/system/nano_scrape/5cbf8efabe804c89.box.png'
adb shell 'chmod 600 /data/system/nano_scrape/5cbf8efabe804c89.box.png; restorecon /data/system/nano_scrape/5cbf8efabe804c89.box.png'
# 2. add or edit the matching item in /data/system/nano_scrape/index.json
#    (rom, box, scraper: "manual"), then restart Nano:
adb shell 'setprop ctl.stop gammaos-nano; setprop ctl.start gammaos-nano'
```

The hard part by hand is computing the `<key>` (the FNV-1a hash of the ROM path) and editing the JSON safely, which is exactly what the tool does for you, so the tool is the recommended route.

## Tips

- Any common image works (PNG, JPG, WebP). Portrait covers around 480x640 look best in the XMB and DSi themes.
- Run `export` before a big change so you always have a backup.
- If a new cover does not appear, restart Nano (the tool does this automatically; by hand, use the `setprop` line above).
- To go back to the generic cartridge icon, `remove` the cover (or Reset Boxart in the game's Options menu inside Nano).

## Related pages

- [Boxart and Metadata](boxart.html)
- [Adding Games](adding-games.html)
- [The GammaOS Boxart Tool](https://github.com/TheGammaSqueeze/GammaOS-BoxartTool)
