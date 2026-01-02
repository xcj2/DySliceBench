import sys
from bisect import bisect_left, bisect_right
input = lambda: sys.stdin.readline()
MOD = 998244353

class SegmentTree:
    def __init__(self, n, func=lambda x, y: min(x, y), ide=float("inf")):
        self.n = 2 ** (n-1).bit_length()
        self.data = [ide] * (self.n*2)
        self.func, self.ide = func, ide
    
    def build(self, data):
        for i, x in enumerate(data):
            self.data[self.n+i] = x
        for i in range(self.n-1, 0, -1):
            self.data[i] = self.func(self.data[i*2], self.data[i*2+1])

    def update(self, i, x):
        i += self.n
        self.data[i] = x
        while i > 1:
            i >>= 1
            self.data[i] = self.func(self.data[i*2], self.data[i*2+1])

    def query(self, l, r):
        l += self.n; r += self.n 
        res = self.ide
        while l < r:
            if l & 1:
                res = self.func(res, self.data[l])
                l += 1
            if r & 1:
                res = self.func(res, self.data[r-1])
            l >>= 1; r >>= 1
        return res
    
    def get(self, i):
        return self.data[self.n + i]

n = int(input())
xd = [tuple(map(int, input().split())) for _ in range(n)]
xd.sort()
x, d = zip(*xd)

s = SegmentTree(n, lambda x, y: max(x, y), -float("inf"))
for i in range(n)[::-1]:
    r = bisect_left(x, x[i]+d[i])
    s.update(i, max(r-1, s.query(i, r)))

dp1, dp2 = [0] * n, [0] * n
dp1[-1], dp2[-1] = 1, 1

for i in range(n-1)[::-1]:
    dp1[i] = dp1[i+1] + dp2[i+1] % MOD
    dp2[i] = dp1[s.get(i)]

print((dp1[0] + dp2[0]) % MOD)
