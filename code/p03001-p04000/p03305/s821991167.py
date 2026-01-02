import sys
input = sys.stdin.buffer.readline
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getlist():
    return list(map(int, input().split()))
import math
import heapq
import fractions
from collections import defaultdict, Counter, deque
MOD = 10**9 + 7
INF = 10**21


def dijkstra(graph, start, n):
    h = []
    heapq.heappush(h, (0, start))
    costs = [INF for _ in range(n)]
    while h:
        cost, cur = heapq.heappop(h)
        if costs[cur] != INF:
            continue
        costs[cur] = cost
        for edge in graph[cur]:
            ecost, tgt = edge
            if costs[tgt] == INF:
                heapq.heappush(h, (cost + ecost, tgt))

    return costs


def main():
    money = 10 ** 15
    n, m, s, t = getlist()
    s -= 1; t -= 1

    yengraph = [[] for _ in range(n)]
    snuukgraph = [[] for _ in range(n)]
    for i in range(m):
        a, b, c, d = getlist()
        a -= 1; b -= 1
        yengraph[a].append([c, b])
        yengraph[b].append([c, a])
        snuukgraph[a].append([d, b])
        snuukgraph[b].append([d, a])

    ycost = dijkstra(yengraph, s, n)
    scost = dijkstra(snuukgraph, t, n)

    sumcost = []
    idx = 1
    for y, s in zip(ycost, scost):
        sumcost.append((y+s, idx))
        idx += 1
    sumcost.sort()
    idx = 0
    for i in range(n):
        while True:
            ans, cid = sumcost[idx]
            if cid > i:
                print(money - ans)
                break
            else:
                idx += 1
    # print(ycost)
    # print(scost)
    # print(sumcost)


if __name__ == '__main__':
    main()

"""
9999
3

2916
"""