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

    navigability = defaultdict(lambda: [])

    for e in edges:
        navigability[e[0]].append(e[1])
        navigability[e[1]].append(e[0])

    def solve1(path, result):
        if len(path) == num_nodes:
            result.append(path)
            return

        for m in navigability[path[-1]]:
            if m not in path:
                solve1(path + [m], result)

        return result

    return solve1([1], [])


def main():
    print(len(solve()))


main()
