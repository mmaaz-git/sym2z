from sympy import *
from sym2z import check_feasibility

x = Symbol('x')
y = Symbol('y')

"""
Checking linear inequalities
"""
print(check_feasibility([x+y<1]))
print(check_feasibility([x+y<1, x > 0, y > 0, x + 2*y > 2]))

"""
Checking non-linear (polynomial) inequalities
"""
print(check_feasibility([x**2 + y**2 > 0, x*y < 1]))

"""
Checking inequalities with boolean operators
"""
print(check_feasibility(Or(x**2 + y**2 > 0, x*y < 1)))
print(check_feasibility([Not(x**2 + y**2 > 0), x*y < 1]))

"""
Checking linear inequalities with integer variables
"""
x = Symbol('x', integer=True)
y = Symbol('y', integer=True)
z = Symbol('z', integer=False)
print(check_feasibility([x+y<1, x > 0, y > 0]))
print(check_feasibility([x+z+y<1, x > 0, y > 0]))

"""
Checking polynomial inequalities with integer variables
"""
print(check_feasibility([x**2 + y**2 > 0, x*y < 1, x>0]))
