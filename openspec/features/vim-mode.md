# Vim Mode

Emulación básica de Vim normal/visual mode para apps que no soportan Vim.

## Problema

Quiero navegación y edición estilo Vim en cualquier app (Teams, Word, browser).

## Solución

Toggle a layer especial que reinterpreta teclas como comandos Vim, usando macros para simular el comportamiento.

## Activación

- **Combo**: Dos thumbs específicos (posiciones 52+57) desde base
- **Salida**: `i`, `a`, o Escape

## Normal Mode (toggle layer activo)

### Movimiento
| Tecla | Acción |
|-------|--------|
| h/j/k/l | Arrow keys |
| w | Ctrl+Right (word forward) |
| b | Ctrl+Left (word back) |
| 0 | Home |
| $ | End |

### Edición
| Tecla | Acción | Shift |
|-------|--------|-------|
| i | Exit to insert | I: Home + exit |
| a | Right + exit | A: End + exit |
| o | End + Enter + exit | - |
| x/Delete | Delete char | dd: delete line |
| c | ciw (change inner word) | C: change to EOL |

### Visual Mode
| Tecla | Acción |
|-------|--------|
| v | Enter visual (hold Shift + toggle) |
| V | Visual line (Home + hold Shift + End) |

## Macros Clave

### vim_kp_exit_norm
Macro paramétrico: ejecuta keypress y sale del mode.
```
bindings = <&kp PARAM &tog 0>
```

### vim_norm_v_kp (enter visual)
```
bindings = <&tog 0 &kt LEFT_SHIFT>
```
Activa sticky Shift para que todo movimiento seleccione.

### vim_exit_visual
```
bindings = <&kt LEFT_SHIFT &tog 0>
```
Desactiva sticky Shift y vuelve a normal.

## Limitaciones

- No hay registers (clipboard del sistema)
- No hay motions complejas (di", ci(, etc.)
- No hay dot repeat
- Visual mode es aproximado (sticky shift)

## Ubicación

- **Behaviors**: `vim_norm_*` mod-morphs
- **Macros**: `vim_*` macros
- **Layer**: Usa toggle en layer 0 para crear un "mode"
