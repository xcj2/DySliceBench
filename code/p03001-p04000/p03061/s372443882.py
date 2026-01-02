import math
N = int(input())
A = [int(_) for _ in input().split()]


def gcd(x, y):
    if x < y:
        return gcd(y, x)
    elif y == 0:
        return x
    else:
        return gcd(y, x % y)


class SegmentTree():
    def m(self, v1, v2):  # ***monoid***
        return gcd(v1, v2)

    def __init__(self, array):
        m = self.m
        e = self.e = 0  # ***identity element***
        size = self.size = 10**5  # ***limit for array size***
        n = self.n = len(array)
        dat = self.dat = [e] * n + array + [e] * (2 * size - 2 * n)
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


ST = SegmentTree(A)
ans = 0
for i, a in enumerate(A):
    ST.modify(i, ST.e)
    ans = max(ans, ST.query(0, N))
    ST.modify(i, a)
print(ans)
