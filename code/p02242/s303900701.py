import sys, collections, heapq
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**10
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

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
    n = I()
    G = [[] for _ in range(n)]
    for i in range(n):
        ukvc = LI()
        u = ukvc[0]
        k = ukvc[1]
        for j in range(k):
            v = ukvc[2*j+2]
            c = ukvc[2*j+3]
            G[u].append((v, c))

    ans = dijkstra(G, 0)
    for i, e in enumerate(ans):
        print(i, e)

if __name__ == '__main__':
    resolve()

