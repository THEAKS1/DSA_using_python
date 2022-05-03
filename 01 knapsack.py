# 0/1 Knapsack problem (DYNAMIC PROGRAMMING)

import numpy as np

# Input profits and wts arranged in increasing order according to weight
wt = np.array([3,4,5,6])
prft = np.array([2,3,4,1])
k_wt = 8

solution_matrix = np.zeros((len(wt) + 1, k_wt + 1), dtype = int)

for i in range(1, len(wt) + 1):
    for j in range(k_wt + 1):
        if wt[i - 1] > j:
            solution_matrix[i][j] = solution_matrix[i-1][j]
        else:
            solution_matrix[i][j] = max(solution_matrix[i-1][j], prft[i - 1] + solution_matrix[i - 1][j - wt[i - 1]])

selected = []
i, j = len(wt), k_wt
while True:
    if not j:
        break
    if solution_matrix[i][j] == solution_matrix[i - 1][j]:
        i -= 1
        continue
    selected.append(wt[i - 1])
    i, j = i - 1, j - wt[i - 1]

print("The objects with following weigths are selected:", *selected, "\nThe total profit is", solution_matrix[len(wt)][k_wt])
