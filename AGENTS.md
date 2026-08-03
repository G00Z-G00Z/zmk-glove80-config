# ZMK Glove80 Keyboard Config

Personal keymap config for Glove80 split ergonomic keyboard using ZMK firmware.

## Layout Documentation

**Read `openspec/` before modifying the keymap.**

- `openspec/layers/` — one file per layer (base, cursor, number, teams, symbols, function, gaming, magic)
- `openspec/features/` — cross-cutting features (home-row-mods, combos, tap-dance, vim-mode, etc.)

Each spec documents: purpose, activation, key mappings, dependencies, and location in keymap.

## Build

**Local (Docker + Nix):**
```bash
./build.sh           # builds firmware, outputs glove80.uf2
./pull-and-build.sh  # git pull + build + open finder (macOS)
```

**CI:** Push to `main` triggers GitHub Action. Artifact: `glove80-{sha}.uf2`

## Key Files

- `config/glove80.keymap` - main config: layers, behaviors, macros, combos
- `config/glove80.conf` - combo limits (auto-updated by script)
- `scripts/update-max-combo.py` - parses keymap, updates conf with combo counts

## Gotchas

- **Combo limits auto-sync:** `update-max-combo.py` runs before every build (local and CI). Do not manually edit `CONFIG_ZMK_COMBO_MAX_*` in `glove80.conf`.
- **Keymap syntax:** ZMK devicetree format. Labels must be short. See ZMK docs for behaviors/macros.
- **Build only triggers on `config/` changes** - workflow ignores other paths.
