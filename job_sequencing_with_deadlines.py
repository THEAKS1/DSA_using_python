def MergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        MergeSort(left)
        MergeSort(right)
        
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i][1] > right[j][1]:
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


arr = [["a", 20, 4],
        ["b", 10, 1],
        ["c", 40, 1],
        ["d", 30, 1]]
MergeSort(arr)

max_dl = 0
for i in arr:
    if i[2] > max_dl:
        max_dl = i[2]

output = [False] * max_dl
for i in arr:
    j = i[2] - 1
    while j >= 0:
        if not output[j]:
            output[j] = i[0]
            break
        j -= 1

for i in output:
    if i:
        print(i, end = " ")