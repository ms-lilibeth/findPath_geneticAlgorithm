import random
from graph import Graph

class Chromosome:
    def __init__(self, graph):
        random.seed()
        self._node_list = graph.get_node_list()
        self._includes = [random.randint(0, 1) for i in range(len(node_list))]

    def get_fitness(self):
        return 0