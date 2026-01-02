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
        def find_first():
            try:
                return visited.index(0) + 1
            except ValueError:
                return None

        visited = [0] * self.size
        first = 1
        while first is not None:
            stack = [(first, 0, 0)]
            while len(stack) > 0:
                i, depth, j = stack.pop()
                if j == 0:
                    if handler:
                        handler.visit(i, depth)
                    visited[i-1] = 1
                    yield i
                try:
                    j = self._nodes[i].index(1, j+1)
                    stack.append((i, depth, j))
                    if visited[j-1] == 0:
                        stack.append((j, depth+1, 0))
                except ValueError:
                    if handler:
                        handler.leave(i)
            first = find_first()

    def bfs(self, handler=None):
        def find_first():
            try:
                return visited.index(0) + 1
            except ValueError:
                return None

        visited = [0] * self.size
        first = 1
        while first is not None:
            queue = [(first, 0)]
            while len(queue) > 0:
                (i, depth), *queue = queue
                if visited[i-1] == 0:
                    if handler:
                        handler.visit(i, depth)
                    visited[i-1] = 1
                    yield i
                    try:
                        j = 0
                        while j < self.size:
                            j = self._nodes[i].index(1, j+1)
                            if visited[j-1] == 0:
                                queue.append((j, depth+1))
                    except ValueError:
                        pass
                if handler:
                    handler.leave(i)
            first = find_first()


class EventHandler(abc.ABC):
    @abc.abstractmethod
    def visit(self, i, depth):
        pass

    @abc.abstractmethod
    def leave(self, i):
        pass


class Logger(EventHandler):
    def __init__(self, n):
        self.log = [(0, 0)] * n
        self.step = 0

    def visit(self, i, depth):
        self.step += 1
        self.log[i-1] = (self.step, depth, 0)

    def leave(self, i):
        self.step += 1
        self.log[i-1] = (self.log[i-1][0], self.log[i-1][1], self.step)

    def by_node(self):
        i = 1
        for discover, depth, finish in self.log:
            yield (i, discover, depth, finish)
            i += 1

def run():
    n = int(input())
    g = AdjacentGraph(n)
    log = Logger(n)

    for i in range(n):
        id_, c, *links = [int(x) for x in input().split()]
        for n in links:
            g.set_adj_node(id_, n)

    for i in g.bfs(log):
        pass

    reachable = None
    for node in log.by_node():
        id_, find, dep, exit = node
        if id_ > 1 and dep == 0:
            reachable = find - 1

        if reachable is not None and find > reachable:
            dep = -1

        print("{} {}".format(id_, dep))


if __name__ == '__main__':
    run()

