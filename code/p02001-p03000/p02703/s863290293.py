#! /usr/bin/env python3
from collections import defaultdict
import heapq
import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))
def make_array(dim, type=int): return defaultdict(lambda: defaultdict(type))


INF=10**20
def main():
    N,M,S=mi()
    
    G = [[] for _ in range(N+1) ]
    T = [None] * M
    for i in range(M):
        u,v,a,b=mi()
        T[i] = (u,v,a,b)
        G[u].append((i,v,a,b)) # i番目の路線
        G[v].append((i,u,a,b))
        

    
    C = []
    D = []
    for i in range(N):
        c,d = mi()
        C.append(c)
        D.append(d)
    
    cost = defaultdict(lambda: defaultdict(int))
    E = defaultdict(lambda: [])
    for i in range(0,2501):
        for track in T:
            u,v,a,b = track
            if i-a < 0: continue
            cost[(u,i)][(v,i-a)] = b
            cost[(v,i)][(u,i-a)] = b
            E[(u,i)].append((v,i-a))
            E[(v,i)].append((u,i-a))
            
        
        for j in range(N):
            c,d = C[j],D[j]
            cost[(j+1,i)][(j+1,i+c)] = d
            E[(j+1,i)].append((j+1,i+c))





    if S > 2500: S = 2500

    s = (1,S)
    hq = [(0,s)]
    heapq.heapify(hq)

    dist = defaultdict(lambda: INF)
    dist[s] = 0
    while hq: 
        d,x = heapq.heappop(hq) # sからxまでの最短経路を探索する
        if dist[x] < d: continue

        for e in E[x]:
            # print(dist[e] , dist[x] , cost[x][e])
            if dist[e] > dist[x] + cost[x][e]:
                dist[e] = dist[x] + cost[x][e]
                heapq.heappush(hq,(dist[e],e))
    
    for t in range(2,N+1):
        ans = INF
        for i in range(0,2501):
            ans = min(ans,dist[(t,i)])
        print(ans)

    # if dist[t] == INF: return -1
    # return dist[t]






if __name__ == "__main__":
    main()