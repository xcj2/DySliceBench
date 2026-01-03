def bellmanford(num, start, goal, edges):
    cost = [float('inf')] * num
    cost[start] = 0
    for _ in range(num):
        updated = False
        for a, b, c in edges:
            if cost[b] > cost[a] + c:
                cost[b] = cost[a] + c
                updated = True
        if not updated: break
    else:
        return (-1,cost)
    return (1,-cost[goal])

def examD(inf):
    N, M = LI()
    v = []
    for i in range(M):
        x, y, z = map(int, input().split())
        v.append((x-1,y-1,-z))
#    print(v)
#    print(bellmanford(N, 0, N-1, v))
    cur,d = bellmanford(N, 0, N-1, v)
    if cur==-1:
        inf_flag = [False]*N
        for i in range(N):
            for f, t, c in v:
                if d[f] == inf: continue
                if inf_flag[f] == True:
                    inf_flag[t] = True
                if d[t] > d[f] + c:
                    d[t] = d[f] + c
                    inf_flag[t] = True
        print("inf" if inf_flag[N-1] else -d[N-1])
    else:
        print(d)

import sys
import copy
import bisect
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examD(inf)