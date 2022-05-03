import numpy as np

def printsolution():
    for i in range(n):
        for j in range(n):
            print(m[i][j], end = " ")
        print()

def isSafe(m, row, col):
    for i in range(col):
        if m[row][i]:
            return False

    for i, j in zip(range(row,-1,-1), range(col,-1,-1)):
        if m[i][j]:
            return False

    for i, j in zip(range(row, n), range(col, -1, -1)):
        if m[i][j]:
            return False

    return True

def solveNQUtil(m, col):
    if col >= n:
        v = []
        for i  in m:
            for j in range(len(i)):
                if i[j]:
                    v.append(j+1)
        result.append(v)
        return True

    res = False
    for i in range(n):
        if isSafe(m, i, col):
            m[i][col] = 1

            if solveNQUtil(m, col + 1):
                res = True

        m[i][col] = 0
    
    return res

def solveNQ(m):
    if not solveNQUtil(m,0):
        print("Solution does not exists.")
        return
    print(result)
    print(len(result))

n = int(input("Enter the number of queens: "))
m = np.zeros((n,n), dtype = int)
result = []
solveNQ(m)