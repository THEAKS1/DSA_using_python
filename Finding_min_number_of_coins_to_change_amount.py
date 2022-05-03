import numpy as np

coins = np.array([1,5,6,9])
total_cost = 10

solution_matrix = np.zeros((len(coins) + 1, total_cost + 1), dtype = int)

for i in range(len(coins) + 1):
    solution_matrix[i][0] = 0
for i in range(total_cost + 1):
    solution_matrix[0][i] = i

for i in range(1, len(coins) + 1):
    for j in range(total_cost + 1):
        # If denomination of coin is greater than the sum, copy the entry of the previous row
        if coins[i - 1] > j:
            solution_matrix[i][j] = solution_matrix[i - 1][j]
        # Else take the minimum of the previous row and the number of coins after selecting the current coin
        else:
            solution_matrix[i][j] = min(solution_matrix[i - 1][j], 1 + solution_matrix[i][j - coins[i - 1]])

# For storing the coins that are finally selected            
min_coins = []
i, j = len(coins), total_cost
while True:
    if not j:
        break
    if solution_matrix[i][j] == solution_matrix[i - 1][j]:
        i -= 1
        continue    
    min_coins.append(coins[i - 1])
    j -= coins[i - 1]

print(f"The minimum number of coins selected is {len(min_coins)} and the coins are {min_coins}.")