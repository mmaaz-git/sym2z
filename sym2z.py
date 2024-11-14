import z3
from z3 import Solver, sat
import re

def _sympy_to_z3(expr):
    variables = set(expr.free_symbols)

    expr_str = str(expr)
    for var in variables:
        # Add word boundaries to only replace whole variable names
        var_str = r'\b' + str(var) + r'\b'
        if var.is_integer:
            expr_str = re.sub(var_str, f"z3.Int('{var}')", expr_str)
        else:
            expr_str = re.sub(var_str, f"z3.Real('{var}')", expr_str)

    # Boolean operators
    expr_str = expr_str.replace("And", "z3.And")
    expr_str = expr_str.replace("Or", "z3.Or")
    expr_str = expr_str.replace("Not", "z3.Not")

    return eval(expr_str)

def check_feasibility(system):
    if not isinstance(system, list):
        system = [system]

    s = Solver()
    for expr in system:
        s.add(_sympy_to_z3(expr))

    if s.check() == sat:
        return "sat", s.model()
    else:
        return "unsat", []
