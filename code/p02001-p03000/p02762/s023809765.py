import sys


class UnionFind():
    def __init__(self, n):
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
            return False
        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x
        return True

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)


readline = sys.stdin.readline
n, m, k = map(int, readline().split())
ab = tuple(tuple(map(int, readline().split())) for i in range(m))
cd = (map(int, readline().split()) for i in range(k))

friend_group = UnionFind(n)
for a, b in ab:
    friend_group.union(a-1, b-1)

ans = [friend_group.size(i) - 1 for i in range(n)]
for a, b in ab:
    ans[a-1] -= 1
    ans[b-1] -= 1
for c, d in cd:
    if friend_group.same(c-1, d-1):
        ans[c-1] -= 1
        ans[d-1] -= 1

print(*ans)
