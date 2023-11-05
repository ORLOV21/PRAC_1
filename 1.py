import numpy as np


def nash_equilibrium(X: np.ndarray):
    from scipy.optimize import linprog

    I=np.array([1 for i in range(len(X))])
    res1 = linprog(I,A_ub=-X,b_ub=-I,method="simplex")  #x
    res2 = linprog(-I,A_ub=X.T,b_ub=I,method="simplex") #y
    g=-1/res2.fun
    G = I*g
    P = G*res1.x
    Q = G*res2.x
    return g,P,Q
    

a=np.array([[4,3,1,6,10,10],[0,8,2,6,4,7],[6,4,6,4,6,0],[2,10,5,4,4,7],[2,4,0,10,0,9],[1,4,0,3,9,8]])
a=np.array([[4,7],[5,3]])
print(nash_equilibrium(a))


