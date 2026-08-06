---
title: Wi-Fi & Bluetooth
group: Connectivity
order: 1
icon: 📶
desc: Connect Wi-Fi and Bluetooth with the setup wizard.
---

Getting online lets you scrape boxart, stream Internet Radio and IPTV, browse network servers, and download updates. GammaOS Nano keeps Wi-Fi and Bluetooth together in one friendly place.
{: .lead }

You will find everything under **Settings > Network Settings**.

## Check your connection

Network Settings opens with a connection status list showing your current SSID, IP address, and signal strength. This is the quickest way to confirm you are online and see which network you are on.

You can turn networking on or off here too, with the **Internet Connection** toggle.

## Connect with the wizard

Choose **Internet Connection Settings** to open the Wi-Fi and Bluetooth setup wizard. It walks you through:

1. Picking your Wi-Fi network (SSID) from the list of nearby networks.
2. Entering your WPA2 password.
3. Pairing a Bluetooth device.

This is the same wizard you meet during first-time setup, so if you skipped Wi-Fi back then you can finish the job here. See [Getting started](getting-started.html) for the first-boot walkthrough.

The wizard no longer blanks out after idle time and now renders in the Minima theme as well as XMB and DSi. As you type a Wi-Fi password it is shown in the clear so you can check it before you connect, and networks whose names contain spaces connect correctly.

![Show Wi-Fi password in clear](assets/img/shots/wn_wifi_show_password.png)

### If Wi-Fi is off

If you open the network list with the radio turned off, the wizard shows a clear prompt to turn Wi-Fi on rather than an empty list. Turn it on and the scan runs.

![Wi-Fi radio-off prompt](assets/img/shots/wn_wifi_radio_off.png)

### Change or forget a network

- **Change Password** on a saved network applies the new password directly.
- **Forget** properly removes a saved network so the device stops reconnecting to it.

## Bluetooth

Bluetooth pairing lives in the same wizard, and the Bluetooth and Accessories screen shows the on/off toggle even when Bluetooth is currently off, so you can turn it back on without hunting for it.

![Bluetooth toggle in System Settings](assets/img/shots/wn_bt_toggle.png)

Device scanning uses native discovery, so nearby devices appear reliably. An already-paired device can be re-registered, and pairing codes are shown clearly so you can confirm them on both ends. Scanning, pairing and connecting all have real timeouts (Bluetooth pairing waits up to 80 seconds), so a slow accessory no longer leaves the screen hanging.

![BT register/pairing codes](assets/img/shots/wn_bt_register.png)

## Test your connection

Use **Internet Connection Test** to confirm your handheld can actually reach the internet after connecting. It is a handy check if a download or scrape is not working as expected.

If a boxart scrape or an online media browser fails, run the Internet Connection Test first to rule out a dropped connection.
{: .callout .note }

## Status at a glance

The HUD top bar shows your **Wi-Fi signal** and **Bluetooth status** at all times, so you can keep an eye on connectivity without opening Settings.

A resident system bridge pushes live Wi-Fi and Bluetooth state to the HUD and reads the settings-screen lists straight from framework data instead of parsing shell output, so the indicators and the network and device lists stay accurate and update quickly.

![Live Wi-Fi/BT HUD](assets/img/shots/wn_network_hud.png)

On single-screen 4:3 DSi layouts, a top status bar reserves space for the clock, Wi-Fi, Bluetooth and date, so the same connectivity indicators are visible in the DSi theme.

![DSi single-screen status bar](assets/img/shots/wn_dsi_statusbar.png)

## Next steps

Once you are online, you can mount SMB, NFS, WebDAV, and FTP shares so files on another computer or NAS appear as if they were local. Head to [Network Shares](network-shares.html) to set those up.
