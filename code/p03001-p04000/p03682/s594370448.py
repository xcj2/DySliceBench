import sys
from collections import Counter, deque, defaultdict
from math import factorial
import heapq, bisect
import math
import itertools
sys.setrecursionlimit(10 ** 5 + 10)
INF = 10**15 +5
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

n = INT()
G = [[]for i in range(n)]   
position = [[]for i in range(n)]
for i in range(n):
    a, b= MAP()
    position[i] = (i, a, b)
position_x = sorted(position, key = lambda x:x[1])
position_y = sorted(position, key = lambda x:x[2])

for i in range(1,n):
    G[position_x[i][0]].append((position_x[i][1]-position_x[i-1][1], position_x[i-1][0]))
    G[position_x[i-1][0]].append((position_x[i][1]-position_x[i-1][1], position_x[i][0]))
    G[position_y[i][0]].append((position_y[i][2]-position_y[i-1][2], position_y[i-1][0]))
    G[position_y[i-1][0]].append((position_y[i][2]-position_y[i-1][2], position_y[i][0]))

def prim(G):
    res = 0
    used = [False]*n
    que = []
    heapq.heapify(que)
    used[0] = True
    for Gs in G[0]:
        heapq.heappush(que,Gs)
    while(len(que) > 0):
        cost, vertex = heapq.heappop(que)
        if used[vertex]:continue
        res += cost
        used[vertex] = True
        for Gs in G[vertex]:
            if used[Gs[1]]:continue
            heapq.heappush(que,Gs)
    return res

print(prim(G))