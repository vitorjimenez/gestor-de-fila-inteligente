"""
Implementação da classe MarketGraph para representar o grafo do mercado.
"""
from collections import deque


class MarketGraph:
    """Classe que representa o grafo do mercado como uma lista de adjacência."""
    
    def __init__(self):
        """Inicializa um grafo vazio."""
        self.graph = {}

    def add_vertex(self, vertex):
        """
        Adiciona um vértice ao grafo se ele não existir.
        
        Args:
            vertex: O vértice a ser adicionado
        """
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, v1, v2):
        """
        Adiciona uma aresta bidirecional entre v1 e v2.
        
        Args:
            v1: Primeiro vértice
            v2: Segundo vértice
        """
        self.add_vertex(v1)
        self.add_vertex(v2)
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)
    
    def get_vertices(self):
        """
        Retorna todos os vértices do grafo.
        
        Returns:
            list: Lista de vértices
        """
        return list(self.graph.keys())
    
    def get_neighbors(self, vertex):
        """
        Retorna os vizinhos de um vértice.
        
        Args:
            vertex: O vértice a consultar
            
        Returns:
            list: Lista de vizinhos do vértice
        """
        if vertex in self.graph:
            return self.graph[vertex]
        return []