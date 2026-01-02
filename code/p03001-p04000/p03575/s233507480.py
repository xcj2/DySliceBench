# https://atcoder.jp/contests/abc075/tasks/abc075_c

from collections import defaultdict

N, M = map(int, input().split())
par = [-1] * N
G = defaultdict(list)

########################################
class UnionFind(object):
    def __init__(self, n):
        self.par = [-1] * n
    
    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        if x == y:
            return False
        else:
            if self.par[x] > self.par[y]:
                x, y = y, x
            self.par[x] += self.par[y]
            self.par[y] = x
            return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.par[self.find(x)]
########################################

edges = []
ufG = UnionFind(N)
for _ in range(M):
    ai, bi = map(int, input().split())
    ai, bi = ai - 1, bi - 1
    edges.append((ai, bi))
    G[ai].append(bi)
    G[bi].append(ai)
    ufG.unite(ai, bi)

# 1本以外を入れたグラフを考える
count = 0
for m in range(M):
    ufGm = UnionFind(N)
    for k in range(M):
        if k == m:
            continue
        ai, bi = edges[k]
        ufGm.unite(ai, bi)

    flag = False
    for k in range(N):
        if ufGm.size(k) != ufG.size(k):
            flag = True
            break
    if flag:
        count += 1
print(count)