import networkx as nx
import random


class GraphVertices:
    def __init__(self, num_vertices=None):
        self.num_vertices = num_vertices or random.randint(5, 20)
        self.graph = None

    def generate(self):
        self.graph = nx.gnm_random_graph(self.num_vertices, random.randint(self.num_vertices, self.num_vertices * (
                self.num_vertices - 1) // 2))

    def visualize(self):
        return self.graph

# Add similar classes for the other graph types
