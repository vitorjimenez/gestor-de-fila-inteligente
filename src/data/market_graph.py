
from collections import deque

class MarketGraph:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Filas em Mercados Inteligentes")
        self.cell_size = 50
        self.rows, self.cols = 5, 5

        self.canvas = tk.Canvas(root, width=self.cols * self.cell_size + 20, 
                                height=self.rows * self.cell_size + 20, 
                                bg="lightgray", highlightthickness=2, highlightbackground="black")
        self.canvas.pack(pady=10)

        btn_frame = tk.Frame(root, bg="lightgray")
        btn_frame.pack(fill=tk.X)
        tk.Button(btn_frame, text="Executar BFS", command=self.run_bfs, bg="lightblue").pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(btn_frame, text="Executar DFS", command=self.run_dfs, bg="lightgreen").pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(btn_frame, text="Novos Bloqueios", command=self.random_blocks, bg="orange").pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(btn_frame, text="Resetar", command=self.reset, bg="salmon").pack(side=tk.LEFT, padx=5, pady=5)

        self.result_label = tk.Label(root, text="Aguardando ação...", font=("Arial", 12), bg="lightgray")
        self.result_label.pack(pady=5)

        self.start = (0, 0)
        self.cashiers = [(4, 4), (4, 0), (0, 4)]
        self.cashier_load = {}
        self.generate_random_cashier_loads()

        self.blocked = []
        self.graph = MarketGraph()
        self.setup_market()
        self.random_blocks()
        self.draw_market()

    def generate_random_cashier_loads(self):
        self.cashier_load = {cashier: random.randint(1, 5) for cashier in self.cashiers}

    def setup_market(self):
        self.graph = MarketGraph()
        for i in range(self.rows):
            for j in range(self.cols):
                vertex = (i, j)
                if vertex in self.blocked:
                    continue
                if i < self.rows - 1 and (i + 1, j) not in self.blocked:
                    self.graph.add_edge(vertex, (i + 1, j))
                if j < self.cols - 1 and (i, j + 1) not in self.blocked:
                    self.graph.add_edge(vertex, (i, j + 1))

    def random_blocks(self):
        self.blocked = []
        self.generate_random_cashier_loads()
        possible = [(i, j) for i in range(self.rows) for j in range(self.cols) 
                    if (i, j) not in [self.start] + self.cashiers]
        self.blocked = random.sample(possible, 5)
        self.setup_market()
        self.draw_market()
        self.result_label.config(text="Bloqueios e filas atualizados!")

    def draw_market(self):
        self.canvas.delete("all")
        for i in range(self.rows):
            for j in range(self.cols):
                x1, y1 = j * self.cell_size + 10, i * self.cell_size + 10
                x2, y2 = x1 + self.cell_size, y1 + self.cell_size
                color = "white"
                if (i, j) == self.start:
                    color = "limegreen"
                elif (i, j) in self.cashiers:
                    color = "dodgerblue"
                elif (i, j) in self.blocked:
                    color = "crimson"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black", width=2)
                text = f"{i},{j}"
                if (i, j) in self.cashiers:
                    text += f"\n{self.cashier_load.get((i, j), '?')}p"
                self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=text, font=("Arial", 8))

    def draw_path(self, path):
        if not path:
            return
        for i in range(len(path) - 1):
            x1 = path[i][1] * self.cell_size + self.cell_size // 2 + 10
            y1 = path[i][0] * self.cell_size + self.cell_size // 2 + 10
            x2 = path[i + 1][1] * self.cell_size + self.cell_size // 2 + 10
            y2 = path[i + 1][0] * self.cell_size + self.cell_size // 2 + 10
            self.canvas.create_line(x1, y1, x2, y2, fill="gold", width=4)

    def run_bfs(self):
        self.draw_market()
        start_time = time.time()
        paths = {}
        for cashier in self.cashiers:
            path, found = self.graph.bfs(self.start, {cashier})
            if path:
                paths[cashier] = path
        end_time = time.time()

        if paths:
            best_cashier = min(paths, key=lambda c: (self.cashier_load.get(c, float('inf')), len(paths[c])))
            best_path = paths[best_cashier]
            steps = len(best_path) - 1
            elapsed = (end_time - start_time) * 1000
            msg = f"BFS: {steps} passos até caixa {best_cashier} (fila: {self.cashier_load[best_cashier]}), {elapsed:.2f}ms"
            print(msg + f": {best_path}")
            self.result_label.config(text=msg)
            self.draw_path(best_path)
        else:
            msg = "BFS: Nenhum caminho encontrado!"
            print(msg)
            self.result_label.config(text=msg)

    def run_dfs(self):
        self.draw_market()
        start_time = time.time()
        paths = {}
        for cashier in self.cashiers:
            path, found = self.graph.dfs(self.start, {cashier})
            if path:
                paths[cashier] = path
        end_time = time.time()

        if paths:
            best_cashier = min(paths, key=lambda c: (self.cashier_load.get(c, float('inf')), len(paths[c])))
            best_path = paths[best_cashier]
            steps = len(best_path) - 1
            elapsed = (end_time - start_time) * 1000
            msg = f"DFS: {steps} passos até caixa {best_cashier} (fila: {self.cashier_load[best_cashier]}), {elapsed:.2f}ms"
            print(msg + f": {best_path}")
            self.result_label.config(text=msg)
            self.draw_path(best_path)
        else:
            msg = "DFS: Nenhum caminho encontrado!"
            print(msg)
            self.result_label.config(text=msg)

    def reset(self):
        self.blocked = []
        self.generate_random_cashier_loads()
        self.setup_market()
        self.draw_market()
        self.result_label.config(text="Mercado resetado com novas filas!")
        print("Mercado resetado!")
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
    
    def get_neighbors(self, vertex): "Lista de vizinhos"