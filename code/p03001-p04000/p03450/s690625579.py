import sys
sys.setrecursionlimit(10**7)

readline = sys.stdin.buffer.readline
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))

class UnionFind_weight:
    # 初期化
    def __init__(self, n):
        # 根なら-size, 子なら親の頂点
        self.par = [-1] * n
        # 木の高さ
        self.rank = [0] * n
        # 親との差分
        self.weight = [0] * n

    # 検索
    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            p = self.par[x]  # 根につなぎ直す前の親をメモ
            self.par[x] = self.find(self.par[x])
            self.weight[x] += self.weight[p]
            return self.par[x]

    # 併合
    # x → y の重みを w とする。
    def unite(self, x, y, w):
        w += self.weight[x] - self.weight[y]
        x = self.find(x)
        y = self.find(y)
        if x != y:  # 異なる集合に属する場合のみ併合
            if self.rank[x] < self.rank[y]:  # 高い方をxとする。
                x,y = y,x
                w = -w
            if self.rank[x] == self.rank[y]:  # 同じ高さの時は高さ+1
                self.rank[x] += 1
            # yの親をxとし、xのサイズにyのサイズを加える。重みも更新。
            self.par[x] += self.par[y]
            self.par[y] = x
            self.weight[y] = w

    # 同集合判定
    def same(self, x, y):
        return self.find(x) == self.find(y)

    # 集合の大きさ
    def size(self, x):
        return -self.par[self.find(x)]
    
    # x → y の重み
    def diff(self, x, y):
        return self.weight[y] - self.weight[x]

n,m = readints()

u = UnionFind_weight(n)

ans = 1
for i in range(m):
    l,r,d = readints()
    l-=1;r-=1
    if u.same(l,r):
        if u.diff(l,r) != d:
            ans = 0
            break
    else:
        u.unite(l,r,d)

print('Yes' if ans else 'No')




