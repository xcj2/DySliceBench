import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()

from collections import deque
class HopcroftKarp:
    def __init__(self, N0, N1):
        self.N0 = N0
        self.N1 = N1
        self.N = N = 2+N0+N1
        self.G = [[] for i in range(N)]
        for i in range(N0):
            forward = [2+i, 1, None]
            forward[2] = backward = [0, 0, forward]
            self.G[0].append(forward)
            self.G[2+i].append(backward)
        self.backwards = bs = []
        for i in range(N1):
            forward = [1, 1, None]
            forward[2] = backward = [2+N0+i, 0, forward]
            bs.append(backward)
            self.G[2+N0+i].append(forward)
            self.G[1].append(backward)

    def add_edge(self, fr, to):
        #assert 0 <= fr < self.N0
        #assert 0 <= to < self.N1
        v0 = 2 + fr
        v1 = 2 + self.N0 + to
        forward = [v1, 1, None]
        forward[2] = backward = [v0, 0, forward]
        self.G[v0].append(forward)
        self.G[v1].append(backward)

    def bfs(self):
        G = self.G
        level = [None]*self.N
        deq = deque([0])
        level[0] = 0
        while deq:
            v = deq.popleft()
            lv = level[v] + 1
            for w, cap, _ in G[v]:
                if cap and level[w] is None:
                    level[w] = lv
                    deq.append(w)
        self.level = level
        return level[1] is not None

    def dfs(self, v, t):
        if v == t:
            return 1
        level = self.level
        for e in self.it[v]:
            w, cap, rev = e
            if cap and level[v] < level[w] and self.dfs(w, t):
                e[1] = 0
                rev[1] = 1
                return 1
        return 0

    def flow(self):
        flow = 0
        G = self.G
        bfs = self.bfs; dfs = self.dfs
        while bfs():
            *self.it, = map(iter, G)
            while dfs(0, 1):
                flow += 1
        return flow

    def matching(self):
        return [cap for _, cap, _ in self.backwards]

def resolve():
    n=int(input())
    AB=[tuple(map(int,input().split())) for _ in range(n)]
    CD=[tuple(map(int,input().split())) for _ in range(n)]

    mm=HopcroftKarp(n,n)
    for i in range(n):
        a,b=AB[i]
        for j in range(n):
            c,d=CD[j]
            if(a<c and b<d):
                mm.add_edge(i,j)
    print(mm.flow())
resolve()