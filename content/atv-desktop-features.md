---
title: Desktop Mode Features
group: Settings
order: 6
icon: 🖥️
desc: What you get when you boot GammaOS into normal Android (desktop and TV mode) instead of the Nano launcher.
---

GammaOS can boot straight into the Nano launcher or into normal Android (desktop and TV mode). Desktop mode is the full Android experience with a launcher, a status bar and a notification shade, and it is where you install and manage apps that expect a normal phone or tablet environment. This page covers the features that only apply in desktop mode. For the Nano launcher itself, see [What Is GammaOS Nano](what-is-nano.html) and [What's New since 1.4](what-s-new-since-1-4.html).
{: .lead }

## Switching between Nano and desktop mode

Nano and desktop mode are two boot targets on the same system. Switching is controlled by a single setting, so your games, saves and apps stay in place either way. When you switch to desktop mode the device boots to a normal Android home screen with a status bar and an app drawer instead of the XMB, DSi or Minima launcher.

The quickest way to switch is the power menu: from Nano, choose **Boot into Android**, and from Android, open the power menu and choose **Boot to Nano**. Because it is the same system underneath, this is a fast round trip, so you can pop into full Android for a native app, a browser or the Play Store, then drop back into Nano for games and media. Setting up Google services with microG is one common reason to boot into Android; see [Applications](applications.html#google-apps-and-the-play-store).

## Custom notification shade (TvGammaShade)

Desktop mode ships a purpose built notification shade that works with a controller and on screens that do not have a touch digitizer.

- **Paged Quick Settings tiles** for the common toggles, laid out so you can move through them with a d-pad.
- **Brightness and volume sliders** right in the shade. On devices with two panels and split brightness enabled, you get a separate brightness slider per panel.
- **Live notifications** that grow and update in place.
- **Swipe up to dismiss** that follows your finger on touch panels, and a controller friendly close.

Open and close the shade with the **ALL_APPS** key on your controller or keyboard.

## Full Android Settings app

Desktop mode now ships the complete Android Settings app rather than the cut down TV Settings. The Settings dashboard also surfaces **GammaOS Toolbox** and shortcuts to the hardware control apps, so the device specific options sit alongside the standard Android ones. See the [Settings Reference](settings-reference.html) and [GammaOS Toolbox](gammaos-toolbox.html) for what each option does.

## Screen orientation in normal Android

A **GammaOS > Screen Orientation** screen lets you set Auto, Landscape or Portrait (with clamping) for normal Android, and the choice persists between Nano and desktop mode. On the RG Rotate the hardware slider is respected in normal Android too, so rotating the panel rotates the desktop as expected. For the Nano side of rotation and the slide clock, see [Slide and Rotate Clock](slide-rotation.html).

## Dual-screen home and per-app primary screen

On dual-screen devices desktop mode keeps a launcher on both displays, so each screen has its own home. Apps that are built for two screens (such as Cocoon Shell) can be set to **Run on Primary Screen**, and the system shows an auto-detect prompt the first time it sees such an app. When one of these apps takes over the bottom panel, the Control Center yields the bottom panel to it so the two do not fight over the same screen. The matching per-app toggle in the Nano launcher is covered in [Applications](applications.html).

## Per-display volume

Volume can be set per physical display, so a dual-screen device can run the two panels at different levels. The per-display sliders live in the shade described above.

## Boot reliability

Two fixes make desktop mode start cleanly:

- The panel no longer blanks for several seconds partway through boot.
- The locked boot home resolves correctly, so a fresh boot into normal Android reaches the home screen instead of hanging before the launcher appears.
