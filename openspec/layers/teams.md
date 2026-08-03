# Teams Layer (MST)

Control completo de Microsoft Teams sin salir del teclado.

## Activación

- Combo: 3 teclas home row (F+G+H en posiciones 29+30+31)
- Toggle bidireccional (funciona desde base y desde teams)
- `go_temp_mst`: Va a Teams temporalmente, vuelve al soltar

## Status

| Tecla | Status |
|-------|--------|
| V | Available |
| C | BRB (Be Right Back) |
| X | Away |
| B | Offline |
| Bottom row | Busy |

Cada macro usa `/status` command en Teams search bar.

## Llamadas

| Tecla/Combo | Acción |
|-------------|--------|
| Row 1 combo | Ir a ventana de llamada (Win+11) |
| Tap-dance | 1t: ir a call, 2t: join desde toast, 3t: llamar desde chat |
| Thumb izq | Hold: mute/unmute y volver a app anterior |
| F2 | `go_call_unmute_mute_go_back` |

## Reacciones

Tap-dance con 4 niveles:
1. Happy (like)
2. Heart
3. LOL
4. Surprise

Tecla adicional para "more reactions" que abre el picker.

## Chat Navigation

- **Ctrl+L**: Lista de chats (tap-dance: 1t lista, 2t toggle unread, 3t toggle mute)
- **Ctrl+J**: Jump to chat
- **Flechas**: Navegar chats
- **Enter**: Abrir chat / enviar mensaje
- **Reply**: Macro para responder mensaje seleccionado

## Screen Sharing

- Tap-dance: 1t show screen, 2t toggle camera
- Macro espera 1750ms antes de enviar shortcuts (Teams es lento)

## Zoom Controls

- **Alt+Shift+=/-/0**: Zoom in/out/reset

## Dependencias

- `mst_*` macros — todas las acciones de Teams
- `go_call_unmute_mute_go_back` — macro compleja con pause_for_release
- `mst_key_exit_mst` — macro paramétrica que ejecuta key y sale del layer
- `layer_mo_tog` — hold-tap para mo/tog
