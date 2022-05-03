# All pairs shortest path (Floyd Warshall Algorithm) 

import numpy as np

D = np.array([[0, 9, -4, np.inf],
                    [6, 0, np.inf, 2],
                    [np.inf, 5, 0, np.inf],
                    [np.inf, np.inf, 1, 0]])
v = len(D) 
for k in range(1,v):
    for i in range(v):
        for j in range(v):
            D[i][j] = min(D[i][j], D[i][k-1] + D[k-1][j])

print(D)