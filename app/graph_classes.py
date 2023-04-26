import networkx as nx
import random
import math
import json


class Graph:
    def __init__(self):
        self.graph = nx.Graph()

    def visualize(self):
        return self.graph

    def save_to_file(self, filename):
        graph_data = {
            "type": self.__class__.__name__,
            "num_vertices": self.num_vertices,
            "params": self.params,
            "edges": list(self.graph.edges)
        }
        with open(filename, "w") as f:
            json.dump(graph_data, f)

    @classmethod
    def load_from_file(cls, filename):
        with open(filename, "r") as f:
            graph_data = json.load(f)

        graph_type = graph_data["type"]
        num_vertices = graph_data["num_vertices"]
        params = graph_data["params"]
        edges = graph_data["edges"]

        graph_class = globals()[graph_type]
        graph_instance = graph_class(**params)
        graph_instance.graph.add_edges_from(edges)

        return graph_instance


class GraphVertices(Graph):
    def __init__(self, num_vertices=None):
        super().__init__()
        self.num_vertices = num_vertices or random.randint(2, 10)
        self.params = {"num_vertices": self.num_vertices}

    def generate(self):
        self.graph = nx.connected_watts_strogatz_graph(self.num_vertices, k=2, p=0.5)


class GraphConnectedComponents(Graph):
    def __init__(self, num_components=None):
        super().__init__()
        self.num_components = num_components or random.randint(2, 5)
        self.params = {"num_components": self.num_components}

    def generate(self):
        for _ in range(self.num_components):
            num_vertices = random.randint(2, 5)
            subgraph = nx.connected_watts_strogatz_graph(num_vertices, k=2, p=0.5)
            self.graph = nx.disjoint_union(self.graph, subgraph)


class TreeLeaves(Graph):
    def __init__(self, num_leaves=None):
        super().__init__()
        self.num_leaves = num_leaves or random.randint(2, 10)
        self.params = {"num_leaves": self.num_leaves}

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
        self.params = {"num_vertices": self.num_vertices}

    def generate(self):
        height = int(self.num_vertices ** 0.5)
        tree = nx.balanced_tree(height, 2)
        nodes_subset = list(tree.nodes)[:self.num_vertices]
        self.graph = tree.subgraph(nodes_subset)


class CompleteGraph(Graph):
    def __init__(self, num_vertices=None):
        super().__init__()
        self.num_vertices = num_vertices or random.randint(2, 10)
        self.params = {"num_vertices": self.num_vertices}

    def generate(self):
        self.graph = nx.complete_graph(self.num_vertices)


class RandomGraph(Graph):
    def __init__(self, num_vertices=None, num_edges=None):
        super().__init__()
        self.num_vertices = num_vertices or random.randint(2, 10)
        self.num_edges = num_edges or random.randint(self.num_vertices - 1,
                                                     self.num_vertices * (self.num_vertices - 1) // 2)
        self.params = {"num_vertices": self.num_vertices, "num_edges": self.num_edges}

    def generate(self):
        self.graph = nx.gnm_random_graph(self.num_vertices, self.num_edges)
