import heapq


class SSST:
    """Given weighted graph, find minimum spanning tree.

    >>> st = SSST([[(2, 3), (3, 1), (1, 2)], \
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
        self.weights = [0] * self.size
        self._search(graph)

    def weight(self, n):
        return self.weights[n]

    def _search(self, graph):
        visited = [0]

        while len(visited) < self.size:
            h = []
            for node in visited:
                for i, w in graph[node]:
                    if i not in visited:
                        heapq.heappush(h, (w+self.weights[node], node, i))

            weight, src, dst = heapq.heappop(h)
            visited.append(dst)
            self.weights[dst] = weight
            self.tree.append((src, dst))


def run():
    n = int(input())

    nodes = [None] * n
    for _ in range(n):
        id_, deg, *edges = [int(i) for i in input().split()]
        nodes[id_] = []
        for _ in range(deg):
            tgt, wgt, *edges = edges
            nodes[id_].append((tgt, wgt))

    st = SSST(nodes)
    for node in range(n):
        print('{} {}'.format(node, st.weight(node)))


if __name__ == '__main__':
    run()

