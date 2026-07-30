# Research brief: Full feature + settings inventory - code-verified

## Home themes (Settings > Theme Settings > Home Theme; applying restarts the home)

### GammaOS XMB (PlayStation 3 style) - default
Horizontal category bar with a vertical item list dropping from the active category, a continuous PS3 "wave" background, glass icons, and firmware-style animations. Adapts to any screen size/orientation.
XMB-only options: **XMB Wave** on/off (default On, auto-off when a custom wallpaper is set), **Background** (Original / Classic / Wallpaper), **Font** (Original / Rounded / Pop), **Day/Night** lighting (Auto by time of day / Day / Morning / Dusk / Evening / Night; default Night).

### DSi Menu (Nintendo DSi system menu)
A carousel of glossy tiles on a light field with a soft scanline background, spring-fall entrance, and a touch fling/scrub carousel with snap-to-slot.
DSi-only option: **Single-Screen / Stacked** layout on single-panel devices (`persist.gammaos.nano.ndstheme.stack`): carousel-only (default) or a stacked status-bar-on-top layout. Dual-screen devices always use both physical panels.

### Minima (NextUI style)
A minimal vertical text list on a black canvas; the selected row is a white rounded capsule with inverted text, plus a small accent status pill and a bottom button-hint bar. Smooth exponential scroll. No icons in the main list.
Minima-only options: **Background Colour** (solid colour instead of black; overridden by a photo/video wallpaper), and an opt-in for the XMB wave (off by default in Minima).

### Accent Colour (all three themes) - Settings > Theme Settings > Colour
21 options: **Original** (each theme's signature colour: XMB uses a per-month hue, Minima a berry tone, DSi its azure) plus Yellow, Green, Pink, Dark Green, Light Purple, Teal, Dark Blue, Magenta, Orange, Brown, Red, Black, White, Gray, Blue, Cyan, Lime, Gold, Violet, Crimson. On XMB it tints the wave + menu accents; on Minima the capsule + hint bar; on DSi it hue-rotates the chrome.

## Wallpapers (Settings > Theme Settings)
- **Wallpaper Image** - pick a photo for the home background (via the photo grid picker).
- **Bottom Wallpaper** - separate wallpaper for the bottom screen (dual-screen only).
- **Video Wallpaper** - pick a looping video for the top-screen background.
- **Clear Wallpaper** - remove custom wallpaper and restore the wave.
- **Wallpaper Dimming** - darken a bright wallpaper so icons/text stay readable (default 25%).
- **XMB Wave** - on/off; auto-off when a wallpaper is set, then honored verbatim.
Supported wallpaper image types: jpg, png, webp, bmp, gif, heic. Video: mp4, mkv, webm, mov, 3gp, avi, ts, mpg.

## Games

### Adding ROMs
Put ROMs in per-system folders, e.g. `/sdcard/ROMs/nes/`, `/sdcard/ROMs/snes/`. SD card, internal storage, or USB all work. Subfolder scanning and multi-disc `.m3u` grouping are configurable (GammaOS Toolbox). After adding files, run **Settings > Game Settings > Rescan Games**.

### Game Systems editor (Settings > Game Settings > Game Systems)
Lists every system with an On/Off enable toggle; reorder with L1/R1. Per-system fields:
Display Name, Short Name, Launch Type (Libretro Core / Custom Package), Emulator (searchable core or app picker), Core .so, Package, Intent Template, Launch Args, Extensions (comma-separated), Scan Folders (folder picker, or default `ROMs/<id>/`), Icon (grid of ~849 icons or a custom PNG), Icon Tint (21 swatches or custom RGB), per-system Scraper + username/password, "Scrape This System", and Reset-to-Default (built-in) or Delete (custom).

### Recently Played
Auto-tracked; the just-played game jumps to the front. Pruned when a game is deleted or rescanned away.

### Collections (cross-system groups)
Create named collections (Favorites, Multiplayer, etc.). Add a game via its Options menu > **Add to Collection** (create new via keyboard or pick an existing one). Collections show as their own entry in the Game category. Per-collection Rename / Delete; a game can be in several collections and removed from any.

### Game Options menu (Options / Triangle on a game)
Information (boxart, synopsis, metadata, size, path), Rename / Edit Title, Set Boxart (custom image), Add to Collection, Remove from Collection (inside a collection).

### Boxart scraping (Settings > Game Settings > Boxart Scraper)
Scraper service (ScreenScraper default, or TheGamesDB), Replace Icons with Boxart (default On), Hover Background Art (fanart behind the highlighted game, default On), Scrape Region, Overwrite Existing (default Off), optional ScreenScraper account username/password (built-in developer credentials are used if blank), TheGamesDB API key, and **Scrape All Systems**. Art is cached under `/data/system/nano_scrape/`. A background thread scrapes during idle time.

## Media

### Photo
Full-screen viewer with thumbnail grid; jpg/png/webp/bmp/gif/heic/heif; touch pan + pinch zoom; slideshow with play/pause, prev/next, info, delete. Group by Month / Year / Album / All. Playlists (manual cross-folder groups). "Search for Media Servers" browses DLNA/network shares.

### Music
Albums / Playlists / Tracks; mp3/flac/m4a/aac/ogg/opus/wav/wma. Now-Playing screen with album art, play/pause, prev/next, volume, and visualizers (Canyon / Globe). **Internet Radio** browser (default On; custom playlist URL configurable in Music Settings). "Search for Media Servers" for DLNA/shares.

### Video
Folders / Playlists / Videos; mp4/m4v/mkv/webm/mov/3gp/avi/ts/mpg. Full-screen player with multi-audio-track selection (language-labeled), subtitle/caption selection, play/pause, seek, volume. **IPTV** live-channel browser (default On; custom playlist URL in Video Settings). Handles MPEG-TS and AVI in-process.

## Applications
Installed apps show as an "Applications" entry in the Game category. Per-app Options: Uninstall, Default handler, Refresh Applications List. System apps are hidden by an exclusion list. Launching an app hands off like a game and returns to the home on exit.

## Network
- **Network Settings**: connection status list (SSID/IP/signal), Internet Connection on/off, **Internet Connection Settings** (the Wi-Fi + Bluetooth setup wizard: SSID pick, WPA2 password, pairing), Internet Connection Test.
- **Network Shares**: connect SMB / NFS / WebDAV / FTP shares; they appear in the File Explorer and can be added to the media libraries so scanned media shows up in Photo/Music/Video.
- HUD top bar shows Wi-Fi signal and Bluetooth status.

## Quick Menu (hold Power on the home, or its home shortcut)
Screen Brightness slider, Performance Mode, Quick Settings tiles, System Settings (launch the Settings app), Global Shaders, Notifications, USB Settings (adb/mtp/rndis/off), Close/Kill Apps, and a Power submenu (Reboot / Shutdown / Recovery / Safe Mode / Android Settings).

## Settings tree (Settings category / Quick Menu > System Settings)

- **User Guide** - built-in how-to.
- **System Update** - OTA/USB system update.
- **Game Settings** - Rescan Games, Boxart Scraper, Game Systems.
- **Video Settings** - IPTV Channels on/off, IPTV Playlist URL.
- **Music Settings** - Internet Radio on/off, Radio Playlist URL.
- **System Settings** - System Name, System Language (live locale preview across many languages).
- **Developer Options** - USB Debugging, Stay Awake While Charging, Show Touches, Pointer Location, transition/window/animator scales.
- **Theme Settings** - Colour, Background, Wallpaper, Wallpaper Image, Bottom Wallpaper, Video Wallpaper, Clear Wallpaper, Background Colour (Minima), Wallpaper Dimming, XMB Wave, Font, Day/Night, Home Theme, Bottom Clock on/off, Bottom Clock FPS (30/60), Home Categories (reorder/hide Settings/Photo/Music/Video/Game/Network with L1/R1).
- **Date and Time Settings** - Date/Time, Date Format, Time Format (12/24h), Time Zone, Daylight Saving, Set via Internet (NTP), Set Manually.
- **Power Save Settings** - Battery Saver.
- **Accessory Settings** - Manage Bluetooth Devices.
- **Gamepad Settings** - Controller Enable, Merge Controllers, Hide Source Device, ABXY Swap, Invert Left/Right Stick, Analog-to-D-Pad, D-Pad-to-Analog, Global Sensitivity, PWM (rumble) Enable + Intensity, D-Pad Threshold, Screen Map, Mouse Mode (stick/d-pad speed, boost, scroll).
- **Slide Behaviour** - configure a slide/swivel/hall switch: enable, device, button code, event type, active value, On Slide Down / Up actions (Rotate/Sleep/Wake/Launch/PSP Clock), sleep delay, rotation angle, launch target, show-clock-on-slide, live backdrop, parallax calibration.
- **GammaOS Toolbox** - Immersive Mode, Refresh Rate Lock, Display Tweaks, Force Client Composition, Desktop Fullscreen, Multi-Volume, Ultra Low Power Saving, Virtual Memory (swap size), RetroArch Back Button Override, Start+Select LED, Scan ROM Subfolders, Group Multi-Disc (.m3u), USB Controller Switch, DC Dimming Emulation, Phone Taskbar, Dual Taskbar, Black Frame Insertion, CRT Shader, Dual-Stack Display, RGB LED, Launch Guard, Widevine L3 Compatibility.
- **File Explorer** - browse/manage files.
- **Network Shares** - SMB/NFS/WebDAV/FTP.
- **GammaRGB** - RGB LED lighting: Effect (Off/Follow Screen/Solid/Effect 1-5), colour, brightness, scale-with-brightness, speed, saturation, fade, split zones + per-zone colours.
- **GammaEQ** - speaker EQ/enhancements: master enable, speaker-only, preview, preamp/postgain, Crystalizer, Bass Limiter, Mid Protector, Stereo Widener, two Parametric EQ bands.
- **Display Settings** - Brightness, LiveDisplay (Night Light + temperature, colour calibration, saturation, reading mode), Screen Saver, Screen Timeout (15s..Never), Font Size, Dark Theme, Screen Orientation, Force Orientation.
- **Sound Settings** - Touch Sounds, Charging Sounds, Screen Lock Sounds.
- **Network Settings** - as above.

## Other home behaviors
- List wrap-around (Up on the first item wraps to the last, and vice versa).
- Bottom-screen PSP-style analog clock on dual-screen devices (Theme Settings > Bottom Clock, FPS 30/60), which can refract the game behind it while playing.
