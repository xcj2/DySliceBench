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


def comb(n):
    return (n * (n - 1)) // 2


n, m = list(map(int, input().split()))
ABs = [list(map(int, input().split())) for _ in range(m)]

results = []
fuben = comb(n)
results.append(fuben)

uf = UnionFind(n)

for i in range(m)[::-1]:
    a, b = ABs[i]
    a -= 1
    b -= 1
    if uf.same(a, b):
        results.append(fuben)
    else:
        tmp = comb(uf.size(a)) + comb(uf.size(b))
        uf.union(a, b)
        fuben = fuben + tmp - comb(uf.size(a))
        results.append(fuben)

for result in results[-2::-1]:
    print(result)
