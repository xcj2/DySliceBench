# -*- coding: utf-8 -*-
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
write = sys.stdout.write
def ii(): return int(readline())
def mi(): return map(int, readline().rstrip().split())
def li(): return list(readline().rstrip())
def lmi(): return list(map(int, readline().rstrip().split()))
def end(*arg): print(*arg); sys.exit()
# template

import collections
import itertools

class edge():
    def __init__(self, src: int, to: int, cost: int):
        self.src = src
        self.to = to
        self.cost = cost
    def __str__(self):
        return "(" + str(self.src) + ", " + str(self.to) + ", " + str(self.cost) + ")"

class rootedtree():
    def __init__(self, n: int) -> None:
        _l = 0
        while pow(2, _l) < n:
            _l += 1
        self._l = _l
        self.size = n
        self.par = [[-1 for i in range(n + 1)] for i in range(_l)]
        self.graph = [[] for i in range(n)]  # type:ignore
        self.depth = [-1 for i in range(n)]
        self.root = -1

    def add_edge(self, src: int, to: int, cost: int = 1):
        self.graph[src].append(edge(src, to, cost))
        self.graph[to].append(edge(to, src, cost))

    def parent(self, x: int):
        return self.par[0][x]

    def bfs(self, s: int) -> list:
        INF = 10**9
        dist = [INF] * self.size
        que = collections.deque()  # type:ignore
        que.append(s)
        dist[s] = 0
        while len(que):
            v = que.popleft()
            for e in self.graph[v]:
                if dist[e.to] != INF:
                    continue
                dist[e.to] = dist[e.src] + 1
                que.append(e.to)
        return dist

    def __dfs1(self, r):
        root = r
        self.depth[r] = 0
        que = collections.deque()
        que.append(root)
        while len(que) != 0:
            v = que.pop()
            for u in self.graph[v]:
                if u.to != self.parent(v):
                    self.par[0][u.to] = v
                    self.depth[u.to] = self.depth[v] + 1
                    que.append(u.to)

    def build(self, _root=0) -> None:
        assert(self.root == -1)
        self.root = _root
        self.__dfs1(self.root)
        for i, j in itertools.product(range(self._l - 1), range(self.size)):
            if(self.par[i][j] == -1):
                self.par[i + 1][j] = -1
            else:
                self.par[i + 1][j] = self.par[i][self.par[i][j]]

    def lca(self, x: int, y: int) -> int:
        assert(self.root != -1)
        if self.depth[x] > self.depth[y]:
            x, y = y, x
        dif = self.depth[y] - self.depth[x]
        for i in range(self._l - 1, -1, -1):
            if dif & (1 << i):
                y = self.par[i][y]
        if x == y:
            return x
        for i in range(self._l - 1, -1, -1):
            nx = self.par[i][x]
            ny = self.par[i][y]
            if nx != ny:
                x = nx; y = ny
        return self.par[0][x]

    def depth_dif(self, x: int, y: int) -> int:
        assert(self.root != -1)
        z = self.lca(x, y)
        return self.depth[x] + self.depth[y] - 2 * self.depth[z]

def main():
    n, u, v = mi()
    u -= 1; v -= 1
    g = rootedtree(n)
    for _ in range(n - 1):
        a, b = mi()
        g.add_edge(a - 1, b - 1)
    ans = -1
    # du = g.bfs(u)
    # dv = g.bfs(v)
    # for i in range(n):
    #     if du[i] < dv[i]:
    #         ans = max(ans, dv[i])
    g.build(v)
    for i in range(n):
        x = g.lca(u, i)
        if g.depth_dif(u, x) < g.depth_dif(v, x):
            ans = max(ans, g.depth_dif(v, i))
    print(ans - 1)
    return


if __name__ == '__main__':
    main()
