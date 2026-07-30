# Research brief: Context/side menus + adding a custom system - code-verified

## The Options (context) menu

Press the **Options button** (Triangle glyph; the X / BTN_NORTH button on the pad, Tab on a keyboard, or middle-click on a mouse) on whatever is highlighted to open a context menu. The menu contents change based on what you selected. The first bold row is the default action (also reachable with A). Below is the exact menu for each item type.

### On a game (or a Recently Played entry)
- **Start** (launch)
- **Rename / Edit Title** - sets the shown name everywhere and becomes the scraper search query
- **Scrape This Game** - re-fetches art/metadata for just this game (forces overwrite)
- **Information** - full scraped info page (cover, fanart, synopsis, genre, players, rating, date, developer/publisher, file path/size)
- **Set Boxart** - pick any image as the cover
- **Reset Boxart** - only shown once a custom/scraped cover exists
- **Add to Collection** - add to a collection (or create a new one)
- **Remove from Collection** - only shown when you are inside a collection

### On an application
- **Start**, **Information**
- **Screen Orientation** submenu: Default / Auto / Landscape / Landscape (reverse) / Portrait / Portrait (reverse) - forces that orientation while the app is foreground
- **Dual-Stack Display** submenu (dual-screen devices only): Disabled / Enabled
- **Uninstall** - real user apps only (system/protected apps do not show it)
- **Refresh Applications List** - rescan installed apps (fresh labels + icons)
- **Show All Apps (On/Off)** - list every launchable app vs only user apps

### On a game-system row (on the Game home)
- **Manage Game System** - jumps straight into that system's editor (emulator, scan folders, icon, etc.)
- **Information**

### On a collection
- **Open**, **Rename Collection**, **Delete Collection**

### On a music album / track / playlist
- **Play**, **Information**

### On a video
- **Resume** + **Play from Beginning** (if partly watched) or just **Play**
- **Add to Playlist**, **Copy**, **Delete**, **Information**

### On an IPTV channel
- **Watch**, **Add to Playlist**

### On a photo album (folder)
- **Sort By** submenu (Film Date newest/oldest, Import Date newest/oldest, Image Name)
- **Group Content**: By Month / By Year / By Album / All
- **Slideshow**: Normal / Slide / Portrait / Photo Album / Photo Album 2
- **Delete**, **Information**

### On a single photo (thumbnail grid)
- **Delete Multiple**, **Sort By**, **Slideshow**, **View**, **Copy**, **Add to Playlist**, **Print**, **Delete**, **Information**

### In the File Explorer
- Folder: **Open**, **Copy**, **Move**, **Paste Here** (when something is on the clipboard), **Rename**, **Delete**, **Information**
- File: **Copy**, **Move**, **Paste Here**, **Rename**, **Delete**, **Information**

### On an imported media folder / game scan source
- **Remove Folder** / **Remove Source** (this is also what the hidden Y-button shortcut does)

Submenu options (Sort By, Slideshow, Screen Orientation, Dual-Stack) expand inline; the default focus lands on the currently active choice.

## Side panels / dialogs

Settings screens, the Game Systems editor, colour/icon pickers, sliders (brightness, volume), Yes/No confirmations, and the media control panels are all "side panel" style modals that share the same frosted-wave chrome. They are fully controller-driven (D-pad + A/B) and touch-capable (tap a row to select+activate, drag to scroll, drag a slider track, tap Yes/No/OK, tap the dimmed area to cancel).

## Adding a custom game system (worked example: AetherSX2 for PlayStation 2)

GammaOS ships a built-in emulator catalog that already knows many standalone emulators (AetherSX2, NetherSX2, Dolphin, azahar, and more) plus every RetroArch core, so adding a system is mostly picking from lists - you rarely type an intent by hand.

### 1. Install the emulator app
Install the AetherSX2 APK (package `xyz.aethersx2.android`) like any other app - side-load it, or copy it to the device and open it in the File Explorer. Launch it once so it finishes first-run setup and you point it at your **PS2 BIOS**.

Note: GammaOS does not include any console BIOS files - you supply your own. For a standalone emulator like AetherSX2 you import the BIOS in that app's own setup on first launch. For RetroArch cores, BIOS files go in `Internal storage / RetroArch / system`.

### 2. Open the Game Systems editor
Settings > Game Settings > **Game Systems**. This lists every system with an On/Off toggle (reorder with L1/R1). Scroll to the top and choose **Add New System...**.

### 3. Pick the emulator
"Add New System..." opens the emulator picker (a searchable catalog). Search "aethersx2" and choose **ps2 - Aethersx2**. Nano fills in the launch details automatically:
- **Launch Type** = Custom Package
- **Package** = `xyz.aethersx2.android`
- **Intent Template** = `-n xyz.aethersx2.android/.EmulationActivity -a android.intent.action.MAIN -e bootPath {file.uri} --activity-clear-task --activity-clear-top`
- suggested **Extensions** for PS2: `iso, chd, gz, mdf, bin`

(The `{file.uri}` placeholder is replaced with the selected game at launch. Other PS2 targets in the same catalog: NetherSX2 Turnip, ARMSX2, EmuCoreX, and RetroArch's Play core - pick whichever emulator you installed.)

### 4. Fill in the rest of the fields
The editor rows:
- **Display Name** - e.g. "PlayStation 2"
- **Short Name** - e.g. "PS2"
- **Launch Type** - already Custom Package
- **Package** - already `xyz.aethersx2.android`
- **Intent Template** - already set (leave as-is)
- **Extensions** - `iso, chd, gz, mdf, bin` (adjust to your files)
- **Scan Folders** - point at your ROM directory. Choose the folder picker and select e.g. `/sdcard/ROMs/ps2/`, or leave Default to use `ROMs/ps2/`.
- **Icon** - pick a system icon (grid of built-in icons) or a custom PNG
- **Icon Tint** - optional colour tint
- **Scraper / Username / Password** - optional per-system scraper override
- **Scrape This System** - fetch boxart now
- **Delete System** - remove this custom system later

### 5. Add ROMs and rescan
Put your PS2 games in the folder you chose (e.g. `/sdcard/ROMs/ps2/`), then run Settings > Game Settings > **Rescan Games**. The new PlayStation 2 system appears in the Game category with your games; launching one hands off to AetherSX2 with the game path.

### Tips
- You can add unlimited custom systems this way (any standalone app or RetroArch core).
- On a system row on the Game home, press Options > **Manage Game System** to jump straight back into this editor.
- If a game does not launch, re-check the Package (the emulator must actually be installed) and the Extensions (they must include your file type).
