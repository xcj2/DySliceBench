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

def main():
    n, frnd, blck = map(int, input().split())
    blst = [set() for i in range(n)]
    flst = [set() for i in range(n)]
    uf = UnionFind(n)
    for _ in range(frnd):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        flst[a].add(b)
        flst[b].add(a)
        uf.union(a, b)
    for _ in range(blck):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        blst[c].add(d)
        blst[d].add(c)
    for i in range(n):
        ans = uf.size(i) - len(flst[i]) - 1
        for v in blst[i]:
            if uf.same(i, v):
                ans -= 1
        print(ans, end="")
        if i < n:
            print(" ", end="")

if __name__ == "__main__":
    main()