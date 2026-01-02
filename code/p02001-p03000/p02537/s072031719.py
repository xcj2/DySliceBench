N, K, *A = [int(_) for _ in open(0).read().split()]


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


st = SegmentTree([0] * 300001, max, 0)
for a in A:
    l = max(0, a - K)
    r = min(a + K, 300000)
    st.update(a, st.query(l, r + 1) + 1)
print(st.query(0, 300001))
