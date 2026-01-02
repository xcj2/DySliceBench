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
class edge():
    def __init__(self, src, to):
        self.src = src
        self.to = to
    def __str__(self):
        return "(" + str(self._from) + ", " + str(self._to) + ")"

class rootedtree():
    def __init__(self, n):
        l = 0
        while pow(2, l) < n:
            l += 1
        self._l = l
        self.size = n
        self.par = [[-1 for i in range(n + 1)] for i in range(l)]
        self.graph = [[] for i in range(n)]
        self.depth = [-1 for i in range(n)]
        self.root = -1

    def add_edge(self, src, to):
        self.graph[src].append(edge(src, to))
        self.graph[to].append(edge(to, src))

    def parent(self, i):
        return self.par[0][i]

    def __dfs1(self, r) -> None:
        root = r
        self.depth[r] = 0
        que = collections.deque()
        que.append((0, root))
        while len(que) != 0:
            v = que.pop()
            for u in self.graph[v[1]]:
                if u.to != self.parent(v[1]):
                    self.par[0][u.to] = v[1]
                    self.depth[u.to] = v[0] + 1
                    que.append((v[0] + 1, u.to))

    def build(self, _root=0) -> None:
        assert(self.root == -1)
        self.root = _root
        self.__dfs1(self.root)
        for i in range(self._l - 1):
            for j in range(self.size):
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
    g.build(v)
    ans = -1
    for i in range(n):
        x = g.lca(u, i)
        if g.depth_dif(u, x) < g.depth_dif(v, x):
            ans = max(ans, g.depth_dif(v, i))
    print(ans - 1)
    return


if __name__ == '__main__':
    main()
