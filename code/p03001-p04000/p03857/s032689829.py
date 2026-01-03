from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        # 親要素のノード番号を格納　par[x] == x の時そのノードは根
        self.par = [i for i in range(n+1)]
        # 木の高さを格納する（初期状態では0)
        self.rank = [0] * (n+1)
        # 各々の集合の要素数（根が代表して値を持っておく）
        self.count = [1] * (n+1)

    # 検索
    def find(self, x):
        # 根ならその番号を返す
        if self.par[x] == x:
            return x
        # 根でないなら親の要素で再検索
        else:
            # 検索する過程で親を更新
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # 併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.count[y] += self.count[x]
            self.count[x] = 0
        else:
            self.par[y] = x
            self.count[x] += self.count[y]
            self.count[y] = 0
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 同じ集合に属しているか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)

    # 属している集合の要素数
    def size(self,x):
        q = UnionFind.find(self,x)
        return self.count[q]

n, k ,l = map(int,input().split())
road = UnionFind(n)
train = UnionFind(n)

for i in range(k):
    p, q = map(int,input().split())
    road.union(p-1,q-1)

for i in range(l):
    r, s = map(int,input().split())
    train.union(r-1,s-1)

d = defaultdict(int)
a = []
for i in range(n):
    t = (road.find(i),train.find(i))
    d[t] += 1
    a.append(t)

print(*[d[i] for i in a])