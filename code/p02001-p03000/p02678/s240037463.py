import sys
input=sys.stdin.readline
def N(): return int(input())
def NM():return map(int,input().split())
def L():return list(NM())
def LN(n):return [N() for i in range(n)]
def LL(n):return [L() for i in range(n)]
def YesNo(x):print("Yes")if x==True else print("No")
n,m=NM()
edge=[[] for i in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    c=1
    edge[a].append((b,c))
    edge[b].append((a,c))
pre=[-1]*(n+1)
from heapq import *
def dijkstra(s,n):
    d = [float('inf') for i in range(n+1)]
    pq = []
    d[s]=0
    heappush(pq,(0,s))
    while pq:
        dist,u = heappop(pq)
        for v,cost in edge[u]:
            if d[v]<=dist+cost:
                continue
            d[v]=dist+cost
            pre[v]=u
            heappush(pq,(d[v],v))
    return d
dijkstra(1,n)
if -1 in pre[2:]:
    print("No")
else:
    print("Yes")
    for i in pre[2:]:
        print(i)