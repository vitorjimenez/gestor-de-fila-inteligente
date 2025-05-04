Gestor de Filas Inteligentes
Descrição
Este projeto simula um mercado inteligente modelado como um grafo, utilizando os algoritmos Busca em Largura (BFS) e Busca em Profundidade (DFS) para guiar um atendente virtual até um caixa ideal, otimizando o fluxo de clientes e reduzindo filas. A interface gráfica, desenvolvida com tkinter, permite visualizar o mercado, os caminhos calculados e os bloqueios aleatórios que simulam filas cheias ou áreas interditadas.
Estrutura do Projeto
project_grafos/
│── src/
│   ├── algorithms/
│   │   ├── bfs.py         # Implementação do algoritmo BFS
│   │   └── dfs.py         # Implementação do algoritmo DFS
│   ├── data/
│   │   └── market_graph.py # Classe base para o grafo do mercado
│   ├── utils/
│   │   └── visualization.py # Interface gráfica e lógica de simulação
│   └── main.py            # Ponto de entrada do programa
│── tests/
│   ├── test_bfs.py        # Testes unitários para BFS
│   └── test_dfs.py        # Testes unitários para DFS
│── requirements.txt       # Dependências do projeto
└── README.md              # Documentação

Requisitos

Linguagem: Python 3.6 ou superior
Bibliotecas:
tkinter (incluída no Python padrão para interface gráfica)
collections (para filas no BFS)
random (para bloqueios aleatórios)
time (para medir desempenho)
unittest (para testes unitários)


Ferramentas: VSCode, Git

Como Instalar e Executar

Clone o repositório:git clone https://github.com/vitorjimenez/gestor-de-fila-inteligente.git
cd project_grafos


Verifique o Python:
Certifique-se de ter Python 3.6+ instalado. Teste com:python --version




Execute o programa:
Abra o projeto no VSCode e rode src/main.py:python src/main.py


Uma janela gráfica será aberta com o simulador de filas.


Execute os testes:
No terminal, rode:python -m unittest tests/test_bfs.py
python -m unittest tests/test_dfs.py





Funcionalidades

Modelagem de um mercado 5x5 como grafo com vértices (células) e arestas (corredores).
Uso de BFS para encontrar o caminho mais curto até um dos três caixas.
Uso de DFS para explorar rotas alternativas até os caixas.
Interface gráfica com tkinter mostrando:
Início (verde limão em (0,0))
Caixas (azul em (4,4), (4,0), (0,4))
Bloqueios (vermelho, 5 aleatórios)
Caminhos (amarelo)


Geração de bloqueios aleatórios simulando filas cheias.
Feedback com número de passos, caixa alcançado e tempo de execução.

Cronograma de Execução



Etapa
Atividades
Prazo
Status



1
Definir o objetivo
24/04/2025
Concluído


2
Seleção dos algoritmos (BFS/DFS)
30/04/2025
Concluído


3
Escolha das tecnologias
05/05/2025
Concluído


4
Criação da estrutura de pastas
10/05/2025
Concluído


5
Implementação do grafo (market_graph.py)
20/05/2025
Concluído


6
Implementação dos algoritmos (bfs.py, dfs.py)
25/05/2025
Concluído


7
Implementação da interface (visualization.py)
30/05/2025
Concluído


8
Testes e validação (test_bfs.py, test_dfs.py)
05/06/2025
A fazer


9
Documentação e apresentação (README.md)
10/06/2025
A fazer


Integrantes

Nicolas Santana (Gerente de Projeto): Definição do escopo, planejamento e acompanhamento.
Vinicius Cerqueira (Desenvolvedor Backend): Modelagem do grafo e implementação de BFS/DFS.
Vitor Jimenez (Desenvolvedor Frontend): Design e implementação da interface gráfica.

Licença
[Adicione uma licença, se aplicável, ex.: MIT ou GPL]
Contato
Para dúvidas ou contribuições, entre em contato via GitHub ou e-mail dos integrantes.
