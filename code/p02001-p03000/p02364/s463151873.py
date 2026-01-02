from heapq import heapify
from heapq import heappop
from heapq import heappush
class UnionFind():
    def __init__(self, n):  #初期化　最初はみんなばらばら
        self.n = n
        self.parents = [-1] * n
    def find(self, x):  #xの根を見つける　たどった経路全ての根を更新
        if self.parents[x] < 0:
            return x   #根の番号を返す
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)  #x,yの木の根
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x  #xをでかい木にする

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):  #xの含まれる木の要素数を返す
        return -self.parents[self.find(x)]

    def same(self, x, y):  #x,yが同じ気に属するか判定
        return self.find(x) == self.find(y)

    def members(self, x):  #xの含まれる木の要素を配列で返す
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):  #根をすべて返す
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self): #木の個数
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())
V,E = map(int,input().split())
uf = UnionFind(V)
hq = []
heapify(hq)
for i in range(E):
    s,t,w = map(int,input().split())
    heappush(hq,(w,s,t))
ans = 0 #最小全域木の辺の重みの総和
while len(hq) != 0:
    w,s,t = heappop(hq)
    if not uf.same(s,t):
        ans += w
        uf.union(s,t)
    else:
        continue
print(ans)
