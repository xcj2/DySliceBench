class WarshallFloyd:
    def __init__(self,n):
        self.v = n
        self.d = [[1e100]*n for _ in range(n)]
        for i in range(n):
            self.d[i][i] = 0

    def path(self,x,y,c):
        if x == y:
            return False
        self.d[x][y] = c
        self.d[y][x] = c
        return True

    def build(self):
        for k in range(self.v):
            for i in range(self.v):
                for j in range(self.v):
                    self.d[i][j] = min(self.d[i][j], self.d[i][k] + self.d[k][j])
        return self.d

class UnionFind:
    def __init__(self, n):
        '木の初期化をする'
        self.p = [-1] * n
        self.rank = [1]*n
    def find(self, x):
        'x の親を返す'
        if self.p[x] == -1:
            return x
        else:
            self.p[x] = self.find(self.p[x])
            return self.p[x]

    def unite(self, x, y):
        'rankの低い親を高い方のの親にする'
        if not self.same(x,y):
            x = self.find(x)
            y = self.find(y)
            if self.rank[x] > self.rank[y]:
                x,y = y,x
            elif self.rank[x] == self.rank[y]:
                self.rank[y] += 1
            self.p[x] = y
            return True
        else:
            return False

    def same(self, x, y):
        return self.find(x) == self.find(y)

n = int(input())
wf = WarshallFloyd(n*2)
uf = UnionFind(n*2)
for i in range(n):
    s = input()
    for j in range(i):
        if s[j] == '1':
            wf.path(i,j,1)
            uf.unite(i,j+n)
            uf.unite(i+n,j)
for i in range(n):
    if uf.same(i,i+n):
        print(-1)
        exit(0)
d = wf.build()
ans = 0
for i in range(n):
    for dist in d[i][:i]:
        ans = max(ans,dist)
print(ans+1)
