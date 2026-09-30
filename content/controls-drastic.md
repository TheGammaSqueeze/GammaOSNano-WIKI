---
title: DraStic Nano Controls
group: Controls
order: 3
icon: 🖊️
desc: In-game controls for the built-in Nintendo DS emulator.
---

Nintendo DS games launch through DraStic Nano, the DS emulator built right into GammaOS. The controls are refreshingly simple: your DS buttons map straight across, and everything else runs off the Back button.
{: .lead }

## Playing a DS game

The DS buttons map one-to-one to your handheld's face buttons, D-Pad, shoulders, and Start/Select: Up, Down, Left, Right, <span class="btnchip">A</span>, <span class="btnchip">B</span>, <span class="btnchip">X</span>, <span class="btnchip">Y</span>, <span class="btnchip">L</span>, <span class="btnchip">R</span>, <span class="btnchip">Start</span>, and <span class="btnchip">Select</span>.

The DS bottom (touch) screen is driven by your touch panel, so you can tap and drag with a finger like a stylus. On devices without a touch panel, or when you prefer buttons, a virtual touch cursor lets the D-Pad or left stick move a pointer over the bottom screen, with <span class="btnchip">A</span> tapping or holding the stylus.

Touch works the moment the device wakes from sleep, and keeps working after you press the D-Pad. Controllers you connect after the game has started are picked up too.

## In-game shortcuts

| Input | Action |
|-------|--------|
| <span class="btnchip">Back</span> (short press) | Open or close the in-game menu (the game pauses while it is open) |
| <span class="btnchip">Back</span> (hold) | Exit the game and return to the Nano home. The sound mutes at once and the home is back in about 2 seconds, on the system you launched from. |
| <span class="btnchip">R2</span> (default) | Fast forward on or off |
| <span class="btnchip">L2</span> (default) | Swap the two DS screens |
| <span class="btnchip">R3</span> (default) | Virtual touch cursor on or off |
| <span class="btnchip">Power</span> (tap) | Sleep the device |
| <span class="btnchip">Power</span> (hold, about 1.5 seconds) | Open the DraStic in-game menu, the same menu as a short Back press |
| <span class="btnchip">Power</span> (hold, about 5 seconds) | Save your place and power off |
| Touch panel | Acts as the DS stylus on the bottom screen |
| Virtual touch cursor | D-Pad or left stick moves a cursor over the bottom screen; <span class="btnchip">A</span> taps or holds the stylus |

A short tap of <span class="btnchip">Back</span> opens the menu (and pauses the game); a hold of <span class="btnchip">Back</span> exits to the home. Same button, two lengths of press.
{: .callout .tip }

Powering off from the in-game menu (or with the long Power hold) saves your spot first, and with [Quick Resume](quick-resume.html) turned on the next boot drops you straight back into the game.
{: .callout .note }

## Fast forward

Fast forward is a **press-to-toggle**: press the Fast Forward button once to speed up and once more to go back to normal speed. You do not have to hold it. While it is on, an amber **>>** badge sits in the top-left corner so you always know, and your other buttons keep responding normally.

How fast it goes is set by **Fast Forward Speed** on the menu's **Video** page: 110% to 300% of normal speed, or Uncapped. See [Fast forward](drastic-nano.html#fast-forward).

## The in-game menu

A short <span class="btnchip">Back</span> press opens the in-game menu, which pauses the game. Use <span class="btnchip">L</span> and <span class="btnchip">R</span> to switch between its pages (General, Save States, Video, Audio, Controls, Cheats, Achievements), Up and Down to move, <span class="btnchip">A</span> to select, Left or Right to change a value, and <span class="btnchip">B</span> to close it.

- **General** is where the menu opens: Brightness, **Quick Save** and **Quick Load** (slot 0), **Undo Quick Save** and **Undo Quick Load** when there is something to undo, Performance, DS Game Language, Restart Game, Exit Game, per-game overrides, Power Off and Reboot.
- **Power Off** and **Reboot** ask you to confirm first, so a stray press cannot switch the device off.
- On the **Cheats** page, <span class="btnchip">L2</span> and <span class="btnchip">R2</span> page up and down through long cheat lists.

For every setting in the menu (screen layout, shaders, GPU 3D, save states, cheats, achievements, and more), see the full [DraStic Nano](drastic-nano.html) page.

## Changing the controls

Every binding lives on the menu's **Controls** page. Select an action with <span class="btnchip">A</span>, then press the button you want for it: any button on your pad can be used, including the stick clicks (<span class="btnchip">L3</span> and <span class="btnchip">R3</span>) and the triggers. Press Left on a row to clear its binding, or choose **Restore Defaults** to start over.

The bindable actions are the DS buttons and D-Pad, plus these extras:

| Action | Default | What it does |
|--------|---------|--------------|
| **Screen Swap** | <span class="btnchip">L2</span> | Swap the top and bottom screens |
| **Fast Forward** | <span class="btnchip">R2</span> | Toggle fast forward |
| **Menu** | <span class="btnchip">Back</span> | Open the in-game menu |
| **Touch Cursor** | <span class="btnchip">R3</span> | Toggle the virtual touch cursor |
| **Save State** | Unmapped | Quick-save to slot 0, even with the menu closed |
| **Load State** | Unmapped | Quick-load slot 0, even with the menu closed |
| **Close Lid** | Unmapped | Close or open the emulated DS lid, for games that react to it |

Binding a key to one action automatically clears it from any other action, so you cannot accidentally leave the same button doing two things.
{: .callout .tip }

A quick save or load you did not mean can be taken back: open the menu and use **Undo Quick Save** or **Undo Quick Load** on the General page.
{: .callout .note }

The Controls page also has **Physical Lid Closes DS Lid** for devices with a real lid: when it is on, shutting the lid briefly pauses the game instead of sleeping the device straight away. See [Close Lid](drastic-nano.html#close-lid).

## Where to go next

- Full DraStic Nano settings and features: [DraStic Nano](drastic-nano.html)
- Pick up exactly where you left off after a reboot: [Quick Resume](quick-resume.html)
- System-wide shortcuts (brightness, sleep, emergency restart): [Controls](controls-os.html)
- Everything added recently: [What's New since 1.4.1](what-s-new-since-1-4-1.html)
