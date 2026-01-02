N, *LR = [int(_) for _ in open(0).read().split()]
LR = sorted(set([(l, r + 1) for l, r in zip(LR[::2], LR[1::2])]))


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


minr = min(r for l, r in LR)
lminr = max(l for l, r in LR if r == minr)
maxl = max(l for l, r in LR)
rmaxl = min(r for l, r in LR if l == maxl)
LR2 = [lr for lr in LR if lr not in [(minr, lminr), (maxl, rmaxl)]]
LR = [(minr, lminr)] + LR2 + [(maxl, rmaxl)]
M = len(LR)
if M == 1:
    ans = 2 * (LR[0][1] - LR[0][0])
elif M == 2:
    ans = sum(r - l for l, r in LR)
else:
    #(lminr,minr)と(maxl,rmaxl)が同一または同じ回
    ans = max(0, minr - maxl) + max(r - l for l, r in LR2)
    #(lminr,minr)と(maxl,rmaxl)が違う回 [0,i)と[i,M)に分けて施行すればよい(i∈[1,M))
    st = SegmentTree([r for l, r in LR], min, 10**10)
    for i in range(1, M):
        v1 = max(0, minr - max(lminr, LR[i - 1][0]))
        v2 = max(0, st.query(i, M) - maxl)
        ans = max(ans, v1 + v2)
print(ans)
