import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

class RangeMinimumQuery:
    def __init__(self, n, F=min, e=float("inf"), fill=None):
        self.n0 = 2**(n-1).bit_length()
        self.F = F
        self.e = e
        if fill is None:
            fill = e
        self.data = [fill]*(2*self.n0)

    def construct(self, a):
        for i, x in enumerate(a):
            self.data[i+self.n0-1] = x
        for i in range(self.n0-2, -1, -1):
            self.data[i] = self.F(self.data[2*i+1], self.data[2*i+2])

    def query(self, l,r):
        l += self.n0
        r += self.n0
        res = self.e
        while l < r:
            if r&1:
                r -= 1
                res = self.F(res, self.data[r-1])
            if l&1:
                res = self.F(res, self.data[l-1])
                l += 1
            l >>=1
            r >>=1
        return res

    def update(self, i, x):
        i += self.n0-1
        self.data[i] = x
        while i:
            i = ~-i//2
            self.data[i] = self.F(self.data[2*i+1], self.data[2*i+2])


from bisect import bisect_left

mod = 998244353

n = int(input())
xd = [list(map(int, input().split())) for i in range(n)]
xd.sort()
xs = [i for i,j in xd]

RMQ = RangeMinimumQuery(n, max,0,0)
RMQ.construct(list(range(n)))

for i in reversed(range(n)):
    r = sum(xd[i])
    j = bisect_left(xs, r)
    k = RMQ.query(i, j)
    RMQ.update(i, k)

DP = [0]*(n+1)
DP[-1] = 1
for i in reversed(range(n)):
    j = RMQ.query(i, i+1)
    DP[i] = DP[i+1]+DP[j+1]
    DP[i] %= mod
print(DP[0])
