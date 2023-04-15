import random
import networkx as nx

class Graph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_node(self, node):
        self.graph.add_node(node)

    def add_edge(self, node1, node2):
        self.graph.add_edge(node1, node2)

class RegularGraph(Graph):
    def __init__(self, vertices=0, edges=0, components=0):
        super().__init__()
        self.vertices = vertices
        self.edges = edges
        self.components = components

    def generate(self):
        # Реализуйте генерацию обычного графа здесь
        pass

class Tree(Graph):
    def __init__(self, vertices=0, leaves=0):
        super().__init__()
        self.vertices = vertices
        self.leaves = leaves

    def generate(self):
        # Реализуйте генерацию дерева здесь
        pass

class CompleteGraph(Graph):
    def __init__(self, vertices=0):
        super().__init__()
        self.vertices = vertices

    def generate(self):
        self.graph = nx.complete_graph(self.vertices)

class RandomGraph(Graph):
    def __init__(self):
        super().__init__()

    def generate(self):
        # Реализуйте генерацию случайного графа здесь
        pass
