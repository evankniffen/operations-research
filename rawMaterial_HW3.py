import numpy as np
from scipy.optimize import linprog

c = [-11, -12, 0, 5]
A = [[2, 0, 2, 0], [0, 1, 0, 0], [1, 2, -1, -1], [-1, 1, 0, 0]]
b = [1300, 250, 0, 0]
geq0 = [(0, None), (0, None), (0, None), (0, None)]
res = linprog(c, A_ub=A, b_ub=b, bounds=geq0, method='highs')
print("monies:", res.fun * -1)
print("sol :", res.x)
