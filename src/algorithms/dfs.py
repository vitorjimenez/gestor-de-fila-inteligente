def dfs(self, start, goals):
        visited = set()
        def dfs_recursive(vertex, path):
            visited.add(vertex)
            if vertex in goals:
                return path, vertex
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    result = dfs_recursive(neighbor, path + [neighbor])
                    if result:
                        return result
            return None, None
        return dfs_recursive(start, [start])