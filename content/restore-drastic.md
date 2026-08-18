---
title: Restore DraStic (RG DS)
group: Help
order: 3
icon: 🔧
desc: Reinstall DraStic Nano and its default configuration on the RG DS from a PC over ADB, and restore the DraStic system properties.
---

If DraStic on your RG DS stops launching, loses its configuration, or you just want to reset it to the
way it shipped, you can put back the exact app and default config that GammaOS installs on first boot,
plus the DraStic system properties, from a computer over ADB. This page is the end to end procedure.
{: .lead }

This restores the **DraStic app and its default config** (the files under the app's own data folder)
and the **DraStic properties**. It does **not** touch your games or saves: ROMs and save files on
internal storage (`/sdcard/ROMs`) are left alone.
{: .callout .note }

## What you need

- A computer with **ADB** installed and your RG DS connected over USB with **USB debugging** on. New
  to this? [ADB Setup and Logs](adb-and-logs.html) gets you set up in a couple of minutes.
- **Root ADB.** The steps write to protected system folders, so they run `adb root` first. This works
  on the standard GammaOS builds.

The files used below (`drastic_r2.6.0.4a.apk` and `drastic.tar.gz`) already live on the device in
`/system/etc`, so you do not need to download anything.
{: .callout .tip }

## Step 1: reinstall DraStic and its default config

Open a terminal or Command Prompt on your computer and run:

```bash
adb root
adb wait-for-device
adb shell 'pm install -r /system/etc/drastic_r2.6.0.4a.apk'
adb shell '
u=$(stat -c "%U" /data/data/com.dsemu.drastic)
g=$(stat -c "%G" /data/data/com.dsemu.drastic)
tar -xf /system/etc/drastic.tar.gz -C /
rm -f /data/data/com.dsemu.drastic/files/DraStic/shaders/SMAA.dfx /data/data/com.dsemu.drastic/files/DraStic/shaders/Scanline.dfx /data/data/com.dsemu.drastic/files/DraStic/shaders/scanline.dsd
rm -rf /data/data/com.dsemu.drastic/files/DraStic/shaders/smaa
chown -R $u:$g /data/data/com.dsemu.drastic
pm grant com.dsemu.drastic android.permission.RECORD_AUDIO
pm grant com.dsemu.drastic android.permission.BLUETOOTH_CONNECT
appops set --uid com.dsemu.drastic RECORD_AUDIO allow
'
```

What each part does:

- `pm install -r ...` installs (or reinstalls, keeping data) the DraStic APK.
- `tar -xf drastic.tar.gz -C /` unpacks the default DraStic configuration into the app's data folder.
- The two `rm` lines remove the SMAA and Scanline shaders. SMAA forces a desktop GLSL path that does
  not exist on the Mali GPU, so DraStic crashes if it is selected; Scanline is unwanted. GammaOS ships
  without them, and this prunes any left over from an older install.
- `chown -R` gives the unpacked files back to DraStic (a tar extract lands them as `root`, and DraStic
  cannot read its own data until the owner is fixed).
- `pm grant` and `appops set` restore the microphone and Bluetooth permissions DraStic expects.

If `pm install` reports that the file does not exist, your build may ship a different DraStic version.
Find the exact name with `adb shell 'ls /system/etc/drastic_*.apk'` and use that path.
{: .callout .note }

## Step 2: restore the DraStic properties

These are the DraStic-related system properties GammaOS sets on the RG DS. They persist across reboots.

```bash
adb root
adb shell '
setprop persist.gammaos.nano.drastic_nano 1
setprop persist.gammaos.nano.triple_buffer 1
setprop persist.gammaos.nano.vsync 1
setprop persist.gammaos.ultra_low_power_saving_freeze_exclude_packages com.dsemu.drastic
'
adb reboot
```

| Property | Value | What it does |
|----------|-------|--------------|
| `persist.gammaos.nano.drastic_nano` | `1` | Turns on DraStic Nano, the built-in DraStic front end and overlay. |
| `persist.gammaos.nano.triple_buffer` | `1` | Quick Resume smoothness: enables the 4-slot buffer ring that hides short GPU stalls. Defaults to on in code; set here to lock it. |
| `persist.gammaos.nano.vsync` | `1` | Quick Resume smoothness: paces rendering to the display flip on the RG DS dual-screen setup. Defaults to on in code; set here to lock it. |
| `persist.gammaos.ultra_low_power_saving_freeze_exclude_packages` | `com.dsemu.drastic` | Keeps DraStic running under the ultra-low-power saving mode instead of freezing it. |

DraStic Nano runs as a GammaOS Nano overlay, so it also relies on the Nano overlay being enabled
(`persist.gammaos.nano.overlay=1`), which is the default on the RG DS.
{: .callout .note }

## Step 3: verify

After the reboot:

- Open DraStic from the Applications category (or launch a DS game) and confirm it starts and plays.
- Confirm the properties took, if you want to double check:

```bash
adb shell getprop persist.gammaos.nano.drastic_nano
adb shell getprop persist.gammaos.ultra_low_power_saving_freeze_exclude_packages
```

## Full reset (optional)

Step 1 keeps any files you added to DraStic's own data folder. To wipe DraStic's internal data back to
a completely clean state first, uninstall it before Step 1:

```bash
adb root
adb shell 'pm uninstall com.dsemu.drastic'
```

Then run Step 1 and Step 2 as above. Your ROMs and save files on `/sdcard/ROMs` are not affected by
the uninstall, but any DraStic settings, cheats, or save states kept inside the app's own data folder
are removed and replaced with the defaults.
{: .callout .note }

## Troubleshooting

- **`adb root` says it cannot run as root.** Make sure the device is actually running GammaOS, not
  stock firmware. See [ADB Setup and Logs](adb-and-logs.html).
- **DraStic installs but has no sound or cannot record.** Re-run the `pm grant` and `appops` lines from
  Step 1; the microphone permission is what DraStic uses for the DS microphone.
- **DraStic starts then closes when you pick a shader.** An old SMAA or Scanline shader is still
  present. Re-run the two `rm` lines from Step 1.
- **DraStic will not launch after a restore.** Confirm ownership was fixed:
  `adb shell 'ls -ld /data/data/com.dsemu.drastic'` should show the DraStic app user, not `root`.
  Re-run the `chown -R` line from Step 1 if it shows `root`.

## Related pages

- [DraStic Nano](drastic-nano.html)
- [DraStic Nano Controls](controls-drastic.html)
- [ADB Setup and Logs](adb-and-logs.html)
