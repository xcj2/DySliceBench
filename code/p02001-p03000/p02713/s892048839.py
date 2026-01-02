import sys
import time
input = sys.stdin.buffer.readline
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getlist():
    return list(map(int, input().split()))
# import math
from math import gcd
import heapq
import bisect
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


def dist(x1, y1, x2, y2):
    return math.sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2)


def main():
    K = getN()
    ans = 0
    for i in range(1, K+1):
        for j in range(1, K+1):
            for k in range(1, K+1):
                tmp = gcd(i, j)
                ans += gcd(tmp, k)
                # print(i,j,k,ans)

    print(ans)

if __name__ == '__main__':
    main()
