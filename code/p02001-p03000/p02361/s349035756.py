import sys, heapq
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**10
MOD = 1000000007
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()

def dijkstra(G, s):
    que = []
    d = [INF]*len(G)
    d[s] = 0
    heapq.heappush(que, (d[s], s))

    while que:
        p = heapq.heappop(que)
        v = p[1]
        if d[v] < p[0]: continue
        for e in G[v]:
            if d[e[0]] > d[v] + e[1]:
                d[e[0]] = d[v] + e[1]
                heapq.heappush(que, (d[e[0]], e[0]))
    return d

def resolve():
    V, E, r = LI()
    std = [LI() for _ in range(E)]

    edge = [[] for _ in range(V)]
    for i in std:
        edge[i[0]].append((i[1], i[2]))

    d = dijkstra(edge, r)

    for i in d:
        if i<INF:
            print(i)
        else:
            print('INF')

if __name__ == '__main__':
    resolve()
