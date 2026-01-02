import sys
import heapq

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


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

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def all_group_memberss(self):
        return [self.size(r) for r in self.roots()]

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


def main():
    N, M = [int(x) for x in input().split()]
    AB = [[int(x) for x in input().split()] for _ in range(M)]

    uf = UnionFind(N)

    for a, b in AB:
        uf.union(a - 1, b - 1)

    hq = []
    for k in uf.all_group_memberss():
        heapq.heappush(hq, k)

    ans = 0
    prev = 0
    while hq:
        c = heapq.heappop(hq)
        if prev != c:
            ans += (c - prev)
            prev = c

    print(ans)


if __name__ == '__main__':
    main()
