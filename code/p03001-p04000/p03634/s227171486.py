#!/usr/bin/env python3
import sys

sys.setrecursionlimit(300000)

def dfs(idx, visited, conn, d, cur):
    visited[idx] = True
    for nex in conn[idx]:
        if not visited[nex[0]]:
            d[nex[0]] = cur + nex[1]
            d = dfs(nex[0], visited, conn, d, cur + nex[1])
    return d


def solve(N: int, A: "List[int]", B: "List[int]", C: "List[int]", Q: int, K: int, x: "List[int]", y: "List[int]"):

    conn = [[] for _ in range(N)]
    for j in range(N - 1):
        a = A[j] - 1
        b = B[j] - 1
        conn[a].append([b, C[j]])
        conn[b].append([a, C[j]])
    visited = [False] * N
    d = [0] * N
    d = dfs(K - 1, visited, conn, d, 0)
    for q in range(Q):
        s = x[q] - 1
        t = y[q] - 1
        ret = d[s] + d[t]
        print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int()] * (N-1)  # type: "List[int]" 
    b = [int()] * (N-1)  # type: "List[int]" 
    c = [int()] * (N-1)  # type: "List[int]" 
    for i in range(N-1):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
        c[i] = int(next(tokens))
    Q = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    x = [int()] * (Q)  # type: "List[int]" 
    y = [int()] * (Q)  # type: "List[int]" 
    for i in range(Q):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, a, b, c, Q, K, x, y)

if __name__ == '__main__':
    main()
