import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7

\

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    # 親が同じか判別
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    # 根を繋ぎ直す
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    # 親が同じか判別
    def same(self, x, y):
        return self.find(x) == self.find(y)

    # 連結成分の大きさを返す
    def size(self, x):
        return -self.parents[self.find(x)]


def resolve():
    n, m = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(m)][::-1]
    uf = UnionFind(n)

    res = [(n * (n - 1)) // 2]
    for a, b in AB:
        if not uf.same(a - 1, b - 1):
            pre1 = uf.size(a - 1)
            pre2 = uf.size(b - 1)
            pre_score = (pre1 * (pre1 - 1)) // 2 + (pre2 * (pre2 - 1)) // 2

            uf.union(a - 1, b - 1)
            now = uf.size(a - 1)
            now_score = (now * (now - 1)) // 2

            res.append(res[-1] + pre_score - now_score)
        else:
            res.append(res[-1])

    for i in reversed(range(m)):
        print(res[i])


if __name__ == '__main__':
    resolve()
