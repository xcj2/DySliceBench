ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

v,e = mi()

path = []

for i in range(e):
    a = li()
    path.append([a[2], a[0], a[1]])

path.sort()

class UnionFind:
    def __init__(self,n):
        self.n = n
        self.d = [-1] * n

    def find(self, x):
        if(self.d[x] < 0):
            return x
        self.d[x] = self.find(self.d[x])
        return self.d[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if(x == y):
            return False
        if(self.d[x] > self.d[y]):
            x, y = y, x
        self.d[x] += self.d[y]
        self.d[y] = x
        return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self,x):
        return -self.d[self.find(x)]

uf = UnionFind(v)

ans = 0
for i in path:
    w = i[0]
    s = i[1]
    t = i[2]
    if uf.same(s,t):
        pass
    else:
        uf.union(s,t)
        ans += w


print(ans)
