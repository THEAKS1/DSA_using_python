def MergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        MergeSort(left)
        MergeSort(right)
        
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i][2] > right[j][2]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
            
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def knapsack(arr, m, i, profit):
    if m <= 0:
        return profit
    if arr[i][1] <= m:
        profit += arr[i][0]
        m -= arr[i][1]
    else:
        profit += arr[i][2] * m
        m = 0
    return knapsack(arr, m, i + 1, profit)

m = 60

arr = [[70, 20],
       [80, 30],
       [90, 40],
       [200, 70]]

for i in arr:
    i.append(i[0] / i[1])

MergeSort(arr)

profit = knapsack(arr, m, 0, 0)

print(profit)