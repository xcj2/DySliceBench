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

n = 10
h,w = myinput()
c = mylistinput(n)
a = mylistinput(h)

d = [[float("inf")]*n for i in range(n)] 
# d[u][v]: 辺uvのコスト(存在しないときはinf)

for i in range(n):
    for j in range(n):
        cost = c[i][j]
        d[i][j] = cost

#自身のところに行くコストは０
for i in range(n):
    d[i][i] = 0

# ワーシャルフロイド（warshall_floyd）法
# d[u][v]: 辺uvのコスト(存在しないときはinf)
def warshall_floyd(n,d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

d = warshall_floyd(n,d)
# pprint(d)

ans = 0
for i in range(h):
    for j in range(w):
        if a[i][j]==-1:
            pass
        else:
            number = a[i][j]
            ans += d[number][1]
print(ans)