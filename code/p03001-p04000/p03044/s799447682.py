#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, u: "List[int]", v: "List[int]", w: "List[int]"):
    colors = [-1] *(N+1)
    g = [[] for i in range(N+1)]
    for i in range(N-1):
        g[u[i]].append([v[i], w[i]])
        g[v[i]].append([u[i], w[i]])

    # print(g)

    from collections import deque
    d = deque()
    colors[1] = 0
    d.append(1)
    while len(d) > 0:
        # print("d:"+d)
        n = d.popleft()
        for V, W in g[n]:
            if colors[V] != -1:
                continue
            d.append(V)
            if W%2 == 0:
                colors[V] = colors[n]
            else:
                colors[V] = int(not colors[n])
    
    for i in range(1, N+1):
        print(colors[i])
            

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    u = [int()] * (N - 1)  # type: "List[int]"
    v = [int()] * (N - 1)  # type: "List[int]"
    w = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        u[i] = int(next(tokens))
        v[i] = int(next(tokens))
        w[i] = int(next(tokens))
    solve(N, u, v, w)

if __name__ == '__main__':
    main()
