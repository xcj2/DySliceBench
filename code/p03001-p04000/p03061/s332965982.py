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


def gcd(x, y):
    if x * y == 0:
        return x + y
    elif x > y:
        return gcd(y, x)
    else:
        return gcd(y % x, x)


N = int(input())
A = [int(_) for _ in input().split()]
ST = SegmentTree(array=A, f=gcd, ti=0)
ans = 0
for i in range(N):
    ans = max(ans, gcd(ST.query(0, i), ST.query(i + 1, N)))
print(ans)
