import sys
input = sys.stdin.buffer.readline

from collections import defaultdict

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

def main():

    n, q = map(int, input().split())
    C = list(map(int, input().split()))
    LI = [[] for _ in range(n)]
    for i in range(q):
        l, r = map(int, input().split())
        l, r = l-1, r-1
        LI[r].append((l, i))

    #LR.sort(key=lambda x: x[1])

    bit = RangeAddBIT(n)
    preidx = defaultdict(lambda: -1)
    ans = [-1]*q
    for r in range(n):
        p = preidx[C[r]]
        bit.add(p+1, r+1, 1)
        preidx[C[r]] = r
        for l, i in LI[r]:
            ans[i] = bit.sum(l, l+1)
    print(*ans, sep='\n')

if __name__ == '__main__':
    main()
