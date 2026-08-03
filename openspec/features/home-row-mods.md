# Home Row Mods

Modificadores en home row sin interferir con typing normal.

## Problema

Quiero GUI/Alt/Ctrl/Shift accesibles sin mover las manos, pero sin falsos positivos al escribir rápido.

## Solución

Behaviors `hrm_left` y `hrm_right` con configuración anti-misfire.

## Configuración

```
tapping-term-ms = <280>
quick-tap-ms = <200>
flavor = "balanced"
require-prior-idle-ms = <150>
hold-trigger-on-release
```

### Parámetros Clave

| Parámetro | Valor | Propósito |
|-----------|-------|-----------|
| tapping-term-ms | 280 | Tiempo para distinguir tap vs hold |
| quick-tap-ms | 200 | Doble-tap rápido siempre es tap |
| require-prior-idle-ms | 175 | Ignora hold si estabas escribiendo |
| hold-trigger-on-release | - | Decide tap/hold cuando soltás la siguiente tecla |

### Posiciones Opuestas

`hold-trigger-key-positions` solo incluye teclas de la mano **opuesta**. Esto evita:
- Falsos mods al escribir "as", "df", "jk", etc.
- Solo activa mod si presionás tecla del otro lado

## Mapping

### Mano Izquierda (hrm_left)
| Tecla | Tap | Hold |
|-------|-----|------|
| A | a | GUI |
| S | s | Alt |
| D | d | Ctrl |
| F | f | Shift |

### Mano Derecha (hrm_right)
| Tecla | Tap | Hold |
|-------|-----|------|
| J | j | Shift |
| K | k | Ctrl |
| L | l | Alt |
| ; | ; | GUI |

## Variantes

- `hmr_shift_left/right`: Shift con timings más cortos (200ms) para typing rápido
- `hrm_right_lpar/rpar`: HRM que produce paréntesis en tap (para combos)

## Ubicación en Keymap

- Definición: `behaviors { hrm_left, hrm_right, ... }`
- Uso: base layer home row
