import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import networkx as nx
from graph_parser import GraphParser
from graph_classes import GraphVertices, GraphConnectedComponents, TreeLeaves, TreeVertices, CompleteGraph, RandomGraph, \
    Graph
from tkinter import filedialog


def visualize_graph(graph):
    G = graph.visualize()
    pos = nx.spring_layout(G)

    fig = plt.figure()
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=12)

    return fig


class GraphVisualization(tk.Tk):
    def __init__(self):
        super().__init__()

        self.graph = None
        self.title("Визуализация графа")
        self.geometry("1000x800")

        self.create_widgets()

    def create_widgets(self):
        self.query_label = ttk.Label(self, text="Введите запрос:")
        self.query_label.pack(side=tk.TOP, padx=10, pady=10)

        self.query_entry = ttk.Entry(self, width=50)
        self.query_entry.pack(side=tk.TOP, padx=10)

        self.submit_button = ttk.Button(self, text="Отправить", command=self.update_graph)
        self.submit_button.pack(side=tk.TOP, padx=10, pady=10)

        self.fig = plt.figure()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.quit_button = ttk.Button(self, text="Закрыть", command=self.quit)
        self.quit_button.pack(side=tk.BOTTOM)

        self.save_button = ttk.Button(self, text="Сохранить граф", command=self.save_graph)
        self.save_button.pack(side=tk.BOTTOM)

        self.load_button = ttk.Button(self, text="Загрузить граф", command=self.load_graph)
        self.load_button.pack(side=tk.BOTTOM)

    def update_graph_load(self, graph=None):
        if graph is None:
            graph_string = self.query_entry.get()
            parser = GraphParser(graph_string)
            graph_type, parameters = parser.parse()

            graph_classes = {
                "Граф_вершины": GraphVertices,
                "Граф_компоненты_связанности": GraphConnectedComponents,
                "Дерево_листы": TreeLeaves,
                "Дерево_вершины": TreeVertices,
                "Полный_граф": CompleteGraph,
                "Случайный": RandomGraph
            }

            num = parameters.get("num", None)
            graph = graph_classes[graph_type](num)
            graph.generate()

        self.fig.clf()
        self.fig = visualize_graph(graph)
        self.canvas.figure = self.fig
        self.canvas.draw()

    def update_graph(self):
        graph_string = self.query_entry.get()
        parser = GraphParser(graph_string)
        graph_type, parameters = parser.parse()

        graph_classes = {
            "Граф_вершины": GraphVertices,
            "Граф_компоненты_связанности": GraphConnectedComponents,
            "Дерево_листы": TreeLeaves,
            "Дерево_вершины": TreeVertices,
            "Полный_граф": CompleteGraph,
            "Случайный": RandomGraph
        }

        num = parameters.get("num", None)
        self.graph = graph_classes[graph_type](num)  # измените эту строку
        self.graph.generate()

        self.fig.clf()
        self.fig = visualize_graph(self.graph)  # измените эту строку
        self.canvas.figure = self.fig
        self.canvas.draw()

    def save_graph(self):
        filename = filedialog.asksaveasfilename(defaultextension=".sgg",
                                                filetypes=[("Smart Graph Generation files", "*.sgg"),
                                                           ("All files", "*.*")])
        if not filename:
            return
        self.graph.save_to_file(filename)

    def load_graph(self):
        filename = filedialog.askopenfilename(defaultextension=".sgg",
                                              filetypes=[("Smart Graph Generation files", "*.sgg"),
                                                         ("All files", "*.*")])
        if not filename:
            return
        loaded_graph = Graph.load_from_file(filename)
        self.update_graph_load(graph=loaded_graph)
