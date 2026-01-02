import abc


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

    def dfs(self, handler=None):

        visited = []
        while len(visited) < self.size:
            for id_ in range(1, self.size+1):
                if id_ not in visited:
                    stack = [(id_, 0)]
                    break
            while len(stack) > 0:
                i, j = stack.pop()
                if j == 0:
                    if handler:
                        handler.visit(i)
                    visited.append(i)
                    yield i
                try:
                    j = self._nodes[i].index(1, j+1)
                    stack.append((i, j))
                    if j not in visited:
                        stack.append((j, 0))
                except ValueError:
                    if handler:
                        handler.leave(i)


class EventHandler(abc.ABC):
    @abc.abstractmethod
    def visit(self, i):
        pass

    @abc.abstractmethod
    def leave(self, i):
        pass


class Logger(EventHandler):
    def __init__(self, n):
        self.log = [(0, 0)] * n
        self.step = 0

    def visit(self, i):
        self.step += 1
        self.log[i-1] = (self.step, 0)

    def leave(self, i):
        self.step += 1
        (n, m) = self.log[i-1]
        self.log[i-1] = (n, self.step)

    def by_node(self):
        i = 1
        for discover, finish in self.log:
            yield (i, discover, finish)
            i += 1


def run():
    n = int(input())
    g = AdjacentGraph(n)
    log = Logger(n)

    for i in range(n):
        id_, c, *links = [int(x) for x in input().split()]
        for n in links:
            g.set_adj_node(id_, n)

    for i in g.dfs(log):
        pass

    for node in log.by_node():
        print(" ".join([str(i) for i in node]))


if __name__ == '__main__':
    run()

