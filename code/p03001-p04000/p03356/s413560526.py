class UnionFind:
    def __init__(self, n, p):
        '木の初期化をする'
        # zero-index
        self.p  = [-1] * n
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
                self.rank[x] += 1
            self.p[x] = y # x の親を y にする
            return True
        else:
            return False

    def same(self, x, y):
        return self.find(x) == self.find(y)

def main():
    n,m = map(int,input().split())
    p = list(map(int,input().split()))

    uf = UnionFind(n,p)
    for i in range(m):
        x,y = map(int,input().split())
        uf.unite(x-1,y-1)

    ans = 0
    for i,j in enumerate(p):
        ans += uf.same(i, j-1)
    print(ans)
main()
