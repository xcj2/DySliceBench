import sys


import heapq
class Dijkstra:
    INF = 10**18

    def __init__(self, N, Graph=[[-1]]):
        self.N = (N+1)
        self.dist = [self.INF] * (N+1)
        if Graph[0][0]!=-1: self.G = Graph
        else: self.G = [[] for _ in range(N+1)]

    def insert(self, From, To, Cost):
        self.G[From].append([To, Cost])

    def reset(self):
        for i in range(self.N): self.dist[i] = self.INF

    def dijkstra(self, st):
        self.reset()
        hq = [(0, st)]
        heapq.heapify(hq)
        while len(hq):
            tmp = heapq.heappop(hq)
            now, now_dist = tmp[1], tmp[0]
            if self.dist[now] <= now_dist: continue
            self.dist[now] = now_dist
            for to in self.G[now]:
                heapq.heappush(hq, (now_dist+to[1], to[0]))

def main():
    input=sys.stdin.readline
    n, m, s = map(int, input().split())
    MAX_MONEY = 2600
    dj = Dijkstra((n+1)*(MAX_MONEY+1))

    for i in range(m):
        a, b, c, d = map(int, input().split())
        a, b = a-1, b-1
        for j in range(c, MAX_MONEY):
            dj.insert(a*MAX_MONEY+j, b*MAX_MONEY+(j-c), d)
            dj.insert(b*MAX_MONEY+j, a*MAX_MONEY+(j-c), d)

    for i in range(n):
        a, b = map(int, input().split())
        for j in range(MAX_MONEY-a-1):
            dj.insert(i*MAX_MONEY+j, i*MAX_MONEY+(j+a), b)

    s = min(s, MAX_MONEY-1)
    dj.dijkstra(0*MAX_MONEY+s)

    for i in range(1, n):
        ans = 10**18
        for j in range(MAX_MONEY):ans = min(ans, dj.dist[i*MAX_MONEY + j])
        print(ans)

if __name__=="__main__":
  main()
