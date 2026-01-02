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

# ソート
c = sorted(a)
d = sorted(b)

# 必要
for i in range(n):
    if c[i]>d[i]:
        print('No')
        exit()

# 十分。同値含むケース除外も
for i in range(n-1):
    if c[i+1]<=d[i]:
        print('Yes')
        exit()

# indexのためのdict
aa = {}  # 初期a
bb = {}  # 初期b
cc = {}  # 最終a
dd = {}  # 最終b
for i in range(n):
    aa[a[i]]=i
    bb[b[i]]=i
    cc[c[i]]=i
    dd[d[i]]=i

# サイクルでグループ化
u = UnionFind(n)
for i in range(n):
    j = aa[c[dd[b[i]]]]
    u.unite(i,j)

# グループ2つ以上でOK
for i in range(n):
    if u.same(0,i)==False:
        print('Yes')
        exit()

print('No')