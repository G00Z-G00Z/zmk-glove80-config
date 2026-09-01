# Design: MuseScore Layer

## Technical Approach

Add layer 11 with left-hand-only MuseScore shortcuts. Reuse existing macro patterns from Teams layer. Activation via three-key combo (Z+X+C positions) with idle guard. Right hand passes through to base.

## Architecture Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Macro style | Simple `behavior-macro` | Existing `mst_*` macros use this; one-shot Ctrl+key combos don't need params |
| Redo shortcut | `Ctrl+Shift+Z` | MuseScore 4 standard (not `Ctrl+Y` like Windows) |
| Combo activation | Z+X+C positions (48, 49, 50) | Bottom-left cluster, mirrors Teams pattern, ergonomic one-hand reach |
| Right hand | `&trans` except corners | Pass-through keeps base shortcuts; corner `&tog 11` for exit |
| Layer index | 11 | Next available after magic_layer (10) |

## Key Position Map (Glove80 Left Hand)

```
Row 2 (Q-T):  22=F5  23=Q   24=W   25=E   26=R   27=T
Row 3 (A-G):  34=.   35=A   36=S   37=D   38=F   39=G
Row 4 (Z-B):  46=N   47=Z   48=X   49=C   50=V   51=B
Thumb cluster: 64-71 (leftmost=64, rightmost=71)
```

## Macros Required

```c
// MuseScore macros (ms_ prefix)
ms_undo: ms_undo {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    bindings = <&kp LC(Z)>;
    label = "MS_UNDO";
};

ms_redo: ms_redo {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    bindings = <&kp LC(LS(Z))>;
    label = "MS_REDO";
};

ms_copy: ms_copy {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    bindings = <&kp LC(C)>;
    label = "MS_COPY";
};

ms_paste: ms_paste {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    bindings = <&kp LC(V)>;
    label = "MS_PASTE";
};

ms_cut: ms_cut {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    bindings = <&kp LC(X)>;
    label = "MS_CUT";
};

ms_triplet: ms_triplet {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    bindings = <&kp LC(N3)>;
    label = "MS_TRIPLET";
};

ms_add_bar: ms_add_bar {
    compatible = "zmk,behavior-macro";
    #binding-cells = <0>;
    bindings = <&kp LC(B)>;
    label = "MS_ADD_BAR";
};
```

## Combo Definition

```c
combo_tog_musescore {
    bindings = <&tog 11>;
    key-positions = <47 48 49>;  // Z X C positions
    layers = <0 11>;
    require-prior-idle-ms = <300>;
    timeout-ms = <50>;
};
```

## Layer 11 Bindings

```c
musescore_layer {
    bindings = <
// Row 0 (F-row)
&tog 11  &tog 11  &tog 11  &tog 11  &tog 11                                                                                  &tog 11  &tog 11  &tog 11  &tog 11  &tog 11
// Row 1 (number row) - left: slur, flip, enharmonic, spare, spare
&none    &kp S    &kp X    &kp J    &none    &none                                                                   &tog 11  &tog 11  &tog 11  &tog 11  &tog 11  &tog 11
// Row 2 (Q-row) - Q=halve, W=double, E=copy, R=repeat, T=tie
&none    &kp Q    &kp W    &ms_copy &kp R    &kp T                                                                   &trans   &trans   &trans   &trans   &trans   &tog 11
// Row 3 (home) - A=16th, S=8th, D=quarter, F=half, G=whole, 6th=dot
&none    &kp N3   &kp N4   &kp N5   &kp N6   &kp N7                                                                  &trans   &trans   &trans   &trans   &trans   &tog 11
// Row 4 (Z-row) - Z=undo, X=redo, C=play, V=paste, B=triplet, N=note-input
&none    &ms_undo &ms_redo &kp SPACE &ms_paste &ms_triplet  &kp ESC  &kp DEL  &kp N0  &tog 11  &tog 11  &tog 11     &kp N    &trans   &trans   &trans   &trans   &tog 11
// Row 5 (thumb) - Esc, Del, Rest(0), AddBar
&trans   &none    &none    &none    &none                   &kp ESC  &kp DEL  &kp N0  &tog 11  &ms_add_bar  &tog 11          &trans   &trans   &trans   &trans   &trans
    >;
};
```

## File Changes

| File | Action | Description |
|------|--------|-------------|
| `config/glove80.keymap` | Modify | Add 7 `ms_*` macros, 1 combo, layer 11 definition |
| `config/glove80.conf` | Auto | `update-max-combo.py` increments combo count |

## Testing Strategy

| Layer | What | Approach |
|-------|------|----------|
| Build | Firmware compiles | `./build.sh` succeeds |
| Manual | Layer activates | Flash, hold Z+X+C, verify layer change |
| Manual | Durations work | In MuseScore, press home row, verify note values |
| Manual | Exit works | Corners and combo both return to base |

## Migration

No migration. Additive change, no existing behavior modified.

## Open Questions

- [ ] Exact thumb positions for Esc/Del/Rest/AddBar — verify against physical layout after testing
