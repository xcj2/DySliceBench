import sys

readline = sys.stdin.readline
readall = sys.stdin.read
ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))
prn = lambda x: print(*x, sep='\n')

class BIT:
    '''
    0-indexed
    '''
    def __init__(self, N):
        self.size = N
        self.tree = [0] * (N + 1)
        self.depth = N.bit_length()

    def _bitsum(self, i):
        ret = 0
        while i:
            ret += self.tree[i]
            i ^= i & -i
        return ret

    def bitsum(self, l, r=None): # [l, r)
        if r is None:
            return self._bitsum(l)
        else:
            return self._bitsum(r) - self._bitsum(l)

    def bitadd(self, i, x):
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
        return

    def lower_bound(self, x):
        sum_ = 0
        pos = 0
        v = 1 << self.depth
        for i in range(self.depth, -1, -1):
            k = pos + v
            if k <= self.size and sum_ + self.tree[k] < x:
                sum_ += self.tree[k]
                pos += v
            v >>= 1
        return pos + 1, sum_


def solve():
    n, q = nm()
    c = nl()
    m = 500010
    m2 = m * m
    g = [0]*q
    for i in range(q):
        l, r = nm()
        g[i] = ((r-1) << 40) + ((l-1) << 20) + i
    mask = (1 << 20) - 1
    g.sort()
    ans = [0] * q
    b = BIT(m)
    last = [n + 5]*(n+1)
    cr = -1
    for r in g:
        i = r & mask
        r >>= 20
        l = r & mask
        r >>= 20
        while cr < r:
            cr += 1
            b.bitadd(last[c[cr]], -1)
            last[c[cr]] = cr
            b.bitadd(cr, 1)
        ans[i] = b.bitsum(l, r+1)
    prn(ans)
    return

solve()
