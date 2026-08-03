# Mouse Layer

Full mouse control via keyboard. Layer index: **9**.

## Activation

- **Combo ZXC** (positions 47+48+49): hold = momentary (layer 9 while held), tap = toggle on/off
- Available from base layer (0) and mouse layer (9)
- Uses existing `layer_mo_tog` hold-tap behavior
- `require-prior-idle-ms = 300` to prevent accidental triggers

> ⚠️ **BLE Re-Pair Required**: Adding `CONFIG_ZMK_POINTING=y` changes the HID descriptor. After flashing, re-pair the keyboard with every BLE host.

## Layout

### Right Hand — Cursor Movement (HJKL vim-style)

| Key | Position | Binding | Action |
|-----|----------|---------|--------|
| H | 40 | `&mmv MOVE_LEFT` | Move cursor left |
| J | 41 | `&mmv MOVE_DOWN` | Move cursor down |
| K | 42 | `&mmv MOVE_UP` | Move cursor up |
| L | 43 | `&mmv MOVE_RIGHT` | Move cursor right |

### Right Hand — Scroll

| Key | Position | Binding | Action |
|-----|----------|---------|--------|
| Y | 28 | `&msc SCRL_UP` | Scroll up |
| U | 29 | `&msc SCRL_LEFT` | Scroll left |
| O | 31 | `&msc SCRL_DOWN` | Scroll down |
| ; | 44 | `&msc SCRL_RIGHT` | Scroll right |

### Left Hand — Mouse Buttons

| Key | Position | Binding | Action |
|-----|----------|---------|--------|
| F | 38 | `&mkp LCLK` | Left click |
| D | 37 | `&mkp RCLK` | Right click |
| S | 36 | `&mkp MCLK` | Middle click |

All other positions: `&trans` (pass through to lower layer).

## Firmware Requirements

- `config/glove80.conf`: `CONFIG_ZMK_POINTING=y`
- `config/glove80.keymap`: `#include <dt-bindings/zmk/pointing.h>`

## Dependencies

- `layer_mo_tog` — hold-tap behavior (already defined in `behaviors {}`)
- ZMK pointing module (`&mmv`, `&msc`, `&mkp`) — enabled via `CONFIG_ZMK_POINTING=y`

## Notes

- Default movement speed: ZMK default (600). Tune with custom `mmv` instances if needed.
- Speed gears (slow/fast macros) deferred — add if default speed proves unusable.
- Scroll directions: Y/O are vertical (vim up/down), U/; are horizontal.
