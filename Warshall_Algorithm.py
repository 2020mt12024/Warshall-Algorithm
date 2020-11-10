import numpy as np

def warshall(x):
    n = x.shape[0]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                x[i,j] = x[i,j] or (x[i,k] and x[k,j])
    return x     

r = np.array([[0,1,0,0],[1,0,1,0],[0,0,0,1],[1,0,0,0]],dtype=bool)
print("Relation R:")
print(1*r)
r_star = warshall(r)
print("Transitive Closure of Relation R by Warshall's Algorithm':")   
print(1*r_star)       
