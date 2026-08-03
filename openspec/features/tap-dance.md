# Tap-Dance

Múltiples acciones en una tecla según cantidad de taps.

## Behaviors

### play_next_prev_td
Control de media en una tecla.

| Taps | Acción |
|------|--------|
| 1 | Play/Pause |
| 2 | Next track |
| 3 | Previous track |

### sk_shift_caps_word_caps_td
Shift progresivo.

| Taps | Acción |
|------|--------|
| 1 | Sticky Shift (una letra) |
| 2 | Caps Word (hasta space/símbolo) |
| 3 | Caps Lock (toggle permanente) |

### paste_copy_cut_td
Clipboard en una tecla.

| Taps | Acción |
|------|--------|
| 1 | Paste |
| 2 | Copy |
| 3 | Cut |

### copy_cut_td
Variante sin paste.

| Taps | Acción |
|------|--------|
| 1 | Copy |
| 2 | Cut |

### app_switcher_td
Alt-Tab mejorado.

| Taps | Acción |
|------|--------|
| 1 | App switcher (Alt+Tab con hold) |
| 2 | App switcher + close app al soltar |

### selec_all_copy_all_tp
Select all progresivo.

| Taps | Acción |
|------|--------|
| 1 | Select all (Ctrl+A) |
| 2 | Select all + Cut |
| 3 | Select all + Copy |

### lock_td
Lock con escape.

| Taps | Acción |
|------|--------|
| 1 | Win+L (lock) |
| 2 | Win+Esc (start menu) |

### vim_norm_delete
Delete progresivo (vim mode).

| Taps | Acción |
|------|--------|
| 1 | Delete char |
| 2 | Delete line |

## Teams Layer

### mst_show_screen_vid_td
| Taps | Acción |
|------|--------|
| 1 | Share screen |
| 2 | Toggle camera |

### mst_call_cmds_td
| Taps | Acción |
|------|--------|
| 1 | Go to call window |
| 2 | Join call from toast |
| 3 | Start call from chat |

### mst_react_td
| Taps | Acción |
|------|--------|
| 1 | React happy |
| 2 | React heart |
| 3 | React LOL |
| 4 | React surprise |

Usa `tapping-term-ms = <300>` para dar tiempo a elegir.

### mst_chatlist_go_unread_mute_td
| Taps | Acción |
|------|--------|
| 1 | Go to chat list |
| 2 | Toggle unread filter |
| 3 | Toggle mute chat |

## Configuración

Default `tapping-term-ms` es 200ms. Algunos usan 300ms para más opciones.

## Ubicación

- **Definición**: `behaviors { *_td: ... }`
- **Uso**: Distribuidos en varios layers
