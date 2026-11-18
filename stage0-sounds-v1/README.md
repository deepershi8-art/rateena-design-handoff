# RATEENA SOUND, Stage 0 UI sounds v1

Original UI sounds, synthesized from scratch (no samples, no third-party audio). `synth.py` regenerates them exactly.

| File | Length | Intended trigger | Character |
|---|---|---|---|
| `tap-A` (default) | 65 ms | Tap on a chapter in the bottom strip | Soft felt click with a warm 620 Hz body |
| `tap-B` | 70 ms | Alternative to tap-A | Small, darker wooden block knock |
| `next-A` (default) | 380 ms | Chapter change (swipe, arrow, or strip) | Soft two-note gold chime, E5 then B5, short room |
| `next-B` | 320 ms | Alternative to next-A | Gentle airy swish rising upward, with a faint glint |
| `toggle` | 40 ms | Small UI tick (for example a mute or on/off switch) | Tiny, crisp tick |

## Formats
- `wav/`: masters, 48 kHz, 24-bit, mono, peak -6 dBFS, no DC offset, faded edges.
- `web/`: MP3 128 kbps and OGG Vorbis of each sound, for the web or app.
- `PREVIEW-all.mp3`: each sound three times with gaps, in this order: tap A, tap B, next A, next B, toggle.

## Suggested use
- Playback gain about 0.35 (quiet and subtle).
- Play only after the first user gesture (no autoplay).
- Default variants are A. Swap to B by changing the file name.
