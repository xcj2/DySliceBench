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

n,m,R = myinput()
r = list(myinput())
abc = mylistinput(m)

d = [[float("inf")]*n for i in range(n)] 
# d[u][v]: 辺uvのコスト(存在しないときはinf)

for i in range(m):
    a = abc[i][0] - 1
    b = abc[i][1] - 1
    c = abc[i][2]
    d[a][b] = c
    d[b][a] = c

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
# print(d)

rp = list(permutations(r))
# print(rp)

ls_count = []
for i in rp:
    count = 0
    for j in range(len(i)-1):
        s = i[j] - 1
        t = i[j+1] - 1
        count += d[s][t]
    ls_count.append(count)
# print(ls_count)

ans = min(ls_count)
print(ans)