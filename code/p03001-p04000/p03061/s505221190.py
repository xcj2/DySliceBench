N = int(input())
A = [int(_) for _ in input().split()]


class SegmentTree():
    def __init__(self, array, f, e, size):
        """
        Parameters
        ----------
        array : list
            to construct segment tree from
        f : func
            binary operation of the monoid
        e : 
            identity element of the monoid
        size : int
            limit for array size
        """
        self.f = f
        self.e = e
        self.size = size
        self.n = n = len(array)
        self.dat = dat = [e] * n + array + [e] * (2 * size - 2 * n)
        for i in range(n - 1, 0, -1):  # build
            dat[i] = f(dat[i << 1], dat[i << 1 | 1])

    def modify(self, p, v):  # set value at position p (0-indexed)
        f, n, dat = self.f, self.n, self.dat
        p += n
        dat[p] = v
        while p > 1:
            dat[p >> 1] = f(dat[p], dat[p ^ 1])
            p >>= 1

    def query(self, l, r):  # result on interval [l, r) (0-indexed)
        f, e, n, dat = self.f, self.e, self.n, self.dat
        res = e
        l += n
        r += n
        while l < r:
            if l & 1:
                res = f(res, dat[l])
                l += 1
            if r & 1:
                r -= 1
                res = f(res, dat[r])
            l >>= 1
            r >>= 1
        return res


gcd = lambda x, y: gcd(y, x) if x < y else gcd(y, x % y) if y else x
e = 0
size = N
ST = SegmentTree(A, f=gcd, e=e, size=size)
ans = 1
for i, a in enumerate(A):
    ST.modify(i, 0)
    ans = max(ans, ST.query(0, N))
    ST.modify(i, a)
print(ans)
