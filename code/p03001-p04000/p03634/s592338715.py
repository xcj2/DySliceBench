# coding:utf-8

import sys
import heapq
from collections import defaultdict

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


def dijkstra(start: int, size: int, G: dict) -> list:
    costs = [INF] * size
    costs[start] = 0
    hp = []
    heapq.heappush(hp, (0, start))
    while hp:
        hc, hv = heapq.heappop(hp)
        for to, move_cost in G[hv]:
            if hc + move_cost >= costs[to]:
                continue
            costs[to] = hc + move_cost
            heapq.heappush(hp, (costs[to], to))

    return costs


n = II()

G = defaultdict(list)
for _ in range(n - 1):
    a, b, c = LI()
    a -= 1
    b -= 1
    G[a].append((b, c))
    G[b].append((a, c))

q, k = LI()
k -= 1
C = dijkstra(k, n, G)

for _ in range(q):
    x, y = LI_()
    print(C[x] + C[y])
