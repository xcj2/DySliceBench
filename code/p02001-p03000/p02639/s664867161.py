def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))

from collections import defaultdict, deque, Counter
from sys import exit
import math
import copy
from bisect import bisect_right

import sys
sys.setrecursionlimit(1000000)
import heapq
INF = 10**10

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
    nums = getList()
    for i in range(5):
        if nums[i] == 0:
            print(i+1)
            return
if __name__ == "__main__":
    main()
