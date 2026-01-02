#!/usr/bin/env python3
import sys
sys.setrecursionlimit(200000)

def solve(N: int, M: int, X: "List[int]", Y: "List[int]", Z: "List[int]"):
    conn = [[] for _ in range(N)]
    for i in range(M):
        conn[X[i] - 1].append(Y[i] - 1)
        conn[Y[i] - 1].append(X[i] - 1)

    def dfs(idx, conn, visited):
        visited[idx] = True
        for c in conn[idx]:
            if not visited[c]:
                dfs(c, conn, visited)
        return visited

    visited = [False] * N
    ret = 0
    for i in range(N):
        if not visited[i]:
            visited = dfs(i, conn, visited)
            ret += 1
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    X = [int()] * (M)  # type: "List[int]" 
    Y = [int()] * (M)  # type: "List[int]" 
    Z = [int()] * (M)  # type: "List[int]" 
    for i in range(M):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
        Z[i] = int(next(tokens))
    solve(N, M, X, Y, Z)

if __name__ == '__main__':
    main()
