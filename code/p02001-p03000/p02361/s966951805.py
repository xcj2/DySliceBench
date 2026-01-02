import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
     
def main():
    N, M, st = LI()
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b, cost = LI()
        G[a].append((cost, b))

    def dijkstra(st):
        d = [inf] * N
        q = []
        d[st] = 0
        heapq.heappush(q, (0, st))
        while q:
            dist, u = heapq.heappop(q)
            for cost, v in G[u]:
                if dist + cost < d[v]:
                    d[v] = dist + cost
                    heapq.heappush(q, (d[v], v))
        return d
    d = dijkstra(st)
    for num in d:
        if num == inf:
            print("INF")
        else:
            print(num)





main()


