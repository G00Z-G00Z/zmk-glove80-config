# Cursor Layer

Navegación, selección de texto, y window management.

## Activación

- Hold thumb izquierdo center (backspace) desde base
- Toggle: tecla dedicada o combo

## Layout Principal

### Mano Derecha — Navegación
- **H/J/K/L**: Arrow keys (vim-style)
- **Home/End/PgUp/PgDn**: En row inferior
- **Alt+Tab / Win+Tab**: Acceso rápido

### Mano Izquierda — Acciones
- **Undo/Redo**: W/E
- **Copy/Cut/Paste**: Tap-dance y teclas dedicadas
- **App Switcher**: R (tap-dance: switch / switch+kill)

## Selección de Texto

| Tecla | Función |
|-------|---------|
| Thumb der outer | `select_word` — selecciona palabra bajo cursor |
| Thumb der center | `select_line` — selecciona línea |
| Thumb der inner | `extend_word` — extiende selección por palabra |
| Row 4 der | `extend_line` — extiende selección por línea |

Todas estas cambian dirección con Shift (ver `features/selection-macros.md`).

## Window Management

- **Win desktop left/right**: Cambiar escritorio virtual
- **Full screen**: Maximizar ventana
- **Ctrl+PgUp/PgDn**: Cambiar tabs

## Teclas Especiales

- **Layer toggle Teams**: Tecla Q
- **Select none**: Deseleccionar (thumb)
- **Select all / cut all / copy all**: Tap-dance en thumb

## Dependencias

- `select_word`, `select_line`, `extend_word`, `extend_line` — mod-morphs
- `app_switcher`, `app_switcher_killer` — macros
- `paste_copy_cut_td` — tap-dance
