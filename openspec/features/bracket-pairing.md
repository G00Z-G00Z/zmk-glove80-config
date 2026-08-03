# Bracket Pairing

Auto-pairing de brackets con cursor posicionado adentro.

## Problema

Al escribir `()`, `[]`, `{}`, `""`, etc., siempre quiero el cursor adentro.

## Solución

Macro `better_delimiter` que escribe ambos caracteres y mueve el cursor.

## Macro

```
better_delimiter: better_delimiter {
    compatible = "zmk,behavior-macro-two-param";
    #binding-cells = <2>;
    bindings = <&kp PARAM1 &kp PARAM2 &kp LEFT>;
};
```

## Uso

```
&better_delimiter LEFT_PARENTHESIS RIGHT_PARENTHESIS  // ()
&better_delimiter LEFT_BRACKET RIGHT_BRACKET          // []
&better_delimiter LEFT_BRACE RIGHT_BRACE              // {}
&better_delimiter LESS_THAN GREATER_THAN              // <>
&better_delimiter DOUBLE_QUOTES DOUBLE_QUOTES         // ""
&better_delimiter SINGLE_QUOTE SINGLE_QUOTE           // ''
&better_delimiter GRAVE GRAVE                         // ``
```

## Ubicación en Layout

### Base Layer (bottom thumb row)
Teclas dedicadas para los 4 brackets principales:
- `()` 
- `[]`
- `{}`
- `<>`

### Combos
Combos para quotes en posiciones cómodas:
- Double quotes: 4 teclas (ring fingers ambas manos)
- Single quote: 2 teclas verticales
- Backtick: 2 teclas verticales

## Block Quotes

Macros adicionales para code blocks:

### surround_block_quotes
```
""" + Enter + Enter + """ + Up
```
Para docstrings Python o markdown.

### surround_block_grave
```
``` + Enter + Enter + ``` + Up
```
Para code blocks en markdown/Teams.

## Ubicación

- **Macro**: `macros { better_delimiter, surround_block_* }`
- **Uso**: Base layer thumbs, combos
