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

n,m = myinput()
abc = mylistinput(m)

for i in range(m):
    a = abc[i][0] - 1
    b = abc[i][1] - 1
    c = -1 * abc[i][2]
    abc[i][0] = a
    abc[i][1] = b
    abc[i][2] = c
# print(abc)

# def BellmanFord(edges,num_v,source):
#     #グラフの初期化
#     inf = float("inf")
#     dist = [ inf for i in range(num_v) ]
#     dist[source] = 0
#     #辺の緩和
#     for i in range(num_v):
#         for edge in edges:
#             if edge[0]!=inf and dist[edge[1]]>(dist[edge[0]]+edge[2]):
#                 dist[edge[1]] = dist[edge[0]] + edge[2]
#                 if i==(num_v-1):
#                     return False,[]
#     return True,dist

# sからiへの最短距離を求める（Bellman-Ford法）
# s:始点，n:頂点数，w:辺の数，es[i]:[辺の始点,辺の終点,辺のコスト]
def BellmanFord(s,n,w,es):
    # 初期化
    d = [float("inf")]*n
    d[s] = 0
    # 更新
    for i in range(n):
        # update = False
        for p,q,r in es:
            # [p,q,r] = [from, to, cost]
            if d[p]!=float("inf") and d[q]>(d[p]+r):
                d[q] = d[p] + r
                # update = True
                if i==(n-1) and q==(n-1):
                    return False,[]
        # if update:
        #     pass
        # else:
        #     break
    return True,d

# def find_negative_loop(s,n,w,es):
#     #負の経路の検出
#     #n:頂点数, w:辺の数, es[i]:[辺の始点,辺の終点,辺のコスト]
#     d = [float("inf")] * n
#     d[s] = 0
#     #この始点はどこでもよい <----よくない
#     for i in range(n):
#         for j in range(w):
#             e = es[j]
#             if d[e[1]] > d[e[0]] + e[2]:
#                 d[e[1]] = d[e[0]] + e[2]
#                 if i==(n-1):
#                     return True
#     return False

flag,distance = BellmanFord(0,n,m,abc)
if flag:
    print(-1*distance[n-1])
else:
    print("inf")