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

n = int(input())
ab = mylistinput(n-1)

g = [ [] for _ in range(n) ]
for i in range(n-1):
    a = ab[i][0] - 1
    b = ab[i][1] - 1
    g[a].append(b)
    g[b].append(a)
# print(g)

color = [-1] * n

def bfs(g):
    used_color = [ [-1] ]*n
    q = deque()
    q.append([0,0])
    while q:
        tmp = q.popleft()
        v = tmp[0]
        c = tmp[1]
        color[v] = c
        ls_nc = list(reversed(list(range(1,len(g[v])+1))))
        if c==0:
            pass
        elif c in ls_nc:
            ls_nc.remove(c)
        else:
            pass
        for nv in g[v]:
            if color[nv]!=-1:
                pass
            else:
                nc = ls_nc.pop()
                q.append([nv,nc])
    return True

if bfs(g):
    print(max(color))
    for i in range(n-1):
        b = ab[i][1] - 1
        print(color[b])
else:
    print("Error")