from src import classes

vf_formulas = {
    "VF": None,
    "VI": "a * t / 2 + x / t",
    "A": "2 * x / t - vi",
    "T": "(vi**2 + 2 * a * x)**0.5",
    "X": "vi + a * t"
}

vi_formulas = {
    "VF": "x / t - a * t / 2",
    "VI": None,
    "A": "2 * x / t - vf",
    "T": "(vf**2 - 2 * a * x)**0.5",
    "X": "vf - a * t"
}

a_formulas = {
    "VF": "2 * (x - vi * t) / t**2", 
    "VI": "2 * (vf * t - x) / t**2",
    "A": None,
    "T": "((vf**2) - (vi**2)) / (2 * x)",
    "X": "(vf - vi) / t"
}

t_formulas = {
    "VF": "(-vi + (vi**2 + 2 * a * x)**0.5) / a",
    "VI": "(vf + (vf**2 - 2 * a * x)**0.5) / a",
    "A": "2 * x / (vf + vi)",
    "T": None,
    "X": "(vf - vi) / a"  
}

x_formulas = {
    "VF": "vi * t + a * t**2 / 2",
    "VI": "vf * t - a * t**2 / 2",
    "A": "t * (vf + vi) / 2",
    "T": "(vf**2 - vi**2) / (2 * a)",
    "X": None
}

# Create objects to store the formulas
vf_obj = classes.FormulaHandler("VF", vf_formulas)
vi_obj = classes.FormulaHandler("VI", vi_formulas)
a_obj = classes.FormulaHandler("A", a_formulas)
t_obj = classes.FormulaHandler("T", t_formulas)
x_obj = classes.FormulaHandler("X", x_formulas)

def solve_missing_variable_mruv(index, variables):
    vf, vi, a, t, x = [var.value for var in variables]
    variables = [var for var in variables if var.short_name != index]
    for variable in variables:
        if not variable.state:
            formula = None
            formula_str = None
            if index == "VF":
                formula_str = vf_obj.get_formula(variable.short_name)
                formula = eval(formula_str)
            elif index == "VI":
                formula_str = vi_obj.get_formula(variable.short_name)
                formula = eval(formula_str)
            elif index == "A":
                formula_str = a_obj.get_formula(variable.short_name)
                formula = eval(formula_str)
            elif index == "T":
                formula_str = t_obj.get_formula(variable.short_name)
                formula = eval(formula_str)
            elif index == "X":
                formula_str = x_obj.get_formula(variable.short_name)
                formula = eval(formula_str)
            return formula, formula_str
    return None, None