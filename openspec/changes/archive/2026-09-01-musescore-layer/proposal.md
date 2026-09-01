# Proposal: MuseScore Layer

## Intent

One-handed MuseScore 4 control while right hand uses MIDI keyboard. Note entry workflow requires rapid duration/modifier access without looking at the keyboard.

## Scope

### In Scope
- Layer 11 with left-hand shortcuts for note durations, rests, modifiers
- Combo activation from base layer (Z+X+C)
- Toggle exits in corners (consistent with other layers)
- Macros for voice selection (Ctrl+Alt+1..4), triplet (Ctrl+3)
- Tap-dance for halve/double duration (Q/W)
- Right hand transparent (pass-through to base)

### Out of Scope
- Articulations (evaluate after real usage)
- Custom tuplet ratios (beyond triplet)
- MuseScore plugin integration
- Right-hand dedicated shortcuts

## Capabilities

### New Capabilities
- `musescore-layer`: Dedicated layer for MuseScore 4 one-handed workflow

### Modified Capabilities
None — this is an additive change.

## Approach

Use **Number Row Literal** layout: keep 1-7 where QWERTY users expect them. Minimal learning curve, easy to iterate after real-world testing. Follow existing patterns from `teams_mst_layer` (combo activation, toggle exits, parameterized macros).

## Affected Areas

| Area | Impact | Description |
|------|--------|-------------|
| `config/glove80.keymap` | Modified | Add layer 11, macros, combo, tap-dance |
| `config/glove80.conf` | Modified | Auto-sync updates combo limits |
| `openspec/layers/` | New | `musescore.md` spec |

## Risks

| Risk | Likelihood | Mitigation |
|------|------------|------------|
| Z+X+C combo collision | Low | Use `require-prior-idle-ms` like Teams combo |
| Right hand accidental pass-through | Med | Accept as feature — keeps base shortcuts available |
| Scope creep (more shortcuts) | Med | Ship minimal, iterate after real usage |

## Rollback Plan

Delete layer 11 definition, remove `ms_*` macros, remove combo. Single commit revert.

## Dependencies

- ZMK behavior-macro (parameterized)
- ZMK behavior-tap-dance
- ZMK combos with layer filtering
- `update-max-combo.py` auto-sync

## Success Criteria

- [ ] Can enter notes with durations 1-7 without looking
- [ ] Toggle in/out via Z+X+C combo
- [ ] Triplet and voice macros work in MuseScore 4
- [ ] No regression in existing layers
