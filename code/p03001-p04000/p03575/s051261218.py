#!/usr/bin/env python3
import sys
from collections import defaultdict
INF = float("inf")


def solve(N: int, M: int, a: "List[int]", b: "List[int]"):

    edges = defaultdict(list)
    for f_, t_ in zip(a, b):
        edges[f_-1].append(t_-1)
        edges[t_-1].append(f_-1)

    visited = [False] * N

    def dfs(f_, pre):
        if visited[f_] is True:
            return True

        visited[f_] = True
        for t_ in edges[f_]:
            if t_ == pre:
                continue
            dfs(t_, f_)
        return

    counter = 0
    for f_, t_ in zip(a, b):
        edges[f_-1].remove(t_-1)
        edges[t_-1].remove(f_-1)
        visited = [False] * N
        dfs(0, -1)
        if all(visited) is False:
            counter += 1
        edges[f_-1].append(t_-1)
        edges[t_-1].append(f_-1)
    print(counter)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    a = [int()] * (M)  # type: "List[int]"
    b = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, M, a, b)


if __name__ == '__main__':
    main()
