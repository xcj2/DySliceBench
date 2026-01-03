import sys
# from collections import defaultdict, deque
import math
# import copy
# from bisect import bisect_left, bisect_right
import heapq

# sys.setrecursionlimit(1000000)

# input aliases
input = sys.stdin.readline

getS = lambda: input().strip()
getN = lambda: int(input())
getList = lambda: list(map(int, input().split()))
getZList = lambda: [int(x) - 1 for x in input().split()]

INF = 10 ** 20
MOD = 1000000007


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

def solve():
    n = getN()
    graph = [[] for _ in range(n)]
    for i in range(n-1):
        a,b,c = getList()
        a,b = a-1, b-1

        graph[a].append([c, b])
        graph[b].append([c, a])
    q, k = getList()
    costs = dijkstra(graph, k-1, n)
    # print(costs)
    for i in range(q):
        s, e = getZList()

        print(costs[s] + costs[e])

    return

def main():
    n = getN()
    for _ in range(n):
        solve()
if __name__ == "__main__":
    # main()
    solve()
