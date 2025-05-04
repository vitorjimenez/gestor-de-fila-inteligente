"""
Testes para o algoritmo DFS.
"""
import unittest
import sys
import os

# Adiciona o diretório raiz do projeto ao caminho Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.data.market_graph import MarketGraph
from src.algorithms.dfs import dfs


class TestDFS(unittest.TestCase):
    """Classe de teste para o algoritmo DFS."""

    def setUp(self):
        """Configura um grafo simples para testes."""
        self.graph = MarketGraph()
        
        # Criar um grafo 3x3 simples
        for i in range(3):
            for j in range(3):
                self.graph.add_vertex((i, j))
        
        # Adicionar arestas horizontais e verticais
        for i in range(3):
            for j in range(2):
                self.graph.add_edge((i, j), (i, j+1))  # Horizontal
                self.graph.add_edge((j, i), (j+1, i))  # Vertical

    def test_dfs_path_exists(self):
        """Testa se o DFS encontra um caminho válido quando ele existe."""
        start = (0, 0)
        goals = {(2, 2)}
        path, goal = dfs(self.graph, start, goals)
        
        # Verificar se encontrou um caminho
        self.assertIsNotNone(path)
        self.assertEqual(goal, (2, 2))
        
        # Verificar se o caminho começa no ponto inicial e termina no objetivo
        self.assertEqual(path[0], start)
        self.assertEqual(path[-1], (2, 2))
        
        # DFS pode não encontrar o caminho mais curto, mas deve encontrar um caminho válido
        self.assertGreaterEqual(len(path), 5)  # Deve ter pelo menos 5 nós

    def test_dfs_multiple_goals(self):
        """Testa se o DFS encontra um dos objetivos quando há múltiplos."""
        start = (0, 0)
        goals = {(1, 1), (2, 2)}
        path, goal = dfs(self.graph, start, goals)
        
        self.assertIsNotNone(path)
        self.assertIn(goal, goals)
        self.assertEqual(path[0], start)
        self.assertEqual(path[-1], goal)

    def test_dfs_unreachable(self):
        """Testa se o DFS retorna None quando não há caminho para o objetivo."""
        # Criar um grafo desconectado
        disconnected_graph = MarketGraph()
        disconnected_graph.add_vertex((0, 0))
        disconnected_graph.add_vertex((1, 1))
        
        path, goal = dfs(disconnected_graph, (0, 0), {(1, 1)})
        
        self.assertIsNone(path)
        self.assertIsNone(goal)


if __name__ == '__main__':
    unittest.main()