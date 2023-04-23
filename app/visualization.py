import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import networkx as nx
from graph_parser import GraphParser
from graph_classes import GraphVertices, GraphConnectedComponents, TreeLeaves, TreeVertices, CompleteGraph, RandomGraph


def visualize_graph(graph):
    G = graph.visualize()
    pos = nx.spring_layout(G)

    fig = plt.figure()
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=12)

    return fig


class GraphVisualization(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Визуализация графа")
        self.geometry("800x600")

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
        graph = graph_classes[graph_type](num)
        graph.generate()

        self.fig.clf()
        self.fig = visualize_graph(graph)
        self.canvas.figure = self.fig
        self.canvas.draw()

    def quit(self):
        self.destroy()
