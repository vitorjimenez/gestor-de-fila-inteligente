# 🧠 Gestor de Filas Inteligentes

Simulador de um mercado inteligente modelado como grafo, com interface gráfica interativa e algoritmos de busca (BFS e DFS) para otimização do atendimento ao cliente.

---

## 📌 Descrição

Este projeto simula um **mercado inteligente** modelado como um **grafo**, utilizando os algoritmos:

- 🔍 **Busca em Largura (BFS)** – para encontrar o caminho mais curto até um caixa.
- 🔍 **Busca em Profundidade (DFS)** – para explorar rotas alternativas.

A interface gráfica foi desenvolvida com **Tkinter**, permitindo a visualização:

- Do mercado em forma de grade 5x5;
- Dos caminhos calculados;
- De bloqueios aleatórios que simulam filas cheias ou áreas interditadas.

---

## 🗂️ Estrutura do Projeto

project_grafos/
├── src/
│ ├── algorithms/
│ │ ├── bfs.py # Implementação do algoritmo BFS
│ │ └── dfs.py # Implementação do algoritmo DFS
│ ├── data/
│ │ └── market_graph.py # Classe base para o grafo do mercado
│ ├── utils/
│ │ └── visualization.py # Interface gráfica e lógica de simulação
│ └── main.py # Ponto de entrada do programa
│
├── tests/
│ ├── test_bfs.py # Testes unitários para BFS
│ └── test_dfs.py # Testes unitários para DFS
│
├── requirements.txt # Dependências do projeto
└── README.md # Documentação

---

## 📦 Requisitos

- **Python**: 3.6 ou superior  
- **Bibliotecas**:
  - `tkinter` (inclusa no Python padrão)
  - `collections` (para filas no BFS)
  - `random` (para bloqueios aleatórios)
  - `time` (para medir desempenho)
  - `unittest` (para testes unitários)
- **Ferramentas recomendadas**: VSCode, Git

---

## 🚀 Como Instalar e Executar

### 2. Verifique o Python:

```bash
python --version

### 3.1 Execute o programa:
python src/main.py
💡 Uma janela gráfica será aberta com o simulador de filas.

### 4.1 Execute os testes unitários:
python -m unittest tests/test_bfs.py
python -m unittest tests/test_dfs.py


### 1. Clone o repositório:

```bash
git clone https://github.com/vitorjimenez/gestor-de-fila-inteligente.git
cd project_grafos
🧩 Funcionalidades
✅ Modelagem de um mercado 5x5 como grafo (vértices e arestas)

✅ Caminho mais curto com BFS

✅ Exploração alternativa com DFS

✅ Interface gráfica com visualização:

🟩 Início: posição (0,0)

🔵 Caixas: (4,4), (4,0), (0,4)

🔴 Bloqueios: 5 aleatórios

🟡 Caminhos: rota percorrida

✅ Geração aleatória de bloqueios simulando filas

✅ Feedback ao usuário com:

Número de passos

Caixa alcançado

Tempo de execução

📆 Cronograma de Execução
Etapa	Atividades	Prazo	Status
1	Definir o objetivo	24/04/2025	✅ Concluído
2	Seleção dos algoritmos (BFS/DFS)	30/04/2025	✅ Concluído
3	Escolha das tecnologias	05/05/2025	✅ Concluído
4	Criação da estrutura de pastas	10/05/2025	✅ Concluído
5	Implementação do grafo (market_graph)	20/05/2025	✅ Concluído
6	Implementação de BFS e DFS	25/05/2025	✅ Concluído
7	Implementação da interface gráfica	30/05/2025	✅ Concluído
8	Testes e validação	05/06/2025	🔜 A fazer
9	Documentação e apresentação	10/06/2025	🔜 A fazer

👥 Integrantes
Nicolas Santana – Gerente de Projeto
Definição do escopo, planejamento e acompanhamento

Vinicius Cerqueira – Desenvolvedor Backend
Modelagem do grafo, algoritmos BFS e DFS

Vitor Jimenez – Desenvolvedor Frontend
Interface gráfica com Tkinter

