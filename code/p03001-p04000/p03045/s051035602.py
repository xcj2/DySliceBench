class Uf:
    def __init__(self, N):
        self.p = list(range(N))
        self.rank = [0] * N
        self.size = [1] * N

    def root(self, x):
        if self.p[x] != x:
            self.p[x] = self.root(self.p[x])

        return self.p[x]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        u = self.root(x)
        v = self.root(y)

        if u == v: return

        if self.rank[u] < self.rank[v]:
            self.p[u] = v
            self.size[v] += self.size[u]
            self.size[u] = 0
        else:
            self.p[v] = u
            self.size[u] += self.size[v]
            self.size[v] = 0

            if self.rank[u] == self.rank[v]:
                self.rank[u] += 1

    def count(self, x):
        return self.size[self.root(x)]

def main():
    n,m = map(int,input().split())
    ls = [[int(x) for x in input().split()] for _ in range(m)]
    uni = Uf(n+1)

    for i in range(m):
        a,b,c = ls[i]
        uni.unite(a,b)
    ans = 0
    for i in range(1,n+1):
        if i == uni.root(i):
            ans +=1
        else:
            pass
    print(ans)

if __name__ == "__main__":
    main()