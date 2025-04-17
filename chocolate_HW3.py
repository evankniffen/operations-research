import numpy as np
from scipy.optimize import linprog
c = [
    4,    
    4.10, 
    4.10,
    3,
    3.05,  
    3.20,
    0.20,
    0.20,  
    0.10, 
    0.10   
]
A_eq = [
    [1, 0, 0, 0, 0, 0, -1,  0,  0,  0], 
    [0, 1, 0, 0, 0, 0,  1, -1,  0,  0], 
    [0, 0, 1, 0, 0, 0,  0,  1,  0,  0],  
    [0, 0, 0, 1, 0, 0,  0,  0, -1,  0],   
    [0, 0, 0, 0, 1, 0,  0,  0,  1, -1],   
    [0, 0, 0, 0, 0, 1,  0,  0,  0,  1]  
]
b_eq = [50, 60, 55, 20, 50, 20]
A_ineq = [
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0]   
]
b_ineq = [100, 100, 100]
geq0 = [(0, None)] * 10

res = linprog(c, A_ub=A_ineq, b_ub=b_ineq,
                 A_eq=A_eq, b_eq=b_eq, bounds=geq0, method='highs')

print("monies:", res.fun)
print("sol :", res.x)
