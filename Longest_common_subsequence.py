# Longest Commomon subsequence

import numpy as np

s1 = "abaaba"
s2 = "babbab"

solution_matrix = np.zeros((len(s1) + 1, len(s2) + 1), dtype = int)

for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        if s1[i - 1] == s2[j - 1]:
            solution_matrix[i][j] = 1 + solution_matrix[i - 1][j - 1]
        else:
            solution_matrix[i][j] = max(solution_matrix[i - 1][j], solution_matrix[i][j - 1])

print(f"The longest common subsequence will be of length {solution_matrix[len(s1)][len(s2)]}.")