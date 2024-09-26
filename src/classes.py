class Variable:
    variables = []
    short_names = []

    def __init__(self, name, state, value, short_name):
        self.name = name
        self.state = state
        self.value = value
        self.short_name = short_name
        Variable.variables.append(self)
        Variable.short_names.append(self.short_name)

class FormulaHandler:
    def __init__(self, variable_name, formulas):
        self.variable_name = variable_name
        self.formulas = formulas

    def get_formula(self, var):
        return self.formulas.get(var)

# Function to check if the system is solvable
def is_solvable(variables):
    available_variables = sum(1 for var in variables if var.state)

    return available_variables >= 3


def is_solvable_MRU(variables):
    available_variables = sum(1 for var in variables if var.state)

    return available_variables >= 2
