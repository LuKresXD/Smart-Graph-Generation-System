import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(graph):
    pos = nx.spring_layout(graph.graph)
    nx.draw(graph.graph, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    plt.show()
