from heapq import heappush, heappop
from collections import deque,defaultdict,Counter
import itertools
from itertools import permutations
import sys
import bisect
import string
sys.setrecursionlimit(10**6)
def SI():
    return input().split()
def MI():
    return map(int,input().split())
def I():
    return int(input())
def LI():
    return [int(i) for i in input().split()]
YN=['Yes','No']
YNeos='YNeos'
mo=10**9+7
imp='IMPOSSIBLE'


def BellmanFord(edges,num_v,source):
  #グラフの初期化
  inf=float("inf")
  dist=[inf for i in range(num_v)]
  dist[source-1]=0
  
  #辺の緩和
  for i in range(num_v):
    for edge in edges:
      if edge[0] != inf and dist[edge[1]-1] > dist[edge[0]-1] + edge[2]:
        dist[edge[1]-1] = dist[edge[0]-1] + edge[2]
        if i==num_v-1 and ans!=dist[n-1]:
            0#return 'neg'
    ans=dist[n-1]
  return dist

def shortest_path(s,n,w,es):
    #s→iの最短距離
    # s:始点, n:頂点数, w:辺の数, es[i]: [辺の始点,辺の終点,辺のコスト]
    d = [float("inf")] * n
    #d[i] : s→iの最短距離
    d[s] = 0
    while True:
        updata = False
        for i in range(w):
            e = es[i]
            ans=d[n-1]
            # e: 辺iについて [from,to,cost]
            if d[e[0]] != float("inf") and d[e[1]] > d[e[0]] + e[2]:
                d[e[1]] = d[e[0]] + e[2]
                updata = True
        if not updata:
            break
    return d

n,m,p=MI()
g=[]
for i in range(m):
    a,b,c=MI()
    #g.append((a-1,b-1,p-c))
    g.append((a,b,p-c))
    

di=BellmanFord(g,n,1)
ans=di[n-1]
di_2=BellmanFord(g,n*2,1)

if ans!=di_2[n-1]:
    print(-1)
else:
    print(max(0,-di[n-1]))