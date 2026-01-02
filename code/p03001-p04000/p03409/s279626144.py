from collections import defaultdict,deque
from sys import stdin,setrecursionlimit
import heapq,bisect,math,itertools,string,queue,datetime
setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inpl(): return list(map(int, stdin.readline().split()))
"""lines:グラフの隣接リスト　dict型　lines[s]に辺が入る　defaultdict(set)で作る
 cost:辺の間の容量
 N：nodeの数（最終インデックスでない）
 start:sorceのnode
 Goal:sinkのnode"""
def ford_fulkerson(lines,cost,N,start,Goal):#linesとcostは上のように受け取っておく
     ans = 0
     INF = float('inf')
     def ford_in(s):#listはミュータブルだからnonlocalにしなくて良い
         nonlocal ans
         route = [0]*N
         ed = [True]*N
         ed[s] = False
         route[s] = -1
         que = deque([])
         que.append([s,INF])
         while que:
             s,flow = que.pop()
             for t in lines[s]:
                 if ed[t]:
                     flow = min(flow,cost[s][t])
                     que.append([t,flow])
                     ed[t] = False
                     route[t] = s
                     if t == Goal:
                         ans += flow
                         break
             else:
                 continue
             break
         else:
             return False

         t = Goal
         s = route[t]
         while s != -1:
             cost[s][t] -= flow
             if cost[s][t] ==0:
                 lines[s].remove(t)
             if cost[t][s] ==0:
                 lines[t].add(s)
             cost[t][s] += flow
             t = s
             s = route[t]

         return True

     while True:
         if ford_in(start):
             continue
         else:
             break
     return ans

N = int(input())
red = []
blue = []
for _ in range(N):
    a,b = inpl()
    red.append((a,b))
for _ in range(N):
    c,d = inpl()
    blue.append((c,d))

lines = defaultdict(set)
nnum = 2*N+2
cost = [[0]*nnum for i in range(nnum)]
for j in range(1,N+1):
    lines[0].add(j)
    cost[0][j] = 1
for k in range(N+1,2*N+1):
    lines[k].add(2*N + 1)
    cost[k][2*N+1]=1
for rd,r in enumerate(red):
    for bd,b in enumerate(blue):
        if (r[0] < b[0]) and (r[1]<b[1]):
            lines[rd+1].add(bd+1+N)
            cost[rd+1][bd+1+N]=1

print(ford_fulkerson(lines,cost,2*N+2,0,2*N+1))
