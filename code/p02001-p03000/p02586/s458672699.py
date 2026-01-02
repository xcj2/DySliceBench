R, C, K, *RCV = [int(_) for _ in open(0).read().split()]
RCV = sorted([(r, -c, v) for r, c, v in zip(RCV[::3], RCV[1::3], RCV[2::3])])


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

    def operate_right(self, p, v):  # apply operator from the right side
        f, n, dat = self.f, self.n, self.dat
        p += n
        dat[p] = f(dat[p], v)
        while p > 1:
            p >>= 1
            dat[p] = f(dat[p << 1], dat[p << 1 | 1])

    def operate_left(self, p, v):  # apply operator from the left side
        f, n, dat = self.f, self.n, self.dat
        p += n
        dat[p] = f(v, dat[p])
        while p > 1:
            p >>= 1
            dat[p] = f(dat[p << 1], dat[p << 1 | 1])

    def query(self, l, r):  # result on interval [l, r) (0-indexed)
        f, ti, n, dat = self.f, self.ti, self.n, self.dat
        vl = vr = ti
        l += n
        r += n
        while l < r:
            if l & 1:
                vl = f(vl, dat[l])
                l += 1
            if r & 1:
                r -= 1
                vr = f(dat[r], vr)
            l >>= 1
            r >>= 1
        return f(vl, vr)


dp1 = SegmentTree([0] * (C + 1), max, -1)
dp2 = SegmentTree([0] * (C + 1), max, -1)
dp3 = SegmentTree([0] * (C + 1), max, -1)

rnow = 0
rcv = {}
for r, c, v in RCV:
    if rnow != r:
        rnow = r
        rcv[r] = []
    rcv[r] += [(-c, v)]
for r in sorted(rcv.keys()):
    cv = rcv[r]
    for c, v in cv:
        dp1.update(c, dp3.query(0, c + 1) + v)
    for c, v in cv:
        dp2.update(c, max(dp1.query(c, c + 1), dp1.query(0, c) + v))
    for c, v in cv:
        dp3.update(c, max(dp2.query(c, c + 1), dp2.query(0, c) + v))
ans = dp3.query(0, C + 1)
print(ans)
