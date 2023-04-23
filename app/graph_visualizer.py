import matplotlib.pyplot as plt
import networkx as nx


class GraphVisualizer:
    def __init__(self, graph):
        self.graph = graph

    def visualize(self):
        nx.draw(self.graph, with_labels=True, node_color="skyblue", edge_color="gray", font_weight="bold",
                font_color="red")
        plt.show()
