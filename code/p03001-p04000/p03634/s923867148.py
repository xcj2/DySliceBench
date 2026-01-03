#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, a: "List[int]", b: "List[int]", c: "List[int]", Q: int, K: int, x: "List[int]", y: "List[int]"):
    """graph.input.linkedlist_with_weight
        input: u[]:start, v[]:end, w[]:weight
        output:g[][]
    """
    INF = 1<<48
    g = [[] for i in range(N+1)]
    for i in range(N-1):
        g[a[i]].append([b[i], c[i]])
        g[b[i]].append([a[i], c[i]])

    from heapq import heapify, heappop, heappush
    hq = []
    heapify(hq)
    # start
    s = K
    colors = ['W'] * (N+1)
    d = [INF] * (N+1)
    d[s] = 0

    heappush(hq, [s, s])
    colors[s] = 'G'

    while hq:
        f = hq.pop()
        u = f[1]
        colors[u]= 'B'
        
        if d[u] < -f[0]:
            continue

        for adj_i in g[u]:
            v = adj_i[0]
            if colors[v] == 'B':
                continue
            if d[v] > d[u] + adj_i[1]:
                d[v] = d[u] + adj_i[1]
                heappush(hq, [-d[v], v])
                colors[v] = 'G'

    for i in range(Q):
        print(d[x[i]]+d[y[i]])

    # print(d)

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
    c = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
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
