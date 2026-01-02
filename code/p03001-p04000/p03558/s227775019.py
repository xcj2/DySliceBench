#!/usr/bin/env python3
#ABC77 D

import sys
import math
import bisect
sys.setrecursionlimit(1000000000)
from heapq import heappush, heappop,heappushpop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
mod = 10**9 + 7
inf = float('inf')
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))

#頂点iにmod(k)でiと等しい正の整数の集合を割り当て、頂点iから10i+j(0≦j≦9,mod(k))にコストjの有向辺を張ったグラフを考える
#頂点v(1≦v≦9)への到達コストの初期値をvとし、ダイクストラ法で頂点0(kの倍数)への到達コストを求める
#頂点iから+1して移動できる頂点:=桁和+1(コスト1),頂点iから*10して移動できる頂点:=桁和そのまま(コスト0) の2通りに遷移できる

k = I()
graph = [[] for _ in range(k)]
for i in range(k):
    graph[i].append([(i+1)%k, 1])
    graph[i].append([(10*i)%k, 0])
#print(graph)

def dijkstra(x):
    d = [inf] * k
    d[x] = 1
    visited = {x}
    h = [(0, x)]

    while h:
        u = heappop(h)[1]
        visited.add(u)
        for node, cost in graph[u]:
            if (node not in visited) and d[node] > d[u] + cost:
                d[node] = d[u] + cost
                heappush(h, (d[u]+cost, node))
    return d


print(dijkstra(1)[0])
