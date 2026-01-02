class UnionFind():

    def __init__(self, n):
        # 頂点の値が0から始まる前提なので注意
        self.par = [i for i in range(n)]

    def root(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return
        
        self.par[x] = y
        return


def main():
    N, M = map(int, input().split())
    p = list(map(lambda x: int(x)-1, input().split()))

    uf = UnionFind(N)
    for i in range(M):
        x, y = map(int, input().split())
        uf.unite(x-1, y-1)
    
    ans = 0
    for i in range(N):
        if uf.same(i, p[i]):
            ans += 1
    
    print(ans)


if __name__ == '__main__':
    main()
