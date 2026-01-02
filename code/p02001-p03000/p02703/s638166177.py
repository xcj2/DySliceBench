from heapq import heappop, heappush
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


def phi(city, silver):
    return city*2501+silver


def psi(x):
    city = x//2501
    silver = x % 2501
    return city, silver


n, m, s = map(int, input().split())
g = [[] for _ in range(n*2501+1)]

for i in range(m):
    u, v, a, b = map(int, input().split())
    for j in range(2501):
        if j-a >= 0:
            g[phi(u-1, j)].append((phi(v-1, j-a), b))
            g[phi(v-1, j)].append((phi(u-1, j-a), b))

for i in range(n):
    c, d = map(int, input().split())
    for j in range(2501):
        if j + c <= 2500:
            g[phi(i, j)].append((phi(i, j+c), d))


def dijkstra(s, n, g):
    # g[i][j] : the cost of i→j  or g[i] = [(target, cost), ...]
    # must import heapq
    # sys.stdin.readline is recommended
    d = [10**18] * n
    d[s] = 0
    q = [(0, s)]
    while q:
        dist_u, u = heappop(q)
        if d[u] < dist_u:
            continue
        for v, c in g[u]:  # 'in g[u]' if g is an adj list.
            if d[v] > dist_u + c:
                d[v] = dist_u + c
                heappush(q, (d[v], v))
    return d


s = min(s, 2500)
d = dijkstra(phi(0, s), n*2501+1, g)

for i in range(1, n):
    print(min(d[phi(i, 0):phi(i+1, 0)]))
