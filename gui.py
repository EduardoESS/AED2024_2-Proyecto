import tkinter as tk
from tkinter import messagebox
from suffix_tree import SuffixTree
import matplotlib.pyplot as plt
import networkx as nx
#pip install pygraphviz
#sudo apt install graphviz
#https://graphviz.org/
#pip install matplotlib networkx


class SuffixTreeApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Suffix Tree Visualizer")
        self.setup_gui()

    def setup_gui(self):
        # Entrada de texto base
        tk.Label(self.root, text="Texto Base:").pack(pady=5)
        self.text_input = tk.Entry(self.root, width=50)
        self.text_input.pack(pady=5)

        # Botón para construir el Suffix Tree
        tk.Button(
            self.root, text="Construir Suffix Tree", command=self.build_tree
        ).pack(pady=10)

        # Entrada y botón para buscar patrón
        tk.Label(self.root, text="Patrón de búsqueda:").pack(pady=5)
        self.pattern_input = tk.Entry(self.root, width=50)
        self.pattern_input.pack(pady=5)
        tk.Button(
            self.root, text="Buscar Patrón", command=self.search_pattern
        ).pack(pady=10)

    def build_tree(self):
        text = self.text_input.get()
        if not text:
            messagebox.showerror("Error", "Por favor, ingresa un texto base.")
            return
        self.tree = SuffixTree(text)
        messagebox.showinfo("Éxito", "Suffix Tree construido.")
        self.visualize_tree()

    def visualize_tree(self):
        if not hasattr(self, "tree"):
            messagebox.showerror("Error", "No se ha construido el Suffix Tree.")
            return

    # Visualizar el árbol con un diseño jerárquico
    edges = self.tree.get_tree_structure()
    graph = nx.DiGraph()
    for label, start, end in edges:
        # Evitamos nodos duplicados en la representación gráfica
        if start != -1 and end != -1:
            graph.add_edge(start, end, label=label)

    # Usamos un diseño jerárquico para los nodos
    pos = nx.nx_agraph.graphviz_layout(graph, prog="dot")  # Necesita Graphviz instalado
    labels = nx.get_edge_attributes(graph, "label")
    nx.draw(
        graph,
        pos,
        with_labels=True,
        node_color="lightblue",
        node_size=3000,
        font_size=10,
        font_color="black",
    )
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels, font_size=8)
    plt.title("Visualización del Suffix Tree")
    plt.show()


    def search_pattern(self):
        if not hasattr(self, "tree"):
            messagebox.showerror("Error", "No se ha construido el Suffix Tree.")
            return

        pattern = self.pattern_input.get()
        if not pattern:
            messagebox.showerror("Error", "Por favor, ingresa un patrón para buscar.")
            return

        exists = self.tree.search(pattern)
        messagebox.showinfo(
            "Resultado de la búsqueda",
            f"El patrón {'existe' if exists else 'no existe'} en el texto.",
        )

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = SuffixTreeApp()
    app.run()
