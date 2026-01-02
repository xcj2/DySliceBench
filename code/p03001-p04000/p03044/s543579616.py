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

n = int(input())
uvw = [ list(myinput()) for _ in range(n-1) ]

g = [ [] for _ in range(n) ]
for i in range(n-1):
    u = uvw[i][0] - 1
    v = uvw[i][1] - 1
    w = uvw[i][2]
    g[u].append([v,w])
    g[v].append([u,w])
# print(g)

def bfs(g):
    ls_ans = [-1] * n
    ls_ans[0] = 0
    q = deque()
    q.append(0)
    while q:
        node = q.popleft()
        ls = g[node]
        # print(ls)
        for i in range(len(ls)):
            child = ls[i][0]
            weight = ls[i][1]
            if ls_ans[child]!=-1:
                pass
            elif ls_ans[node]==0 and weight%2==0:
                ls_ans[child] = 0
                q.append(child)
            elif ls_ans[node]==0 and weight%2==1:
                ls_ans[child] = 1
                q.append(child)
            elif ls_ans[node]==1 and weight%2==0:
                ls_ans[child] = 1
                q.append(child)
            elif ls_ans[node]==1 and weight%2==1:
                ls_ans[child] = 0
                q.append(child)
            else:
                print("error")
        # print(ls_ans)
    return ls_ans

ls_ans = bfs(g)
# print(ls_ans)

for i in range(n):
    print(ls_ans[i])