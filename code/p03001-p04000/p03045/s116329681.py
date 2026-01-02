from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)

    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # 併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def main(self):
        N, M = map(int, input().split())
        ufind = UnionFind(N)
        for _ in range(M):
            X, Y, Z = map(int, input().split())
            ufind.union(X-1, Y-1)
        print(len(set([ufind.find(i) for i in range(N)])))


if __name__ == '__main__':
    Solution().main()