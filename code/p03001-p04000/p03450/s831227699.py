from sys import exit, stdin

class WeightedUnionFind:

    def __init__(self, n=1, sum_unity=0):

        self.par = [i for i in range(n)]

        self.rank = [0]*n

        self.diff_weight = [sum_unity]*n

    

    def find_root(self, x):

        if self.par[x] == x:

            return x

        else:

            y = self.find_root(self.par[x])

            self.diff_weight[x] += self.diff_weight[self.par[x]]

            self.par[x] = y

            return y

    def merge(self, x, y, w):

        rx, ry = self.find_root(x), self.find_root(y)

        if self.rank[rx] < self.rank[ry]:

            self.par[rx] = ry

            self.diff_weight[rx] = w - self.diff_weight[x] + self.diff_weight[y]

        else:

            self.par[ry] = rx

            self.diff_weight[ry] = -w - self.diff_weight[y] + self.diff_weight[x]

            if self.rank[rx] == self.rank[ry]:

                self.rank[rx] += 1

    def issame(self, x, y):

        return self.find_root(x) == self.find_root(y)

    def diff(self, x, y):

        return self.diff_weight[x] -  self.diff_weight[y]

N, M = [int(_) for _ in stdin.readline().rstrip().split()]

wuf = WeightedUnionFind(N)

for i in range(M):

    l, r, d = [int(_) for _ in stdin.readline().rstrip().split()]

    l -= 1

    r -= 1

    if wuf.issame(l, r):

        diff = wuf.diff(l, r)

        if diff != d:

            print("No")

            exit()

    else:

        wuf.merge(l, r, d)

print("Yes")

