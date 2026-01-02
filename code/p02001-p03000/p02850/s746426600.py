#!/usr/bin/env python3
import sys
import queue

def create_graph(N, a, b):
    g = {}
    for i in range(N-1):
        if a[i] in g:
            g[a[i]][b[i]] = 0
        else:
            g[a[i]] = {b[i]: 0}
        if b[i] in g:
            g[b[i]][a[i]] = 0
        else:
            g[b[i]] = {a[i]: 0}
    return g


def bfs(g, s):
    Q = queue.Queue()
    Q.put(s)
    while not Q.empty():
        p = Q.get()
        cs = set(range(len(g[p])+2)) - set([v for k, v in g[p].items()])
        for q in g[p].keys():
            # print(f"p:{p} q:{q} g:{g[p][q]}")
            if not g[p][q]:
                c = cs.pop()
                g[p][q] = c
                g[q][p] = c
                Q.put(q)


def solve(N: int, a, b):
    g = create_graph(N, a, b)
    bfs(g, a[0])
    # print(g)
    m = 1
    for i in range(N-1):
        m = max(m, g[a[i]][b[i]])
    print(m)
    for i in range(N-1):
        print(g[a[i]][b[i]])


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
