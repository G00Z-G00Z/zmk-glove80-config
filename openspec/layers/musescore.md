# MuseScore Layer (Layer 11)

One-handed MuseScore 4 control while the right hand operates a MIDI keyboard for pitch input.

## Activation

- **Entry:** Combo from base layer — three keys, bottom-left cluster (Z+X+C equivalent positions), with `require-prior-idle-ms` to avoid accidental trigger
- **Exit:** `tog 11` on right-hand corner keys, or same combo from base

## Layout (Left Hand Only)

### Home Row (A–G + 6th key)

| Key | Function | MuseScore Shortcut |
|-----|----------|--------------------|
| A   | Semicorchea (16th) | `3` |
| S   | Corchea (8th) | `4` |
| D   | Negra (quarter) | `5` |
| F   | Blanca (half) | `6` |
| G   | Redonda (whole) | `7` |
| 6th | Puntillo (dot) | `.` |

### Row Above Home (Q–T)

| Key | Function | MuseScore Shortcut |
|-----|----------|--------------------|
| Q   | Halve duration | `Q` |
| W   | Double duration | `W` |
| E   | Copy | `Ctrl+C` (macro) |
| R   | Repeat selection | `R` |
| T   | Tie | `T` |

### Row Below Home (Z–V)

| Key | Function | MuseScore Shortcut |
|-----|----------|--------------------|
| Z   | Undo | `Ctrl+Z` (macro) |
| X   | Redo | `Ctrl+Shift+Z` (macro) |
| C   | Play/Stop | `Space` |
| V   | Paste | `Ctrl+V` (macro) |

### Additional Left-Hand Keys

| Key | Function | MuseScore Shortcut |
|-----|----------|--------------------|
| B   | Triplet | `Ctrl+3` (macro) |
| N   | Toggle note input | `N` |
| Other | Cut | `Ctrl+X` (macro) |
| Other | Slur | `S` |
| Other | Enharmonic respell | `J` |
| Other | Flip direction | `X` |

### Thumbs (4 positions)

| Position | Function | MuseScore Shortcut |
|----------|----------|--------------------|
| Thumb 1  | Esc (exit note input mode) | `Esc` |
| Thumb 2  | Delete → rest | `Del` |
| Thumb 3  | Rest | `0` |
| Thumb 4  | Add bar | `Ctrl+B` (macro) |

### Right Hand

- `&trans` on all keys (pass-through to base layer)
- Right-hand corner keys: `tog 11` to exit layer

## Priority Reference

| Priority | Keys |
|----------|------|
| 5 — always | Durations (A–G), dot, rest (Thumb 3), delete (Thumb 2), undo (Z), halve/double (Q/W) |
| 4 — almost always | Redo (X), copy (E), paste (V) |
| 3 — sometimes | Tie (T), play (C), add bar (Thumb 4), repeat (R), toggle note input (N), Esc (Thumb 1) |
| 2 — rarely | Triplet (B) |
| 1 — nice to have | Slur, enharmonic respell (J), flip direction (X) |

## Macros Required

| Macro | Keys Sent |
|-------|-----------|
| `ms_undo` | `Ctrl+Z` |
| `ms_redo` | `Ctrl+Shift+Z` |
| `ms_copy` | `Ctrl+C` |
| `ms_paste` | `Ctrl+V` |
| `ms_cut` | `Ctrl+X` |
| `ms_triplet` | `Ctrl+3` |
| `ms_add_bar` | `Ctrl+B` |

## Dependencies

- ZMK `behavior-macro` (simple, one key-combo per macro)
- ZMK `combos` with layer filter on base layer + `require-prior-idle-ms`
- `update-max-combo.py` — auto-updates combo count in `glove80.conf`

## Notes

- Delete and Backspace are identical in MuseScore; only `Del` is needed
- All shortcuts emit a single keypress from the user's perspective (macros handle multi-key combos internally)
- Right-hand pass-through is intentional: base layer shortcuts remain available if needed
