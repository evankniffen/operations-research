import numpy as np
from scipy.optimize import linprog

def main_linprog():
    c = np.array([0,0,0,0,0,0,0,-1,-1])
    ub = [4,6,4,4,2,6,1,2,6]
    bounds = [(0,u) for u in ub]
    A_eq = np.array([
        [ 1,  0, -1, -1, -1,  0,  0,  0,  0],
        [ 0,  1,  1,  0,  0, -1, -1,  0,  0],
        [ 0,  0,  0,  1,  0,  1,  0, -1,  0],
        [ 0,  0,  0,  0,  1,  0,  1,  0, -1],
    ])
    b_eq = np.zeros(4)
    res = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')
    if res.success:
        z = -res.fun
        flows = res.x
        print("z =", z)
        print("flows vector =", flows)
    else:
        print("All bad no good", res.message)

if __name__=="__main__":
    main_linprog()
