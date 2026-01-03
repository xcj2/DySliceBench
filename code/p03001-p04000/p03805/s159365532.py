import array
import itertools
from collections import defaultdict, deque


def log(s):
    # print("| " + str(s), file=sys.stderr)
    pass


def output(x):
    print(x, flush=True)


def input_ints():
    return map(int, input().split())


def solve():
    num_nodes, num_edges = tuple(input_ints())

    edges = [tuple(input_ints()) for _ in range(num_edges)]

    navigatility = defaultdict(lambda: [])

    for e in edges:
        navigatility[e[0]].append(e[1])
        navigatility[e[1]].append(e[0])

    queue = deque()
    queue.append([1])
    result = []

    while queue:
        path = queue.popleft()

        if len(path) == num_nodes:
            result.append(path)
        else:
            n = path[-1]

            for m in navigatility[n]:
                if m not in path:
                    queue.append(path + [m])

    return result


def main():
    print(len(solve()))


main()
