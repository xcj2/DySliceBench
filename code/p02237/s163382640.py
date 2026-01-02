class AdjacentGraph:
    """Implementation adjacency-list Graph.
    Beware ids are between 1 and size.
    """
    def __init__(self, size):
        self.size = size
        self._nodes = [[0] * (size+1) for _ in range(size+1)]

    def set_adj_node(self, id_, adj_id):
        self._nodes[id_][adj_id] = 1

    def __iter__(self):
        self._id = 0
        return self

    def __next__(self):
        if self._id < self.size:
            self._id += 1
            return (self._id, self._nodes[self._id][1:])

        raise StopIteration()


def run():
    n = int(input())
    g = AdjacentGraph(n)

    for i in range(n):
        id_, c, *links = [int(x) for x in input().split()]
        for n in links:
            g.set_adj_node(id_, n)

    for id_, nodes in g:
        print(" ".join([str(x) for x in nodes]))


if __name__ == '__main__':
    run()

