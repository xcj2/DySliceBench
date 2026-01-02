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
    ans = [0] * M
    bridges = []
    for _ in range(M):
        A, B = map(int, input().split())
        bridges.append((A-1, B-1))
    ans[M-1] = N * (N-1) // 2
    for i in range(M-1, 0, -1):
        A = bridges[i][0]
        B = bridges[i][1]
        if UFT.same(A, B):
            ans[i-1] = ans[i]
        else:
            ans[i-1] = ans[i] - UFT.count(A) * UFT.count(B)
            UFT.unite(A, B)
    for i in ans:
        print(i)


if __name__ == '__main__': main()