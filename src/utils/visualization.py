"""
Módulo para visualização do mercado e caminhos.
"""
import tkinter as tk
import random
import time
from data.market_graph import MarketGraph
from algorithms.bfs import bfs
from algorithms.dfs import dfs


class MarketApp:
    def __init__(self, root):
        """
        Inicializa a aplicação com janela, canvas e botões.
        
        Args:
            root: Janela principal do tkinter
        """
        self.root = root
        self.root.title("Gestor de Filas em Mercados Inteligentes")
        self.cell_size = 50
        self.grid_size = (5, 5)  # (linhas, colunas)
        self.start = (0, 0)
        self.cashiers = [(4, 4), (4, 0), (0, 4)]
        self.cashier_load = {}
        self.blocked = []

        self._setup_ui()
        self.graph = MarketGraph()
        self.reset()

    def _setup_ui(self):
        """Configura o canvas, botões e label da interface."""
        canvas_width = self.grid_size[1] * self.cell_size + 20
        canvas_height = self.grid_size[0] * self.cell_size + 20
        self.canvas = tk.Canvas(self.root, width=canvas_width, height=canvas_height,
                                bg="lightgray", highlightthickness=2, highlightbackground="black")
        self.canvas.pack(pady=10)

        btn_frame = tk.Frame(self.root, bg="lightgray")
        btn_frame.pack(fill=tk.X)
        buttons = [
            ("Executar BFS", self.run_bfs, "lightblue"),
            ("Executar DFS", self.run_dfs, "lightgreen"),
            ("Novos Bloqueios", self.generate_random_blocks, "orange"),
            ("Resetar", self.reset, "salmon")
        ]
        for text, command, bg in buttons:
            tk.Button(btn_frame, text=text, command=command, bg=bg).pack(side=tk.LEFT, padx=5, pady=5)

        self.result_label = tk.Label(self.root, text="Aguardando ação...", font=("Arial", 12), bg="lightgray")
        self.result_label.pack(pady=5)

    def generate_graph(self):
        """Cria o grafo do mercado com base no grid e bloqueios."""
        self.graph = MarketGraph()
        rows, cols = self.grid_size
        for i in range(rows):
            for j in range(cols):
                vertex = (i, j)
                if vertex in self.blocked:
                    continue
                if i < rows - 1 and (i + 1, j) not in self.blocked:
                    self.graph.add_edge(vertex, (i + 1, j))
                if j < cols - 1 and (i, j + 1) not in self.blocked:
                    self.graph.add_edge(vertex, (i, j + 1))

    def generate_random_blocks(self):
        """Gera bloqueios aleatórios e cargas nos caixas."""
        self.blocked = []
        possible = [(i, j) for i in range(self.grid_size[0]) for j in range(self.grid_size[1])
                    if (i, j) not in [self.start] + self.cashiers]
        self.blocked = random.sample(possible, 5)

        self.cashier_load = {cashier: random.randint(1, 5) for cashier in self.cashiers}

        self.generate_graph()
        self.draw_market()
        self.result_label.config(text="Bloqueios e filas atualizados!")
        print("Bloqueios e filas atualizados!")

    def draw_market(self):
        """Desenha o grid do mercado no canvas."""
        self.canvas.delete("all")
        rows, cols = self.grid_size
        for i in range(rows):
            for j in range(cols):
                x1, y1 = j * self.cell_size + 10, i * self.cell_size + 10
                x2, y2 = x1 + self.cell_size, y1 + self.cell_size
                color = "white"
                text = f"{i},{j}"
                if (i, j) == self.start:
                    color = "limegreen"
                elif (i, j) in self.cashiers:
                    color = "dodgerblue"
                    text += f"\n{self.cashier_load.get((i, j), '?')}p"
                elif (i, j) in self.blocked:
                    color = "crimson"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black", width=2)
                self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=text, font=("Arial", 8))

    def draw_path(self, path):
        """Desenha o caminho no canvas com linhas amarelas."""
        if not path:
            return
        for i in range(len(path) - 1):
            x1 = path[i][1] * self.cell_size + self.cell_size // 2 + 10
            y1 = path[i][0] * self.cell_size + self.cell_size // 2 + 10
            x2 = path[i + 1][1] * self.cell_size + self.cell_size // 2 + 10
            y2 = path[i + 1][0] * self.cell_size + self.cell_size // 2 + 10
            self.canvas.create_line(x1, y1, x2, y2, fill="gold", width=4)

    def run_search(self, algorithm):
        """
        Executa o algoritmo de busca especificado (BFS ou DFS).
        
        Args:
            algorithm: Função de busca (bfs ou dfs)
        """
        self.draw_market()
        start_time = time.time()
        
        if algorithm == bfs:
            path, cashier = bfs(self.graph, self.start, set(self.cashiers))
            name = "BFS"
        else:
            path, cashier = dfs(self.graph, self.start, set(self.cashiers))
            name = "DFS"

        elapsed = (time.time() - start_time) * 1000  # tempo em ms

        if path:
            steps = len(path) - 1
            fila = self.cashier_load.get(cashier, "?")
            msg = f"{name}: {steps} passos até caixa {cashier} (fila: {fila}), {elapsed:.2f}ms"
            print(msg + f": {path}")
            self.result_label.config(text=msg)
            self.draw_path(path)
        else:
            msg = f"{name}: Nenhum caminho encontrado!"
            print(msg)
            self.result_label.config(text=msg)

    def run_bfs(self):
        """Executa a busca em largura."""
        self.run_search(bfs)

    def run_dfs(self):
        """Executa a busca em profundidade."""
        self.run_search(dfs)

    def reset(self):
        """Reseta o mercado, removendo bloqueios e recriando o grafo."""
        self.blocked = []
        self.cashier_load = {cashier: random.randint(1, 5) for cashier in self.cashiers}
        self.generate_graph()
        self.draw_market()
        self.result_label.config(text="Mercado resetado!")
        print("Mercado resetado!")
