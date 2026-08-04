# Mouse Layer

Full mouse control via keyboard. Layer index: **8**.

## Activation

- **Tap-dance on backslash key** in base layer: `&mouse_layer_td`
  - **Tap**: backslash character
  - **Hold**: momentary mouse layer
  - **Double-tap**: toggle mouse layer ON/OFF
  - Tapping term: 150ms (snappy)
- **Top corners** (positions 0 and 9) in mouse layer: `&tog 8` — exit mouse layer
- **Escape keys** on thumbs for quick exit

> ⚠️ **BLE Re-Pair Required**: Adding `CONFIG_ZMK_POINTING=y` changes the HID descriptor. After flashing, re-pair the keyboard with every BLE host.

## Layout

### Right Hand — Cursor Movement (HJKL vim-style, home row)

| Key | Position | Binding | Action |
|-----|----------|---------|--------|
| H | 40 | `&mmv MOVE_LEFT` | Move cursor left |
| J | 41 | `&mmv MOVE_DOWN` | Move cursor down |
| K | 42 | `&mmv MOVE_UP` | Move cursor up |
| L | 43 | `&mmv MOVE_RIGHT` | Move cursor right |

### Right Hand — Scroll (row above home)

| Key | Position | Binding | Action |
|-----|----------|---------|--------|
| Y | 29 | `&msc SCRL_LEFT` | Scroll left |
| U | 30 | `&msc SCRL_DOWN` | Scroll down |
| I | 31 | `&msc SCRL_UP` | Scroll up |
| O | 32 | `&msc SCRL_RIGHT` | Scroll right |

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
| R | 27 | `&mo 9` | Hold for precision (1/3 speed) |

### Thumb Clusters

**Left Thumb:**
| Position | Binding | Action |
|----------|---------|--------|
| 52 | `&mo 9` | Precision mode |
| 53 | `&none` | — |
| 54 | `&kp ESCAPE` | Exit |

**Right Thumb:**
| Position | Binding | Action |
|----------|---------|--------|
| 55 | `&mkp RCLK` | Right click |
| 56 | `&kp ESCAPE` | Exit |
| 57 | `&mkp MCLK` | Middle click |

### Right Hand — Bottom Row (Mouse Buttons)

| Position | Binding | Action |
|----------|---------|--------|
| 58 | `&mkp MB4` | Back |
| 59 | `&mkp LCLK` | Left click |
| 60 | `&mkp RCLK` | Right click |
| 61 | `&mkp MB5` | Forward |

All other positions: `&none`.

## Mouse Precision Layer

Layer index: **9**. Transparent layer — activates input processor scaler.

When layer 9 is active (hold R or left thumb), mouse movement is scaled to 1/3 speed via `&zip_xy_scaler 1 3`.

## Speed Configuration

```c
// Mouse speed (precision mode divides by 3 via scaler)
#define ZMK_POINTING_DEFAULT_MOVE_VAL 350

// No acceleration — constant predictable speed
&mmv {
    time-to-max-speed-ms = <0>;
    acceleration-exponent = <0>;
};

// Precision scaler when layer 9 active
&mmv_input_listener {
    precision {
        layers = <9>;
        input-processors = <&zip_xy_scaler 1 3>;
    };
};
```

| Mode | Speed | Use Case |
|------|-------|----------|
| Normal | 350 | General navigation, less overshoot |
| Precision (hold R) | ~117 | Fine positioning, small targets |

## Tap-Dance Behavior

```dts
mouse_layer_td: mouse_layer_td {
    compatible = "zmk,behavior-tap-dance";
    label = "MOUSE_LAYER_TD";
    #binding-cells = <0>;
    tapping-term-ms = <150>;
    bindings = <&lt 8 BACKSLASH>, <&tog 8>;
};
```

## Firmware Requirements

- `config/glove80.conf`: `CONFIG_ZMK_POINTING=y`
- `config/glove80.keymap`:
  - `#define ZMK_POINTING_DEFAULT_MOVE_VAL 350` (before pointing.h include)
  - `#include <dt-bindings/zmk/pointing.h>`
  - `#include <input/processors.dtsi>`

## Dependencies

- ZMK pointing module (`&mmv`, `&msc`, `&mkp`) — enabled via `CONFIG_ZMK_POINTING=y`
- ZMK input processors (`&zip_xy_scaler`) — via `<input/processors.dtsi>`

## Notes

- Mods on home row allow Ctrl+click, Shift+drag, etc.
- Clicks on left bottom row and right thumb for easy access.
- Precision available on R (index finger) and left thumb — hold while moving with right hand.
- Escape on multiple thumb positions for quick layer exit.
- Tap-dance allows backslash tap, hold for momentary, double-tap for toggle.
