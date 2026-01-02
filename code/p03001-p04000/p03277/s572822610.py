import itertools
N = int(input())
A = [int(_) for _ in input().split()]


class BinaryIndexedTree:
    """
        Parameters
        ----------
        array : list
            to construct BIT from
        f : func
            binary operation of the abelian group
        fi : func
            inverse mapping of f
            i.e. f(a, b) == c <-> fi(c, a) == b
        e : 
            identity element of the abelian group
        size : int
            limit for array size
    """

    def __init__(self, array, f, fi, e, size):
        self.f = f
        self.fi = fi
        self.e = e
        self.size = size
        self.n = len(array)
        self.dat = [e] * (size + 1)
        self.array = [e] * size
        self.build(array)

    def build(self, array_):
        for i, v in enumerate(array_):
            self.modify(i, v)

    def modify(self, p, v):
        """
        set value at position p (0-indexed)
        """
        fi, dat, f, size, array = self.fi, self.dat, self.f, self.size, self.array
        dv = fi(v, array[p])
        array[p] = v
        p += 1
        while p <= size:
            dat[p] = f(dat[p], dv)
            p += p & -p

    def query(self, l, r):
        """
        result on interval [l, r) (0-indexed)
        """
        return self.fi(self._query(r), self._query(l))

    def _query(self, p):
        dat, f, res = self.dat, self.f, self.e
        while p:
            res = f(res, dat[p])
            p -= p & -p
        return res


e = 0
size = 2 * N + 2
f = lambda a, b: a + b
fi = lambda c, a: c - a
offset = N


def check(x):
    cumsum = list(itertools.accumulate([0] + [1 if a <= x else -1 for a in A]))
    # sum([l:r)) = cumsum[r] - cumsum[l] >= 0
    # ⇔ cumsum[l] <= cumsum[r]
    BIT = BinaryIndexedTree([e] * size, f=f, fi=fi, e=e, size=size)
    count = 0
    for c in cumsum:
        c += offset
        count += BIT.query(0, c + 1)
        BIT.modify(c + 1, BIT.query(c + 1, c + 2) + 1)
    return 2 * count > N * (N + 1) // 2


A_sorted = [0] + sorted(set(A)) + [10**10]
lb = 0
rb = len(A_sorted) - 1
# check(x) == Trueとなる最小のx
while rb - lb > 1:
    mid = (rb + lb) // 2
    if check(A_sorted[mid]):
        rb = mid
    else:
        lb = mid
print(A_sorted[rb])
