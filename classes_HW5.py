import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

def main_scipy():
    c = np.ones(7)
    A_ub = np.array([
        [-1, -1, -1,  0,  0, -1,  0], 
        [ 0, -1,  0, -1,  0, -1, -1], 
        [ 0,  0, -1, -1, -1,  0,  0], 
        [-1,  0,  0,  0,  0,  0,  1], 
        [ 0,  0,  0,  1, -1,  0,  0], 
        [ 0,  0,  1,  0, -1,  0,  0], 
        [ 0,  0,  0,  0,  0,  1, -1] 
    ])
    b_ub = np.array([-2, -2, -2, 0, 0, 0, 0])
    constraint = LinearConstraint(A_ub, -np.inf*np.ones(7), b_ub)
    bounds_obj = Bounds(np.zeros(7), np.ones(7))
    integrality = np.ones(7, dtype=int)
    res = milp(c=c, integrality=integrality, bounds=bounds_obj, constraints=constraint)
    if res.success:
        sol = res.x
        print("z =", sum(sol))
        print("classes vector =", sol)
    else:
        print("All bad no good", res.message)

if __name__=="__main__":
    main_scipy()
