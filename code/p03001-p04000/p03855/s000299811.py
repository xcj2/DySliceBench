import sys
input = sys.stdin.readline

from collections import Counter

class Unionfind:

    __slots__ = ['nodes','size']

    def __init__(self, n):
        self.nodes = list(range(n))
        self.size = [1]*n

    def root(self, x):
        if self.nodes[x] == x:
            return x
        else:
            root_x = self.root(self.nodes[x])
            self.nodes[x] = root_x
            return root_x

    def unite(self, x, y):
        x = self.root(x); y = self.root(y)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.size[x] += self.size[y]
        self.nodes[y] = x

    def same(self, x, y):
        return self.root(x) == self.root(y)

N,K,L = map(int,input().split())

uf1 = Unionfind(N)
uf2 = Unionfind(N)

for _ in range(K):
    p,q = map(int,input().split())
    p -= 1; q -= 1
    uf1.unite(p,q)

for _ in range(L):
    r,s = map(int,input().split())
    r -= 1; s -= 1
    uf2.unite(r,s)

# 方針 :各nodeについて(r1,r2)を求める
# dicで(r1,r2)となるようなnodeを数える

keys = []
dic = Counter()

for node in range(N):
    key = (uf1.root(node),uf2.root(node))
    keys.append(key)
    dic[key] += 1

print(*(dic[key] for key in keys))