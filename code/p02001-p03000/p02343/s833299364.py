import sys
input = sys.stdin.readline

class UnionFindTree:
    def __init__(self, n: int):
        self.n = n
        self.root = [-1] * (n+1)
        self.rank = [0] * (n+1)
    def findRoot(self, x: int) -> int:
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.findRoot(self.root[x])
            return self.root[x]
    def unite(self, x: int, y: int):
        x = self.findRoot(x)
        y = self.findRoot(y)
        if x == y:
            return
        elif self.rank[x] > self.rank[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1
    def same(self, x: int, y: int) -> bool:
        if self.findRoot(x) == self.findRoot(y):
            return True
        else:
            return False
    def count(self, x: int) -> int:
        return -self.root[self.findRoot(x)]


def main():
    n, q = map(int, input().split())
    UFT = UnionFindTree(n-1)
    for _ in range(q):
        com, x, y = map(int, input().split())
        if com == 0:
            UFT.unite(x, y)
        else:
            if UFT.same(x, y):
                print(1)
            else:
                print(0)


if __name__ == '__main__': main()
