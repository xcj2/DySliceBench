import sys, math
from itertools import permutations, combinations
from collections import defaultdict, Counter, deque
from math import factorial
from bisect import bisect_left #bisect_left(list, value)
import heapq
#from fractions import gcd
sys.setrecursionlimit(10**7)
enu = enumerate
MOD = 10**9+7
def input(): return sys.stdin.readline()[:-1]
def pri(x): print('\n'.join(map(str, x)))

N, X, Y = map(int, input().split())

def dijkstra_heap(s,edge):
    d = [10**20] * N
    used = [True] * N #True:未確定
    d[s] = 0
    used[s] = False
    edgelist = []
    for a,b in edge[s]:
        heapq.heappush(edgelist,a*(10**6)+b)
    while len(edgelist):
        minedge = heapq.heappop(edgelist)
        if not used[minedge%(10**6)]:
            continue
        v = minedge%(10**6)
        d[v] = minedge//(10**6)
        used[v] = False
        for e in edge[v]:
            if used[e[1]]:
                heapq.heappush(edgelist,(e[0]+d[v])*(10**6)+e[1])
    return d
# n,w = map(int,input().split()) #n:頂点数　w:辺の数

edge = [[] for i in range(N)]

for i in range(1, N-1):
    edge[i].append([1, i+1])
    edge[i].append([1, i-1])
edge[0].append([1, 1])
edge[N-1].append([1, N-2])
edge[X-1].append([1, Y-1])
edge[Y-1].append([1, X-1])

dd = defaultdict(int)
for i in range(N):
    dists = dijkstra_heap(i, edge)
    for j in dists[i+1:]:
        dd[j] += 1

for k in range(1, N):
    print(dd[k])
