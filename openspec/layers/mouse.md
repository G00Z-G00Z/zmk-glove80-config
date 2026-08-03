# Mouse Layer

Full mouse control via keyboard. Layer index: **8**.

## Activation

- **Hold backslash key** in base layer: `&lt 8 BACKSLASH` — hold = mouse layer, tap = backslash
- **Top corners** (positions 0 and 9) in mouse layer: `&tog 8` — exit mouse layer

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
| U | 29 | `&msc SCRL_DOWN` | Scroll down |
| I | 31 | `&msc SCRL_UP` | Scroll up |
| O | 32 | `&msc SCRL_UP` | Scroll up (alt) |
| ; | 44 | `&msc SCRL_RIGHT` | Scroll right |
| , | 53 | `&msc SCRL_DOWN` | Scroll down |
| G (left of H) | 39 | `&msc SCRL_LEFT` | Scroll left |

### Left Hand — Modifiers (Home Row)

| Key | Position | Binding | Action |
|-----|----------|---------|--------|
| A | 36 | `&kp LGUI` | GUI (Win/Cmd) |
| S | 37 | `&kp LALT` | Alt |
| D | 38 | `&kp LCTRL` | Control |
| F | 39 | `&kp LSHIFT` | Shift |

### Left Hand — Mouse Buttons (Bottom Row)

| Key | Position | Binding | Action |
|-----|----------|---------|--------|
| X | 48 | `&mkp MCLK` | Middle click |
| C | 49 | `&mkp RCLK` | Right click |
| V | 50 | `&mkp LCLK` | Left click |

### Left Hand — Precision Mode

| Key | Position | Binding | Action |
|-----|----------|---------|--------|
| R | 27 | `&mo 9` | Hold for precision (1/6 speed) |

### Right Thumb — Mouse Buttons

| Key | Position | Binding | Action |
|-----|----------|---------|--------|
| Thumb inner | 57 | `&mkp MB4` | Back |
| Thumb center | 56 | `&mkp MB5` | Forward |
| Thumb outer | 55 | `&mkp RCLK` | Right click |
| Row above outer | 50 | `&mkp MCLK` | Middle click |
| Row above center | 51 | `&mkp LCLK` | Left click |

All other positions: `&none`.

## Mouse Precision Layer

Layer index: **9**. Transparent layer — activates input processor scaler.

When layer 9 is active (hold R), mouse movement is scaled to 1/6 speed via `&zip_xy_scaler 1 6`.

## Speed Configuration

```c
// Mouse speed (precision mode divides by 6 via scaler)
#define ZMK_POINTING_DEFAULT_MOVE_VAL 600

// No acceleration — constant predictable speed
&mmv {
    time-to-max-speed-ms = <0>;
    acceleration-exponent = <0>;
};

// Precision scaler when layer 9 active
&mmv_input_listener {
    precision {
        layers = <9>;
        input-processors = <&zip_xy_scaler 1 6>;
    };
};
```

| Mode | Speed | Use Case |
|------|-------|----------|
| Normal | 600 | General navigation |
| Precision (hold R) | 100 | Fine positioning, small targets |

## Firmware Requirements

- `config/glove80.conf`: `CONFIG_ZMK_POINTING=y`
- `config/glove80.keymap`:
  - `#define ZMK_POINTING_DEFAULT_MOVE_VAL 600` (before pointing.h include)
  - `#include <dt-bindings/zmk/pointing.h>`
  - `#include <input/processors.dtsi>`

## Dependencies

- ZMK pointing module (`&mmv`, `&msc`, `&mkp`) — enabled via `CONFIG_ZMK_POINTING=y`
- ZMK input processors (`&zip_xy_scaler`) — via `<input/processors.dtsi>`

## Notes

- Mods on home row allow Ctrl+click, Shift+drag, etc.
- Clicks moved to bottom row to free home row for mods.
- Precision hold (R) is above shift finger — easy to hold while moving with right hand.
