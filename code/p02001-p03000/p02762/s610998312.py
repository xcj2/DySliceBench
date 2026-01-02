import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline
n,m,k = [int(i) for i in readline().split()]
ab = [[int(i) for i in readline().split()] for _ in range(m)]
cd = [[int(i) for i in readline().split()] for _ in range(k)]

class UnionFind():
    def __init__(self, n=0):
        self.d = [-1]*n # 負なら根、非負なら親IDの情報を持たせる。負の値の絶対値で連結成分のサイズを表す（-2なら連結成分サイズ2の根）

    def find(self, x):
        """
        根のIDを返す
        """
        if self.d[x] < 0: return x # 今の頂点が根なら頂点番号を返す
        self.d[x] = self.find(self.d[x]) # 今の頂点が根でないなら親についてfindクエリを投げる. d[x] = find(d[x])で経路縮約できる
        return self.d[x]

    def unite(self, x, y):
        """
        根同士をくっつける
        """
        x = self.find(x); y = self.find(y) # 根同士をくっつける
        if x == y: return False # 根が同じなら何もする必要はない。Falseを返しているのは、くっつけられたかどうかを返した方が便利なときがあるから（MSTなど）
        if self.d[x] > self.d[y]: x,y = y,x # 小さい方の部分木を大きい方の部分木にくっつけるためにswap。dがマイナスなので不等号が逆になる点に注意
        self.d[x] += self.d[y] # 連結成分サイズを更新
        self.d[y] = x # 根をyからxに張り替える
        return True

    def same(self, x, y):
        """
        同じ集合に所属しているかどうか
        """
        return self.find(x) == self.find(y)

    def size(self, x):
        """
        連結成分サイズを返す
        """
        return -self.d[self.find(x)]

MAXN = 100005
deg = [0]*MAXN
to = [[] for _ in range(MAXN)]

uf = UnionFind(n)

for a,b in ab:
    a -= 1
    b -= 1
    deg[a] += 1
    deg[b] += 1
    uf.unite(a, b)

for c,d in cd:
    c -= 1
    d -= 1
    to[c].append(d)
    to[d].append(c)

anss = []
for i in range(n):
    ans = uf.size(i)-1-deg[i] # 連結成分サイズから自分自身と友達を引く
    for u in to[i]:
        if uf.same(i,u): ans -= 1 # 同じ連結成分にあってブロック関係にあったら友達候補にはなれないので-1する
    anss.append(ans)
print(*anss)