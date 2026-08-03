# Smart Thumbs

Thumb cluster con layer-taps y mod-morphs para máxima utilidad.

## Problema

Los thumbs son las teclas más accesibles. Quiero que hagan más que Space/Backspace.

## Solución

Hold-taps customizados que combinan:
- Tap: acción frecuente (space, backspace, shift)
- Hold: activar layer
- Modificadores: variar el tap

## Behaviors

### lt_thumb_better_space
```
bindings = <&mo>, <&better_space>
tapping-term-ms = <175>
quick-tap-ms = <300>
flavor = "tap-preferred"
```

- **Tap**: Space
- **Shift+Tap**: `. ` + sticky Shift (auto-capitalización)
- **Hold**: Activa layer (symbols)

### lt_thumb_backspace
```
bindings = <&mo>, <&better_backspace>
```

- **Tap**: Backspace
- **Shift+Tap**: Delete
- **Hold**: Activa layer (cursor)

### lt_thumb_gresc
```
bindings = <&mo>, <&gresc>
```

- **Tap**: Escape
- **Shift+Tap**: Grave (`)
- **Hold**: Activa layer (function)

### lt_thumb_shift_td
```
bindings = <&mo>, <&sk_shift_caps_word_caps_td>
```

- **1 Tap**: Sticky Shift
- **2 Taps**: Caps Word
- **3 Taps**: Caps Lock
- **Hold**: Activa layer (number)

## Mod-Morphs Internos

### better_space
```
bindings = <&kp SPACE>, <&auto_cap_dot>
mods = <(MOD_LSFT)>
```

### better_backspace
```
bindings = <&kp BACKSPACE>, <&kp DELETE>
mods = <(MOD_LSFT|MOD_RSFT)>
```

### auto_cap_dot (macro)
```
bindings = <&kp DOT &kp SPACE &sk LEFT_SHIFT>
```
Escribe `. ` y activa sticky shift para la próxima letra.

## Parámetros

| Param | Valor | Razón |
|-------|-------|-------|
| tapping-term-ms | 175 | Más corto que HRM — thumbs son intencionales |
| quick-tap-ms | 300 | Permite repetir rápido (space space space) |
| flavor | tap-preferred | Prioriza tap sobre hold |

## Ubicación

- **Behaviors**: `lt_thumb_*`, `better_*`
- **Macros**: `auto_cap_dot`
- **Uso**: Base layer thumb cluster
