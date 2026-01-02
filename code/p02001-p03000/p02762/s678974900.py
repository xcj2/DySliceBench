class union_find():
    __slots__ = ["par", "rank", "size"]
    def __init__(self, n):
        self.par = [i for i in range(n + 1)]
        self.rank = [1 for i in range(n + 1)]
        self.size = [1 for i in range(n + 1)]

    def find(self, c):
        if self.par[c] == c:
            return c

        ret = self.find(self.par[c])
        self.par[c] = ret
        return ret

    def union(self, x, y):

        xr = self.find(x)
        yr = self.find(y)
        if xr == yr:
            return

        if self.rank[yr] > self.rank[xr]:
            self.par[xr] = yr
            self.size[yr] += self.size[xr]
        else:
            self.par[yr] = xr
            self.size[xr] += self.size[yr]
            if self.rank[xr] == self.rank[yr]:
                self.rank[xr] += 1

    def size_belong(self, i):
        return self.size[self.find(i)]

    def mass_size(self):
        return [i == v for i, v in enumerate(self.par)].count(True) - 1

    def show(self):
        print('parent', self.par[1:])
        print('rank', self.rank[1:])

def main():
    from collections import defaultdict

    dicf = defaultdict(lambda :[])
    dicb = defaultdict(lambda :[])

    N, M, K = map(int, input().split())

    uf = union_find(N)
    for i in range(M):
        a, b = map(int, input().split())
        dicf[a].append(b)
        dicf[b].append(a)
        if a > b:
            a, b = b, a
        uf.union(a, b)

    for i in range(K):
        c, d = map(int, input().split())
        dicb[c].append(d)
        dicb[d].append(c)

    ans = []
    for i in range(1, N + 1):
        x = uf.size_belong(i) - len(dicf[i]) - 1
        m = 0
        for b in dicb[i]:
            if uf.find(b) == uf.find(i):
                m += 1

        ans.append(x - m)


    print(' '.join(map(str, ans)))




if __name__ == '__main__':
    main()