# MuseScore Layer (Layer 11)

One-handed MuseScore 4 control while the right hand operates a MIDI keyboard for pitch input.

## Activation

- **Entry:** `&tog 11` on F-row (position 3, where skedpal_inbox was)
- **Exit:** Any key on right hand triggers `&tog 11`, or same F-row key

## Layout (Left Hand Only)

### Home Row (6th key + A–G)

| Position | Function | Macro/Key |
|----------|----------|-----------|
| 6th (leftmost) | Puntillo (dot) | `&kp DOT` |
| A | Semicorchea (16th) | `&kp N3` |
| S | Corchea (8th) | `&kp N4` |
| D | Negra (quarter) | `&kp N5` |
| F | Blanca (half) | `&kp N6` |
| G | Redonda (whole) | `&kp N7` |

### Row Above Home (Q–T positions)

| Position | Function | Macro |
|----------|----------|-------|
| Q | Slur | `&ms_slur` |
| W | Halve duration | `&ms_halve` |
| E | Double duration | `&ms_double` |
| R | Repeat selection | `&ms_repeat` |
| T | Tie | `&ms_tie` |

### Row Below Home (Z–B positions)

| Position | Function | Macro |
|----------|----------|-------|
| Z | Cut | `&ms_cut` |
| X | Undo | `&ms_undo` |
| C | Redo | `&ms_redo` |
| V | Copy | `&ms_copy` |
| B | Paste | `&ms_paste` |
| (next) | Triplet | `&ms_triplet` |

### Number Row (non-premium)

| Position | Function | Macro |
|----------|----------|-------|
| 1 | Save | `&ms_save` |
| 2 | Flip direction | `&ms_flip` |
| 3 | Enharmonic respell | `&ms_enhar` |
| 4 | Octave up | `&ms_oct_up` |
| 5 | Octave down | `&ms_oct_dn` |

### Bottom Row (non-premium)

| Position | Function | Macro |
|----------|----------|-------|
| 1 | Grace note | `&ms_grace` |
| 2 | Accent | `&ms_accent` |
| 3 | Staccato | `&ms_stacc` |

### Thumbs

| Position | Function | Key |
|----------|----------|-----|
| Thumb 1 | Esc | `&kp ESC` |
| Thumb 2 | Delete | `&kp DEL` |
| Thumb 3 | Add bar | `&ms_add_bar` |
| Thumb 4 | Rest | `&kp N0` |
| Thumb 5 | Play/Stop | `&kp SPACE` |
| Thumb 6 | Toggle note input | `&kp N` |

### Right Hand

- All keys: `&tog 11` (any keypress exits layer)
- Exceptions: corner keys remain `&trans` (consistent with other layers)

## Macros

| Macro | Keys Sent | Description |
|-------|-----------|-------------|
| `ms_undo` | `Ctrl+Z` | Undo |
| `ms_redo` | `Ctrl+Shift+Z` | Redo |
| `ms_copy` | `Ctrl+C` | Copy |
| `ms_paste` | `Ctrl+V` | Paste |
| `ms_cut` | `Ctrl+X` | Cut |
| `ms_triplet` | `Ctrl+3` | Create triplet |
| `ms_add_bar` | `Ctrl+B` | Add bar/measure |
| `ms_save` | `Ctrl+S` | Save |
| `ms_flip` | `X` | Flip stem/direction |
| `ms_enhar` | `J` | Enharmonic respell |
| `ms_oct_up` | `Ctrl+↑` | Octave up |
| `ms_oct_dn` | `Ctrl+↓` | Octave down |
| `ms_grace` | `/` | Grace note (acciaccatura) |
| `ms_accent` | `Shift+V` | Accent articulation |
| `ms_stacc` | `Shift+S` | Staccato articulation |
| `ms_slur` | `S` | Slur |
| `ms_tie` | `T` | Tie |
| `ms_repeat` | `R` | Repeat selection |
| `ms_halve` | `Q` | Halve duration |
| `ms_double` | `W` | Double duration |

## Notes

- Delete and Backspace are identical in MuseScore; only `Del` is needed
- Right hand exits layer on any keypress (user's right hand is on MIDI keyboard)
- Activation changed from combo (Z+X+C) to direct toggle on F-row for easier access
