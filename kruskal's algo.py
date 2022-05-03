class array_node():

    def __init__(self, vi, vj, weight):
        self.vi = vi
        self.vj = vj
        self.weight = weight
        self.selected = False

class Graph():

    def __init__(self, v, graph):
        self.v = v
        self.graph = graph

    def warshall(self, adj):
        path = [[0 for i in range(self.v)] for j in range(self.v)]
        for i in range(self.v):
            for j in range(self.v):
                path[i][j] = adj[i][j]
        for k in range(self.v):
            for i in range(self.v):
                for j in range(self.v):
                    path[i][j] = (path[i][j] | (path[i][k] & path[k][j]))
        return path

    def sort_edges(self, array):
        for i in range(self.num_edges):
            for j in range(i+1, self.num_edges):
                if array[i].weight > array[j].weight:
                    array[i], array[j] = array[j], array[i]
        return array

    def Kruskal_algo(self):
        # Initialisation 
        array = []
        self.num_edges = 0
        for i in range(self.v):
            for j in range(i+1, self.v):
                if self.graph[i][j] > 0:
                    node = array_node(i, j, self.graph[i][j])
                    array.append(node)
                    self.num_edges += 1
        
        if self.num_edges < self.v - 1:
            print("No spanning tree possible.")
            return

        # Sort edges based on their weights
        array = self.sort_edges(array)
        
        tree = [[0 for i in range(self.v)] for j in range(self.v)]

        k, l = 0, 0
        while (k < self.v - 1):
            if not array[l].selected:
                temp = tree
                i, j = array[l].vi, array[l].vj
                temp[i][j], temp[j][i] = 1, 1
                temp = self.warshall(temp)
                flag = False
                for p in range(self.v):
                    if temp[p][p] > 0:
                        flag = True
                if not flag:
                    tree[i][j], tree[j][i] = 1, 1
                    k += 1
                    array[l].selected = True
                    #print(str(i + 1) + "-" + str(j + 1) + "\t" + str(array[l].weight))
            for i in temp:
                print(i)
            print("&*******************&\n")
            l += 1

    

graph = [   [0,4,5,2,0,0,0],
            [4,0,0,1,2,0,0],
            [5,0,0,8,0,1,0],
            [2,1,8,0,3,4,7], 
            [0,2,0,3,0,9,0],
            [0,0,1,4,0,0,6],
            [0,0,0,7,9,6,0]]

gr = Graph(7, graph)
gr.Kruskal_algo()