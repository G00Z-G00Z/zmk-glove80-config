# Mouse Layer

Full mouse control via keyboard. Layer index: **8**.

## Activation

- **Hold backslash key** in base layer: `&lt 8 BACKSLASH` — hold = mouse layer, tap = backslash
- **Top corners** (positions 0 and 9) in mouse layer: `&tog 8` — exit mouse layer

> ⚠️ **BLE Re-Pair Required**: Adding `CONFIG_ZMK_POINTING=y` changes the HID descriptor. After flashing, re-pair the keyboard with every BLE host.

## Layout

### Right Hand — Cursor Movement (IJKL)

| Key | Position | Binding | Action |
|-----|----------|---------|--------|
| J | 41 | `&mmv MOVE_LEFT` | Move cursor left |
| K | 42 | `&mmv MOVE_DOWN` | Move cursor down |
| I | 31 | `&mmv MOVE_UP` | Move cursor up |
| L | 43 | `&mmv MOVE_RIGHT` | Move cursor right |

### Right Hand — Scroll

| Key | Position | Binding | Action |
|-----|----------|---------|--------|
| U | 29 | `&msc SCRL_UP` | Scroll up |
| H | 40 | `&msc SCRL_LEFT` | Scroll left |
| , | 53 | `&msc SCRL_DOWN` | Scroll down |
| ; | 44 | `&msc SCRL_RIGHT` | Scroll right |
| O | 32 | `&msc SCRL_UP` | Scroll up (alt) |
| . | 54 | `&msc SCRL_DOWN` | Scroll down (alt) |

### Left Hand — Mouse Buttons

| Key | Position | Binding | Action |
|-----|----------|---------|--------|
| F | 38 | `&mkp LCLK` | Left click |
| D | 37 | `&mkp RCLK` | Right click |
| S | 36 | `&mkp MCLK` | Middle click |

### Right Thumb — Mouse Buttons

| Key | Position | Binding | Action |
|-----|----------|---------|--------|
| Thumb inner | 57 | `&mkp MB4` | Back |
| Thumb center | 56 | `&mkp MB5` | Forward |
| Thumb outer | 55 | `&mkp RCLK` | Right click |
| Row above outer | 50 | `&mkp MCLK` | Middle click |
| Row above center | 51 | `&mkp LCLK` | Left click |

All other positions: `&none`.

## Firmware Requirements

- `config/glove80.conf`: `CONFIG_ZMK_POINTING=y`
- `config/glove80.keymap`: `#include <dt-bindings/zmk/pointing.h>`

## Dependencies

- ZMK pointing module (`&mmv`, `&msc`, `&mkp`) — enabled via `CONFIG_ZMK_POINTING=y`

## Notes

- Default movement speed: ZMK default (600). Tune with custom `mmv` instances if needed.
- Speed gears (slow/fast macros) deferred — add if default speed proves unusable.
- Scroll directions: Y/O are vertical (vim up/down), U/; are horizontal.
