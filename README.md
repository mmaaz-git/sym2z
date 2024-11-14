# sym2z
Check feasibility of SymPy systems with Z3

Z3 by Microsoft Research is a powerful satisfiability modulo theories (SMT) solver for checking feasibility (or satisfiability as the computer scientists like to call it) of Boolean expressions with some background theory, e.g., linear arithmetic. Essentially, it can check feasibility of linear or polynomial systems. It will provide a satisfying point, if one exists, or tells you if the system is not satisfiable. SymPy currently cannot check feasibility of some types of systems, like multivariate polynomial inequalities. Currently there is no good way to use SymPy's great computer algebra capabilities alongside Z3's satisfiability checking. This tool converts SymPy systems to Z3 ones and checks their feasibility.

The only function you need to call is `check_feasibility` in the file `sym2z.py`. You can pass it a list of SymPy (in)equalities -- objects in the list are assumed to be "and"-ed together. It will then call Z3 on these expressions. It will return a tuple of a string and a dictionary. The possibilities are:
- If the system is satisfiable, it will return `('sat', {<sympy variable>: <value>, ...})`.
- If the system is not satisfiable, it will return `('unsat', {})`.
- If Z3 returns an unknown result, it will return `('unknown', {})`.

Here are some example usages.

```
>>> x = Symbol('x')
>>> y = Symbol('y')
>>> check_feasibility([x+y<1]) # linear system
('sat', {y: 0, x: 0})
>>> check_feasibility([x**2 + y**2 > 0, x*y < 1]) # polynomial system
('sat', {y: 7, x: 1/8})
```

Z3 uses simplex as the background solver for linear systems and cylindrical algebraic decomposition (CAD) for polynomial systems, along with Boolean satisfiability (SAT) algorithms to "guide"  the search.

It can also use the Boolean operators from SymPy, like `And`, `Or`, `Not`, and will convert them to their Z3 analogs. Note that Z3 can solve arbitrary Boolean expressions of linear or polynomial inequalities, i.e., not just those with 'And'.
```
>>> check_feasibility([Not(x**2 + y**2 > 0), x*y < 1])
('sat', {y: 0, x: 0})
```

It can also handle mixed-integer problems. In SymPy, variables can be declared as integer. This tool will also handle this appropriately.
```
>>> x = Symbol('x', integer=True)
>>> y = Symbol('y', integer=True)
>>> check_feasibility([x+y<1, x > 0, y > 0])
('unsat', {})
```

Mixed-intger linear problems, i.e., mixed-integer linear programs, are solvable by branch-and-bound methods. However, solving polynomial systems over integers may not be possible. This is because this problem is not decidable in general, as proven by Matiyasevich's theorem. Z3 may still be able to find a satisfying solution, or it may tell you it is simply "unknown".

There are more examples in `examples.py`.
