import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

from heapq import heappop, heappush
H, W = mapint()
Cs = [list(mapint()) for _ in range(10)]
lis = []
for h in range(H):
    lis.extend(list(mapint()))

def dijkstra(start):
    Q = [(0, start)]
    checked = [0]*10
    while Q:
        d, v = heappop(Q)
        checked[v] = 1
        if v==1:
            return d
        for i in range(10):
            if not checked[i]:
                heappush(Q, (d+Cs[v][i], i))

costs = [0]*10
for i in range(10):
    costs[i] = dijkstra(i)

from collections import Counter
c = Counter(lis)
ans = 0
for i in range(10):
    ans += costs[i]*c[i]
print(ans)
        