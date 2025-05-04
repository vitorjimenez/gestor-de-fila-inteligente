"""
Implementação do algoritmo de Busca em Profundidade (DFS).
"""


def dfs(graph, start, goals):
    """
    Executa busca em profundidade para encontrar um caminho até um dos goals.
    
    Args:
        graph: Instância de MarketGraph
        start: Vértice inicial
        goals: Conjunto de vértices de destino
        
    Returns:
        tuple: (caminho, vértice de destino) ou (None, None) se não encontrar caminho
    """
    if not isinstance(goals, set):
        goals = set(goals)
        
    def dfs_recursive(vertex, path, visited):
        """
        Função recursiva auxiliar para DFS.
        
        Args:
            vertex: Vértice atual
            path: Caminho percorrido até o momento
            visited: Conjunto de vértices visitados
            
        Returns:
            tuple: (caminho, vértice de destino) ou (None, None)
        """
        visited.add(vertex)
        
        if vertex in goals:
            return path, vertex
            
        for neighbor in graph.graph[vertex]:
            if neighbor not in visited:
                result = dfs_recursive(neighbor, path + [neighbor], visited)
                if result:
                    return result
                    
        return None, None
        
    return dfs_recursive(start, [start], set())