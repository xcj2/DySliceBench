import sys
from collections import deque
read = sys.stdin.read
readline = sys.stdin.buffer.readline
INF = float('inf')

class Dinic:
    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]

    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)

    def add_multi_edge(self, v1, v2, cap1, cap2):
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.G[v1].append(edge1)
        self.G[v2].append(edge2)

    def bfs(self, s, t):
        self.level = level = [None]*self.N
        deq = deque([s])
        level[s] = 0
        G = self.G
        while deq:
            v = deq.popleft()
            lv = level[v] + 1
            for w, cap, _ in G[v]:
                if cap and level[w] is None:
                    level[w] = lv
                    deq.append(w)
        return level[t] is not None

    def dfs(self, v, t, f):
        if v == t:
            return f
        level = self.level
        for e in self.it[v]:
            w, cap, rev = e
            if cap and level[v] < level[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, s, t):
        flow = 0
        G = self.G
        while self.bfs(s, t):
            *self.it, = map(iter, self.G)
            f = INF
            while f:
                f = self.dfs(s, t, INF)
                flow += f
        return flow

def main():
    N = int(readline())

    AB = []
    for _ in range(N):
        a, b = map(int, readline().split())
        AB.append([a,b])

    CD = []
    for _ in range(N):
        c, d = map(int, readline().split())
        CD.append([c,d])

    dinic = Dinic(2*N+2)

    for i in range(N):
        a, b = AB[i]
        for j in range(N):
            c, d = CD[j]
            if a<c and b<d:
                dinic.add_edge(i+1,N+j+1,1)

    for i in range(N):
        dinic.add_edge(0, i+1, 1)
        dinic.add_edge(N+i+1, 2*N+1, 1)

    ans = dinic.flow(0, 2*N+1)
    print(ans)

if __name__ == '__main__':
    main()
