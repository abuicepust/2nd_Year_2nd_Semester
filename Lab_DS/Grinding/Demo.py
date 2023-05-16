#Problem-9: Write a program to find the shortest path from a graph using Kruskal’s Algorithm
# Kruskal Algorithm  in Python
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # Search function

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    #  Applying Kruskal algorithm
    def kruskal_algo(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        print("The sortest path : ")
        for u, v, weight in result:
            print("%d - %d: %d" % (u, v, weight))


g = Graph(7)
g.add_edge(0, 1, 25)
g.add_edge(0, 5, 10)
g.add_edge(1, 0, 25)
g.add_edge(1, 2, 14)
g.add_edge(1, 6, 12)
g.add_edge(2, 1, 14)
g.add_edge(2, 3, 11)
g.add_edge(3, 6, 17)
g.add_edge(3, 4, 20)
g.add_edge(4, 3, 20)
g.add_edge(4, 6, 22)
g.add_edge(4, 5, 23)
g.add_edge(5, 4, 23)
g.add_edge(5, 0, 10)
g.add_edge(6, 1, 12)
g.add_edge(6, 3, 17)
g.add_edge(6, 4, 22)
g.kruskal_algo()

