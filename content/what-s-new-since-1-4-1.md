---
title: What's New since 1.4.1
group: Get Started
order: 3
icon: ✨
desc: A tour of everything new in GammaOS Nano 1.4.2 and 1.4.3, from the ES-DE theme engine and Syncthing to the GPU 3D DS renderer and the Control Center.
---

GammaOS Nano 1.4.2 and 1.4.3 are two big releases centred on the built-in DS player and the dual-screen handhelds, with a new ES-DE theme engine, Syncthing built in, a much more colourful DSi theme and a long list of fixes. This page is a quick, user-facing tour grouped by area, with links to the pages that hold the full details. The screenshots were captured on an RG DS Plus running 1.4.3.
{: .lead }

Looking for the previous release? See [What's New in 1.4.1](what-s-new-since-1-4.html).
{: .callout .note }

## Themes and the home look

- **A fourth home theme: Custom / ES-DE.** **Settings > Theme Settings > Home Theme** now offers **GammaOS XMB**, **DSi Menu**, **Minima** and **Custom / ES-DE**, and applies live. See [Home Themes](themes.html).

    ![Home Theme chooser with four themes](assets/img/shots/v143_dsi_home_theme_picker.png){: .dual }

- **ES-DE theme engine.** Custom / ES-DE renders real EmulationStation-DE theme sets with their variants, colour schemes and per-game art. The **Slate** theme comes preinstalled. See [ES-DE Themes](esde-themes.html).

<figure class="ui-video-fig ar-43">
  <span class="ui-video-badge">Live demo</span>
  <video class="ui-video ar-43" autoplay loop muted playsinline poster="assets/video/esde-browse-poster.jpg">
    <source src="assets/video/esde-browse.mp4" type="video/mp4">
  </video>
  <figcaption>Scrolling through systems in the ES-DE Slate theme.</figcaption>
</figure>

- **ES-DE menu and Theme Downloader.** Press <span class="btnchip">Start</span> in the ES-DE home to open **UI Settings**: pick a theme, variant, colour scheme, font size and aspect ratio, or open **Theme Downloader** to fetch any theme from the official ES-DE list. **Nano Settings** takes you to the normal settings. You can also drop ES-DE theme folders into `ES-DE/themes` on internal storage.

    ![ES-DE UI Settings menu](assets/img/shots/v143_esde_ui_settings.png){: .wide }

    ![ES-DE Theme Downloader list](assets/img/shots/v143_esde_theme_downloader.png){: .wide }

- **Startup Menu.** **Theme Settings > Startup Menu** picks where the home opens at boot: the default, any category, or straight into one game system such as your Nintendo DS list. See [Theme Settings](theme-settings.html).

    ![Startup Menu listing game systems](assets/img/shots/v143_dsi_startup_menu_systems.png){: .dual }

- **Custom accent colour.** The **Colour** setting gains 21 presets and a **Custom...** entry at the end. It opens a full-screen picker: d-pad left and right for hue, up and down for brightness, <span class="btnchip">L1</span> / <span class="btnchip">R1</span> for saturation, <span class="btnchip">A</span> to apply. The colour drives the XMB wave, the Minima accent and the DSi chrome, live.

<figure class="ui-video-fig ar-43">
  <span class="ui-video-badge">Live demo</span>
  <video class="ui-video ar-43" autoplay loop muted playsinline poster="assets/video/colour-picker-poster.jpg">
    <source src="assets/video/colour-picker.mp4" type="video/mp4">
  </video>
  <figcaption>Moving hue and brightness in the Custom Colour picker; the hex value updates live.</figcaption>
</figure>

![XMB with a custom accent on the RG DS Plus](assets/img/shots/v143_xmb_custom_accent_dual.png){: .dual }

- **DSi top screen follows your colour.** Any accent other than Original recolours the DSi top-screen canvas, text, selection frame and scroll bar in its true hue.

    ![DSi home with a custom accent](assets/img/shots/v143_dsi_custom_accent.png){: .dual }

- **DS games show their own icon and title (DSi).** DS games without a scraped cover show the icon and name stored in the cartridge (**Titles From ROM**, on by default). New in 1.4.3, **DS Icons On Tiles** keeps the cartridge icon on the carousel tile even when box art exists; the box art still shows on the top screen.

    ![DSi carousel with cartridge icons and ROM titles](assets/img/shots/v143_dsi_rom_icons.png){: .dual }

- **DSi Background Effect on both screens.** The **Wallpaper** row in the DSi theme now offers animated effects (Snow, Rain, Confetti, Fireflies, Starfield, Aurora, XMB Wave and more) behind a see-through canvas, name balloon and scroll rail. The DSi keeps its own choice separate from XMB.

<figure class="ui-video-fig ar-23">
  <span class="ui-video-badge">Live demo</span>
  <video class="ui-video ar-23" autoplay loop muted playsinline poster="assets/video/dsi-effect-poster.jpg">
    <source src="assets/video/dsi-effect.mp4" type="video/mp4">
  </video>
  <figcaption>The XMB Wave background effect behind the DSi carousel on both screens (a real on-device capture, so the frame rate is low).</figcaption>
</figure>

- **DSi button legends.** X and Y prompts (Options, Sort, Pin, Info) sit in the top-screen corners, DSi style, in light and dark variants. See [Navigating](navigating.html).

    ![DSi top screen button legends](assets/img/shots/v143_dsi_button_legends.png){: .dual }

- **DSi launch effect plays to the end.** The tile lift, sparkle ring and white wash complete smoothly before the game appears, and the carousel comes back on the game you launched.

<figure class="ui-video-fig ar-43">
  <span class="ui-video-badge">Live demo</span>
  <video class="ui-video ar-43" autoplay loop muted playsinline poster="assets/video/dsi-launch-poster.jpg">
    <source src="assets/video/dsi-launch.mp4" type="video/mp4">
  </video>
  <figcaption>The DSi launch effect when starting a DS game.</figcaption>
</figure>

- **DSi settings as lists, and a faster DSi theme.** Game Settings and Theme Settings show as lists in the DSi theme, the scroll bar lands on the last card, and the DSi home holds 60 fps even in power saver mode.
- **Half Resolution for XMB.** **Half Resolution: Wave** and **Half Resolution: Clock** render just those parts at half size, so weaker GPUs keep a full frame rate while the menu text stays sharp.

    ![Half Resolution: Wave in XMB Theme Settings](assets/img/shots/v143_xmb_half_res_wave.png){: .wide }

- **Boot Sound, Menu Music and Show Battery Percent.** Turn the boot chime off in any theme, the DSi menu music on or off, and show the charge as a number in the DSi and Minima status bars.
- **Charging indicator.** The battery icon in every theme shows a lightning bolt while charging.
- **New confirmation toast.** Setting, sort and pin confirmations appear as a compact corner card, and slot into the XMB clock bar as frosted glass.

    ![Battery percent and the compact Setting changed card](assets/img/shots/v143_dsi_toast_battery_pct.png){: .dual }

- **Slide clock options.** In **Settings > Slide Behaviour**, **Freeze App Under Clock** pauses the game while the slide clock is up, and **Parallax**, **Parallax Strength** and **Parallax Direction** replace the old calibration field. See [Slide and Rotation](slide-rotation.html).

    ![Slide clock rows](assets/img/shots/v143_xmb_slide_clock_rows.png){: .wide }

- **Right-to-left languages.** Arabic and Hebrew render correctly everywhere, with over 800 translation fixes across all 14 languages.
- **Keyboard prompts on their own line.** The on-screen keyboard shows what a field wants above the text you type.

    ![Keyboard prompt on its own line](assets/img/shots/v143_osk_prompt_line.png){: .dual }

- **Minima dialogs page long text** with <span class="btnchip">L</span> and <span class="btnchip">R</span> instead of cutting it off.

## Game library

- **Show Display Names.** Games list and sort by their scraped or custom names by default instead of raw file names. See [Game Systems](game-systems.html).
- **Boxart Folder.** **Game Settings > Boxart Scraper > Boxart Folder** moves scraped covers and backgrounds to the SD card (or any folder). Existing art is moved over and follows the card at boot and when you reinsert it. See [Boxart](boxart.html).

    ![Boxart Folder row](assets/img/shots/v143_dsi_boxart_folder_row.png){: .dual }

- **Clear Boxart per system.** The Game Systems editor has a **Clear Boxart** action that deletes one system's downloaded covers and backgrounds.

    ![Clear Boxart confirmation](assets/img/shots/v143_dsi_clear_boxart_confirm.png){: .dual }

- **Your own PNG as a system icon.** Press <span class="btnchip">X</span> in the Game Systems icon grid to import any PNG or JPG. See [Custom Boxart](custom-boxart.html) for making your own art.

    ![Game Systems icon grid with Import PNG hint](assets/img/shots/v143_xmb_icon_grid.png){: .wide }

- **Manual system order sticks.** Reorder systems with <span class="btnchip">L1</span> / <span class="btnchip">R1</span> in the editor and that is the order the home shows.
- **Arcade systems stay separate.** Adding CPS1, FBNeo or MAME no longer pulls in every other arcade folder, and a system with chosen scan folders scans only those.
- **Arcade (Vertical).** Folders named VERTICAL, VARCADE, TATE or TateGame are added automatically as their own Arcade (Vertical) system with the FBNeo and MAME players. See [Adding Games](adding-games.html).
- **Search finds games in every system.** Global search now considers every match and shows the best 250, so games in systems added last show up too. See [Search](search.html).
- **Back to the right system after a game,** not the tile before it.
- **Box art reloads live** when the PC GammaOS Boxart Tool changes it, scraped names prefer the English title, and the screen stays on while scraping.

## Apps and home

- **Quick Resume is now a choice, off by default.** Turn it on in **Settings > Game Settings > Quick Resume** or from the Quick Menu. See [Quick Resume](quick-resume.html).

    ![Quick Resume row in Game Settings](assets/img/shots/v143_dsi_quick_resume_row.png){: .dual }

- **No more quick resume loop.** Holding <span class="btnchip">Back</span> after a resumed DS game always brings the home back, and two resumed sessions in a row with no button press make the next boot land on the home.
- **Home returns instantly after a DS game.** The home stays resident during a DraStic Nano session and is back in a fraction of a second.
- **Faster app launches on 1 GB devices.** RetroArch opens in about 6 seconds instead of up to 22, and Mupen64Plus AE launches straight into the game.
- **Lower idle CPU.** The DSi, Minima and ES-DE homes stop redrawing when nothing moves.
- **Mouse mode behaves.** Switching mouse mode on or off no longer relaunches or crashes the app, and if an app quits while mouse mode is on, the home switches it off so the d-pad works again. See [Gamepad Settings](gamepad-settings.html).
- **Landscape-only apps on portrait devices** such as PPSSPP and Flycast render upright and fill the panel.
- **Install apps from file managers and stores** without hunting for the per-app install toggle. See [Applications](applications.html).
- **Device sleeps after the Android Screen Timeout** you set, in the menu and on the boot intro.
- **System Information and System Update.** **Settings > System Settings > System Information** shows the GammaOS version and edition, Android version, build date and more. **System Update** only checks when you ask and explains the result in plain words. See [Settings Reference](settings-reference.html).

    ![System Update result in plain words](assets/img/shots/v143_dsi_system_update_uptodate.png){: .dual }

- **Video wallpapers on 1 GB devices** refuse clips above 720p so a wallpaper cannot drain memory.
- **Network category hidden on 1 GB devices.** Turn it back on in Home Categories if you need it.
- **Tidier Quick Settings.** The unused Immersive Mode and Analog Calibration tiles are gone.

## Media

See [Media](media.html) for the full player guide.

- **Embedded MKV subtitles.** The video player finds SubRip and ASS/SSA tracks inside MKV files and renders styled ASS subtitles with their positions, sizes and colours.

    ![Styled ASS subtitles](assets/img/shots/v143_video_ass_subtitles.png){: .wide }

- **Chapter previews in Scene Search,** pre-cached when a video opens.
- **Global Shaders from the video player.** Pick Off, CRT, LCD3x, LCD, Blur Fill or a custom shader without leaving the video.

    ![Global Shaders from the video player](assets/img/shots/v143_video_global_shaders.png){: .wide }

- **Large video files play reliably.** Seeking, chapter jumps and audio track switches on big MKV files no longer crash or desync.
- **Playlists everywhere.** Add, remove and reorder tracks, videos and photos in Playlists from the Options menu in any theme.
- **Headphone fixes.** Menu sounds survive a headphone plug, the volume overlay follows the real level, and the boot chime plays from the first second on the RG DS Plus speaker.

## DraStic Nano (DS emulation)

The full reference is on [DraStic Nano](drastic-nano.html), and the buttons on [DraStic Controls](controls-drastic.html).

- **No DraStic APK needed.** Everything DraStic Nano needs ships in the system image. Your saves live in `drastic-nano` on internal storage, with an offer to import old DraStic saves on first launch.
- **GPU 3D renderer (experimental).** The DS 3D scene can render on the GPU at hi-res, with DS-accurate blending, toon shading and shadows. In 1.4.3 its textures and shading match DraStic's own renderer on fine detail, and Mario and Luigi rooms render correctly.

    ![A DS racing game on the GPU 3D renderer](assets/img/shots/v143_drastic_gpu3d_mariokart.png){: .dual }

    ![Video page with GPU 3D Renderer](assets/img/shots/v143_drastic_ov_video_gpu3d.png){: .wide }

- **Low-latency audio.** Game audio delay drops from roughly 300 ms to a few tens of milliseconds, and the clicks and pops in heavy scenes are gone. Golden Sun speech and echo-heavy games such as Yoshi's Island DS sound as they do on hardware.
- **Low latency on headphones (RG DS Plus).** From 1.4.3 the low-latency audio also reaches the headphone jack on the RG DS Plus, not just the speakers.
- **Smoother frame pacing** in heavy scenes, and a low-latency display path on the RG DS and RG DS Plus.
- **Two FPS counters.** **BLIT** shows the present rate and **GAME** the real emulation rate.

    ![BLIT and GAME FPS counters](assets/img/shots/v143_drastic_fps_counters.png){: .dual }

- **Fast Forward Speed.** Cap fast-forward from 110% to 300% in steps of 10, or leave it Uncapped. Fast-forward is a press-to-toggle with an amber badge, and no longer corrupts or flickers.

    ![Fast Forward Speed set to Uncapped](assets/img/shots/v143_drastic_ov_ffspeed.png){: .wide }

- **Run-Ahead (experimental).** An optional one-frame run-ahead lets a press reach the screen sooner. It can now be on together with the GPU 3D renderer.
- **38 RetroArch LCD and CRT shaders** in the Shader row, adapted to any screen size.

    ![Shader row set to crt-lottes-fast](assets/img/shots/v143_drastic_ov_shader_row.png){: .wide }

- **Per-game settings.** **Create Per-Game Override** on the General page saves every setting for the current game, now including its Performance mode. Delete it and the global settings come back.

    ![Per-game override confirmation](assets/img/shots/v143_drastic_ov_pergame_confirm.png){: .dual }

- **Undo Quick Save and Undo Quick Load,** plus Quick Save and Quick Load right on the General page, and **DS Game Language**.
- **Save folders shown in the menu.** The Save States page names the folders your saves and save states go to. **DraStic Data Folder** moves them anywhere, including the SD card or a network share.

    ![Save States page naming the folders](assets/img/shots/v143_drastic_ov_savestates.png){: .wide }

- **Your own cheat files.** Drop R4 style `usrcheat.dat` files into `drastic-nano/cheats` (or the folder picked in **Game Settings > DraStic Cheats Folder**) and they merge with the built-in cheats. The Cheats page can filter Built-in and Custom, and <span class="btnchip">L2</span> / <span class="btnchip">R2</span> page long lists.

    ![Cheats page with the Cheat files row](assets/img/shots/v143_drastic_ov_cheats.png){: .wide }

- **Close Lid button.** A mappable **Close Lid** action toggles the DS hinge, and **Physical Lid Closes DS Lid** does it with the real lid.

    ![Close Lid binding row](assets/img/shots/v143_drastic_ov_closelid.png){: .wide }

- **RetroAchievements toggles** for the progress toast and challenge indicators.
- **A snappier menu.** The overlay opens without stalls, Power Off and Reboot ask for confirmation, every label is translated, the volume keys respond at once in heavy scenes, and a back-hold exit takes about 2 seconds with no screech.
- **Zipped ROMs** show a loading screen and keep their save states, and in-game brightness is remembered.

## Dual-screen devices and the Control Center

- **Control Center.** On the RG DS and RG DS Plus the bottom screen shows the Control Center while a single-screen game runs: brightness for each screen, quick tiles (Sleep Screen, Performance, Split Bright, Shader, Gamma EQ, Mouse, Screenshot, Wi-Fi), volume, temperatures and live CPU, GPU, power and RAM gauges. The CPU and GPU rings show the clock against the chip's top clock. See [Control Center](control-center.html).

    ![Control Center on the bottom screen](assets/img/shots/v143_cc_dashboard.png){: .dual }

- **Screen options.** Swipe to the third page for **Double Tap to Wake** and **Screen Timeout** for the bottom screen (also in [GammaOS Toolbox](gammaos-toolbox.html)).

    ![Control Center screen options](assets/img/shots/v143_cc_screen_options.png){: .wide }

- **Mouse tile** toggles GammaPad's virtual mouse with the pointer on the top screen, and brightness set on the Control Center slider is kept.
- **Layout rows hidden** in DraStic Nano on the RG DS and RG DS Plus, where each DS screen has its own panel.

## Gamepad and navigation

- **Faster list skipping.** <span class="btnchip">L1</span> / <span class="btnchip">R1</span> page in XMB and <span class="btnchip">L2</span> / <span class="btnchip">R2</span> jump to the ends; in DSi and Minima the shoulder buttons jump by initial letter. See [Navigating](navigating.html).
- **Trigger to axis while keeping the button.** GammaPad trigger-to-axis rules can send both the analog value and the original button.
- **Slide Launch Target picker.** Choose the app (and activity) the slide opens from a list, and a **Close App** action force-stops it. See [Slide and Rotation](slide-rotation.html).

    ![Slide Launch Target row](assets/img/shots/v143_xmb_slide_launch_target.png){: .wide }

## Network and Bluetooth

- **Syncthing built in.** Sync saves and folders with your PC or phone from **Settings > Network Shares > Syncthing**: add folders and devices, accept pending requests and optionally open the web interface to your network. See [Syncthing](syncthing.html).

    ![Syncthing running](assets/img/shots/v143_dsi_syncthing_running.png){: .dual }

- **Bluetooth stays off.** A fresh install starts with Bluetooth off, the setup wizard no longer has a Bluetooth step, and scanning no longer switches it back on. Turn it on from Bluetooth & Accessories or the Quick Menu. See [Connectivity](network.html).
- **Wi-Fi after sleep (RG DS Plus).** Wi-Fi now comes back about two seconds after waking instead of looking connected but loading nothing, which also fixes scraping that failed after a sleep.
- **SD card paths stay stable** when a card is ejected or remounted, and the USB File Transfer switch really changes between MTP and charge only. See [Network Shares](network-shares.html) for other ways to move files.

## System and settings

- **Setup wizard finishes by itself.** After configuration it counts down and moves on. On the RG DS Plus it now runs at 60 fps with a progress bar, centred screens and your language applied before the Wi-Fi step. See [Getting Started](getting-started.html).
- **Setup on battery (RG DS Plus).** A freshly flashed RG DS Plus no longer switches itself off part way through setup when no charger is connected.
- **Touch right after waking (RG DS Plus).** The touchscreen answers the first tap after waking from deep sleep, instead of ignoring taps for up to ten seconds.
- **Brightness remembered across boots,** with no flashes while the system starts.
- **First-boot setup on 1 GB devices** no longer runs out of memory and retries failed app installs, and setup is faster overall.
- **MTP transfers stay alive** for the whole copy.

## Full-Android and desktop mode

See [Desktop Mode Features](atv-desktop-features.html).

- **Syncthing** is also in Settings and TV Settings.
- **Auto-granted permissions** apply to frontends launched from a normal launcher and stick after store updates.
- **Secondary-display home** ships on the Lite and Full images.
- **Sharper dual-stack apps on the RG DS and RG DS Plus,** rendered at the panels' native 1024x1536.

## Fixed

- Settings screens (Network and Internet, Security, VPN, Wi-Fi Direct, credentials, Printing) no longer crash in nano, and apps using the Android keystore no longer crash.
- The framework follows the panel's real refresh rate instead of compositing at 30 Hz on 61 Hz panels.
- Large scraped and media libraries no longer lose covers, names and playlists.
- The home no longer crashes shortly after start on the RG DS Plus, and no longer comes back flipped after a DS session.
- Navigation sounds no longer take all audio down on the RK3568 handhelds, and menu sounds play after the setup wizard.
- Holding Back in RetroArch returns to the home instead of restarting the app, and stock DraStic no longer launches on wake.
- DraStic Nano cheats work again, a leftover exit request no longer quits the next game, and a factory-reset first launch no longer shows red panels.
- Touch in DS games works after pressing the d-pad, and rotated panels use the home's touch calibration.
- Leaving the video player in DSi or Minima stops the video and its audio.
- The Control Center Screenshot tile captures the game, not the Control Center.
- Quick Resume boots no longer hang, normal boots chime, and a stale overlay flag no longer wedges the home.
- The secondary panel is fully released during the setup wizard on dual-screen devices.
- DSi dark theme edges and scroll bar, clock contrast, stale values and missing checkboxes are fixed, and Minima glyphs stay readable on light accents.
- An XMB page skip plays one cursor sound instead of a clipping burst.
- The Slide On Key Up and Down dialogs have OK and Cancel, so ticked actions save.
- The hidden source controller no longer shows up next to the virtual pad after boot.
- Releasing a capped fast-forward no longer leaves heavy 3D scenes crawling, and the GPU 3D renderer and 4x supersampling apply with Threaded 3D off.
- Syncthing folders can be picked again from the Path row, and the Web Interface option really opens it to your network.

Still stuck? The [FAQ](faq.html#new-in-142-and-143) answers the most common questions about these releases.
