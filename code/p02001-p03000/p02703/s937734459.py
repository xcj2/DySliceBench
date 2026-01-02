def examA():
    S, W = LI()
    if S<=W:
        print("unsafe")
    else:
        print("safe")
    return

def examB():
    A, B, C, D = LI()
    while(True):
        C -= B
        if C<=0:
            print("Yes")
            break
        A -= D
        if A<=0:
            print("No")
            break
    return

def examC():
    N = I()
    S = [SI()for _ in range(N)]
    Set = set(S)
    ans = len(Set)
    print(ans)
    return

def examD():
    S = SI()
    N = len(S)
    D = [0]*(N+1)
    for i in range(N):
        D[i+1] = (D[i]+int(S[N-1-i])*pow(10,i,2019))%2019
    #print(D)
    ans = 0
    C = Counter(D)
    #print(C)
    for c in C.values():
        ans += (c-1)*c//2
    print(ans)
    return

def examE():
    def dijkstra(n, edges, start, C, silver):
        maxC = (2*n-1)*50
        dist = [[inf]*(maxC+1) for _ in range(n)]
        dist[start][silver] = 0
        Q = [(0, (start, silver))]  # (dist,vertex)
        while (Q):
            d, (v, c) = heapq.heappop(Q)
            if dist[v][c]<d:continue
            loop = (maxC-c)//C[v][0] + 1
            for i in range(loop):
                nextc = c+i*C[v][0]
                nextd = d+i*C[v][1]
                if nextc>maxC:
                    nextc=maxC
                if dist[v][nextc] < nextd: continue  # 候補として挙がったd,vだが、他に短いのがある
                for u, cost, coin in edges[v]:
                    k = nextc-coin
                    if k<0:
                        continue
                    if dist[u][k] > nextd + cost:
                        dist[u][k] = nextd + cost
                        heapq.heappush(Q, (dist[u][nextc-coin], (u, k)))
        return dist
    N, M, S = LI()
    V = [[]for _ in range(N)]
    for _ in range(M):
        s, t, a, b = LI()
        s -= 1; t -= 1
        V[s].append((t,b,a))
        V[t].append((s,b,a))
    C = [LI()for _ in range(N)]
    D = dijkstra(N,V,0,C,min(S,(2*N-1)*50))
    for i in range(1,N):
        print(min(D[i]))
    return

def examE2():
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
    maxS = 2501
    N, M, S = LI()
    V = [[]for _ in range(N*(maxS+1))]

    for _ in range(M):
        u, v, a, b = LI()
        u -= 1; v -= 1
        for i in range(a, maxS):
            V[u * maxS + i].append([v * maxS + i - a, b])
            V[v * maxS + i].append([u * maxS + i - a, b])
    for i in range(N):
        c, d = LI()
        for j in range(maxS-1):
            V[i * maxS + j].append([i * maxS + min(j + c, maxS-1), d])
    #print(V)
    D = dijkstra(V,min(maxS-1,S))
    #for i in range(N):
    #    print(D[i*maxS:(i+1)*maxS])

    for i in range(1,N):
        print(min(D[i*maxS:(i+1)*maxS]))
    return

def examF():
    N = I()
    S = LI()
    T = LI()
    U = LI()
    V = LI()

    ans = 0
    print(ans)
    return

import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def I(): return int(readline())
def LI(): return list(map(int,readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = 10**(-12)
alphabet = [chr(ord('a') + i) for i in range(26)]

sys.setrecursionlimit(10**7)

if __name__ == '__main__':
    examE2()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""