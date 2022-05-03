class Graph():

    def __init__(self, v, graph):
        self.v = v
        self.graph = graph

    def prims_algo(self):
        selected = [False for i in range(self.v)]
        num_edges = 0
        tree = [[0 for i in range(self.v)] for j in range(self.v)]
        selected[0] = True
        print("Edges\tWeight")
        while num_edges < self.v - 1:
            minimum = float("inf")
            for i in range(self.v):
                if selected[i]:
                    for j in range(self.v):
                        if not selected[j] and graph[i][j]:
                            if minimum > graph[i][j]:
                                minimum = graph[i][j]
                                x, y = i, j
            selected[y] = True
            tree[x][y] = 1
            num_edges += 1
            print(str(x + 1) + "-" + str(y + 1) + "\t" + str(graph[x][y]))
        print(tree)

graph = [[0,4,5,2,0,0,0],
      [4,0,0,1,2,0,0],
      [5,0,0,8,0,1,0],
      [2,1,8,0,3,4,7], 
      [0,2,0,3,0,9,0],
      [0,0,1,4,0,0,6],
      [0,0,0,7,9,6,0]]

gr = Graph(7, graph)
gr.prims_algo()