import sys
import heapq
from collections import namedtuple
inf = float('inf')
Node = namedtuple('Node', 'd, no')

def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None

def SSSP(n, Adj):
    d = [inf] * n
    p = [-1] * n
    checked = [False] * n
    d[0] = 0
    checked[0] = True
    heap = [Node(d[0], 0)]

    while heap:
        u = heapq.heappop(heap)

        if d[u.no] < u.d:
            continue

        checked[u.no] = True

        for v, cost in Adj[u.no]:
            if not checked[v] and d[u.no] + cost < d[v]:
                d[v] = d[u.no] + cost
                p[v] = u.no
                heapq.heappush(heap, Node(d[v], v))

    return d

def solve():
    n = int(input())
    Adj = [[] for i in range(n)]

    for i in range(n):
        u, k, *line = [int(i) for i in input().split()]
        for j in range(k):
            Adj[u].append((line[2*j], line[2*j + 1]))

    # debug(Adj, locals())

    d = SSSP(n, Adj)

    for i in range(n):
        print(i, d[i])

if __name__ == '__main__':
    solve()