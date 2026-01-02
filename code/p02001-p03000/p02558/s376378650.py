import sys
input = sys.stdin.readline

class DSU:
    __slots__ = ["_n", "parent_or_size"]
    def __init__(self, n):
        self._n = n
        self.parent_or_size = [-1] * n

    def merge(self, a, b):
        x, y = self.leader(a), self.leader(b)
        if x == y:
            return x
        if self.parent_or_size[x] > self.parent_or_size[y]:
            x, y = y, x
        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x
        return x

    def same(self, a, b):
        return self.leader(a) == self.leader(b)

    def leader(self, a):
        while self.parent_or_size[a] >= 0:
            a = self.parent_or_size[a]
        return a

def main():
    n, q = map(int, input().split())
    dsu = DSU(n)
    for _ in range(q):
        t, u, v = map(int, input().split())
        if t == 0:
            dsu.merge(u, v)
        else:
            print(1 if dsu.same(u, v) else 0)

main()