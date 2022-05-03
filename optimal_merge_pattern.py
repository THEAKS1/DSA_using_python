class Node:

    def __init__(self, moves, l, r):
        self.moves = moves
        self.lchild = l
        self.rchild = r

def MergeSort(node_arr):
    if len(node_arr) > 1:
        mid = len(node_arr) // 2
        left = node_arr[:mid]
        right = node_arr[mid:]
        MergeSort(left)
        MergeSort(right)
        
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i].moves < right[j].moves:
                node_arr[k] = left[i]
                i += 1
            else:
                node_arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            node_arr[k] = left[i]
            i += 1
            k += 1
            
        while j < len(right):
            node_arr[k] = right[j]
            j += 1
            k += 1

def omp(node_arr):
    for i in range(len(node_arr) - 1):
        MergeSort(node_arr)
        node = Node(0, None, None)
        node.lchild = node_arr[0]
        node.rchild = node_arr[1]
        node_arr.remove(node_arr[0])
        node_arr.remove(node_arr[0])
        node.moves = node.lchild.moves + node.rchild.moves
        node_arr.append(node)
    
    print("Inorder traveresal of the tree is: ", end = "")
    print_tree(node_arr[0])

def print_tree(node_arr):
    if not node_arr:
        return
    print(node_arr.moves, end = " ")
    print_tree(node_arr.lchild)
    print_tree(node_arr.rchild)

arr = [46,35,10,14,78,6,31,2,27]
node_arr = []
for i in arr:
    node_arr.append(Node(i, None, None))
omp(node_arr)

t_moves = 0
root = node_arr[0]
while root.rchild:
    t_moves += root.moves
    root = root.rchild


print("\nTotal number of moves are: ", t_moves)