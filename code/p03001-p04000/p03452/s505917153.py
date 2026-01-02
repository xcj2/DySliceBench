import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline


class WeightedUnionFind:
    def __init__(self, N):
        self.par = [i for i in range(N)]
        self.rank = [0] * N
        self.weight = [0] * N  # 親までの距離

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            r = self.find(self.par[x])
            self.weight[x] += self.weight[self.par[x]]
            self.par[x] = r
            return r

    def union(self, x, y, w):
        rx = self.find(x)
        ry = self.find(y)
        if self.rank[rx] < self.rank[ry]:
            self.par[rx] = ry
            self.weight[rx] = w - self.weight[x] + self.weight[y]
        else:
            self.par[ry] = rx
            self.weight[ry] = -w - self.weight[y] + self.weight[x]
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def diff_w(self, x, y):
        return self.weight[x] - self.weight[y]


def main():
    N, M = map(int, readline().split())
    m = map(int, read().split())
    LRD = list(zip(m, m, m))

    D = WeightedUnionFind(N)

    for l, r, d in LRD:
        l -= 1
        r -= 1
        D.union(l, r, d)

    for i in range(N):
        D.find(i)

    for l, r, d in LRD:
        l -= 1
        r -= 1
        if d != D.diff_w(l, r):
            print('No')
            sys.exit()
    
    print('Yes')


main()
