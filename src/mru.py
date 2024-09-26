# Definición de las fórmulas
formulas = {
    "X": lambda v, t: v * t,
    "V": lambda x, t: x / t if t != 0 else None,
    "T": lambda x, v: x / v if v != 0 else None
}

def solve_missing_variable_mru(missing_variable, variables):
    values = {var.short_name: var.value for var in variables}

    if missing_variable == "X":
        v = values.get("V")
        t = values.get("T")
        if v is not None and t is not None:
            return formulas["X"](v, t), "X = V * T"
    elif missing_variable == "V":
        x = values.get("X")
        t = values.get("T")
        if x is not None and t is not None:
            return formulas["V"](x, t), "V = X / T"
    elif missing_variable == "T":
        x = values.get("X")
        v = values.get("V")
        if x is not None and v is not None:
            return formulas["T"](x, v), "T = X / V"

    return None, None  # No se pudo calcular
