# Tasks: MuseScore Layer

## Review Workload Forecast

| Field | Value |
|-------|-------|
| Estimated changed lines | ~65–80 (7 macros + 1 combo + 1 layer block) |
| 400-line budget risk | Low |
| Chained PRs recommended | No |
| Suggested split | Single PR |
| Delivery strategy | ask-always |
| Chain strategy | size-exception (not needed) |

Decision needed before apply: No
Chained PRs recommended: No
Chain strategy: size-exception
400-line budget risk: Low

### Suggested Work Units

| Unit | Goal | Likely PR | Notes |
|------|------|-----------|-------|
| 1 | Macros + combo + layer 11 + build | PR 1 | All additive; single coherent change; glove80.conf auto-updated by script |

## Phase 1: Macros

- [x] 1.1 In `config/glove80.keymap`, locate the `macros` node (where `mst_*` macros live) and add `ms_undo` with `bindings = <&kp LC(Z)>`
- [x] 1.2 Add `ms_redo` with `bindings = <&kp LC(LS(Z))>`
- [x] 1.3 Add `ms_copy` with `bindings = <&kp LC(C)>`
- [x] 1.4 Add `ms_paste` with `bindings = <&kp LC(V)>`
- [x] 1.5 Add `ms_cut` with `bindings = <&kp LC(X)>`
- [x] 1.6 Add `ms_triplet` with `bindings = <&kp LC(N3)>`
- [x] 1.7 Add `ms_add_bar` with `bindings = <&kp LC(B)>`

## Phase 2: Layer 11

- [x] 2.1 In `config/glove80.keymap`, add `musescore_layer` block after `magic_layer` (layer 10)
- [x] 2.2 Bind home row: positions 35–39 → `&kp N3 N4 N5 N6 N7`; position 34 → `&kp DOT`
- [x] 2.3 Bind Q-row: 23=`&kp Q`, 24=`&kp W`, 25=`&ms_copy`, 26=`&kp R`, 27=`&kp T`
- [x] 2.4 Bind Z-row: 47=`&ms_undo`, 48=`&ms_redo`, 49=`&kp SPACE`, 50=`&ms_paste`, 51=`&ms_triplet`; 46=`&kp N`
- [x] 2.5 Bind number row: 23=slur `&kp S`, 24=flip `&kp X`, 25=enharmonic `&kp J`, rest `&none`
- [x] 2.6 Bind thumb cluster: Esc=`&kp ESC`, Del=`&kp DEL`, Rest=`&kp N0`, AddBar=`&ms_add_bar`; exit thumb=`&tog 11`
- [x] 2.7 Bind right hand: all `&trans` except corner keys → `&tog 11`
- [x] 2.8 Bind F-row: all left positions `&tog 11`

## Phase 3: Combo

- [x] 3.1 In `config/glove80.keymap`, locate the `combos` node and add `combo_tog_musescore`
- [x] 3.2 Set `key-positions = <47 48 49>` (Z X C positions), `layers = <0 11>`, `require-prior-idle-ms = <300>`, `timeout-ms = <50>`, `bindings = <&tog 11>`

## Phase 4: Build Verification

- [ ] 4.1 Run `./build.sh` and confirm exit code 0 (firmware compiles without errors)
- [ ] 4.2 Verify `config/glove80.conf` has `CONFIG_ZMK_COMBO_MAX_*` auto-updated by `update-max-combo.py`
