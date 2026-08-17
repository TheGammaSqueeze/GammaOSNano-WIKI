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

### The home screen feels laggy or the device runs hot

The GammaOS XMB theme, with its flowing wave and glass icons, is the heaviest home to draw. On lower-powered devices, the TrimUI Brick for example, it can stutter and warm the device up. Two things help, and both take effect right away:

- Switch to a lighter home in **Settings > Theme Settings > Home Theme**. The **DSi** and **Minima** themes are much lighter than XMB.
- Keep XMB but turn on its **Half Resolution** toggles (Wave, Icons and Clock) in **Theme Settings**. Each renders that layer at half size for a large speed-up while the menu text stays crisp.

### A game crashes back to the menu, especially under load

Being dropped back to the home is usually a crashing core or a device throttling under load, not a safety feature. Try:

- Set **Performance Mode** to **Max Performance** in the [Quick Menu](quick-menu.html) (hold <span class="btnchip">Power</span>). This keeps the CPU from slowing down under load.
- Change the core or emulator for that system in **Settings > Game Settings > Game Systems**. A different core is often more stable for demanding systems like Nintendo 64.

On a low-memory device, a first-time RetroArch setup can also crash once; force a restart (hold <span class="btnchip">Power</span>) and run it again, and the second attempt usually succeeds.

### Where does RetroArch keep my saves?

By default RetroArch stores save files and save states in the same folder as the game. You can change where they go in **RetroArch > Settings > Directory** (Save Files and Save States). When moving to another device, ordinary in-game saves (`.srm`) transfer reliably; save states are tied to the exact core version and may not carry across. For the built-in DS emulator, see [DraStic Nano](drastic-nano.html) instead.

### Wi-Fi keeps dropping after sleep, or will not hold on my mesh network

If Wi-Fi drops when the screen sleeps or the lid closes, it normally reconnects on wake; if it does not, toggle Wi-Fi off and on in **Network Settings**. If the device keeps dropping, or reboots, on a mesh network or a mixed 2.4/5GHz network, connect it to a dedicated **2.4GHz** access point (or your router's 2.4GHz band under its own name). This has been the reliable fix on the RG DS and RG Vita.

### My device will not power off, turns back on when I close the lid, or will not power on

After switching to GammaOS from another OS (Rocknix in particular), the power controller can be left in a state the GammaOS kernel does not expect. The symptoms arrive together: the device will not power off, turns itself back on when you close the lid, drains to empty overnight, or will not power on after charging.

The fix is to reset the power controller by disconnecting the battery: open the back cover, unplug the battery for 10 to 15 minutes, then reconnect it. No reinstall is needed. This has mainly been seen on the Anbernic RG DS.
{: .callout .warn }

### How do I get back to Nano from full Android?

Nano and full Android (desktop or TV mode) are two boot targets on the same system, so your games, saves and apps stay in place either way. To return to Nano, open the power menu and choose **Boot to Nano**. The full walkthrough, including why you might boot to Android for a native app or the Play Store, is on [Desktop Mode Features](atv-desktop-features.html).

### How do I get the Play Store or Google apps?

It depends on your edition. **GammaOS Full** already includes the Play Store and Google apps. On **Lite** and **Core**, which ship without Google services, use **Aurora Store** for most apps, or install **microG** while in full Android mode for full Google services and paid apps. The step-by-step is on the [Applications](applications.html#google-apps-and-the-play-store) page.

microG is a community-collected setup, not officially endorsed or supported by GammaOS, and it should not be used on low-memory devices such as the TrimUI Brick (1GB RAM).

### More help

- [OS Controls](controls-os.html) and [RetroArch Controls](controls-retroarch.html)
- [Adding Games](adding-games.html), [Game Systems](game-systems.html), and [Custom System](custom-system.html)
- [Boxart](boxart.html) and [Emulators](emulators.html)
- [Settings Reference](settings-reference.html) and [GammaOS Toolbox](gammaos-toolbox.html)
- [ADB Setup and Logs](adb-and-logs.html) to connect a PC and collect logs for support

## New in this release

Common questions about the features added since GammaOS Nano 1.4.

### How do I mark a game as a favourite?

Highlight the game and press the Options button, then choose **Add to Favorites**. A single cross-system **Favorites** list appears under the Game category (above Collections) as soon as you star your first game, and it disappears again when you remove your last. Use **Remove from Favorites** in the same menu to un-star.

### Can I set my own box art from an image on the device?

Yes. Highlight the game, press Options and choose **Set Boxart**, then pick any image from your Photos. It is copied into the cover cache and shows up immediately in every theme. Use **Reset Boxart** to remove it. This is the easiest way to give cover art to homebrew, undubs, prototypes and romhacks that the scraper cannot match by filename. If you prefer, the game's **Information** page shows the exact cover file path so you can drop your own image there manually.

### A game's name is wrong or the scraper cannot match it. Can I fix it?

Open the game's Options menu and choose **Rename / Edit Title** to type the correct name. The new name is used everywhere (game lists, Recently Played, search and the Information page) and is also used as the scraper search query, so you can rename a game and then run **Scrape This Game** to fetch the right art and details. To scrape one game under a different name without renaming the file, use **Scrape with Custom Name...**. Renaming to an empty title reverts to the filename.

### How do I transfer ROMs and files onto my device?

Connect the device to a PC, then go to **Settings > USB & Docking** and select **File Transfer (MTP)**. The device appears as a drive on your PC; switch back to **Charge Only** when you are done. On a brand-new install MTP can be reluctant until you have launched a game once.

If MTP does not connect or your PC does not see storage, try these in order:

- **Check the cable and port.** Use a data cable, not a charge-only one, and try a different USB port. On the TrimUI Brick, use the **bottom charging port**, not the OTG port next to the shoulder buttons.
- **Use ADB Explorer.** [ADB Explorer](https://github.com/Alex4SSB/ADB-Explorer) is the recommended alternative when MTP is unreliable. It browses and copies files over ADB and does not depend on MTP.
- **Use a network share.** Copy files over Wi-Fi with SMB, FTP or WebDAV, no cable needed. See [Network Shares](network-shares.html).

On a device that boots from its SD card (the A133P handhelds such as the TrimUI Brick and the MagicX Zero 28), do not remove the card and put it in your PC to copy games. Those cards hold an encrypted Android partition layout, so a computer will not show your storage. That is expected, not a fault. Use MTP, ADB Explorer or a network share instead.
{: .callout .warn }

### How do I hide game systems or home categories I don't use?

Go to **Settings > Theme Settings > Home Categories**. Use X to hide or show a category and L1/R1 to reorder them. To hide individual rows inside a category (for example specific game systems), drill into that category and toggle the rows there. Quick Menu always stays first, Settings cannot be hidden, and at least one category must remain visible. Changes are saved and apply live across XMB, DSi and Minima.

### How do I pin my favourite apps to the home?

Open the Applications category, highlight an app and press Y. A **Pinned Apps** row appears in the Game column showing your pinned apps with their real icons, and it persists across restarts. Press Y again on a pinned app to unpin it.

### Can I keep an app running in the background when I leave it?

Yes. Open the app's Options menu and turn on **Keep Running in Background**. That app will not be force-stopped when you return to the menu, which is useful for music players, file managers and other tools you want to stay warm. Leave it off for games so they close cleanly.

### How do I make text bigger or smaller?

Go to **Settings > Theme Settings > Font Size** (also listed under Display). The size applies live across XMB, DSi and Minima, and word-wrapped text reflows as you change it. In Minima, long names scroll on the focused row at the normal size by default; you can switch to Shrink to Fit in Theme Settings if you prefer.

### My whole ROMs folder has many systems. Do I have to add each one?

No. Go to **Settings > Game Settings > Game Systems > Auto-add Systems from Folder** and point it at your ROMs root. Nano recognises ES-DE style folders, links them to built-in systems or creates new ones, and skips empty and media-only folders. A summary tells you what was added and which systems still need an emulator installed.

### Why does a game show a black screen instead of launching?

If the emulator for that game is not installed, Nano now shows a short warning message instead of black-screening. Install the required RetroArch core or standalone emulator app, or set the correct emulator for that system in **Settings > Game Settings > Game Systems**, and try again.

### Does the DSi theme have a dark mode?

Yes. Switch to the DSi theme, then in **Settings > Theme Settings** turn on **Dark Theme**. The whole DSi look flips to light text and icons on a dark field, and it applies immediately. The DSi theme also follows your accent **Colour** setting.

### How do I paste a URL or long text into a text field?

When the on-screen keyboard is open, press Y to paste whatever is on the system clipboard into the field. This saves typing out long URLs and passwords by hand.

### My multi-disc PS1 game shows every disc separately. How do I group them?

Create a `.m3u` playlist file listing the disc images and place it alongside them. Nano groups multi-disc games referenced by an `.m3u` into a single launchable entry and hides the individual discs. This is on by default. If your CD games are in subfolders, you can also enable **Scan ROM Subfolders** in GammaOS Toolbox so they are found.

### Can I move where DraStic keeps its saves?

Yes. Go to **Settings > Game Settings > DraStic Data Folder** and choose a folder on shared storage. drastic-nano and the standalone DraStic app then use that same location, so your saves, config and BIOS live in one place you can reach outside the app.

### DraStic runs slowly on my device. What can I try?

Open the in-game overlay and go to Video. Turn on **Half Resolution** to render at half size and upscale (a big speed-up on fill-bound panels, at the cost of a softer image). You can also try **16-Bit Layout** to cut bandwidth. **SF Vsync Lock** is off by default and only helps once the frame already fits inside the vblank. All three are opt-in and safe to toggle live. The optional **FPS Counter** in the same menu helps you see the effect.

### Streaming apps like Disney+ show a DRM or certification error. Any fix?

Go to **Settings > GammaOS Toolbox** and enable **Widevine L3 Compatibility**. This forces Widevine L3 mode, which resolves common DRM errors (such as the Disney+ error) on uncertified devices.
