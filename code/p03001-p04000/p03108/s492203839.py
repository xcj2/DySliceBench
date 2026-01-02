import sys

input = sys.stdin.readline

class uf_tree:
    def __init__(self, n):
        self._size = n
        self.sizes = [1] * n
        self.par = list(range(n))

    def find(self, x):
        if x == self.par[x]:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def unite(self, x, y):
        self._size -= 1
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.sizes[x] < self.sizes[y]:
            x, y = y, x
        self.par[y] = x
        self.sizes[x] += self.sizes[y]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return self.sizes[self.find(x)]


def com(x):
    return x*(x-1)//2

n, m = map(int, input().split())
AB = [ list(map(int, input().split())) for _ in range(m) ]

ans = []
benri = 0

uf = uf_tree(n+1)

for a, b in AB[::-1]:
    ans += [ com(n) - benri ]    
    if uf.same(a, b):
        continue

    a_benri = com(uf.size(a) )
    b_benri = com(uf.size(b) )

    uf.unite(a, b)
    sum_benri = com( uf.size(a) )
    benri += sum_benri - a_benri - b_benri

print (*ans[::-1], sep="\n")

