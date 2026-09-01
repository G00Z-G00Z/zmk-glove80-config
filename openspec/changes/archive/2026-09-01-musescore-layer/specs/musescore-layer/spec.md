# MuseScore Layer Specification

## Purpose

New dedicated layer (11) for one-handed MuseScore 4 control. Left hand handles note input; right hand operates MIDI keyboard.

## Requirements

### Requirement: Layer Activation

The layer MUST be reachable via a 3-key combo from the base layer. The combo MUST include `require-prior-idle-ms` to prevent accidental activation during fast typing.

#### Scenario: Enter layer via combo

- GIVEN the keyboard is on the base layer and has been idle for the required prior-idle duration
- WHEN the user presses the activation combo (bottom-left cluster)
- THEN the keyboard switches to layer 11

#### Scenario: Accidental combo during fast typing is ignored

- GIVEN the keyboard is on the base layer and prior-idle duration has NOT elapsed
- WHEN the activation combo keys are pressed in quick succession
- THEN the layer does NOT activate and individual key events are sent normally

### Requirement: Layer Exit

The layer MUST be exitable via `tog 11` on right-hand corner keys and via the same base-layer combo.

#### Scenario: Exit via right-hand toggle

- GIVEN the keyboard is on layer 11
- WHEN the user presses the designated right-hand corner key
- THEN the keyboard returns to the base layer

### Requirement: Duration Keys on Home Row

The six most common note durations MUST be reachable from the home row without hand movement.

| Position | Duration | Key sent |
|----------|----------|----------|
| A | 16th (semicorchea) | `3` |
| S | 8th (corchea) | `4` |
| D | quarter (negra) | `5` |
| F | half (blanca) | `6` |
| G | whole (redonda) | `7` |
| 6th home key | dot (puntillo) | `.` |

#### Scenario: Select quarter note duration

- GIVEN the keyboard is on layer 11 and MuseScore is in note input mode
- WHEN the user presses D (home row, middle finger)
- THEN MuseScore receives `5` and sets duration to quarter note

### Requirement: Thumb Actions

The four thumb positions MUST cover the most-reached non-duration actions.

| Thumb | Function | Key sent |
|-------|----------|----------|
| 1 | Exit note input (Esc) | `Esc` |
| 2 | Delete → rest | `Del` |
| 3 | Insert rest | `0` |
| 4 | Add bar | `Ctrl+B` |

#### Scenario: Delete note and replace with rest

- GIVEN the keyboard is on layer 11 and a note is selected in MuseScore
- WHEN the user presses Thumb 2
- THEN MuseScore receives `Del` and the note becomes a rest

### Requirement: Row Above Home Shortcuts

Q–T MUST provide duration manipulation and common editing shortcuts.

| Key | Function | Sent |
|-----|----------|------|
| Q | Halve duration | `Q` |
| W | Double duration | `W` |
| E | Copy | `Ctrl+C` |
| R | Repeat selection | `R` |
| T | Tie | `T` |

#### Scenario: Halve note duration

- GIVEN the keyboard is on layer 11 and a note is selected
- WHEN the user presses Q
- THEN MuseScore receives `Q` and the note duration is halved

### Requirement: Row Below Home Shortcuts

Z–V MUST provide undo, redo, play/stop, and paste.

| Key | Function | Sent |
|-----|----------|------|
| Z | Undo | `Ctrl+Z` |
| X | Redo | `Ctrl+Shift+Z` |
| C | Play/Stop | `Space` |
| V | Paste | `Ctrl+V` |

#### Scenario: Undo last action

- GIVEN the keyboard is on layer 11
- WHEN the user presses Z
- THEN the `ms_undo` macro fires and MuseScore receives `Ctrl+Z`

### Requirement: Additional Left-Hand Keys

Lower-priority shortcuts MUST be reachable without leaving the layer.

| Key | Function | Sent |
|-----|----------|------|
| B | Triplet | `Ctrl+3` |
| N | Toggle note input | `N` |
| (other) | Cut | `Ctrl+X` |
| (other) | Slur | `S` |
| (other) | Enharmonic respell | `J` |
| (other) | Flip direction | `X` |

#### Scenario: Insert triplet

- GIVEN the keyboard is on layer 11 and a note or rest is selected
- WHEN the user presses B
- THEN the `ms_triplet` macro fires and MuseScore receives `Ctrl+3`

### Requirement: Right Hand Pass-Through

All right-hand keys MUST be `&trans`, passing events through to the base layer.

#### Scenario: Right-hand key pressed while in layer 11

- GIVEN the keyboard is on layer 11
- WHEN the user presses any right-hand key (excluding the exit toggle)
- THEN the base layer binding for that key fires

### Requirement: Macros for Multi-Key Shortcuts

All MuseScore shortcuts requiring modifier keys MUST be implemented as macros so the user sends a single keypress.

Required macros: `ms_undo` (`Ctrl+Z`), `ms_redo` (`Ctrl+Shift+Z`), `ms_copy` (`Ctrl+C`), `ms_paste` (`Ctrl+V`), `ms_cut` (`Ctrl+X`), `ms_triplet` (`Ctrl+3`), `ms_add_bar` (`Ctrl+B`).

#### Scenario: Macro sends correct key combination

- GIVEN the keyboard is on layer 11
- WHEN the user presses the key bound to `ms_redo`
- THEN the firmware sends `Ctrl+Shift+Z` to the host as a single atomic action

### Requirement: No Regression on Existing Layers

Adding layer 11, new macros, and a new combo MUST NOT alter the behavior of layers 0–10.

#### Scenario: Existing layer unchanged after adding layer 11

- GIVEN layer 11 has been added to the keymap
- WHEN the user activates any layer 0–10
- THEN all key bindings on those layers behave identically to before the change
