import heapq
from itertools import product
h, w = map(int, input().split())
si, sj = map(lambda x: int(x)-1, input().split())
gi, gj = map(lambda x: int(x)-1, input().split())
fld = ''.join([input()for _ in range(h)])
INF = 10**18


def to_v(i, j):
    return i*w+j


n = h*w
start = to_v(si, sj)
goal = to_v(gi, gj)


def generate_v2(v):
    i, j = divmod(v, w)
    it = [-2, -1, 0, 1, 2]
    for di, dj in product(it, repeat=2):
        x, y = i+di, j+dj
        if x < 0 or h <= x or y < 0 or w <= y:
            continue
        if (di, dj) in [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]:
            d = 0
        else:
            d = 1
        yield d, x*w+y


def dijkstra(init_v):
    next_v = [(0, init_v)]
    dist = [INF]*n
    dist[init_v] = 0
    while next_v:
        d, v = heapq.heappop(next_v)
        if dist[v] < d:
            continue
        for d, v2 in generate_v2(v):
            if fld[v2] == '#':
                continue
            if dist[v2] <= dist[v]+d:
                continue
            dist[v2] = dist[v]+d
            heapq.heappush(next_v, (dist[v2], v2))
    return dist


ans = dijkstra(start)[goal]
print(-1 if ans == INF else ans)
