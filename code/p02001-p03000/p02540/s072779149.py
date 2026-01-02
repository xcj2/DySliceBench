N, *XY = [int(_) for _ in open(0).read().split()]
X = XY[::2]
Y = XY[1::2]
y_k = {}
k_y = {}
for y, k in zip(Y, range(N)):
    y_k[y] = k
    k_y[k] = y


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1] * (n + 1)
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return 0
        elif self.rank[x] > self.rank[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.root[self.find(x)]


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


XY = sorted(zip(X, Y))
uf = UnionFind(N + 1)
stmin = SegmentTree([10**10] * (N + 1), min, 10**10)
stmax = SegmentTree([-10**10] * (N + 1), max, -10**10)
for x, y in XY:
    ymin = stmin.query(0, x)
    ymax = stmax.query(0, y)
    stmin.update(x, y)
    stmax.update(y, y)
    for y2 in (ymin, ymax):
        if abs(y2) != 10**10 and y > y2:
            uf.unite(y, y2)
stmin = SegmentTree([10**10] * (N + 1), min, 10**10)
stmax = SegmentTree([-10**10] * (N + 1), max, -10**10)
for x, y in XY[::-1]:
    ymin = stmin.query(y + 1, N + 1)
    ymax = stmax.query(x + 1, N + 1)
    stmax.update(x, y)
    stmin.update(y, y)
    for y2 in (ymin, ymax):
        if abs(y2) != 10**10 and y < y2:
            uf.unite(y, y2)
print('\n'.join(str(uf.size(k_y[k])) for k in range(N)))
