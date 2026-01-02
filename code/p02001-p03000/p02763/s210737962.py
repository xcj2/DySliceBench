import itertools, operator
N = int(input())
S = [ord(s) - 97 for s in input()]
Q = int(input())
Query = [input().split() for _ in range(Q)]
cntraw = [[0] * (N + 1) for _ in range(26)]
for i, v in enumerate(S):
    cntraw[v][i + 1] = 1


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


sts = [SegmentTree(cntraw[i], f=operator.add, ti=0) for i in range(26)]
for query in Query:
    if query[0] == '1':
        i, c = query[1:]
        i = int(i)
        for st in sts:
            st.update(i, 0)
        sts[ord(c) - 97].update(i, 1)
    else:
        l, r = [int(_) for _ in query[1:]]
        r += 1
        print(sum(st.query(l, r) > 0 for st in sts))
