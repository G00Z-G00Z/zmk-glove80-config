# Exploration: MuseScore Layer

Layer dedicada para MuseScore 4 con workflow mano izquierda + MIDI keyboard.

## Current State

### Layer Structure
```
0:  base_layer
1:  cursor_layer
2:  number_layer
3:  teams_mst_layer    <- modelo a seguir
4:  symbols_layer
5:  function_layer
6:  gaming_layer       <- mano izquierda dedicada
7:  gaming_aux_layer
8:  mouse_layer
9:  mouse_precision
10: magic_layer
```

**Layer 11** disponible. ZMK soporta hasta 16 layers sin impacto.

### Existing Patterns

1. **`layer_mo_tog`**: hold=momentary, tap=toggle — ideal para activación
2. **Toggle en esquinas**: todas las layers tienen `tog X` en las esquinas para salir
3. **Macros parametrizadas**: `mst_key_exit_mst` hace key + exit layer
4. **Combos por layer**: limitados a layers específicas con `layers = <0 3>`

### Glove80 Left Hand Physical Layout

Referencia visual (índices ZMK):
```
Row 0:    0     1     2     3     4
Row 1:   10    11    12    13    14    15
Row 2:   22    23    24    25    26    27
Row 3:   34    35    36    37    38    39
Row 4:   46    47    48    49    50    51
Row 5:   64    65    66    67    68
Thumbs:  69    70    71    52    53    54
```

## Affected Areas

- `config/glove80.keymap` — nuevo layer + macros + posible combo
- `config/glove80.conf` — si se agregan combos, auto-sync los actualiza
- `openspec/layers/` — spec nueva `musescore.md`

## MuseScore Shortcuts Analysis

### Priority 1: Note Durations (CRITICAL)
```
1=64th  2=32nd  3=16th  4=eighth  5=quarter  6=half  7=whole
0=rest
```
**Problema**: Number row está lejos. Opciones:
- Poner en home row (A-;) — más cómodo pero menos intuitivo
- Dejar en number row — más intuitivo, menos cómodo
- Hybrid: números en number row, dot/modifiers en home

### Priority 2: Modifiers (FREQUENT)
```
.  = dot (add 50% duration)
T  = tie
S  = slur
Q  = halve duration
W  = double duration
```

### Priority 3: Tuplets (COMMON)
```
Ctrl+3 = triplet (80% de uso)
Ctrl+2..9 = other tuplets
```
Macro simple: `&kp LC(N3)` para triplet

### Priority 4: Voice Selection
```
Ctrl+Alt+1..4 = voice 1-4
```
Macro: `&kp LA(LC(N1))` etc. — tres modificadores pero uso esporádico.

### Priority 5: Articulations
```
Shift+S = staccato
Shift+V = accent
Shift+N = tenuto
Shift+O = marcato
```
Todos con Shift — poner Shift en thumb permite teclas directas.

### Priority 6: Essential
```
N     = toggle note input
Space = play/stop
Esc   = exit mode
Del   = delete
R     = repeat selection
X     = flip direction
J     = enharmonic respell
</>   = hairpins (crescendo/decrescendo)
```

### Priority 7: Navigation
```
Arrows       = note selection (ya disponible)
Ctrl+Left/Right = prev/next measure
```

## Approaches

### Approach A: Number Row Literal
Mantener números en su posición QWERTY.

```
Row 1:  1   2   3   4   5   (duraciones)
Row 2:  Q   W   E   R   T   (Q=halve, W=double, E=?, R=repeat, T=tie)
Row 3:  Esc A   S   D   F   (A=?, S=slur, D=dot, F=?)
Row 4:  Ctrl Z  X   C   V   (ctrl=tuplets, X=flip, ...)
```

**Pros:**
- Intuitivo: 1234567 son las duraciones como en MuseScore
- Curva de aprendizaje mínima

**Cons:**
- Number row requiere estiramiento constante
- Ergonomía subóptima para uso intensivo

**Effort:** Low

### Approach B: Home Row Durations
Duraciones en home row, modifiers en row superior.

```
Row 1:  Trip 2nd 3rd 4th 5th (tuplets via tap-dance)
Row 2:  Esc  W   E   R   T   (W=double, R=repeat, T=tie)
Row 3:  REST 64  32  16  8   Qtr (home row = duraciones frecuentes)
Row 4:  Ctrl .   S   Hlf Whl (dot, slur, half, whole)
```

**Pros:**
- Duraciones más frecuentes (quarter, eighth, half) accesibles sin mover mucho
- Ergonómico para sesiones largas

**Cons:**
- Re-aprender mapping (no es 1=64th)
- Menos intuitivo inicialmente

**Effort:** Medium

### Approach C: Hybrid con Macros
Usar macros para combos frecuentes (voice+duration, articulation+note).

```
Row 1:  N   1   2   3   4   5   (note-input, durations)
Row 2:  Esc 6   7   0   DOT T   (more durations, rest, dot, tie)
Row 3:  GUI ALT CTL SFT S   Q   (mods + slur, halve)
Row 4:  Tri V1  V2  V3  V4  W   (triplet, voices, double)
```

**Pros:**
- Acceso directo a voces sin triple-modifier
- Triplet en tecla dedicada (muy frecuente)

**Cons:**
- Más macros = más complejidad
- Debugging más difícil

**Effort:** Medium-High

## Recommendation

**Approach A (Number Row Literal)** — Start simple.

Razones:
1. **YAGNI**: No sabemos qué shortcuts usarás más hasta probarlo
2. **Muscle memory**: MuseScore users ya tienen 1-7 memorizado
3. **Iteración**: Fácil cambiar después de uso real
4. **Ponytail principle**: La solución más simple que funciona

### Proposed Layout (Left Hand Only)

```
Row 0:  tog11  --   --   --   --          (exit en esquina)
Row 1:  N      1    2    3    4    5      (note-input, durations)
Row 2:  Esc    6    7    0    .    T      (esc, durations, rest, dot, tie)
Row 3:  GUI    ALT  CTL  SFT  S    Q/W    (mods, slur, halve/double td)
Row 4:  Trip   V1   V2   V3   V4   R      (triplet, voices, repeat)
Row 5:  tog11  <    >    X    J           (exit, hairpins, flip, enharmonic)
Thumbs: Spc    Bsp  Del  --   --   tog11  (play, backspace, delete)
```

### Right Hand: Transparent
`&trans` en todas las teclas — pasa a base layer.
Mano derecha no se usa (está en MIDI keyboard).

### Activation Options

| Method | Pros | Cons |
|--------|------|------|
| Combo desde base | Rápido, no ocupa tecla | Otro combo más |
| Key en magic layer | Descubrible, organizado | Requiere 2 pasos |
| Hold en tecla libre | Un paso | Ocupa tecla base |

**Recomendación**: Combo 3-teclas desde base (como Teams).
Posición: Z+X+C (izquierda inferior) — intuitivo para "modo música".

### New Macros Needed

```c
// Voice selection macros
ms_voice_1: { bindings = <&kp LA(LC(N1))>; }
ms_voice_2: { bindings = <&kp LA(LC(N2))>; }
ms_voice_3: { bindings = <&kp LA(LC(N3))>; }
ms_voice_4: { bindings = <&kp LA(LC(N4))>; }

// Triplet (most common tuplet)
ms_triplet: { bindings = <&kp LC(N3)>; }

// Articulations (tap Shift+key)
ms_staccato: { bindings = <&kp LS(S)>; }
ms_accent:   { bindings = <&kp LS(V)>; }
ms_tenuto:   { bindings = <&kp LS(N)>; }
ms_marcato:  { bindings = <&kp LS(O)>; }
```

**Nota**: Las articulations podrían ser teclas directas si Shift está en thumb hold. Evaluar en uso real.

### Behaviors Needed

```c
// Halve/Double duration tap-dance
ms_halve_double_td: {
    compatible = "zmk,behavior-tap-dance";
    bindings = <&kp Q>, <&kp W>;  // 1t=halve, 2t=double
}

// Key + exit layer (reuse pattern from teams)
ms_key_exit: {
    compatible = "zmk,behavior-macro-one-param";
    bindings = <&macro_param_1to1 &kp MACRO_PLACEHOLDER &tog 11>;
}
```

## Risks

1. **Collision con combos existentes**: Z+X+C podría interferir. Verificar `require-prior-idle-ms`.
2. **Right hand pass-through**: Si accidentalmente se toca el lado derecho, pasan teclas base. Podría ser confuso. Alternativa: `&none` pero pierde funcionalidad si necesitas algo.
3. **Complexity creep**: Tentación de agregar más shortcuts. Mantener minimal viable primero.

## Ready for Proposal

**Yes** — Hay suficiente claridad para definir:
- Layer index: 11
- Activation: Combo Z+X+C
- Layout: Number row literal para duraciones
- Right hand: Transparent
- Macros: 8 nuevas (4 voices, 1 triplet, 3 tuplets opcionales)
- Behaviors: 1 tap-dance, 1 macro paramétrica

### Next Steps
1. Crear proposal con scope exacto
2. Definir spec con layout final
3. Implementar layer + macros
4. Probar con MuseScore real y iterar
