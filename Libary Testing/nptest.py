import numpy as np
from sympy import sympify
import sympy as sym
'''
z = z1, z2, z3 = sym.symbols('z:3')
expr2 = x*y*(z1 + z2 + z3)
func2(1, 2, (3, 4, 5))
'''
from sympy.parsing.sympy_parser import parse_expr

#def f(x):
#    return x*x
expression = "x*x"

x, y = sym.symbols('x y')

expr = parse_expr(expression)

f = sym.lambdify([x], expr)

X = np.arange(-200,100,1)
Y = f(X)

print(Y)
