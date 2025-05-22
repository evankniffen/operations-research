import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

def main_scipy():
    edges = [(i,j) for i in range(1,6) for j in range(i+1,7)]
    c = np.array([
        20800,25800,35500,53700,83100,
        22800,27800,37500,54700,
        24800,29800,39500,
        28800,33800,
        33800
    ])
    n = len(edges)
    A = []; b = []
    A.append([1 if i==1 else 0 for (i,j) in edges]); b.append(1)
    A.append([1 if j==6 else 0 for (i,j) in edges]); b.append(1)
    for k in range(2,6):
        row=[]
        for (i,j) in edges:
            if j==k: row.append(1)
            elif i==k: row.append(-1)
            else: row.append(0)
        A.append(row); b.append(0)
    cons = LinearConstraint(np.array(A), b, b)
    bounds = Bounds(0,1)
    integrality = np.ones(n,int)
    res = milp(c=c, integrality=integrality, bounds=bounds, constraints=cons)
    if res.success:
        chosen = [edges[i] for i,v in enumerate(res.x) if v>0.5]
        print("z =", res.fun)
        print("replacement schedule:", chosen)
    else:
        print("All bad no good", res.message)

if __name__=="__main__":
    main_scipy()