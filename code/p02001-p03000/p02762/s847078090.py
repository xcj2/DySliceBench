def main():
    n,m,k = map(int,input().split())
    # frend = [[10**6] * n for i in range(n)]
    # block = [[0] * n for i in range(n)]
    # f = [[0]*n for i in range(n)]
    fq = []
    # b = [[0]*n for i in range(n)]
    bq = []
    uf = UnionFind(n)
    dame = [0] * n

    for _ in range(m):
        a,bb = map(int,input().split())
        # f[a-1][bb-1] = 1
        # f[bb-1][a-1] = 1
        uf.union(a-1,bb-1)
        fq.append([a-1,bb-1])

    for _ in range(k):
        c,d = map(int,input().split())
        # b[c-1][d-1] = 1
        # b[d-1][c-1] = 1
        bq.append([c-1,d-1])
        if uf.same(c-1,d-1):
            dame[c-1] += 1
            dame[d-1] += 1


    for i, ff in enumerate(fq):
        if uf.same(ff[0],ff[1]):
            dame[ff[0]] += 1
            dame[ff[1]] += 1



    for i in range(n):
        print(str(uf.size(i)-dame[i]-1 ), end = " ")
    print("")

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


if __name__=='__main__':
    main()
