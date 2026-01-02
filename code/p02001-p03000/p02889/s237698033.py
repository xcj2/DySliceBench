from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())

N,M,L = inpl()
cost = [[INF]*N for _ in range(N)]
for i in range(N):
    cost[i][i] = 0

for _ in range(M):
    a,b,c = inpl()
    a,b = a-1,b-1
    cost[a][b] = c
    cost[b][a] = c

for k in range(N):
    for i in range(N):
        for j in range(N):
            cost[i][j]=min(cost[i][j],cost[i][k]+cost[k][j])

# print(cost)

for i in range(N):
    for j in range(N):
        if cost[i][j] == 0:
            cost[i][j] = 0
        elif cost[i][j] <= L:
            cost[i][j] = 1
        else:
            cost[i][j] = INF

# print(cost)

for k in range(N):
    for i in range(N):
        for j in range(N):
            cost[i][j]=min(cost[i][j],cost[i][k]+cost[k][j])


Q = inp()
ans = []
for _ in range(Q):
    s,t = inpl()
    tmp = cost[s-1][t-1]
    if tmp == INF:
        ans.append(-1)
    else:
        ans.append(tmp-1)

print('\n'.join(map(str,ans)))
