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


from operator import itemgetter

n = int(input())

xy = []
for i in range(n):
    x,y = map(int, input().split())
    xy.append([i,x,y])

x = sorted(xy,key=itemgetter(1))
y = sorted(xy,key=itemgetter(2))

xx = []
yy = []

for i in range(n-1):
    xx.append([x[i][0],x[i+1][0],x[i+1][1]-x[i][1]])
    yy.append([y[i][0],y[i+1][0],y[i+1][2]-y[i][2]])

xx.sort(key=itemgetter(2))
yy.sort(key=itemgetter(2))
xx.reverse()
yy.reverse()

a = UnionFind(n)

ans = 0

i = 0
xxx = xx.pop()
yyy = yy.pop()
while i!=n-1:
    if xxx[2] < yyy[2]:
        if not a.same(xxx[0],xxx[1]):
            a.unite(xxx[0],xxx[1])
            ans += xxx[2]
            i += 1
        if xx:
            xxx = xx.pop()
        else:
            xxx = [0,0,float('inf')]
    else:
        if not a.same(yyy[0],yyy[1]):
            a.unite(yyy[0],yyy[1])
            ans += yyy[2]
            i += 1
        if yy:
            yyy = yy.pop()
        else:
            yyy = [0,0,float('inf')]
print(ans)