import heapq


class MST:
    """Given weighted graph, find minimum spanning tree.

    >>> mst = MST([[-1, 2, 3, 1, -1], \
                   [2, -1, -1, 4, -1], \
                   [3, -1, -1, 1, 1], \
                   [1, 4, 1, -1, 3], \
                   [-1, -1, 1, 3, -1]]);
    >>> mst.weight()
    5
    """
    MAX_WEIGHT = 2001

    def __init__(self, graph):
        self.graph = graph
        self.size = len(graph)
        self.tree = []
        self._search()

    def weight(self):
        return sum([self.graph[i][j] for i, j in self.tree])

    def _search(self):
        visited = [0]

        while len(visited) < self.size:
            h = []
            for node in visited:
                for i, w in enumerate(self.graph[node]):
                    if w == -1:
                        continue
                    if i in visited:
                        continue
                    heapq.heappush(h, (w, node, i))

            weight, src, dst = heapq.heappop(h)
            visited.append(dst)
            self.tree.append((src, dst))


def run():
    n = int(input())

    nodes = []
    for _ in range(n):
        nodes.append([int(i) for i in input().split()])

    mst = MST(nodes)
    print(mst.weight())


if __name__ == '__main__':
    run()

