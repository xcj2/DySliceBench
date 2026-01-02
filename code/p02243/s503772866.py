from heapq import heappop, heappush
import sys


class SSSP:
    """Given weighted graph, find Single Sorce Shortest Path from node 0.

    >>> st = SSSP([[(2, 3), (3, 1), (1, 2)], \
                   [(0, 2), (3, 4)], \
                   [(0, 3), (3, 1), (4, 1)], \
                   [(2, 1), (0, 1), (1, 4), (4, 3)], \
                   [(2, 1), (3, 3)]])
    >>> [st.weight(n) for n in range(5)]
    [0, 2, 2, 1, 3]
    """
    def __init__(self, graph):
        self.size = len(graph)
        self.tree = []
        self.weights = [-1] * self.size
        self._search(graph)

    def weight(self, n):
        return self.weights[n]

    def _search(self, graph):
        h = []
        self.weights[0] = 0
        count = 1
        for i, w in graph[0]:
            heappush(h, (w, 0, i))

        while count < self.size:
            while len(h) > 0:
                weight, src, dst = heappop(h)
                if self.weights[dst] < 0:
                    self.weights[dst] = weight
                    count += 1
                    self.tree.append((src, dst))
                    for i, w in graph[dst]:
                        if self.weights[i] < 0:
                            heappush(h, (w+weight, dst, i))
                    break


def run():
    n = int(input())

    nodes = [None] * n
    for line in sys.stdin:
        id_, deg, *edges = [int(i) for i in line.split()]
        nodes[id_] = []
        for _ in range(deg):
            tgt, wgt, *edges = edges
            nodes[id_].append((tgt, wgt))

    st = SSSP(nodes)
    for node in range(n):
        print('{} {}'.format(node, st.weight(node)))


if __name__ == '__main__':
    run()

