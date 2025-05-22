import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

def main_scipy():
    N = 16
    tempA = np.array([10000]*6 + [2000]*4 + [2500]*5 + [0])
    tempB = np.array([8000]*4 + [6000]*8 + [2000]*3 + [0])
    c = -np.concatenate([tempA, tempB])
    A = np.concatenate([1000*np.ones(N), 1200*np.ones(N)])[None, :]
    b = np.array([20000])
    cons = LinearConstraint(A, -np.inf, b)
    bounds = Bounds(0, 1)
    integrality = np.ones(2*N, int)
    res = milp(c=c, integrality=integrality, bounds=bounds, constraints=cons)
    if res.success:
        sol = res.x
        z = -res.fun
        print("z =", z)
        print("Ads on A =", int(sol[:N].sum()))
        print("Ads on B =", int(sol[N:].sum()))
    else:
        print("All bad no good", res.message)

if __name__=="__main__":
    main_scipy()
