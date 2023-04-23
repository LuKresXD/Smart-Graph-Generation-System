import networkx as nx
import random
import math


class Graph:
    def __init__(self):
        self.graph = nx.Graph()

    def visualize(self):
        return self.graph


class GraphVertices(Graph):
    def __init__(self, num_vertices=None):
        super().__init__()
        self.num_vertices = num_vertices or random.randint(2, 10)

    def generate(self):
        self.graph = nx.connected_watts_strogatz_graph(self.num_vertices, k=2, p=0.5)


class GraphConnectedComponents(Graph):
    def __init__(self, num_components=None):
        super().__init__()
        self.num_components = num_components or random.randint(2, 5)

    def generate(self):
        for _ in range(self.num_components):
            num_vertices = random.randint(2, 5)
            subgraph = nx.connected_watts_strogatz_graph(num_vertices, k=2, p=0.5)
            self.graph = nx.disjoint_union(self.graph, subgraph)


class TreeLeaves(Graph):
    def __init__(self, num_leaves=None):
        super().__init__()
        self.num_leaves = num_leaves or random.randint(2, 10)

    def generate(self):
        height = int(math.log2(self.num_leaves + 1))
        tree = nx.balanced_tree(2, height)
        leaves = [n for n in tree.nodes if tree.degree(n) == 1]

        while len(leaves) < self.num_leaves:
            node = random.choice(leaves)
            tree.add_edges_from([(node, tree.number_of_nodes() + i) for i in range(2)])
            leaves.remove(node)
            leaves.extend([tree.number_of_nodes() - 1, tree.number_of_nodes() - 2])

        self.graph = tree


class TreeVertices(Graph):
    def __init__(self, num_vertices=None):
        super().__init__()
        self.num_vertices = num_vertices or random.randint(2, 10)

    def generate(self):
        height = int(self.num_vertices ** 0.5)
        tree = nx.balanced_tree(height, 2)
        nodes_subset = list(tree.nodes)[:self.num_vertices]
        self.graph = tree.subgraph(nodes_subset)


class CompleteGraph(Graph):
    def __init__(self, num_vertices=None):
        super().__init__()
        self.num_vertices = num_vertices or random.randint(2, 10)

    def generate(self):
        self.graph = nx.complete_graph(self.num_vertices)


class RandomGraph(Graph):
    def __init__(self, num_vertices=None, num_edges=None):
        super().__init__()
        self.num_vertices = num_vertices or random.randint(2, 10)
        self.num_edges = num_edges or random.randint(self.num_vertices - 1,
                                                     self.num_vertices * (self.num_vertices - 1) // 2)

    def generate(self):
        self.graph = nx.gnm_random_graph(self.num_vertices, self.num_edges)
