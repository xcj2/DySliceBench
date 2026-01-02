import math
from functools import reduce
from collections import deque
import sys
sys.setrecursionlimit(10**7)

def input():
    return sys.stdin.readline().strip()

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]

# 改行またはスペース区切りの入力をすべて読み込んでイテレータを返します。
def get_all_int():
    return map(int, open(0).read().split())

def rangeI(it, l, r):
    for i, e in enumerate(it):
        if l <= i < r:
            yield e
        elif l >= r:
            break

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

from heapq import heappush, heappop

def dijkstra(su):
    costs = [ INF ] * (n+1)

    hq = []
    hq.append((0, su))

    while hq:
        c, u = heappop(hq)
        # log(" ", c,x,y)
        if c >= costs[u]:
            continue
        costs[u] = c

        for v in edges[u]:
            heappush(hq, (c + 1, v))

    return costs



INF = 999999999999999999999999
MOD = 10**9+7

n,m = get_nums_l()
edges = [ [] for _ in range(n+1)]
for _ in range(m):
    a,b = get_nums_l()
    edges[a].append(b)
    edges[b].append(a)


costs = dijkstra(1)



ans = [0] * (n+1)
for u in range(2, n+1):
    c = costs[u]
    for v in edges[u]:
        if costs[v]+1 == c:
            ans[u] = v
            break

print("Yes")
for u in range(2,n+1):
    print(ans[u])
