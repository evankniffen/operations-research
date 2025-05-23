import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

def main_scipy():
    c = np.array([42,70,930,710,
                  340,43,120,7,
                  560,32,40,9,
                  71,760,5,80,
                  10,20,60,85])
    
    A = np.array([
        [1,0,0,0, 1,0,0,0, 1,0,0,0, 1,0,0,0, 0,0,0,0],
        [0,1,0,0, 0,1,0,0, 0,1,0,0, 0,1,0,0, 0,0,0,0],
        [0,0,1,0, 0,0,1,0, 0,0,1,0, 0,0,1,0, 0,0,0,0],
        [0,0,0,1, 0,0,0,1, 0,0,0,1, 0,0,0,1, 0,0,0,0],
        [1,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, -1,0,0,0],
        [0,1,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, -1,0,0,0],
        [0,0,1,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, -1,0,0,0],
        [0,0,0,1, 0,0,0,0, 0,0,0,0, 0,0,0,0, -1,0,0,0],
        [0,0,0,0, 1,0,0,0, 0,0,0,0, 0,0,0,0, 0,-1,0,0],
        [0,0,0,0, 0,1,0,0, 0,0,0,0, 0,0,0,0, 0,-1,0,0],
        [0,0,0,0, 0,0,1,0, 0,0,0,0, 0,0,0,0, 0,-1,0,0],
        [0,0,0,0, 0,0,0,1, 0,0,0,0, 0,0,0,0, 0,-1,0,0],
        [0,0,0,0, 0,0,0,0, 1,0,0,0, 0,0,0,0, 0,0,-1,0],
        [0,0,0,0, 0,0,0,0, 0,1,0,0, 0,0,0,0, 0,0,-1,0],
        [0,0,0,0, 0,0,0,0, 0,0,1,0, 0,0,0,0, 0,0,-1,0],
        [0,0,0,0, 0,0,0,0, 0,0,0,1, 0,0,0,0, 0,0,-1,0],
        [0,0,0,0, 0,0,0,0, 0,0,0,0, 1,0,0,0, 0,0,0,-1],
        [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,1,0,0, 0,0,0,-1],
        [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,1,0, 0,0,0,-1],
        [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,1, 0,0,0,-1],
        [0,0,0,0, 0,1,0,0, 0,0,0,0, 0,0,0,0, 0,1,1,0]
    ])
    
    lb_cons = np.array([1,1,1,1] + [-np.inf]*16 + [-np.inf])
    ub_cons = np.array([1,1,1,1] + [0]*16 + [2])
    
    cons = LinearConstraint(A, lb_cons, ub_cons)
    bounds_obj = Bounds(np.zeros(20), np.ones(20))
    integrality = np.ones(20, dtype=int)
    
    res = milp(c=c, integrality=integrality, bounds=bounds_obj, constraints=cons)
    if res.success:
        sol = res.x
        print("z =", res.fun)
        assign = sol[:16].reshape((4,4))
        y_sol = sol[16:]
        for i in range(4):
            jobs = np.where(assign[i] > 0.5)[0] + 1
            print(f"M{i+1}: Jobs = {jobs}")
    else:
        print("All bad no good", res.message)

if __name__ == "__main__":
    main_scipy()
