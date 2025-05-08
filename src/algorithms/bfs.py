from collections import deque

def bfs(self, start, goals):
        visited = set()
        queue = deque([[start]])
        while queue:
            path = queue.popleft()
            vertex = path[-1]
            if vertex in goals:
                return path, vertex
            if vertex not in visited:
                visited.add(vertex)
                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        queue.append(path + [neighbor])
        return None, None
