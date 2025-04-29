
class Graph:
    
    def __init__(self, path):
        # Read the adjacency matrix from the file
        with open(path, 'r') as file:
            self.adj_matrix = [list(map(int, line.split())) for line in file.readlines()]
        
        # Set the size of the graph based on the matrix dimensions
        self.size = len(self.adj_matrix)
        
        # Initialize vertex data with empty strings
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.vertex_data = [alphabet[i - 1] for i in range(self.size)]
        self.vertex_data[0] = 's'
        self.vertex_data[-1] = 't'


    def dfs(self, s, t, visited=None, path=None):
        if visited is None:
            visited = [False] * self.size
        if path is None:
            path = []

        visited[s] = True
        path.append(s)

        if s == t:
            return path

        for ind, val in enumerate(self.adj_matrix[s]):
            if not visited[ind] and val > 0:
                result_path = self.dfs(ind, t, visited, path.copy())
                if result_path:
                    return result_path

        return None

    def fordFulkerson(self, source, sink):
        max_flow = 0

        path = self.dfs(source, sink)
        while path:
            path_flow = float("Inf")
            for i in range(len(path) - 1):
                u, v = path[i], path[i + 1]
                path_flow = min(path_flow, self.adj_matrix[u][v])

            for i in range(len(path) - 1):
                u, v = path[i], path[i + 1]
                self.adj_matrix[u][v] -= path_flow
                self.adj_matrix[v][u] += path_flow

            max_flow += path_flow

            path_names = [self.vertex_data[node] for node in path]
            print("Path:", " -> ".join(path_names), ", Flow:", path_flow)

            path = self.dfs(source, sink)

        return max_flow

g = Graph('assets/model/test.txt')
max_flow = g.fordFulkerson(0, g.size - 1)
print("Max Flow:", max_flow)