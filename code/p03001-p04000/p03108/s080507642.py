
n, m = list(map(int, input().split()))

br = [list(map(int, input().split())) for _ in range(m)]

ans = []

def nc2(n):
    if n<2:
        return 0
    return n * (n-1) // 2


class UnionFind:

    def __init__(self, size):
        self.table = [-1 for _ in range(size+1)]
        self.size = [1 for _ in range(size+1)]

    def find(self, x):
        while self.table[x] >= 0:
            x = self.table[x]
        return x

    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            if self.table[s1] != self.table[s2]:
                if self.table[s1] < self.table[s2]:
                    self.table[s2] = s1
                    self.size[s1] += self.size[s2]
                    self.size[s2] = 0
                else:
                    self.table[s1] = s2
                    self.size[s2] += self.size[s1]
                    self.size[s1] = 0
            else:
                self.table[s1] += -1
                self.table[s2] = s1
                self.size[s1] += self.size[s2]
                self.size[s2] = 0

    def get_size(self, x):
        s1 = self.find(x)
        return self.size[s1]

    def check_same(self, x, y):
        return self.find(x) == self.find(y)

res = []
r = nc2(n)

uf = UnionFind(n)

for a, b in reversed(br):

    res.append(r)

    if not uf.check_same(a,b):
        r -= uf.get_size(a)*uf.get_size(b)

    uf.union(a,b)

for i in reversed(res):
    print(i)