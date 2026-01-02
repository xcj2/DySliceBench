N = int(input())
A = [int(_) for _ in input().split()]


class SegmentTree():
    def __init__(self, array, m, e, size):
        self.m = m  # monoid
        self.e = e  # identity element
        self.size = size  # limit for array size
        self.n = n = len(array)  # array size
        self.dat = dat = [e] * n + array + [e] * (2 * size - 2 * n)
        for i in range(n - 1, 0, -1):  # build
            dat[i] = m(dat[i << 1], dat[i << 1 | 1])

    def modify(self, p, v):  # set value at position p (0-indexed)
        m, n, dat = self.m, self.n, self.dat
        p += n
        dat[p] = v
        while p > 1:
            dat[p >> 1] = m(dat[p], dat[p ^ 1])
            p >>= 1

    def query(self, l, r):  # result on interval [l, r) (0-indexed)
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


gcd = lambda x, y: gcd(y, x) if x < y else x if y == 0 else gcd(y, x % y)
e = 0
size = 10**6
ST = SegmentTree(A, m=gcd, e=e, size=size)

ans = 1
for i, a in enumerate(A):
    ST.modify(i, 0)
    ans = max(ans, ST.query(0, N))
    ST.modify(i, a)
print(ans)
