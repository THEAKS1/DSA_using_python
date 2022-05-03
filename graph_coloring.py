import numpy as np

def graphColoring(m, vertex):
    if vertex == v:
        return m
    m[vertex] = 1
    for i in range(v):
        if adjMat[vertex][i] and m[i] == m[vertex]:
            m[vertex] += 1
    return graphColoring(m, vertex + 1)

adjMat = np.array([[0,1,1,0,1],
                    [1,0,1,1,1],
                    [1,1,0,1,0],
                    [0,1,1,0,1],
                    [1,1,0,1,0]])
v = len(adjMat)
m = np.zeros(v, int)
m = graphColoring(m,0)

print(m)