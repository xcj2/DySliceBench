class UnionFind:
    # 初期化
    def __init__(self, n):
        # 根なら-size, 子なら親の頂点
        self.par = [-1] * n
        # 木の高さ
        self.rank = [0] * n

    # 検索
    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # 併合
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        # 異なる集合に属する場合のみ併合
        if x != y:
            # 高い方をxとする。
            if self.rank[x] < self.rank[y]:
                x,y = y,x
            # 同じ高さの時は高さ+1
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            # yの親をxとし、xのサイズにyのサイズを加える
            self.par[x] += self.par[y]
            self.par[y] = x

    # 同集合判定
    def same(self, x, y):
        return self.find(x) == self.find(y)

    # 集合の大きさ
    def size(self, x):
        return -self.par[self.find(x)]


n,m = map(int, input().split())
l = [[] for i in range(n+m)]
for i in range(n):
    k = list(map(int, input().split()))
    for j in range(1,k[0]+1):
        l[i].append(k[j]-1+n)
        l[k[j]-1+n].append(i)

u = UnionFind(len(l))
for i in range(len(l)):
    for j in range(len(l[i])):
        u.unite(i,l[i][j])

for i in range(n):
    if not u.same(0,i):
        print('NO')
        exit()
print('YES')
