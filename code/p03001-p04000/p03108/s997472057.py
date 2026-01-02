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
n,m = map(int, input().split())
uf = UnionFind(n)
b = [list(map(int, input().split())) for i in range(m)]
b.reverse()
def kumi(x):
    return x*(x-1)//2
c = kumi(n)
ans = [0 for i in range(m)]
nextans = c
for i,bri in enumerate(b):
    ans[m-1-i] = nextans
    if uf.same(bri[0]-1, bri[1]-1):
        continue
    else:
        a_num = uf.size(bri[0]-1)
        b_num = uf.size(bri[1]-1)
        a_num = kumi(a_num)
        b_num = kumi(b_num)
        uf.union(bri[0]-1, bri[1]-1)
        c_num = uf.size(bri[0]-1)
        c_num = kumi(c_num)
        nextans = nextans - (c_num - a_num - b_num)
for i in range(m):
    print(ans[i])