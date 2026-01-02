import sys
sys.setrecursionlimit(100000)
import collections

class UnionFind:

    def __init__(self, N):
        self.raw = [i for i in range(N)]

    def root(self, i):
        if self.raw[i] == i:
            return i
        self.raw[i] = self.root(self.raw[i])
        return self.raw[i]

    def unite(self, a, b):
        a_root = self.root(a)
        b_root = self.root(b)
        self.raw[a_root] = b_root

    def is_same(self, a, b):
        return self.root(a) == self.root(b)


def solve(N, M, K, AB, CD):
    uf = UnionFind(N)
    minus_count = [0 for _ in range(N)]
    for a, b in AB:
        uf.unite(a - 1, b - 1)
        minus_count[a - 1] += 1
        minus_count[b - 1] += 1
    for c, d in CD:
        if uf.is_same(c - 1, d - 1):
            minus_count[c - 1] += 1
            minus_count[d - 1] += 1
    counter = collections.Counter()
    roots = [uf.root(i) for i in range(N)]
    counter.update(roots)

    ans = []
    for i in range(N):
        ans.append(str(counter[uf.root(i)] - minus_count[i] - 1))
    return " ".join(ans)

if __name__ == "__main__":
    N, M, K = tuple(map(int, input().split(" ")))
    AB = []
    for _ in range(M):
        AB.append(tuple(map(int, input().split(" "))))
    CD = []
    for _ in range(K):
        CD.append(tuple(map(int, input().split(" "))))
    print(solve(N, M, K, AB, CD))
