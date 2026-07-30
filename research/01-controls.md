# Research brief: OS + Nano control scheme (code-verified)

## Gamepad buttons in the Nano UI

| Button | Home menu | Game / media list | On-Screen Keyboard (OSK) |
|--------|-----------|-------------------|--------------------------|
| D-Pad Up | Move up; cycle prev sort in photo/music | Move up a row (hold = accelerating scroll) | Cursor up |
| D-Pad Down | Move down | Move down a row (hold = accelerating scroll) | Cursor down |
| D-Pad Left | Move left across XMB categories | Horizontal XMB nav | Cursor left |
| D-Pad Right | Move right across XMB categories | Horizontal XMB nav | Cursor right |
| A (BTN_SOUTH) | Confirm / launch selected item | Launch game or open submenu | Submit query / password |
| B (BTN_EAST) | Back / exit submenu / close modal | Back one level | Close OSK |
| X (BTN_NORTH) | Open the Options (Triangle) menu | Open the Options menu | Backspace |
| Y (BTN_WEST) | Cycle Sort By; Music: cycle visualizer; Photo: 2D/3D | Cycle Sort By | (unused) |
| L1 (BTN_TL) | Toggle XMB/text mode; reorder system up | Page-skip back 10 items; prev photo/track | Toggle Shift (ABC/abc/symbols) |
| R1 (BTN_TR) | Toggle Quick Resume; reorder system down | Page-skip forward 10 items; next photo/track | Toggle symbols mode |
| L2 / R2 | Not mapped in the menu | Not mapped | Not mapped |
| Select (BTN_SELECT) | Open global Search; cycle OSK language | Close search; toggle photo info / video OSD | Cycle language |
| Start (BTN_START) | Submit OSK; setup-wizard nav | Play/pause slideshow or video | Submit query |

Notes:
- Hold-to-accelerate scroll: 300 ms initial delay, 200 ms base repeat, accelerates x1.4 down to a 50 ms floor. The DSi carousel root uses a steady 250/150 ms cadence and only accelerates once you drill into a list.
- L1/R1 do a 10-item page-skip when you are inside a drilled game or media list (very handy in big libraries). At the home level they reorder systems or toggle XMB/Quick-Resume.
- On the "X removes item" special lists (custom Game Systems, music/photo/video folders), pressing Y removes the highlighted entry.
- Analog stick and HAT are treated the same as the D-Pad (edge-triggered at ~90% throw, then repeat).

## OS-level global shortcuts

These are handled by the framework (PhoneWindowManager) and work everywhere on these handhelds.

| Shortcut | What it does |
|----------|--------------|
| **Select + Volume Up** | Increase screen brightness |
| **Select + Volume Down** | Decrease screen brightness |
| Volume Up / Down alone | System volume |
| **Power (short press)** | Sleep / wake (blanks the panel, drops to powersave) |
| **Power (long press, ~1.5 s)** | Open the Power menu (Restart / Power Off / Recovery) |
| **Power + Select (held)** | Emergency: disable the system display shader (escape hatch when a shader makes the screen unreadable) |
| **Hold Back 10 s** or **hold the Guide/Mode button 10 s** | Emergency restart of a frozen/dead home screen |
| Lid / hall / slide switch | Sleep on close (on devices with one) |

Brightness detail: the combo only fires while Select is genuinely held (validated against the live kernel key state to avoid a "stuck" modifier). If BACK is held longer than 6 seconds the state self-clears. Brightness applies to the default display and is clamped to the panel's min/max.

## RetroArch menu and exit (in-game)

Inside RetroArch, GammaOS drives the menu with the **Back** button (no hotkey-modifier combo; this is the Back button specifically, not Select):
- **Tap Back once** -> opens the RetroArch menu (GammaOS injects F1).
- **Hold Back** -> exits RetroArch back to the Nano home (GammaOS injects Quit/ESC). Same hold-to-exit works for DraStic.
- **L3 + R3** (click both sticks) -> also opens the RetroArch menu (RetroArch's native combo).

This is the RetroArch Back Button Override behavior (GammaOS Toolbox). Only active while RetroArch/DraStic is foreground.

## Touch support

The whole Nano UI is touch-capable where a touch panel exists:
- Tap a row to select + activate; tap a carousel tile to launch (DSi); tap side tiles to select.
- Drag to scroll lists and fling the DSi carousel (snap-to-slot).
- Drag slider tracks; tap dialog Yes/No/OK; tap the dimmed scrim to cancel; swipe paginated dialogs left/right.
- Panel calibration props correct rotated/flipped panels: `persist.gammaos.nano.osk_touch_swap` / `_flipx` / `_flipy`.

## USB mouse support

| Input | Action |
|-------|--------|
| Move | Moves an on-screen cursor (self-hiding) |
| Wheel up / down | Scroll the list up / down |
| Left click | Tap at the cursor |
| Right click | Back |
| Middle click | Open the Options (Triangle) menu |

## USB keyboard support (US layout)

| Key | Action |
|-----|--------|
| Arrow keys | D-Pad navigation (with hold-repeat) |
| Enter / Keypad Enter | Confirm (A) / submit OSK |
| Esc | Back |
| Tab | Open the Options (Triangle) menu |
| Letters / numbers / punctuation | Type into the OSK |
| Shift | Uppercase / symbols |
| Backspace | Delete a character |

## Test/automation hook (for reference, not for end users)

`setprop sys.gammaos.nano.nav <token>` injects navigation for testing: `up`, `down`, `left`, `right`, `enter`, `back`, `tri` (options), `sq` (sort/visualizer), `l1`, `r1`, `x`, `search`, `search:<query>`, `type:<text>`, `submit`, `powermenu`, `boottouch`, `bootreplay`.
