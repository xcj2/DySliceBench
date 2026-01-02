# https://ikatakos.com/pot/programming_algorithm/data_structure/binary_indexed_tree

class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

class RangeUpdate:
    def __init__(self, n):
        self.p = Bit(n + 1)
        self.q = Bit(n + 1)

    def add(self, s, t, x):
        t += 1
        self.p.add(s, -x * s)
        self.p.add(t, x * t)
        self.q.add(s, x)
        self.q.add(t, -x)

    def sum(self, s, t):
        t += 1
        return (self.p.sum(t) + self.q.sum(t) * t - \
               self.p.sum(s) - self.q.sum(s) * s) % mod


mod = 998244353

N, K, *LR = map(int, open(0).read().split())

LR = list(zip(*[iter(LR)] * 2))

dp = RangeUpdate(N)
dp.add(1, 1, 1)
for i in range(1, N + 1):
    for l, r in LR:
        dp.add(i + l, i + r, dp.sum(i, i))

print(dp.sum(N, N))