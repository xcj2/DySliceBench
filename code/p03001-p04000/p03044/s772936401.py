#!/usr/bin/env python3
import sys
sys.setrecursionlimit(200000)

def dfs(idx, color, colors, conn, visited):
    visited[idx] = True
    colors[idx] = color
    for node, w in conn[idx]:
        if visited[node]:
            continue
        if w % 2 == 0:
            colors = dfs(node, color, colors, conn, visited)
        else:
            colors = dfs(node, (color + 1) % 2, colors, conn, visited)
    return colors


def solve(N: int, u: "List[int]", v: "List[int]", w: "List[int]"):
    conn = [[] for _ in range(N)]
    for i in range(N - 1):
        conn[u[i] - 1].append([v[i] - 1, w[i]])
        conn[v[i] - 1].append([u[i] - 1, w[i]])
    colors = [-1] * N
    visited = [False] * N
    colors = dfs(0, 0, colors, conn, visited)
    #for i in range(N - 1):
    #    if w[i] % 2 == 0:
    #        if color[u[i]] >= 0 or color[w[i]] >= 0 :
    #            color[w[i]] = color[u[i]]
    #            color[u[i]] = color[w[i]]
    #    else:
    #        if color[u[i]] >= 0:
    #            color[w[i]] = (color[u[i]] + 1) % 2
    for c in colors:
        print(c)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    u = [int()] * (N-1)  # type: "List[int]" 
    v = [int()] * (N-1)  # type: "List[int]" 
    w = [int()] * (N-1)  # type: "List[int]" 
    for i in range(N-1):
        u[i] = int(next(tokens))
        v[i] = int(next(tokens))
        w[i] = int(next(tokens))
    solve(N, u, v, w)

if __name__ == '__main__':
    main()
