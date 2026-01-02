from collections import deque
from heapq import heapify,heappop,heappush,heappushpop
from copy import copy,deepcopy
from itertools import permutations,combinations
from collections import defaultdict,Counter
from pprint import pprint

def myinput():
    return map(int,input().split())

def mylistinput(n):
    return [ list(myinput()) for _ in range(n) ]

def mycol(data,col):
    return [ row[col] for row in data ]

def mysort(data,col):
    data.sort(key=lambda x:x[col],reverse=False)
    return data

def mymax(data):
    M = -1*float("inf")
    for i in range(len(data)):
        m = max(data[i])
        M = max(M,m)
    return M

def mymin(data):
    m = float("inf")
    for i in range(len(data)):
        M = min(data[i])
        m = min(m,M)
    return m

n,m,s,t = myinput()
uvab = mylistinput(m)

# Dijkstra法(O(ElogV))
# edge[i] : iから出る道の[重み,行先]の配列
# import heapq
# def dijkstra_heap(n,s,edge):
#     #始点sから各頂点への最短距離
#     d = [float("inf")] * n
#     used = [True] * n # True:未確定
#     d[s] = 0
#     used[s] = False
#     edgelist = []
#     for e in edge[s]:
#         heapq.heappush(edgelist,e)
#     while len(edgelist):
#         minedge = heapq.heappop(edgelist)
#         # まだ使われてない頂点の中から最小の距離のものを探す
#         if not used[minedge[1]]:
#             continue
#         v = minedge[1]
#         d[v] = minedge[0]
#         used[v] = False
#         for e in edge[v]:
#             if used[e[1]]:
#                 heapq.heappush(edgelist,[e[0]+d[v],e[1]])
#     return d

# Dijkstra法(O(ElogV))
# edge[i] : iから出る道の[重み,行先]の配列
# 高速化版 
import heapq
def dijkstra_heap(n,s,edge):
    #始点sから各頂点への最短距離
    d = [10**20] * n
    used = [True] * n #True:未確定
    d[s] = 0
    used[s] = False
    edgelist = []
    for a,b in edge[s]:
        heapq.heappush(edgelist,a*(10**6)+b)
    while len(edgelist):
        minedge = heapq.heappop(edgelist)
        #まだ使われてない頂点の中から最小の距離のものを探す
        if not used[minedge%(10**6)]:
            continue
        v = minedge%(10**6)
        d[v] = minedge//(10**6)
        used[v] = False
        for e in edge[v]:
            if used[e[1]]:
                heapq.heappush(edgelist,(e[0]+d[v])*(10**6)+e[1])
    return d

g1 = [ [] for _ in range(n) ]
g2 = [ [] for _ in range(n) ]
for i in range(m):
    u = uvab[i][0] - 1
    v = uvab[i][1] - 1
    a = uvab[i][2]
    b = uvab[i][3]
    g1[u].append([a,v])
    g1[v].append([a,u])
    g2[u].append([b,v])
    g2[v].append([b,u])
# print(g1)
# print(g2)

d1 = dijkstra_heap(n,s-1,g1)
d2 = dijkstra_heap(n,t-1,g2)
# print(d1)
# print(d2)

yen = 10**15
ans = -1*float("inf")
ls_ans = [0]*n
for i in reversed(range(n)):
    snuke = yen - d1[i] - d2[i] 
    ans = max(ans,snuke)
    ls_ans[i] = ans

for i in range(n):
    print(ls_ans[i])