import sys
from collections import deque

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(N, M, inputs):
    relations = {}
    visited_all = (2 ** N) - 1
    for i in range(1, N + 1):
        relations[i] = []

    for i in inputs:
        [parent, child] = string_to_int(i)
        relations[parent].append(child)
        relations[child].append(parent)

    routes = 0
    queue = deque([[1, 0]])
    while len(queue) > 0:
        [node, visited] = queue.popleft()

        if visited & (1 << (node - 1)) != 0:
            continue

        visited = visited + (1 << (node - 1))

        if visited == visited_all:
            routes += 1
            continue

        for next in relations[node]:
            queue.append([next, visited])
    return routes


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    [N, M] = string_to_int(input())
    ret = solve(N, M, inputs(M))
    print(ret)
