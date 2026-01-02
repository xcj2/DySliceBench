N, M, Q = [int(_) for _ in input().split()]
Query = []
for _ in range(M):
    Query += [[int(_) for _ in input().split()] + [0, _]]
for _ in range(Q):
    p, q = [int(_) for _ in input().split()]
    Query += [[p, q + 1, 1, _]]
Query.sort(key=lambda xs: 2 * xs[1] - xs[2])
ans = [0] * Q


class SegmentTree():
    def __init__(self, array, m, e, size):
        """
        Parameters
        ----------
        array : list
            to construct segment tree from
        m : func
            binary operation of the monoid
        e : 
            identity element of the monoid
        size : int
            limit for array size
        """
        self.m = m
        self.e = e
        self.size = size
        self.n = n = len(array)
        self.dat = dat = [e] * n + array + [e] * (2 * size - 2 * n)
        self.build()

    def build(self):
        dat, n, m = self.dat, self.n, self.m
        for i in range(n - 1, 0, -1):
            dat[i] = m(dat[i << 1], dat[i << 1 | 1])

    def modify(self, p, v):
        """
        set value at position p (0-indexed)
        """
        m, n, dat = self.m, self.n, self.dat
        p += n
        dat[p] = v
        while p > 1:
            dat[p >> 1] = m(dat[p], dat[p ^ 1])
            p >>= 1

    def query(self, l, r):
        """
        result on interval [l, r) (0-indexed)
        """
        m, e, n, dat = self.m, self.e, self.n, self.dat
        res = e
        l += n
        r += n
        while l < r:
            if l & 1:
                res = m(res, dat[l])
                l += 1
            if r & 1:
                r -= 1
                res = m(res, dat[r])
            l >>= 1
            r >>= 1
        return res


e = 0
size = N + 2
ST = SegmentTree([0] * (N + 2), m=lambda x, y: x + y, e=e, size=size)
for l, r, t, i in Query:
    if t:
        ans[i] = ST.query(l, r)
    else:
        ST.modify(l, ST.query(l, l + 1) + 1)
print(*ans, sep='\n')
