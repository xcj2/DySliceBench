n, k = map(int, input().split())
mod = 998244353
LR = []
for i in range(k):
    l, r = map(int, input().split())
    LR.append((l, r))

class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0]*(self.n+1) # 1-indexed

    def init(self, init_val):
        for i, v in enumerate(init_val):
            self.add(i, v)

    def add(self, i, x):
        # i: 0-indexed
        i += 1 # to 1-indexed
        while i <= self.n:
            self.bit[i] += x
            i += (i & -i)

    def sum(self, i, j):
        # return sum of [i, j)
        # i, j: 0-indexed
        return self._sum(j) - self._sum(i)

    def _sum(self, i):
        # return sum of [0, i)
        # i: 0-indexed
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i & (-i)
        return res

class RangeAddBIT:
    def __init__(self, n):
        self.n = n
        self.bit1 = BIT(n)
        self.bit2 = BIT(n)

    def init(self, init_val):
        self.bit2.init(init_val)

    def add(self, l, r, x):
        # add x to [l, r)
        # l, r: 0-indexed
        self.bit1.add(l, x)
        self.bit1.add(r, -x)
        self.bit2.add(l, -x*l)
        self.bit2.add(r, x*r)

    def sum(self, l, r):
        # return sum of [l, r)
        # l, r: 0-indexed
        return self._sum(r) - self._sum(l)

    def _sum(self, i):
        # return sum of [0, i)
        # i: 0-indexed
        return self.bit1._sum(i)*i + self.bit2._sum(i)

bit = RangeAddBIT(n+10)
bit.add(1, 2, 1)
for i in range(1, n):
    t = bit.sum(i, i+1)
    t %= mod
    #print(t)
    for j in range(k):
        l, r = LR[j]
        bit.add(i+l, i+r+1, t)
print(bit.sum(n, n+1)%mod)
