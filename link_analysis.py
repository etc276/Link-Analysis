import sys
import numpy as np
from collections import defaultdict

from modules.hits import hits

class Graph:

    def __init__(self, nodes, sources, targets):
        self.nodes = nodes
        self.sources = sources
        self.targets = targets

def get_graph(argv):

    if len(argv) < 1:
        print('Error')
        exit(-1)

    fname = argv[1]
    nodes = set()
    sources = defaultdict(list)
    targets = defaultdict(list)

    with open(fname, 'r') as fp:
        for line in fp:
            a, b = line.rstrip('\n').split(',')
            nodes.add(a)
            nodes.add(b)
            sources[a].append(b)
            targets[b].append(a)

    return Graph(nodes, sources, targets)

if __name__=='__main__':

    # read data and return graph
    graph = get_graph(sys.argv)

    # HITS
    auth, hubs = hits(graph)
    print('auth:', auth)
    print('hubs:', hubs)
    