---
title: Wallpapers & Theme Settings
group: The Interface
order: 5
icon: 🖼️
desc: Set a photo or looping video wallpaper, darken it with a scrim, and tune the home look.
---

Beyond the three home themes, Theme Settings is where you make the home your own: a still photo or a looping video wallpaper, a dimming scrim so bright art does not drown the menu, accent colour, fonts, and more. It all lives under Settings > Theme Settings.
{: .lead }

![Theme Settings](assets/img/shots/xmb_themesettings.png)

For the three home looks themselves (XMB, DSi, Minima), see [Home Themes](themes.html). This page focuses on wallpapers and the finer appearance controls.

## The wallpaper rows

![The wallpaper rows in Theme Settings](assets/img/shots/xmb_wallpaper_rows.png)

| Row | What it does |
|-----|--------------|
| **Wallpaper Image** | Pick a photo as the home background, chosen from a picker grid |
| **Bottom Wallpaper** | A separate wallpaper for the bottom screen (dual-screen devices only) |
| **Video Wallpaper** | Pick a looping video as the top-screen background |
| **Clear Wallpaper** | Remove the custom wallpaper and bring back the moving wave |
| **Wallpaper Dimming** | Darken a photo or video wallpaper so icons and text stay readable |
| **XMB Wave** | Show or hide the PS3 wave (auto-off when a wallpaper is set) |

## Setting a video wallpaper

A looping video makes a lively, console-like backdrop. Here is the whole flow.

1. Go to **Settings > Theme Settings > Video Wallpaper**.
2. Nano scans your videos and shows them in a picker. Choose the one you want.

![The Video Wallpaper picker](assets/img/shots/xmb_videowallpaper_picker.png)

3. Select it, and it starts playing behind the home right away, looping quietly.

<figure class="ui-video-fig">
  <span class="ui-video-badge">Live demo</span>
  <video class="ui-video" autoplay loop muted playsinline poster="assets/video/video-wallpaper-poster.jpg">
    <source src="assets/video/video-wallpaper.mp4" type="video/mp4">
  </video>
  <figcaption>A looping video wallpaper playing live behind the XMB home.</figcaption>
</figure>

Put the videos you want to use in your Movies folder so the picker can find them. The XMB wave switches off automatically when a wallpaper is set, so the video shows cleanly.
{: .callout .note }

## The darkened scrim (Wallpaper Dimming)

A bright or busy wallpaper can make the menu text and icons hard to read. **Wallpaper Dimming** lays a dark scrim over the wallpaper to fix that. Higher values make it darker. The range is 0 to 70 percent, and the default is a gentle 25 percent. You can push it much higher for a moody, high-contrast look where the menu really pops.

![Adjustable wallpaper dimming](assets/img/shots/wn_wallpaper_dimming.png)

<figure class="ui-video-fig">
  <span class="ui-video-badge">Live demo</span>
  <video class="ui-video" autoplay loop muted playsinline poster="assets/video/scrim-poster.jpg">
    <source src="assets/video/scrim.mp4" type="video/mp4">
  </video>
  <figcaption>Raising Wallpaper Dimming darkens the scrim so the menu stays readable.</figcaption>
</figure>

Wallpaper Dimming only affects a custom photo or video wallpaper. With no wallpaper set (just the wave), it does nothing.
{: .callout .tip }

## Removing a wallpaper

Choose **Clear Wallpaper** to drop the custom image or video on both screens and bring back the moving wave. If you would rather keep a wallpaper but see the wave too, turn **XMB Wave** back on.

## Font Size

**Font Size** scales the UI text live across all three themes (XMB, DSi and Minima). As you change it the text resizes immediately, and word-wrapped paragraphs reflow so nothing runs off the edge. Bump it up for readability on a small panel or across the room, or down to fit more on screen.

![Font scaling across themes](assets/img/shots/wn_font_size_setting.png)

Font Size lives here in Theme Settings, not in the [GammaOS Toolbox](gammaos-toolbox.html), in case you go looking for it there.
{: .callout .note }

## Home Categories editor

**Home Categories** lets you tidy the home to just the columns you use. You can hide categories you never open, reorder the ones you keep, and even drill into a category to hide individual rows inside it. Changes save straight away and apply live.

On-screen controls:

| Button | What it does |
|--------|--------------|
| <span class="btnchip">X</span> | Hide or show the highlighted category |
| <span class="btnchip">L1</span> / <span class="btnchip">R1</span> | Move the highlighted category up or down the order |
| <span class="btnchip">A</span> | Drill into a category to hide or show its individual rows |
| <span class="btnchip">B</span> | Back out and save |

![Home Categories editor](assets/img/shots/wn_home_categories_editor.png)

A few rules keep the home usable:

- **Quick Menu always stays first** and cannot be moved out of place.
- **Settings cannot be hidden**, so you can always get back into the menus.
- **At least one category must stay visible.** Nano will not let you hide the very last one.

The same on-screen legend is shown on the editor screen itself, so you never have to guess the controls.

## Rows adapt to your theme

Theme Settings only shows the rows that apply to the theme you are using, so the menu stays short and relevant. Options that belong to a theme you are not currently running are hidden until you switch to it.

## Other appearance controls

Theme Settings also holds:

- **Colour**: the accent colour, with 21 choices (see [Home Themes](themes.html)). It now recolours the DSi chrome too.
- **Background** and **Font**: overall background style and font look.
- **Day/Night**: the XMB lighting blend.
- **Background Colour**: a solid colour for the Minima home (Minima only).
- **XMB Wave**: also available in Minima as an opt-in alternative to the plain black canvas; the choice persists (Minima only).
- **Bottom Clock** and **Bottom Clock FPS**: the PSP-style clock on dual-screen devices.
- **Home Theme**: switch between XMB, DSi, and Minima (this restarts the home).

### DSi-only rows

With the DSi theme active you also get:

- **Dark Theme**: flip the whole DSi look to light-on-dark, live (see [Home Themes](themes.html)).
- **Dual Screen**: choose **Auto**, **Top+Bottom**, or **Carousel-Only** for how the two DSi screens are laid out.
- **Screen Gap**: tune the spacing between the stacked screens on portrait panels.

![DSi dual-screen settings](assets/img/shots/wn_dsi_dualscreen_settings.png)

On single-screen 4:3 DSi layouts, a top **status bar** reserves space for the clock, Wi-Fi, Bluetooth and date.

![DSi single-screen status bar](assets/img/shots/wn_dsi_statusbar.png)

## The wizard and HUD follow your theme

The first-run setup wizard and the on-screen HUDs now render in whichever theme is active. Scraper progress and the setup wizard show the Minima or DSi look when you use those themes, and the brightness and volume HUD popups match the active theme too.

## Where to go next

- [Home Themes](themes.html) for the three looks in detail.
- [Settings Reference](settings-reference.html) for the whole Settings tree.
