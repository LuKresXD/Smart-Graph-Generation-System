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
        if self.components == 0:
            self.components = 1
        if self.vertices == 0:
            self.vertices = self.components * random.randint(2, 10)

        for _ in range(self.components):
            nodes = [i for i in range(self.vertices)]
            random.shuffle(nodes)

            for i in range(len(nodes) - 1):
                self.add_edge(nodes[i], nodes[i + 1])

            if self.edges > len(nodes) - 1:
                for _ in range(self.edges - len(nodes) + 1):
                    n1, n2 = random.sample(nodes, 2)
                    self.add_edge(n1, n2)

class Tree(Graph):
    def __init__(self, vertices=0, leaves=0):
        super().__init__()
        self.vertices = vertices
        self.leaves = leaves

    def generate(self):
        if self.vertices == 0:
            self.vertices = random.randint(2, 10)

        nodes = [i for i in range(self.vertices)]
        random.shuffle(nodes)

        for i in range(len(nodes) - 1):
            self.add_edge(nodes[i], nodes[i + 1])

        if self.leaves > 0:
            for _ in range(self.leaves - 1):
                leaf = random.choice(nodes)
                new_node = max(nodes) + 1
                self.add_edge(leaf, new_node)
                nodes.append(new_node)

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
        vertices = random.randint(2, 10)
        edges = random.randint(vertices - 1, vertices * (vertices - 1) // 2)

        nodes = [i for i in range(vertices)]

        for _ in range(edges):
            n1, n2 = random.sample(nodes, 2)
            self.add_edge(n1, n2)
