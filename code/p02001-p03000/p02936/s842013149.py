#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(N: int, Q: int, a: "List[int]", b: "List[int]", p: "List[int]", x: "List[int]"):
    conn = [[] for _ in range(N)]
    for i in range(N - 1):
        conn[a[i] - 1].append(b[i] - 1)
        conn[b[i] - 1].append(a[i] - 1)
    plus = [0] * N
    for i in range(Q):
        plus[p[i] - 1] += x[i]

    ret = [0] * N
    def dfs(idx, cur, visited):
        visited[idx] = True
        cur += plus[idx]
        ret[idx] = cur
        for nex in conn[idx]:
            if not visited[nex]:
                dfs(nex, cur, visited)
        return
    visited = [False] * N
    dfs(0, 0, visited)
    print(' '.join([str(r) for r in ret]))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    a = [int()] * (N-1)  # type: "List[int]" 
    b = [int()] * (N-1)  # type: "List[int]" 
    for i in range(N-1):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    p = [int()] * (Q)  # type: "List[int]" 
    x = [int()] * (Q)  # type: "List[int]" 
    for i in range(Q):
        p[i] = int(next(tokens))
        x[i] = int(next(tokens))
    solve(N, Q, a, b, p, x)

if __name__ == '__main__':
    main()
