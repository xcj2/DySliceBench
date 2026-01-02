import sys
sys.setrecursionlimit(10**9)

from collections import deque

class LCA1():
    def __init__(self, l, start):
        self.n = len(l)
        self.dep=[0]*self.n
        self.par=[[-1]*self.n for i in range(18)]

        def bfs(start):
            is_leaf = [0]*n
            que = deque()
            que.append((start, -1, 0))
            while que:
                c,p,d = que.pop()
                self.dep[c]=d
                self.par[0][c]=p
                cnt = 0
                for to in G[c]:
                    if to != p:
                        que.append((to,c,d+1))
                        cnt += 1
                if not cnt:
                    is_leaf[c] = 1
            return is_leaf

        self.is_leaf = bfs(start)

        for i in range(17):
            for j in range(self.n):
                self.par[i+1][j]=self.par[i][self.par[i][j]]

    def lca(self,a,b):
        if self.dep[a]>self.dep[b]:
            a,b=b,a
        for i in range(18):
            if (self.dep[b]-self.dep[a]) & 1<<i:
                b=self.par[i][b]
        if a==b:
            return a
        for i in range(18)[::-1]:
            if self.par[i][a]!=self.par[i][b]:
                a=self.par[i][a]
                b=self.par[i][b]
        return self.par[0][a]

    def dist(self, a,b):
        return abs(self.dep[a]-self.dep[b])

n, u, v = map(int, input().split())
u, v = u-1, v-1
G = [[] for i in range(n)]
for i in range(n-1):
    a,b = map(int, input().split())
    a,b = a-1,b-1
    G[a].append(b)
    G[b].append(a)

LCA = LCA1(G, v)
ans = 0
for i in range(n):
    if not LCA.is_leaf[i]:
        continue
    lca = LCA.lca(u, i)
    if lca == v:
        continue
    if LCA.dist(lca, u) >= LCA.dist(lca, v):
        continue
    turn = 0
    tmp = 0
    d = LCA.dist(u, lca) + LCA.dist(lca, i)
    if d != 0:
        tmp = 2*d
        aoki = d
    else:
        aoki = 0
    tak = LCA.dep[i]
    m = tak-aoki
    if m%2==1:
        tmp += 2*m -1
    else:
        tmp += 2*(m-1)
    ans = max(ans, tmp)
print(ans//2)
