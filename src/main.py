"""
Ponto de entrada principal para a aplicação Gestor de Filas Inteligente.
"""
import tkinter as tk
from utils.visualization import MarketApp


def main():
    """Função principal que inicia a aplicação."""
    root = tk.Tk()
    app = MarketApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
