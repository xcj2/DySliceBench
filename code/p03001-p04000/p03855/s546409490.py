from collections import Counter
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            # 経路圧縮
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

N,K,L = map(int,input().split())
l = []
ufp = UnionFind(N)
ufr = UnionFind(N)
for i in range(K):
    p,q = map(int, input().split())
    ufp.union(p-1, q-1)
for i in range(L):
    r,s = map(int,input().split())
    ufr.union(r-1, s-1)

for i in range(N):
    tup = (ufp.find(i), ufr.find(i))
    l.append(tup)
c = Counter(l)
for i in range(N):
    # 個数を調べたいデータを入れると、その個数が返される
    print(c[l[i]], end=" ")