# coding:utf-8

import sys
import heapq
import itertools
from collections import defaultdict

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


def dijkstra(start: int, size: int, graph: dict) -> list:
    costs = [INF] * size
    costs[start] = 0
    hp = []
    heapq.heappush(hp, (0, start))
    while hp:
        hc, hv = heapq.heappop(hp)
        for to, move_cost in graph[hv]:
            if hc + move_cost >= costs[to]:
                continue
            costs[to] = hc + move_cost
            heapq.heappush(hp, (costs[to], to))

    return costs


n, m, r = LI()
R = LI_()

G = defaultdict(list)
for i in range(m):
    a, b, c = LI()
    a -= 1
    b -= 1
    G[a].append((b, c))
    G[b].append((a, c))

C = {}
for ri in R:
    C[ri] = dijkstra(ri, n, G)

ans = INF
for root in itertools.permutations(R):
    tmp = 0
    for i in range(r - 1):
        tmp += C[root[i]][root[i + 1]]
    ans = min(ans, tmp)

print(ans)
