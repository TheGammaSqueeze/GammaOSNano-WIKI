---
title: Installing GammaOS
group: Get Started
order: 3
icon: 💾
desc: Choosing an SD card, the flashing tools that work, and getting a fresh install to boot.
---

GammaOS ships as a per-device image that you write to your device's storage, usually an SD card. This page covers picking a card, which flashing tools work (and which to avoid), and what to do when a fresh install will not boot. Exact steps differ by handheld, so always follow the [device install guides on the GammaOS Next wiki](https://github.com/TheGammaSqueeze/GammaOSNext/wiki/GammaOS-Next-Installation) for your model.
{: .lead }

## Pick the right SD card

On many handhelds, especially the A133P devices like the TrimUI Brick and the MagicX Zero 28, GammaOS boots directly from the SD card, so the card is the whole system and its speed matters.

- Use an **A2**-rated card where possible for the best performance and load times.
- An **A1** card works fine, but expect slower loading and longer waits.
- Stick to good-quality, known-brand cards. If a card will not boot at all, try a different one; some large cards have been reported not to boot on certain devices.

Once GammaOS is installed on a device that boots from SD, do not put that card back into a PC to copy games onto it. The card holds an encrypted Android partition layout, so your computer will not show your usable storage. That is expected. Transfer files with MTP, [ADB Explorer](https://github.com/Alex4SSB/ADB-Explorer) or a network share instead. See [How do I transfer ROMs and files onto my device?](faq.html) for the details.
{: .callout .warn }

## Write the image with a reliable tool

Use a tool that writes the image exactly as-is:

- **Raspberry Pi Imager** or **Rufus** (choose the write-image / DD option) are known-good.
- **Avoid Balena Etcher, Ventoy and Etchdroid.** These have been reported to leave GammaOS hanging on the boot logo. If you flashed with one of these and the device sticks on the logo, re-flash with one of the tools above.
- If you flash on a Rockchip device with an RKImage or RK flasher, run it on a real Windows or Linux machine, not inside a virtual machine. The card often will not format correctly in a VM.
- Some SteamOS-based Linux distributions can interfere with the boot partition. A standard Windows or Linux host is the safer choice.

## Device-specific steps

Flashing differs from one handheld to the next: the partitions, drivers and any extra patches are not the same across devices, so the most important step is to follow the install guide for your exact model. These live on the GammaOS Next wiki:

- [GammaOS Next Installation](https://github.com/TheGammaSqueeze/GammaOSNext/wiki/GammaOS-Next-Installation) is the main install guide and the place to start.
- [Installation for Allwinner SD-Card Devices](https://github.com/TheGammaSqueeze/GammaOSNext/wiki/GammaOS-Next-Installation-for-Allwinner-SD-Card-Devices) covers the A133P SD-boot handhelds, such as the TrimUI Brick and MagicX Zero 28.
- [Installation Guide for the Anbernic RG557, RG477M and RG477V](https://github.com/TheGammaSqueeze/GammaOSNext/wiki/GammaOS-Installation-Guide-for-Anbernic-RG557,-RG477M,-and-RG477V-%28SP-Flash-Tool,-Full-and-Lite-Builds%29) is a device-specific example using SP Flash Tool.

Some devices need extra care while flashing, such as powering fully off and removing every SD card and USB drive first so the device does not try to boot from the wrong place. Always defer to your device's own guide over any general advice here.
{: .callout .note }

## First boot

The first boot after a flash takes longer than usual while the system sets itself up, and the device may reboot once on its own. Give it a few minutes.

If it stays stuck on the boot logo on the very first try, the flash is the usual culprit: re-flash with Raspberry Pi Imager or Rufus (see above) rather than Balena Etcher, and make sure you used a good card.

Once it boots, head to [Getting Started](getting-started.html) to finish setup, connect Wi-Fi and add your first games. Not sure which build to install? See the editions rundown in [What Is GammaOS Nano?](what-is-nano.html).

## Related pages

- [GammaOS Next install guides (wiki)](https://github.com/TheGammaSqueeze/GammaOSNext/wiki/GammaOS-Next-Installation)
- [Getting Started](getting-started.html)
- [What Is GammaOS Nano?](what-is-nano.html)
- [FAQ and Troubleshooting](faq.html)
