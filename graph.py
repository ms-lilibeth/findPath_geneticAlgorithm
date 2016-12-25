import random
from collections import defaultdict


class Graph:
    def __init__(self, filename):
        self._container = defaultdict(lambda : None)
        self._destination = None
        # self._start == 1
        self._create_from_file(filename)
        random.seed()
        pass

    def get_node_list(self):
        return [key for key in self._container]

    def _create_from_file(self, filename):
        with open(filename, 'r') as f:
            # Reading nodes num and destination node
            line = f.readline()
            vals = [int(s) for s in line.split() if s.isdigit()]
            self._destination = vals[1]
            # Reading list of edges
            for line in f:
                weight = random.randint(1, 10)
                vals = [int(s) for s in line.replace('\n', '').split('-') if s.isdigit()]
                node_from = vals[0]
                node_to = vals[1]
                if node_from not in self._container:
                    self._container[node_from] = defaultdict(lambda : None)
                self._container[node_from][node_to] = weight

    # returns None if the edge does not exist
    def get_weight(self, node1, node2):
        return self._container[node1][node2]
