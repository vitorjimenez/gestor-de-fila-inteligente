
from collections import deque


class MarketGraph:
   
    
    def __init__(self):
        
        self.graph = {}

    def add_vertex(self, vertex):
        
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, v1, v2):
        
        self.add_vertex(v1)
        self.add_vertex(v2)
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)
    
    def get_vertices(self):
        
        return list(self.graph.keys())
    
    def get_neighbors(self, vertex):
        
            list: Lista de vizinhos do vértice
        """
        if vertex in self.graph:
            return self.graph[vertex]
        return []
