class Graph():

    def __init__(self, vertices, gra):
        self.V = vertices
        self.graph = gra

    def minDistance(self, dist, Set):
        minimum = float("inf")
        for v in range(self.V):
            if dist[v] <= minimum and Set[v] == False:
                minimum = dist[v]
                min_index = v
        return min_index

    def printout(self, dist):
        for node in range(self.V):
            print (node + 1 , "\t", dist[node]) 


    def dijkstra(self, src):
        dist = [float("inf")] * self.V
        dist[src] = 0
        Set = [False] * self.V

        for cout in range(self.V):
            u = self.minDistance(dist, Set)
            Set[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and Set[v] == False and dist[v] > dist [u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.printout(dist)

# Driver program 

gra = [[0,16,0,0,19,21],
        [16, 0, 5, 6,0,11],
        [0,5,0,10,0,0],
        [0,6,10,0,18,14],
        [19,0,0,18,0,33],
        [21,11,0,14,33,0]]; 

g = Graph(6, gra) 

g.dijkstra(0); 