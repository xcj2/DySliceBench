# ユニオンファインド
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

def cmb(n, r):
    if (r < 0 or r > n):
        return 0
    r=min(r,n-r)

    return g1[n] * g2[r] * g2[n - r] % mod

def comb(n):
    x=1
    y=1
    for i in range(2):
        x*=(n-i)
        y*=(i+1)
    return x//y


n,m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(m)]
b = [[] for i in range(n)]
uf = UnionFind(n)

ans=[]
x=comb(n)
for i in range(m):
    ans.append(x)
    if uf.same(a[m-i-1][0]-1,a[m-i-1][1]-1):
        uf.union(a[m-i-1][0]-1,a[m-i-1][1]-1)
    else:
        x-=uf.size(a[m-i-1][0]-1)*uf.size(a[m-i-1][1]-1)
        uf.union(a[m-i-1][0]-1,a[m-i-1][1]-1)
for i in range(m):
    print(ans[-1-i])