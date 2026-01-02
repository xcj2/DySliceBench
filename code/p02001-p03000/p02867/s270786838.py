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

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 必要
c = sorted(a)
d = sorted(b)
for i in range(n):
    if c[i]>d[i]:
        print('No')
        exit()

for i in range(n-1):
    if c[i+1]<=d[i]:
        print('Yes')
        exit()

for i in range(n-1):
    if c[i]==c[i+1]:
        print('Yes')
        exit()
    if d[i]==d[i+1]:
        print('Yes')
        exit()

# 理想と現実の対応
e = {}
f = {}
for i in range(n):
    e[c[i]]=d[i]
    f[a[i]]=b[i]

# 理想と現実の対応の逆
ee = {v: k for k, v in e.items()}
ff = {v: k for k, v in f.items()}

for x in a:
    if e[x]==f[x]:
        print('Yes')
        exit()

z = [0]*n
u = UnionFind(n)

g = {}
for i in range(n):
    g[a[i]]=i

for i in range(n):
    if z[i]==1:
        continue
    x = a[i]
    y = f[x]
    j = i
    while z[j]==0:
        z[j]=1
        x = ee[y]
        y = f[x]
        jj = g[x]
        u.unite(j,jj)
        j=jj

for i in range(n):
    if u.same(0,i)==False:
        print('Yes')
        exit()


print('No')