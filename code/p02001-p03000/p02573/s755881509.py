import sys
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

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    uf = UnionFind(n)
    for _ in range(m):
        a, b = map(lambda x: int(x) - 1, input().split())
        uf.union(a, b)
    ans = max(-uf.parents[uf.find(x)] for x in uf.roots())
    print(ans)


if __name__ == '__main__':
    main()

