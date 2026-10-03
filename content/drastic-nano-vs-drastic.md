---
title: DraStic Nano vs DraStic
group: Emulators
order: 3
icon: 🔬
desc: "Every difference between DraStic Nano and the stock DraStic app: the emulation, audio, microphone, 3D and pacing fixes injected into the core, with the games they were found in."
---

DraStic Nano runs the same DraStic emulation core as the DraStic app (r2.6.0.4a), but it hosts that core in its own player and corrects it while it runs. This page lists what is different from playing in the stock DraStic app: the bugs in the core that are fixed, what was added around it, and what was deliberately left alone. Each entry names the game the problem was found in, so you can see what it looks or sounds like.
{: .lead }

For how to use DraStic Nano itself (the menu, layouts, saves and every option), see [DraStic Nano](drastic-nano.html). This page is about what changes under the hood.
{: .callout .note }

## How DraStic Nano runs the DraStic core

The DraStic app is an Android app: a Java front end that loads the emulation library and draws through Android's normal display path. DraStic Nano keeps the library and replaces everything around it.

- **No app needed.** The DraStic library, BIOS files, firmware, game database and default shaders ship inside GammaOS. DraStic Nano loads the library directly into its own process and answers the few calls it expects from its Java side itself, so the core runs exactly as it would inside the app without the app being installed.
- **Drawn straight to the panels.** On the RG DS and RG DS Plus the two DS screens go to the two panels directly, without Android's compositor in between. Single-screen devices use a normal Android surface.
- **Fixes are applied in memory.** When a game starts, DraStic Nano patches the loaded copy of the core: single instructions changed, or short detours that call corrected code and return. The library file on the system is never modified, and every patch checks that the code it replaces is exactly what it expects before writing, so it never patches the wrong thing.
- **Checked against melonDS and real hardware.** Most fixes below were found by running the same save state in melonDS (a highly accurate DS emulator) and comparing the output frame by frame or sample by sample. The microphone work was checked against a real DS Lite recorded at the same moment, using test ROMs written for the purpose.

## Emulation accuracy fixes

These are bugs in the DraStic core itself. The stock DraStic app has all of them.

### Pokemon Ranger: top screen panels drift off position

On a real DS, some display registers can be written but not read back, and reading them returns zero. These include the background scroll positions, the rotation and scaling settings, the window sizes, mosaic, the brightness fade and the main memory display FIFO. DraStic returned whatever value was last written to them.

Pokemon Ranger slides the panels on its top screen by reading a scroll register back, adding an offset and writing the result, on every scanline. On DraStic each write built on the one before, so after every slide the panels kept the leftover: the header went off the top of the screen, the map and the text boxes shifted, and the layout changed again with every press of Start.

DraStic Nano makes those registers read as zero on both screens, exactly like the hardware and melonDS. The check costs nothing measurable. A check across 18 other games found that none of them read those registers in the scenes tested, so nothing else changes.

### Hotel Dusk: backdrops bob and characters flicker

The DS takes the 3D rendering settings for the next frame (the DISP3DCNT register, which controls things like alpha blending) at the very start of the vertical blank. DraStic read them later in the frame, after the game had already written the value meant for the frame after. Every frame was rendered with its neighbour's settings.

Hotel Dusk changes this register every frame and draws its top screen in two alternating passes. With the settings one frame off, one pass lost its alpha blending: the backdrop bobbed up and down, the character portrait flickered between old and new frames, and the head crossfade after loading a state jumped back. DraStic Nano captures the settings at the start of the vertical blank, as the DS does, at the cost of one memory read and write per frame. Verified frame by frame against melonDS.

### Hotel Dusk with Hi-res 3D: crash after loading a state

With Hi-res 3D on, DraStic keeps a high resolution copy of every captured video memory bank, but its capture code assumes the capture is the full 256 pixels wide. A small 128x128 capture that ends at the end of a bank wrote its last line 256 bytes past the end of that buffer, and Hotel Dusk crashed on the first frame after a state load. DraStic Nano gives that buffer enough room for the worst case.

### The DS birthday reaches games one month late

DraStic's firmware builder adds one to the birthday month, so a birthday set as January 28 reaches games as February 28. The DraStic app has the same bug. DraStic Nano corrects it, so games see the date you set. This was found with a test ROM that reads back exactly what a game sees of the system settings.

## Sound fixes

### Golden Sun Dark Dawn speech, and DS reverb and echo

Some DS games build reverb or stream speech by recording the console's own audio output back into memory (the SPU capture units) and playing it again. The DS moves the recording and the playback one sample at a time. DraStic moves both in blocks, so the playback regularly read memory the recording had cleared but not yet refilled.

In Golden Sun Dark Dawn this turned the voiced speech scratchy: 137 dropouts of up to 9 ms in one scene where melonDS has none. The same technique is behind the reverb in Animal Crossing, Mario Kart DS, Kirby Super Star Ultra, Lufia, the Boktai ports and the Need for Speed games.

DraStic Nano fixes this in three steps:
- **The capture rings are repaired.** Before each mix the gaps are bridged, and the real data is put back afterwards, because the game's own echo code reads it. Golden Sun's dropouts went from 137 to 9 threshold-grazing pairs.
- **The DS sound routing is emulated.** The console's SOUNDCNT register decides which channels reach the speaker and which only feed the capture. DraStic Nano now reads it from the game, so Golden Sun's echo comes from the capture ring the way the DS does it.
- **Speech samples are interpolated smoothly.** They are read with a 4-tap interpolation instead of nearest neighbour, which removes a grinding sound while keeping the highs.

The result matches melonDS to within about a decibel up to 12 kHz. Games that do not use capture keep DraStic's own audio path and CPU cost.

### Yoshi's Island DS: the pipe sound loops forever

Yoshi's Island DS plays its sound through both capture units in 8-bit mode as a cave echo. DraStic's 8-bit capture added every new sample on top of the old one even in the normal overwrite mode, so each lap of the ring summed onto the last. The echo never decayed, drifted and clipped, and was heard as the pipe sound looping forever, with a click every 93 ms and the music buried underneath. Fixed, together with the 8-bit ring length. The game's cave music now matches melonDS: overall level within 0.2 dB, every frequency band within 1.6 dB, and the echo delay 92.6 against 93.1 ms.

### Crackles in heavy scenes

DraStic's mixer turns the emulated CPU time since its last call into audio samples. A frame that ends a little late mixes 736 samples and the next one 734, but the output always advanced by 735. So every short frame left one stale sample behind, and every long frame lost one.

On Golden Sun Dark Dawn this was heard as bursts of clicks about a minute into a busy scene, and the clicks lined up exactly with runs of those uneven frames. DraStic Nano evens every frame out to exactly 735 samples, carrying any surplus over to the next frame and padding a small shortfall.

### Pops after an underrun, and a click every few seconds

- **Pops after an underrun.** DraStic counts its queued audio buffers, including the silent filler it adds after an underrun, so after each underrun the count was one short. It then overfilled the queue, and a whole 33 ms chunk was rejected and lost, heard as a pop. DraStic Nano re-reads the real queue depth before every submit.
- **A click every six seconds.** The audio is produced for exactly 60 frames a second, while the panels refresh slightly slower (59.83 Hz on the RG DS family), so the queue slowly filled up and DraStic dropped a whole chunk about every six seconds. DraStic Nano resamples the stream continuously to match the real output rate.
- **Smaller audio steps.** DraStic's four 67 ms output buffers are split into eight 33 ms buffers in the same memory: the same total buffering and latency, half the step.
- **State loads.** The output is filled ahead of a state load, so a load no longer leaves a gap.

### Low latency audio

The DraStic app plays through Android's normal audio mixer, about 300 ms behind the game. Where the hardware supports it, DraStic Nano plays through an exclusive low latency stream instead: a few tens of milliseconds on the RG DS Plus and RG DS. It falls back to DraStic's own player on hardware without a low latency path, and re-applies the GammaEQ speaker tuning, which the low latency path would otherwise skip.

### Smaller sound fixes

- **No screech when exiting.** The output stops the instant you ask to leave, so nothing the emulator emits while it saves and shuts down reaches the speaker.
- **The volume keys respond at once.** In a heavy scene the volume moves within a few milliseconds of the press instead of up to a second later.

## Microphone fixes

The DS microphone in DraStic chops, repeats, distorts and is too quiet for speech recognition. All of this was measured against a DS Lite recorded at the same moment, with a test ROM written to record, play back and analyse microphone input on any emulator or console.

- **Repeated and missing audio.** DraStic hands the game the next of its five recording buffers whether or not that buffer has been refilled. Whenever the emulator ran slightly ahead of the microphone, the game heard audio from 83.6 ms earlier: about a quarter of a loud recording was exact copies of earlier sound, with holes of room noise in the middle of words. DraStic Nano feeds the game from its own queue, in order, and absorbs the small clock difference smoothly.
- **Distortion.** DraStic squares every sample, which crushes quiet speech and clips anything over half volume. DraStic Nano uses a straight, linear response.
- **The game's gain was ignored.** A DS game sets its microphone amplifier to 20x, 40x, 80x or 160x, and its speech recognition is tuned for that level. DraStic ignores it and applies one fixed level: Brain Age sets 160x and heard the voice at less than 60 percent of the level a DS Lite delivers. DraStic Nano follows the game's setting, calibrated against the DS Lite. Mic Level becomes a trim on top: 0 (the default, which Brain Age's colour test responds to best) is half, 1 is the hardware level and 2 is double.
- **The sample count.** The game reads exactly 737.13 microphone samples per DS frame, and it now gets exactly that.

## 3D and video

### GPU 3D renderer

The DraStic app draws the DS 3D scene on the CPU only. DraStic Nano adds a GPU renderer (experimental, off by default) that reads DraStic's own polygon and texture data and draws it on the GPU, at native resolution or Hi-res 3D, with optional 4x supersampling. It was built to match DraStic's CPU renderer, and each rule below was checked pixel by pixel against it:

- **How the DS draws, rule by rule:** the DS blending rules, toon and highlight shading, fog, stencil shadows drawn in the DS's own order, the depth rules for coplanar and decal polygons, and the DS rule that a translucent polygon never draws over itself.
- **Mario Kart DS:** the kart shadow is solid and holds its shape as the kart turns.
- **Pokemon White 2:** the pond, soil and grass show correctly in town, the floor shadows appear, and the round cushion no longer vanishes as you walk.
- **GTA Chinatown Wars:** the clouds and haze match the CPU renderer.
- **Mario and Luigi Bowser's Inside Story:** its rooms keep about 130 textures in use at once, so the texture store grows to hold them instead of drawing white floors.
- **Crash of the Titans:** textures are sampled along each row the way DraStic does, so the ferns and flowers use the same texels as the CPU renderer on 97 to 99 percent of their pixels. The colours follow DraStic's own rounding, so lit surfaces are no longer one to four levels darker.

If the GPU renderer cannot keep up with a scene, DraStic Nano drops back to the CPU renderer for the rest of the session rather than stutter.

### Faster CPU rendering

- **Threaded 3D overlaps with the emulation.** The DraStic app renders 3D in parallel too, but DraStic Nano splits each frame into bands and starts drawing as soon as each band's geometry is ready. It produces exactly the same frames as rendering with threading off. This also fixes a crash with 3D edge marking on.
- **A faster 2D blend.** DraStic's two-layer colour blending loop, about 7 percent of the core's time, runs as a vector (NEON) routine instead. It is bit-exact against the original over every possible input and cuts the emulation thread's CPU use by 7.6 percent.

### Shaders

- **38 more shaders.** DraStic Nano ships faithful ports of 38 RetroArch LCD and CRT shaders, such as crt-lottes-fast, zfast-crt and lcd-grid. Their patterns are tied to the DS pixel grid, so Hi-res 3D never doubles the scanlines or the LCD grid.
- **SMAA removed.** DraStic's SMAA shader needs desktop OpenGL features that phone GPUs do not have. Selecting it crashed the emulator, so it has been removed. The Scanline shader was removed too.

## Frame pacing and fast-forward

### Steady 60 fps on the real panel refresh

DraStic paces itself at exactly 60.00 frames a second, but the RG DS panels refresh at about 59.83 Hz. The two drifted through a full cycle every 5.7 seconds, and each time several frames in a row landed a refresh late: the periodic micro stutter on Pokemon White 2's title screen. DraStic Nano locks the emulator to the panels' real refresh instead. A frame that runs long is caught up rather than dropped, which used to cost a frame and 16.7 ms of audio each time.

Measured on Pokemon White 2's title screen: the frame rate low went from 53 to 54 fps up to 57 to 59 fps, with no pacing misses and no audio underruns in steady play.

### Fast-forward

- **No garbage or flicker in games that show their own screen captures.** Under fast-forward DraStic still captures the screen on frames it skips drawing, so it captures an unrendered picture. Pokemon White 2's screen transitions became a grey field with bands. Golden Sun Dark Dawn, which renders on one frame and shows the capture on the next, flickered black every other frame. DraStic Nano decides frame by frame which frames to render so captures always hold a real picture.
- **Any speed you choose.** DraStic's limiter only offers six fixed speeds. DraStic Nano can cap fast-forward anywhere from 110 to 300 percent, or leave it uncapped. Every frame is still emulated in full at a capped speed.
- **No slow motion afterwards.** After a capped fast-forward, the limiter's timing was left pointing the wrong way. On HeartGold and the Pokemon Diamond title screen, heavy scenes then ran at about 17 fps until the next fast-forward. Fixed.
- **No flicker after returning to normal speed.** In Golden Sun's capture scenes, the top screen strobed between the two DS screens after a fast-forward ended. Fixed.
- **Buttons keep working.** Fast-forward no longer takes all the processor time from the threads that read the controls, so you can always turn it off again.

### Run-Ahead

Run-Ahead is new and experimental, and off by default. It replays the last frame with your new input before the next one is shown, so on Sonic Rush a press reaches the screen one frame after it instead of three. It uses fast in-memory save states and only runs when the frame still fits before the screen refresh, so it never repeats a frame. Two DraStic bugs that it exposed are fixed:
- The 3D command buffer could be left inconsistent after a state load and crash the emulator.
- A state load reset the frame timer, so games ran fast while you mashed buttons.

## Stability fixes

- **Crashes from the core's error handling.** DraStic jumps back to a recovery point when certain errors happen. Outside its own app it could reach that jump before the recovery point existed, and crashed within seconds of starting. Those paths are made safe. The catch is that DraStic's built-in soft reset relies on the same jump, so **Restart Game** does a clean relaunch of the game instead.
- **Switching shaders.** Freeing the old shader's GPU resources triggered a double free, inside DraStic or the GPU driver, and crashed on the second switch. DraStic Nano leaves those few kilobytes allocated instead.
- **The 1 GB handhelds.** Large ROMs (up to 512 MB for DSi-enhanced games like Pokemon White 2) are read from storage on demand, as in the DraStic app, rather than pinned in memory. The emulator's own code is kept in memory so it never has to be re-read from the SD card mid-game, and the GPU renderer only allocates the texture memory a game actually uses.

## What DraStic Nano adds

These have no equivalent in the DraStic app, or work differently:

| Feature | In DraStic Nano |
|---|---|
| Per-game settings | Any setting can be kept for one game only, including its performance mode. |
| Undo quick save and quick load | A wrong hotkey press can be undone from the menu. |
| RetroAchievements | Built in (Softcore), reading the DS memory directly. |
| Your own cheat files | R4 style `usrcheat.dat` files are merged with the built-in cheats. |
| Fast Forward Speed | Any speed from 110 to 300 percent, or uncapped. |
| Run-Ahead | One frame, adaptive (experimental). |
| GPU 3D renderer | Optional, with 4x supersampling (experimental). |
| Low latency audio and display | An exclusive audio stream, and a direct dual-panel path on the RG DS family. |
| Two FPS counters | BLIT (what reaches the screen) and GAME (what the DS core produces). |
| Quick Resume | Boots straight back into your last game. |
| Screen layouts | Presets, picture-in-picture, rotation and fine tuning for single-screen devices. |
| Close Lid | A mappable button, and an option to close the DS lid with the device's own lid. |
| Save folder anywhere | Saves, save states and shaders can live on internal storage, the SD card or a network share. |

## What stays the same

- **The core.** It is the same DraStic r2.6.0.4a emulation as the app. Everything not listed here behaves exactly as it does in the app.
- **Save files and save states.** These are the same DraStic `.dsv` and `.dss` formats. The first launch offers to import your DraStic app saves and settings.
- **Settings.** The System settings (nickname, birthday, language, colour, Slot-2 and clock) match DraStic's own page and are imported from it once.
- **Cheats.** The same cheat database is used.

## Turning a fix off

For comparisons and bug reports, the main fixes can be switched off from a computer over ADB, one at a time. These are for testing only; every fix is on by default. Properties starting with `sys.` are read when a game starts, so set them before you launch it.

| Fix | Property | Off value |
|---|---|---|
| Write-only display registers read as zero (Pokemon Ranger) | `sys.gammaos.drastic_nano.io_wo_zero` | `0` |
| 3D settings captured at vblank (Hotel Dusk) | `sys.gammaos.drastic_nano.disp3d_latch` | `0` |
| Capture ring repair (Golden Sun speech, reverb) | `persist.gammaos.drastic_nano.ring_repair` | `0` |
| DS sound routing for capture games | `persist.gammaos.drastic_nano.hw_route` | `0` |
| Microphone fixes | `persist.gammaos.drastic_nano.mic_fix` | `0` |
| Audio clock match | `persist.gammaos.drastic_nano.clock_match` | `0` |
| Low latency audio stream | `persist.gammaos.drastic_nano.audio_aaudio` | `0` |
| Pacing at the panel refresh in heavy scenes | `persist.gammaos.drastic_nano.bypass_panel_rate` | `0` |
| Fast-forward capture repair | `persist.gammaos.drastic_nano.ff_capfix` | `0` |
| NEON 2D blend | `persist.gammaos.drastic_nano.lerp_neon` | `0` |

## Related pages

- [DraStic Nano](drastic-nano.html): the complete guide to the player and its menu.
- [DraStic controls](controls-drastic.html): the default buttons.
- [Quick Resume](quick-resume.html): booting straight back into a game.
