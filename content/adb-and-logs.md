---
title: ADB Setup and Logs
group: Help
order: 2
icon: 🧰
desc: Install ADB on Windows, macOS or Linux, connect your handheld, and collect logs (logcat, dmesg, bugreport) for support.
---

**ADB** (Android Debug Bridge) is a small program for your computer that talks to your handheld over USB. You need it to use PC tools like the [GammaOS Boxart Tool](custom-boxart.html), and, most usefully, to **collect logs** when something goes wrong so a developer can see what happened. This page sets it up from scratch on any computer, then shows exactly what to run to grab the logs.
{: .lead }

You do not need the whole Android SDK. Pick the option for your computer below, and you are done in a couple of minutes.

## Install ADB

### Windows (easiest)

Use **ADB & Fastboot++**, a tiny installer that sets up the latest `adb` and `fastboot` and, importantly, installs the **USB driver** Windows needs to see your device.

1. Download it from the [ADB & Fastboot++ Releases page](https://github.com/K3V1991/ADB-and-FastbootPlusPlus/releases) (grab the latest **Installer**).
2. Run it. When asked, tick **Add to System Path Environment** and, if you are not sure your device has a driver, tick the **Universal ADB Driver** option too.
3. Finish. Now `adb` works from any Command Prompt or PowerShell window.

That is the whole Windows setup. It also comes with a **Toolkit** that can create a bugreport with one click (see the logs section below).
{: .callout .tip }

### macOS (easiest)

If you have [Homebrew](https://brew.sh/) (a popular Mac package manager), open **Terminal** and run:

```bash
brew install android-platform-tools
```

That installs `adb` and puts it on your PATH. No Homebrew? Use [the official download](#the-official-download-any-computer) below.

### Linux (easiest)

Install it from your distribution's package manager in a terminal:

```bash
# Debian / Ubuntu / Linux Mint / SteamOS
sudo apt install adb

# Fedora
sudo dnf install android-tools

# Arch / Manjaro
sudo pacman -S android-tools
```

That is it: `adb` is now on your PATH.

### The official download (any computer)

If the options above do not fit, Google publishes just `adb` and `fastboot` (no SDK) for every system. This always works.

1. Open the [SDK Platform Tools page](https://developer.android.com/tools/releases/platform-tools) and download the zip for your OS (or use a direct link: [Windows](https://dl.google.com/android/repository/platform-tools-latest-windows.zip), [macOS](https://dl.google.com/android/repository/platform-tools-latest-darwin.zip), [Linux](https://dl.google.com/android/repository/platform-tools-latest-linux.zip)).
2. Unzip it somewhere you can find, for example your Desktop. You get a `platform-tools` folder with `adb` inside.
3. Open a terminal or Command Prompt **inside that folder** and run the commands as `./adb ...` (macOS/Linux) or `adb ...` (Windows). On Windows you can also add that folder to your PATH so `adb` works everywhere.

On macOS the first run may be blocked ("cannot be opened because Apple cannot check it"). Right-click `adb` in Finder and choose **Open** once to allow it.
{: .callout .note }

## Connect your handheld

1. On the device, make sure **USB debugging** is on. On most GammaOS builds it already is. If your PC does not see the device, enable it in **Settings > Developer Options > USB debugging** (in desktop mode you get the full Android Settings; if Developer Options is hidden, open Settings > About and tap **Build Number** seven times to reveal it).
2. Plug the handheld into the computer with a **data** USB cable (some cables are charge-only and will not work).
3. Open a terminal (macOS/Linux) or Command Prompt / PowerShell (Windows) and run:

```bash
adb devices
```

The first time, the handheld shows an **Allow USB debugging?** prompt. Tick "Always allow" and accept it, then run `adb devices` again. You should see a line with your device's serial and the word `device`. If it says `unauthorized`, you missed the prompt; reconnect and accept it.

## Collect logs for support

When you report a problem, logs are what let a developer actually diagnose it. The steps are the same on every computer; only the folder you start in differs.

First, open your terminal in a folder where the files will be easy to find, so everything saves to your Desktop:

```bash
# macOS / Linux
cd ~/Desktop

# Windows (Command Prompt)
cd %USERPROFILE%\Desktop
```

Then run these. The single most useful one is the **bugreport**, so start there:

```bash
adb bugreport bugreport.zip          # everything at once (best single file to send)
adb logcat -d > logcat.txt           # the Android log (app + system)
adb shell getprop > getprop.txt      # device + build properties
adb root                             # switch to root so the kernel log is readable
adb shell dmesg > dmesg.txt          # the kernel log (crashes, drivers, power)
```

- **bugreport.zip** is a full snapshot and usually all a developer needs.
- **logcat.txt** captures what GammaOS Nano and Android printed. If you can, reproduce the problem and then grab the log right after, so the failure is near the end.
- **dmesg.txt** is the kernel side (freezes, USB, power, reboots). It needs root, which `adb root` provides on GammaOS (a normal Android phone would refuse this).

If the device is **stuck or will not reach the home screen**, you can often still run `adb devices` and the commands above while it is stuck; that log is exactly what pins down a boot problem.
{: .callout .tip }

Finally, share the files: put `bugreport.zip`, `logcat.txt` and `dmesg.txt` together (zip them if needed) and attach them where you were asked, or send them to the developer.

On Windows, ADB & Fastboot++ makes this even easier: its **Toolkit** has a **Create Bugreport** button that saves the report straight to your Desktop, no typing required.
{: .callout .note }

### Handy extras

```bash
adb logcat -d | findstr GammaOS      # Windows: only GammaOS lines
adb logcat -d | grep GammaOS         # macOS / Linux: only GammaOS lines
adb reboot                           # reboot the device
adb shell getprop ro.gammaos.device  # your device codename
```

## FAQ and troubleshooting

### `adb devices` shows nothing / my device is not listed

- Use a **data** USB cable and a different USB port (front-panel and hub ports are less reliable).
- Make sure **USB debugging** is on (see above).
- **Windows:** install the driver. The ADB & Fastboot++ installer includes the Universal ADB Driver; tick that option, or install it from the Toolkit.
- macOS and Linux normally need no driver.

### It says `unauthorized`

You did not accept the **Allow USB debugging** prompt on the handheld. Reconnect the cable, watch the device screen, and tick "Always allow". If no prompt appears, go to Developer Options, choose **Revoke USB debugging authorizations**, and reconnect.

### Windows says `'adb' is not recognized`

`adb` is not on your PATH. Re-run the ADB & Fastboot++ installer and tick **Add to System Path Environment**, or open the Command Prompt inside the folder that contains `adb.exe` and run it from there.

### `adb root` says it cannot run as root

That message means the build does not allow root. GammaOS builds do, so make sure the device is actually running GammaOS and not stock firmware. You still get `logcat` and `bugreport` without root; only `dmesg` needs it.

### macOS will not open adb

Right-click `adb` in Finder and choose **Open** the first time, or run `xattr -d com.apple.quarantine adb` in the folder, then try again.

## Related pages

- [GammaOS Boxart Tool](custom-boxart.html) uses ADB to manage your covers.
- [FAQ and Troubleshooting](faq.html) for in-device fixes.
- [Wi-Fi and Bluetooth](network.html) and [Network Shares](network-shares.html) for wireless file transfer.
