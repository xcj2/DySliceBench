class SegmentTree():
    def __init__(self, array, f, ti):
        """
        Parameters
        ----------
        array : list
            to construct segment tree from
        f : func
            binary operation of the monoid
        ti : 
            identity element of the monoid
        """
        self.f = f
        self.ti = ti
        self.n = n = 2**(len(array).bit_length())
        self.dat = dat = [ti] * n + array + [ti] * (n - len(array))
        for i in range(n - 1, 0, -1):  # build
            dat[i] = f(dat[i << 1], dat[i << 1 | 1])

    def update(self, p, v):  # set value at position p (0-indexed)
        f, n, dat = self.f, self.n, self.dat
        p += n
        dat[p] = v
        while p > 1:
            p >>= 1
            dat[p] = f(dat[p << 1], dat[p << 1 | 1])

    def query(self, l, r):  # result on interval [l, r) (0-indexed)
        f, ti, n, dat = self.f, self.ti, self.n, self.dat
        res = ti
        l += n
        r += n
        while l < r:
            if l & 1:
                res = f(res, dat[l])
                l += 1
            if r & 1:
                r -= 1
                res = f(dat[r], res)
            l >>= 1
            r >>= 1
        return res


I = [int(_) for _ in open(0).read().split()]
N, M = I[:2]
L, R, C = I[2::3], I[3::3], I[4::3]
ti = float('inf')
ST = SegmentTree([0] * 2 + [ti] * (N - 1), min, ti)
for l, r, c in sorted(zip(L, R, C)):
    ST.update(r, min(ST.query(r, r + 1), ST.query(l, r) + c))
ans = ST.query(N, N + 1)
print(-1 if ans == ti else ans)
