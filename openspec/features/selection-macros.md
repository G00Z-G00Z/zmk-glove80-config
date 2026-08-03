# Selection Macros

Selección de texto estilo Vim con dirección modificable por Shift.

## Problema

Seleccionar palabras/líneas requiere muchas teclas. Quiero un solo key que seleccione inteligentemente.

## Solución

Mod-morphs que cambian dirección según Shift, combinados con macros de selección.

## Behaviors

### select_word
- **Tap**: Selecciona palabra a la derecha del cursor
- **Shift+Tap**: Selecciona palabra a la izquierda

Macro interno:
```
// select_word_right
Ctrl+Right, Ctrl+Left, Ctrl+Shift+Right

// select_word_left  
Ctrl+Left, Ctrl+Right, Ctrl+Shift+Left
```

### select_line
- **Tap**: Selecciona línea completa (cursor al final)
- **Shift+Tap**: Selecciona línea completa (cursor al inicio)

Macro interno:
```
// select_line_right
Home, Shift+End

// select_line_left
End, Shift+Home
```

### extend_word
- **Tap**: Extiende selección una palabra a la derecha
- **Shift+Tap**: Extiende selección una palabra a la izquierda

### extend_line
- **Tap**: Extiende selección una línea abajo
- **Shift+Tap**: Extiende selección una línea arriba

## Uso Típico

1. `select_word` → selecciona palabra actual
2. `extend_word` repetido → agranda selección
3. Copy/Cut → acción

## Ubicación

- **Definición**: `behaviors { select_word, extend_word, select_line, extend_line }`
- **Macros**: `macros { select_word_right, select_word_left, ... }`
- **Uso**: Cursor layer thumbs
