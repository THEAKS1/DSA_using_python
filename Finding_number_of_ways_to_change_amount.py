import numpy as np

coins = np.array([2,3,5,10])
total_cost = 15

solution_matrix = np.zeros((len(coins) + 1, total_cost + 1), dtype = int)

for i in range(len(coins) + 1):
    solution_matrix[i][0] = 1

for i in range(1, len(coins) + 1):
    for j in range(total_cost + 1):
        # If denomination of coin is greater than the sum, copy the entry of the previous row
        if coins[i - 1] > j:
            solution_matrix[i][j] = solution_matrix[i - 1][j]
        # Else add the previous row sum and the sum of possibiltes after selecting the current coin
        else:
            solution_matrix[i][j] = solution_matrix[i - 1][j] + solution_matrix[i][j - coins[i - 1]]

print(f"There are {solution_matrix[len(coins)][total_cost]} possible ways to produce the change of given amount.")