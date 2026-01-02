import sys
sys.setrecursionlimit(100000)

class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n + 1)]

    def root(self, i):
        if self.parents[i] == i:
            return i
        else:
            self.parents[i] = self.root(self.parents[i])
            return self.parents[i]

    def unite(self, i, j):
        self.parents[self.root(self.parents[i])] = self.root(j)

    def is_unite(self, i, j):
        return self.root(i) == self.root(j)


from collections import Counter


def solve(N, M, ABs):
    uf = UnionFind(N)
    counter = Counter([i + 1 for i in range(N)])
    ans = []
    tans = N * (N - 1)
    for a, b in ABs[::-1]:
        ans.append(str(tans // 2))

        if not uf.is_unite(a, b):
            ar = uf.root(a)
            br = uf.root(b)

            tans -= counter[ar] * (N - counter[ar])
            tans -= counter[br] * (N - counter[br])
            counter[br] += counter[ar]
            tans += counter[br] * (N - counter[br])

            uf.unite(a, b)
    return "\n".join(ans[::-1])

if __name__ == "__main__":
    N, M = tuple(map(int, input().split(" ")))
    ABs = [tuple(map(int, input().split(" "))) for _ in range(M)]
    print(solve(N, M, ABs))
