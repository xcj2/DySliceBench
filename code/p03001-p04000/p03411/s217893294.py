#!/usr/bin/env python3
import sys
sys.setrecursionlimit(4100000)

def augment(g, src, matchTo, visited):
    if src < 0:
        return True
    for dst in g.get(src, []):
        if not visited[dst]:
            visited[dst] = True
            if augment(g, matchTo[dst], matchTo, visited):
                matchTo[src] = dst
                matchTo[dst] = src
                return True
    return False


def match(g, L):
    n = len(g)
    matchTo = [-1] * n
    m = 0
    for src in range(L):
        visited = [False] * n
        if augment(g, src, matchTo, visited):
            m += 1
    return m


def solve(N, a, b, c, d):
    g = dict()
    for i in range(2*N):
        g[i] = []
    for i in range(N):
        for j in range(N):
            if a[i] < c[j] and b[i] < d[j]:
                g[i].append(N+j)
                g[N+j].append(i)
    print(match(g, N))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    a = [int()] * (N)
    b = [int()] * (N)
    for i in range(N):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    c = [int()] * (N)
    d = [int()] * (N)
    for i in range(N):
        c[i] = int(next(tokens))
        d[i] = int(next(tokens))
    solve(N, a, b, c, d)

if __name__ == '__main__':
    main()
