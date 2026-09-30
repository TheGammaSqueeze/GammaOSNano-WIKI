---
title: Game Systems
group: Games
order: 2
icon: 🗃️
desc: Enable, disable, reorder and fully edit each game system.
---

The Game Systems editor is where you control every console in your library. You can turn systems on or off, change the order they appear in, and edit every detail of how a system finds and launches its games.
{: .lead }

## Opening the editor

1. Open the **Settings** category.
2. Go to **Game Settings**.
3. Choose **Game Systems**.

You get a list of every system Nano knows, each with an On/Off toggle. The editor uses your home theme's own look, so it feels native whether you are on XMB, DSi or Minima.

In the DSi theme, Game Settings is a list with Game Systems at the top, followed by Quick Resume, Rescan Games, DraStic Data Folder, DraStic Cheats Folder and Boxart Scraper.

![Game Settings list in the DSi theme](assets/img/shots/v143_dsi_game_settings_list.png){: .wide }

<div class="theme-trio">
  <figure><img src="assets/img/shots/xmb_gamesystems.png" alt="Game Systems list in the XMB theme"><figcaption><b>GammaOS XMB</b></figcaption></figure>
  <figure><img src="assets/img/shots/min_gamesystems.png" alt="Game Systems editor in the Minima theme"><figcaption><b>Minima</b></figcaption></figure>
</div>

## Turning systems on and off

Each system has an **On/Off** toggle (press <span class="btnchip">X</span> on a system in the list to flip it). Turn a system Off to hide it from the Game category (handy if you do not own any games for it). Turn it back On whenever you like. Turning a system off does not delete any files.

## Reordering systems

To change the order systems appear in on the home screen, highlight a system and press <span class="btnchip">L1</span> or <span class="btnchip">R1</span> to move it up or down the list. Put your favourites at the top.

The order you set here is exactly what the home shows. Reordering also sets the Game category's <span class="btnchip">Y</span> sort back to **Default** (the manual order), so a sort you picked earlier cannot hide your new order. See [Sorting the Game category (Y)](#sorting-the-game-category-y).

## Editing a system

Select any system to open its editor. Every field below can be changed, so you can point a system at a different emulator, add file types, or give it a new icon.

| Field | What it does |
|-------|-------------|
| **Display Name** | The name shown in your library (for example "PlayStation 2"). |
| **Short Name** | A brief label (for example "PS2"). |
| **Launch Type** | Choose **Libretro Core** (runs inside RetroArch) or **Custom Package** (runs a standalone emulator app). |
| **Emulator** | A searchable picker of RetroArch cores or installed apps. Picking one fills in the launch details for you. |
| **Core .so** | The libretro core file used, when Launch Type is a Libretro Core. |
| **Package** | The app the game hands off to, when Launch Type is a Custom Package. |
| **Intent Template** | The launch command Nano sends to a standalone app. Usually filled in for you when you pick the emulator. |
| **Launch Args** | Extra arguments passed at launch. |
| **Extensions** | The file types this system scans for, comma-separated (for example `iso, chd, gz`). |
| **Scan Folders** | Which folders to search for games. Use the folder picker, or leave the default `ROMs/<id>/`. |
| **Icon** | The system's icon. Choose from a grid of built-in icons, or press <span class="btnchip">X</span> in the grid to import your own PNG. See [Custom system icons](#custom-system-icons). |
| **Icon Tint** | Recolour the icon from 21 swatches, or set a custom RGB colour. |
| **Scraper / Username / Password** | An optional per-system override for the cover-art scraper. See [Boxart & Metadata](boxart.html). |
| **Scrape This System** | Fetch boxart and metadata for every game in this system now. |
| **Clear Boxart** | Delete this system's downloaded covers and background art. See [Clear Boxart](#clear-boxart). |
| **Reset-to-Default** | On built-in systems, restore the original settings. |
| **Delete** | On custom systems, remove the system. |

Built-in systems show **Reset-to-Default**, and custom systems you created show **Delete** instead. That way you can always undo your changes to a built-in system, and cleanly remove ones you made yourself.

## A quicker way in

From the **Game** category, highlight a system row and press the Options button, then choose **Manage Game System**. That jumps you straight into this editor for that system, without going through Settings. See [Context Menus](context-menus.html) for more shortcuts.
{: .callout .tip }

![Manage Game System shortcut](assets/img/shots/wn_manage_system_shortcut.png)

## Scan folders and default locations

The **Scan Folders** field lists which folders a system searches for games. It now also shows the built-in default folders (for example `ROMs/nes/`) with the number of games found in each, so you can see at a glance where to drop your ROMs. A default folder that has no games yet is shown as **Default (empty)**.

When you remove a scan-source folder, Nano first asks you to confirm with a **Cancel** or **Remove Folder** dialog that shows the folder path, so you do not drop a source by accident. Removing a folder only stops Nano scanning it; your files are left in place.

### Arcade systems stay separate

Each arcade system only scans its own folders. Adding CPS1, FBNeo or MAME no longer pulls in every other arcade folder on your storage, so your CPS1 list shows only CPS1 games and MAME only MAME games. The generic `arcade` folder counts as MAME, and `fba` counts as FBNeo.

If you choose scan folders for a system yourself, it scans **only** those folders, not its defaults as well.

## Arcade (Vertical)

Vertical (TATE) arcade games, the ones made for a portrait screen, get a system of their own called **Arcade (Vertical)**. Put them in a ROM folder named any of these (upper or lower case both work):

- `VARCADE`
- `VERTICAL`
- `TATE`
- `TATEGAME`
- `verticalarcade`

The system is added automatically from those folders and appears under **Game** once it has games. It runs them with MAME by default, with FBNeo available as the other choice (change it with the **Emulator** field). Before this, those folders were ignored or folded into MAME.

## Clear Boxart

To wipe the artwork for one system (for example before scraping it again from scratch), open the system in the editor and choose **Clear Boxart**. Nano asks you to confirm with **Cancel** or **Clear Boxart**, then deletes that system's downloaded covers and background art. Your games are not touched, and other systems keep their art.

![Clear Boxart confirmation](assets/img/shots/v143_dsi_clear_boxart_confirm.png){: .dual }

## Missing-emulator warning

If a system's libretro core or standalone emulator app is not installed, Nano tells you rather than launching into a black screen. When you try to start a game whose core `.so` or standalone package is missing, a short toast appears explaining what is needed. See [Emulators & Cores](emulators.html) for which core or app each system uses.

## Auto-add whole systems from a folder

At the top of the Game Systems list you can bulk-import an entire ROMs collection in one pass. Choose **Auto-add Systems from Folder** and point it at your ROMs root (laid out with one folder per system, the ES-DE style).

Nano walks the folders and, for each recognised system, links it to a built-in system or creates a new one for it. Empty folders and media-only folders are skipped. When it finishes it shows a summary of what was added, including any systems that still need an emulator installed to run.

![Bulk auto-add systems](assets/img/shots/wn_bulk_autoadd.png)

## Sorting the Game category (Y)

The order systems appear on the home screen is separate from how you sort the tiles on screen. In the **Game** category, press <span class="btnchip">Y</span> to cycle the tile order: **Default**, **A to Z**, **Most Games**, and **By Manufacturer**. **Default** is the order you set in the Game Systems editor. The choice persists across restarts, and it only changes the on-screen order. It never reorders or touches your actual games or systems.

![Game category sort](assets/img/shots/wn_game_sort.png)

## Adding a whole new system

The editor is also how you add a console Nano does not list yet. Scroll to the top of the Game Systems list, choose **Add New System...**, and pick your emulator. For a full worked example (adding AetherSX2 for PlayStation 2, step by step), see [Add a Custom System](custom-system.html).

## Custom system icons

Every system has an **Icon** field in its editor. Selecting it opens the icon grid (**Choose Icon**), a searchable set of hundreds of built-in console and platform glyphs. Press <span class="btnchip">Y</span> to filter by name, highlight the one you want, and press <span class="btnchip">Cross</span> to assign it.

![The Choose Icon grid with the X: Import PNG hint](assets/img/shots/v143_xmb_icon_grid.png){: .wide }

### Import your own PNG

If none of the built-in glyphs suit you, you can use any PNG or JPG as the system's icon, right from the menu:

1. Open the system's **Icon** field to show the icon grid.
2. Press <span class="btnchip">X</span> (**Import PNG**, shown in the hint along the bottom). A file browser opens at your storage.
3. Browse to your image and select it. Nano copies it into its own storage and sets it as the system's icon straight away. The **Icon** row then reads **Custom**.

In this release, the icon grid can appear empty in the **DSi theme on dual-screen devices** (such as the RG DS Plus). If that happens, switch to the XMB theme (**Settings > Theme Settings > Home Theme**), set the icon there, and switch back. The icon you choose shows in every theme.
{: .callout .warn }

Your file is copied, so you can delete the original afterwards and the icon still works. If you later delete the custom system, its imported icon is cleaned up with it.

**Icon requirements**
{: .callout .note }

- **Format:** PNG (recommended) or JPG. PNG is preferred because it keeps transparency.
- **Shape:** square. A non-square image is stretched to fit, so trim it to 1:1 first.
- **Size:** at least 8x8 pixels. Around 256x256 is a good target; anything larger is just scaled down and wastes space.
- **Transparency:** use a transparent background (PNG) so only your artwork shows, not a solid block behind it.
- **Colour:** the built-in glyphs are single-colour and respond to the **Icon Tint** setting. A full-colour PNG is shown as-is, untinted, so if you want the tint swatches to affect your icon, supply a white or light silhouette on a transparent background.

### Over ADB (older builds only)

You do not need this on current builds: use **Import PNG** above. It is kept for older builds that do not have the in-menu button. On those, you can set a custom icon by hand over [ADB](adb-and-logs.html). Nano reads its systems from `/data/system/nano_systems.json` and accepts a `file:` icon reference that points at any image on the device.

1. Copy your PNG into Nano's icon folder (create it if needed), naming it after the system's id:

   ```
   adb shell mkdir -p /data/system/nano_user_icons
   adb push myicon.png /data/system/nano_user_icons/<system-id>.png
   ```

2. Pull the systems file, edit it, and push it back:

   ```
   adb pull /data/system/nano_systems.json .
   ```

   Find your system in the JSON and set its icon `ref` to the file path:

   ```
   "icon": { "ref": "file:/data/system/nano_user_icons/<system-id>.png", "tintR": 1, "tintG": 1, "tintB": 1 }
   ```

   ```
   adb push nano_systems.json /data/system/nano_systems.json
   ```

3. Reboot, or restart Nano, so the new config is read.

The `<system-id>` is the `id` value shown next to each system in the same JSON file. Do not drop your PNG into `/system/` (it is read-only), and avoid the `/data/system/nano_xmb/icons_retroarch/` override folder: putting files there makes the icon grid show only that folder and hides all the built-in glyphs.
{: .callout .warn }

## Related pages

- [Adding Games](adding-games.html) for where to put your ROM files.
- [Add a Custom System](custom-system.html) for a complete walkthrough.
- [Boxart & Metadata](boxart.html) for cover art and game info.
