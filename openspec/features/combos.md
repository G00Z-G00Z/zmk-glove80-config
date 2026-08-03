# Combos

~60 combos para símbolos, acciones, y layer toggles.

## Configuración Global

```
require-prior-idle-ms = <150>  // default, algunos usan 50-200
timeout-ms = <18>              // default para la mayoría
```

El archivo `glove80.conf` tiene límites auto-calculados por `scripts/update-max-combo.py`.

## Categorías

### Window Management
- **W+H**: Desktop izquierdo (vim-like)
- **W+L**: Desktop derecho (vim-like)
- **W+Q**: Cerrar app (Alt+F4)
- **W+Up**: Fullscreen window
- **Ctrl+tecla+Left/Right**: Mover ventana entre monitores

### Copy/Paste/Undo
- **X+C**: Copy (tap-dance: 2t = cut)
- **C+V**: Paste
- **Z+X**: Undo

### Símbolos Frecuentes
Combos verticales (tecla + tecla abajo):
- **$**: tecla + abajo
- **#**: tecla + abajo
- **@**: tecla + abajo
- **%**: tecla + abajo
- **^**: tecla + abajo
- **&**: tecla + abajo
- **/\\**: tecla + abajo (mod-morph: Alt = backslash)
- **|**: tecla + abajo
- **_**: tecla + abajo

### Brackets (combos horizontales)
- **()**: dos teclas adyacentes (con HRM para Shift+Ctrl)
- **[]**: dos teclas adyacentes
- **{}**: Shift + bracket combo

### Puntuación
- **:**: dos teclas home row
- **~**: dos teclas adyacentes
- **"**: combo con positioning
- **?**: tecla + abajo
- **!**: tecla + abajo
- **\***: dos teclas adyacentes

### Quotes con Pairing
- **""**: 4 teclas (dedos anulares)
- **''**: 2 teclas verticales
- **``**: 2 teclas verticales
- **"""block**: combo diagonal
- **```block**: combo diagonal

### Layer Toggles
- **Teams**: 3 teclas home row (F+G+H area)
- **Teams (alt)**: thumb + tecla
- **Vim mode**: dos thumbs
- **Gaming**: 4 teclas (protegido con idle 500ms)
- **Single number**: dos thumbs izq
- **Single symbol**: dos thumbs der

### Navegación
- **Tab**: dos teclas (con HRM para GUI+Alt)
- **Esc**: dos teclas adyacentes
- **App switcher**: dos teclas adyacentes
- **Key repeat**: múltiples combos disponibles

### Especiales
- **ñ**: combo con N
- **Mute+Lock**: 4 teclas (protección accidental)

## Layers Activos

La mayoría de combos especifican `layers = <0 4>` o `layers = <0 4 3>`:
- Layer 0: Base
- Layer 3: Teams  
- Layer 4: Symbols

Algunos solo en layers específicos (ej: space/backspace en number layer).

## Ubicación

- **Definición**: `combos { compatible = "zmk,combos"; ... }`
- **Config**: `glove80.conf` para límites
