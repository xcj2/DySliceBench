#!/usr/bin/env python3
import sys
from collections import defaultdict
INF = float("inf")

count = 0


def solve(N: int, M: int, a: "List[int]", b: "List[int]"):
    A = [[0]*N for _ in range(N)]

    def dfs(curr, visited):
        global count
        visited[curr] = True
        if all(visited):
            count += 1
            return

        for t in edges[curr]:
            if visited[t] == False:
                dfs(t, visited[:])
        return

    edges = defaultdict(list)
    for aa, bb in zip(a, b):
        edges[aa-1].append(bb-1)
        edges[bb-1].append(aa-1)
    dfs(0, [False]*N)
    print(count)

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
