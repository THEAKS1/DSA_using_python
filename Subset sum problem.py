# Subset sum problem
import numpy as np

arr = np.array([1,4,5,8,9])
tsum = 18

solution_matrix = np.zeros((len(arr) + 1, tsum + 1), dtype = int)

for i in range(len(arr) + 1):
    solution_matrix[i][0] = 1

for i in range(1, len(arr) + 1):
    for j in range(1, tsum + 1):
        if arr[i - 1] > j:
            solution_matrix[i][j] = solution_matrix[i - 1][j]
        else:
            if solution_matrix[i - 1][j]:
                solution_matrix[i][j] = 1
            elif i - 1 == j:
                solution_matrix[i][j] = 1
            else:
                solution_matrix[i][j] = solution_matrix[i - 1][j - arr[i - 1]]

if solution_matrix[len(arr)][tsum]:
    print(f"Yes, the given set contains a subset whose sum is {tsum}.")
else:
    print(f"No, the given set do not contain a subset whose sum is {tsum}.")