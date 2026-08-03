# Magic Layer

Bluetooth, RGB, y system controls.

## Activación

- Hold en teclas magic (esquinas inferiores) desde cualquier layer
- `magic` behavior: hold-tap con `rgb_ug_status_macro` en tap

## Bluetooth

### Profiles

| Tecla | Profile |
|-------|---------|
| Thumb izq inner | BT 0 |
| Thumb izq center | BT 1 |
| Thumb izq outer | BT 2 |
| Row 4 | BT 3 |

Cada profile macro hace: `&out OUT_BLE &bt BT_SEL n`

### Clear

- **Esquina sup izq**: BT_CLR (clear current profile)
- **Esquina sup der**: BT_CLR_ALL (clear all)

### Output

- **Thumb**: OUT_USB para forzar USB

## RGB Controls

### Ajustes

| Tecla | Función |
|-------|---------|
| W row | Speed +/- |
| E row | Saturation +/- |
| R row | Hue +/- |
| T row | Brightness +/- |
| Y | Effect cycle |

### Colores Preset

Varios presets de color en mano derecha:
- Rojo, verde, azul
- Morado, amarillo, cyan
- Blanco, off

### Layer Glow

`mo_w_glow` macro: activa layer + cambia color RGB, al soltar vuelve a off.
Usado para indicar visualmente qué layer está activo.

## System

| Tecla | Función |
|-------|---------|
| Home row izq | Bootloader (para flash) |
| Row 4 izq | System reset |
| Thumb der | Lock tap-dance |

## Dependencias

- `bt_0`, `bt_1`, `bt_2`, `bt_3` — profile macros
- `rgb_ug_status_macro` — muestra status RGB
- `mo_w_glow` — macro con color temporal
- `lock_td` — tap-dance
