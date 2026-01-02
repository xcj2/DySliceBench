import sys
sys.setrecursionlimit(10**7)

readline = sys.stdin.buffer.readline
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))


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

n,m = readints()

a = readints()

u = UnionFind(n)
for i in range(m):
    x,y = readints()
    u.unite(x,y)

for i in range(n):
    u.find(i)

b = {}
for i in range(n):
    if u.par[i]<0:
        b[i] = (a[i],i)

for i,p in enumerate(u.par):    
    if p>=0 and b[p][0]>a[i]:
        b[p] = (a[i],i)

for v in b.values():
    a[v[1]]=10**10

a.sort()
if len(b)==1:
    print(0)
elif n < len(b)*2-2:
    print('Impossible')
else:
    print(sum([x[0] for x in b.values()]) + sum(a[:len(b)-2]))
