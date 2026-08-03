# Base Layer

QWERTY layout con home-row mods y smart thumb clusters.

## Activación

Layer default (0). Siempre activo como fallback.

## Layout

- **Letras**: QWERTY estándar
- **Home row**: A/S/D/F y J/K/L/; tienen home-row mods (ver `features/home-row-mods.md`)
- **Top row numérica**: Hold para BT profiles (1,2,0) y media controls
- **Bottom row**: Z-B y N-/ sin modificadores

## Thumb Cluster

| Posición | Tap | Hold | Notas |
|----------|-----|------|-------|
| Inner izq | Grave/Esc | Layer 5 (function) | `lt_thumb_gresc`, flavor balanced |
| Center izq | Backspace/Delete | Layer 1 (cursor) | Shift → Delete |
| Outer izq | Sticky Shift / CapsWord / CapsLock | Layer 2 (number) | Tap-dance 3 niveles |
| Inner der | Shift | - | Sticky |
| Center der | Shift tap-dance | - | `sk_shift_caps_word_caps_td` |
| Outer der | Space / auto-cap dot | Layer 4 (symbols) | Shift+Space → `. ` + sticky shift |

## Teclas Especiales

- **Row 0 (F-row)**: Escape, volumen, skedpal inbox, task manager, display settings, play/next/prev, file explorer, brightness
- **Row 1**: Undo (Ctrl+Z), números con BT hold, ñ macro
- **Magic keys**: Esquinas inferiores → layer 8 (magic)

## Combos Activos

Ver `features/combos.md` — la mayoría de combos están activos en este layer.

## Dependencias

- `hrm_left`, `hrm_right` — home row mods
- `hmr_shift_left`, `hmr_shift_right` — shift en home row
- `lt_thumb_*` — layer-tap en thumbs
- `better_backspace`, `better_space` — mod-morphs
- `hold_bt_*` — bluetooth profile macros
