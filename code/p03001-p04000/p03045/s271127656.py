import sys
input = sys.stdin.readline


class UnionFindTree:
    def __init__(self, n: int):
        self.n = n
        self.root = [-1] * n
        self.rank = [0] * n
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
    def treeCount(self) -> int:
        cou = 0
        for i in self.root:
            if i < 0:
                cou += 1
        return cou


def main():
    N, M = map(int, input().split())
    UFT = UnionFindTree(N)
    for _ in range(M):
        u, v, __ = map(int, input().split())
        UFT.unite(u-1, v-1)
    ans = UFT.treeCount()
    print(ans)


if __name__ == '__main__': main()