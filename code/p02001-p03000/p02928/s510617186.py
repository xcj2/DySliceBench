N, K = [int(_) for _ in input().split()]
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
        self.add(p, self.fi(v, self.array[p]))

    def add(self, p, dv):
        """
        add value at position p (0-indexed)
        """
        fi, dat, f, size, array = self.fi, self.dat, self.f, self.size, self.array
        array[p] = f(array[p], dv)
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


f = lambda x, y: x + y
fi = lambda z, x: z - x
e = 0
BIT = BinaryIndexedTree([0] * 2001, f=f, fi=fi, e=e, size=2001)
ans1 = N * (N + 1) // 2
for a in A:
    BIT.add(a, 1)
    ans1 -= BIT._query(a + 1)

BIT = BinaryIndexedTree([0] * 2001, f=f, fi=fi, e=e, size=2001)
ans2 = 2 * N * (2 * N + 1) // 2
for a in A:
    BIT.add(a, 1)
    ans2 -= BIT._query(a + 1)
for a in A:
    BIT.add(a, 1)
    ans2 -= BIT._query(a + 1)

BIT = BinaryIndexedTree([0] * 2001, f=f, fi=fi, e=e, size=2001)
ans3 = 3 * N * (3 * N + 1) // 2
for a in A:
    BIT.add(a, 1)
    ans3 -= BIT._query(a + 1)
for a in A:
    BIT.add(a, 1)
    ans3 -= BIT._query(a + 1)
for a in A:
    BIT.add(a, 1)
    ans3 -= BIT._query(a + 1)

x = ans1
y = ans2
z = ans3
mod = 10**9 + 7
K -= 1
print(((
    (K - 2) * (K - 1) * x - 2 * K * (K - 2) * y + (K - 1) * K * z) // 2) % mod)
