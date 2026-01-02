def examC():
    ans = 0
    print(ans)
    return

def examD():
    ans = 0
    print(ans)
    return

def examE():
    def dijkstra(edges, start=0):
        dist = [inf] * len(edges)
        dist[start] = 0
        Q = [(0, start)]  # (dist,vertex)
        while (Q):
            d, v = heapq.heappop(Q)
            if dist[v] < d: continue  # 候補として挙がったd,vだが、他に短いのがある
            for u, cost in edges[v]:
                if dist[u] > dist[v] + cost:
                    dist[u] = dist[v] + cost
                    heapq.heappush(Q, (dist[u], u))
        return dist
    N, M = LI()
    S, T = LI()
    S -= 1; T -= 1
    V = [set()for _ in range(N)]
    for _ in range(M):
        u, v, c = LI()
        u -= 1; v -= 1
        V[u].add((v,c))
        V[v].add((u,c))
    distS = dijkstra(V,S)
    distT = dijkstra(V,T)
    L = distS[T]
    numS = [i for i in range(N)]
    C = list(zip(distS,numS))
    C.sort()
    _, numS = zip(*C)
    numT = [i for i in range(N)]
    C = list(zip(distT,numT))
    C.sort()
    _, numT = zip(*C)
    #print(numS)

    dp1 = [0]*N
    dp2 = [0]*N
    dp1[S] = 1; dp2[T] = 1
    S_collision_points = set()
    S_collision_edges = set()
    for now in numS:
        if distS[now] + distT[now] == L and distS[now] == distT[now]:
            S_collision_points.add(now)
        #print(now,used,dp1)
        for v,c in V[now]:
            if distT[v]+distS[now]==L-c:
                #print(distS[v],distS[now],now)
                dp1[v] += dp1[now]
                dp1[v] %= mod
                if distS[now]*2<L and L<distS[v]*2:
                    S_collision_edges.add((now,v))
    for now in numT:
        for v,c in V[now]:
            if distS[v]+distT[now]==L-c:
                dp2[v] += dp2[now]
                dp2[v] %= mod
    collision_points = S_collision_points
    collision_edges = S_collision_edges
    #print(distS)
    #print(distT)
    #print(dp1)
    #print(dp2)
    #print(S_collision_edges)
    ans = 0
    ans += dp1[T]**2
    ans %= mod
    for p in collision_points:
        if distS[p]==distT[p]:
            ans -= (dp1[p]**2)*(dp2[p]**2)
            ans += supermod
            ans %= mod
            #print(ans,p)
    for u,v in collision_edges:
        ans -= (dp1[u]**2)*(dp2[v]**2)
        ans += supermod
        ans %= mod
        #print(ans,u,v)
    print(ans)
    return

def examF():
    ans = 0
    print(ans)
    return


from decimal import getcontext,Decimal as dec
import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def I(): return int(input())
def LI(): return list(map(int,sys.stdin.readline().split()))
def DI(): return dec(input())
def LDI(): return list(map(dec,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
supermod = mod**4
mod2 = 998244353
inf = 10**18
_ep = dec("0.000000000001")
alphabet = [chr(ord('a') + i) for i in range(26)]
alphabet_convert = {chr(ord('a') + i): i for i in range(26)}

getcontext().prec = 28

sys.setrecursionlimit(10**7)

if __name__ == '__main__':
    examE()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""