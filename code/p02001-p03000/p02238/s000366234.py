NOT_FOUND = 0
FOUND = 1
FINISHED = 2


class Stack(object):
    def __init__(self):
        self._stack = []

    def push(self, val):
        self._stack.append(val)

    def pop(self):
        val = self._stack[-1]
        del self._stack[-1]
        return val

    def top(self):
        if len(self._stack) > 0:
            return self._stack[-1]
        else:
            return None

    def is_stacked(self, val):
        if len(self._stack) > 0:
            return val in self._stack
        else:
            return None

    def get_len(self):
        return len(self._stack)


def parse_line(line):
    vals = [int(v) for v in line.split(' ')]
    node, n_node, nodes = vals[0], vals[1], vals[2:]
    # convert zero origin
    nodes = [n - 1 for n in nodes]
    return node, n_node, nodes


def main():
    # get input
    n = int(input().strip())
    graph = []
    for _ in range(n):
        line = input().strip()
        _, _, nodes = parse_line(line)
        graph.append(nodes)

    # initialize
    stack = Stack()
    stats = [NOT_FOUND for _ in range(n)]
    found_times = [None for _ in range(n)]
    finished_times = [None for _ in range(n)]
    counter = 0

    # dfs
    while sum(stats) < n * FINISHED:
        counter += 1
        init_node = None
        for node in range(n):
            if stats[node] == NOT_FOUND:
                init_node = node
                break
        assert init_node is not None
        stack.push(init_node)
        stats[init_node] = FOUND
        found_times[init_node] = counter

        while stack.get_len() > 0:
            counter += 1
            crr_node = stack.top()
            adj_nodes = graph[crr_node]
            for adj_node in adj_nodes:
                # exist not stacked node
                if stats[adj_node] == NOT_FOUND:
                    found_times[adj_node] = counter
                    stats[adj_node] = FOUND
                    stack.push(adj_node)
                    crr_node = adj_node
                    break
            else:
                # not exist not stacked node
                finished_times[crr_node] = counter
                stats[crr_node] = FINISHED
                stack.pop()
                crr_node = stack.top()

    for i in range(n):
        print('{} {} {}'.format(i + 1, found_times[i], finished_times[i]))


if __name__ == '__main__':
    main()

