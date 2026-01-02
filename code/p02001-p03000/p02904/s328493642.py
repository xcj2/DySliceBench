import sys
sys.setrecursionlimit(100000)


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


N, K = [int(_) for _ in input().split()]
P = [int(_) for _ in input().split()]

STmax = SegmentTree(array=P, f=max, ti=-float('inf'))
STmin = SegmentTree(array=P, f=min, ti=float('inf'))

size = N - K + 1
UF = list(range(size))
SIZE = [1] * size  # 0-indexed


def find(x):
    stack = [x]
    while True:
        y = stack[-1]
        if UF[y] != y:
            stack += [UF[y]]
        else:
            break
    for s in stack:
        UF[s] = y
    return y


def unite(x, y):
    if not is_same(x, y):
        X, Y = find(x), find(y)
        SX, SY = SIZE[X], SIZE[Y]
        if SX > SY:
            m = UF[X] = Y
        else:
            m = UF[Y] = X
        SIZE[m] = SX + SY
        SIZE[X + Y - m] = 0


def is_same(x, y):
    return find(x) == find(y)


def scan_uf():
    length = len(UF)
    for i in range(length):
        find(i)


for i in range(N - K):
    if P[i] == STmin.query(i, i + K) and P[i + K] == STmax.query(
            i + 1, i + K + 1):
        unite(i, i + 1)

inc = 0
incK = []
for i in range(N - 2, -1, -1):
    if P[i] <= P[i + 1]:
        inc += 1
        if inc >= K - 1:
            incK += [i]
    else:
        inc = 0
for i in incK:
    unite(incK[0], i)

scan_uf()
print(len(set(UF)))
