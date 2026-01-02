from collections import deque
from heapq import heapify,heappop,heappush,heappushpop
from copy import copy,deepcopy
from itertools import permutations,combinations
from collections import defaultdict,Counter
from pprint import pprint

def myinput():
    return map(int,input().split())

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
ab = [ list(myinput()) for _ in range(m) ]

g = [ [] for _ in range(n) ]
for i in range(m):
    a = ab[i][0] - 1
    b = ab[i][1] - 1
    g[a].append(b)
    g[b].append(a)
# print(g)

def dfs(g):
    color = [0]*n
    stack = deque()
    stack.append([0,1])
    while stack:
        tmp = stack.pop()
        v = tmp[0]
        c = tmp[1]
        color[v] = c
        for i in g[v]:
            if color[i]==c:
                return False,[]
            elif color[i]==0:
                stack.append([i,-1*c])
    return True,color

flag,color =  dfs(g)
# print(flag)
if flag:
    black = color.count(1)
    white = color.count(-1)
    ans = black * white - m
else:
    ans = n*(n-1)//2 - m
print(ans)