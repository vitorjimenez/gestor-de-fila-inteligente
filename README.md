# 🚀 SmartQueue Market - Gestor de Filas Inteligentes

**Resumo:** Sistema simulador avançado para otimização de filas em supermercados que utiliza estrutura de grafos e algoritmos de busca (BFS e DFS) para encontrar o caminho mais eficiente até o caixa com menor fila, proporcionando uma experiência mais eficiente aos clientes através de visualização gráfica interativa.

---

## 🎯 Objetivo

O SmartQueue Market resolve o problema de otimização de deslocamento em supermercados, modelando o ambiente como um grafo onde cada nó representa uma posição no espaço e as arestas indicam os possíveis deslocamentos. O sistema permite localizar o caminho mais eficiente até o caixa com menos fila, simular obstáculos e áreas congestionadas, e comparar a eficiência entre diferentes algoritmos de busca.

A motivação surge da necessidade de melhorar a experiência do cliente em ambientes comerciais, reduzindo o tempo gasto em filas e otimizando o fluxo de pessoas. O projeto aplica diretamente os conceitos de estrutura de dados (grafos, filas, pilhas) e algoritmos de busca estudados na disciplina, demonstrando sua aplicação prática em problemas reais.

---

## 👨‍💻 Tecnologias Utilizadas

- **Python 3.6+** - Linguagem principal do projeto
- **Tkinter** - Framework para desenvolvimento da interface gráfica
- **Collections** - Para implementação de filas no BFS
- **Random** - Para geração de bloqueios aleatórios
- **Time** - Para medição de desempenho
- **Unittest** - Para execução de testes unitários
- **Estruturas de Dados Avançadas** - Implementação de grafos, filas e pilhas
- **Algoritmos de Busca** - BFS e DFS otimizados para o contexto de filas

---

## 🗂️ Estrutura do Projeto

```
📦 gestor-de-fila-inteligente
├── 📁 src
│   ├── 📁 algorithms
│   │   ├── bfs.py                # Implementação do algoritmo BFS
│   │   └── dfs.py                # Implementação do algoritmo DFS
│   ├── 📁 data
│   │   └── market_graph.py       # Classe base para o grafo do mercado
│   ├── 📁 utils
│   │   └── visualization.py      # Interface gráfica e lógica de simulação
│   └── main.py                   # Ponto de entrada do programa
├── 📁 tests
│   ├── test_bfs.py               # Testes unitários para BFS
│   └── test_dfs.py               # Testes unitários para DFS
├── 📁 images
│   ├── Logo.png                  # Logo do projeto
│   └── fluxo-aplicacao.png       # Fluxograma da aplicação
├── requirements.txt              # Dependências do projeto
└── README.md                     # Documentação
```

---

## ⚙️ Como Executar

### ✅ Rodando Localmente

1. Clone o repositório:

```bash
git clone https://github.com/vitorjimenez/gestor-de-fila-inteligente.git
cd gestor-de-fila-inteligente
```

2. Verifique a versão do Python (necessário 3.6+):

```bash
python --version
```

3. Execute a aplicação:

```bash
python src/main.py
# ou
python -m src.main
```

4. Para executar os testes unitários:

```bash
python -m unittest tests/test_bfs.py
python -m unittest tests/test_dfs.py
```

> 💡 Uma janela gráfica será aberta automaticamente com o simulador de filas.

---

## 📸 Demonstrações

### Funcionalidades Principais:

- **Modelagem Completa**: Representação do mercado como um grafo em estrutura 11x11
- **Interface Gráfica Interativa**:
  - Visualização do mercado em forma de grade
  - Carrinho inicia na posição (0, 0) - indicado em verde claro 🛒
  - Caixas localizados em (9, 0), (9, 2), (9, 4), (9, 6) e (9, 9) - indicados em azul 💳
  - Bloqueios aleatórios (produtos 📦 em laranja e empilhadeiras 🚜 em cinza)
  - Corredores marrons nas colunas 2, 5 e 8 (linhas 2-5)
  - Caminho calculado mostrado em amarelo 🟡

### Como Usar:
1. Clique em "Adicionar Produtos" para gerar obstáculos aleatórios
2. Use "Mover Carrinho (Aleatório)" ou clique em uma célula livre para reposicionar
3. Selecione "Navegar com BFS" ou "Navegar com DFS" para encontrar o melhor caminho
4. Observe a animação do caminho calculado até o caixa mais próximo
5. Use "Resetar Mercado" para reiniciar a simulação

### Algoritmos Implementados:
- **BFS (Busca em Largura)**: Encontra o caminho mais curto até um caixa disponível
- **DFS (Busca em Profundidade)**: Explora rotas alternativas em caso de obstáculos

---

## 👥 Equipe

| Nome | GitHub | Função |
|------|--------|--------|
| Nicolas Santana | [@nicolas](https://github.com/nicolassantana42) | Gerente de Projeto |
| Vinicius Cerqueira | [@vinicius](https://github.com/ViniCerqueira/ViniCerqueira) | Desenvolvedor Backend |
| Vitor Jimenez | [@vitorjimenez](https://github.com/vitorjimenez) | Desenvolvedor Frontend |

---

## 🧠 Disciplinas Envolvidas

- **Estrutura de Dados I** - Implementação de grafos, filas e pilhas
- **Algoritmos de Busca** - Aplicação prática de BFS e DFS
- **Programação Orientada a Objetos** - Modelagem das classes do sistema

---

## 🏫 Informações Acadêmicas

- **Universidade:** Universidade Braz Cubas
- **Curso:** Ciência da Computação
- **Semestre:** 2º
- **Período:** Manhã/Noite
- **Professora orientadora:** Dra. Andréa Ono Sakai
- **Evento:** Mostra de Tecnologia 1º Semestre de 2025
- **Local:** Laboratório 12
- **Datas:** 05 e 06 de junho de 2025

---

## 📊 Cronograma de Desenvolvimento

| Etapa | Atividades | Prazo | Status |
|-------|-----------|-------|--------|
| 1 | Definição do objetivo | 24/04/2025 | ✅ Concluído |
| 2 | Seleção dos algoritmos (BFS/DFS) | 30/04/2025 | ✅ Concluído |
| 3 | Escolha das tecnologias | 05/05/2025 | ✅ Concluído |
| 4 | Criação da estrutura de pastas | 10/05/2025 | ✅ Concluído |
| 5 | Implementação do grafo | 10/05/2025 | ✅ Concluído |
| 6 | Implementação de BFS e DFS | 12/05/2025 | ✅ Concluído |
| 7 | Interface gráfica | 13/05/2025 | ✅ Concluído |
| 8 | Testes e validação | 13/06/2025 | ✅ Concluído |
| 9 | Documentação | 15/06/2025 | ✅ Concluído |

---

## 🔍 Detalhes Técnicos

### Estrutura do Grafo
- **Vértices**: Representam posições acessíveis no mercado (células da grade 11x11)
- **Arestas**: Representam movimentos possíveis entre vértices adjacentes
- **Restrições**: Corredores marrons, produtos e empilhadeiras bloqueiam o movimento

### Análise de Desempenho
- Comparação de eficiência entre algoritmos BFS e DFS
- Medição de tempo de execução
- Contagem de passos necessários para chegar ao destino

---

## 📄 Licença

MIT License — sinta-se à vontade para utilizar, estudar e adaptar este projeto.
