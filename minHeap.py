class MinHeap:

    def __init__(self):
        self.size = -1
        self.heap = []

    def insert_element(self, element):
        self.heap.append(element)
        self.size += 1
        self.heapUp()

    def heapUp(self):
        parent, current = (self.size - 1) // 2, self.size
        while self.heap[parent] > self.heap[current] and parent >= 0:
            self.heap[parent], self.heap[current] = self.heap[current], self.heap[parent]
            current, parent = parent, (parent - 1) // 2
            
    def heapDown(self):
        current = 0
        lchild = 1
        while self.heap[current] > self.heap[lchild] or self.heap[current] > self.heap[lchild + 1]:
            if self.heap[lchild + 1] > self.heap[lchild]:
                self.heap[current], self.heap[lchild] = self.heap[lchild], self.heap[current]
                current = lchild 
            else:
                self.heap[current], self.heap[lchild + 1] = self.heap[lchild + 1], self.heap[current]
                current = lchild + 1
            lchild = 2 * current + 1
            if lchild + 1 > self.size:
                break

    def extractMin(self):
        minimum = self.heap[0]
        self.heap[0] = self.heap[self.size]
        self.heap.pop(self.size)
        self.size -= 1
        self.heapDown()
        return minimum


    def print_heap(self):
        print(self.heap)
