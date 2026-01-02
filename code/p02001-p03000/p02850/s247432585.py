#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(N: int, a: "List[int]", b: "List[int]"):
    conns = [[] for _ in range(N)]
    for i in range(N - 1):
        conns[a[i] - 1].append((b[i] - 1, i))
        conns[b[i] - 1].append((a[i] - 1, i))
    k = 0
    for i in range(N):
        k = max(k, len(conns[i]))
    ret = [0] * (N - 1)
    def dfs(idx, prev, visited):
        visited[idx] = True
        color = 0 if prev != 0 else 1
        for node, idx in conns[idx]:
            if not visited[node]:
                ret[idx] = color + 1
                dfs(node, color, visited)
                color += 1
                if color == prev:
                    color += 1
    visited = [False] * N
    dfs(0, -1, visited)
    print(k)
    for r in ret:
        print(r)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int()] * (N - 1)  # type: "List[int]"
    b = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, a, b)

if __name__ == '__main__':
    main()
