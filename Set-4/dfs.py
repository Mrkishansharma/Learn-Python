class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {vertex: [] for vertex in range(vertices)}

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def dfs(self, start):
        visited = [False] * self.vertices
        stack = [start]
        
        while stack:
            vertex = stack.pop()
            if not visited[vertex]:
                print(vertex, end=" ")
                visited[vertex] = True
                for neighbor in self.adj_list[vertex]:
                    if not visited[neighbor]:
                        stack.append(neighbor)

g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)

print("DFS traversal starting from vertex 0:")
g.dfs(0)
