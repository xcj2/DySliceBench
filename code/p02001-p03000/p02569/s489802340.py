I = [int(_) for _ in open(0).read().split()]
N, Q = I[:2]
A = I[2:2 + N]
T = I[2 + N::3]
L = I[3 + N::3]
R = I[4 + N::3]


class LazySegmentTree():
    def __init__(self, array, f, g, h, ti, ei):
        """
        Parameters
        ----------
        array : list
            to construct segment tree from
        f : func
            binary operation of the monoid
            T x T -> T
            T is dat
        g : func
            binary operation of the monoid
            T x E -> T
            T is dat, E is laz
        h : func
            binary operation of the monoid
            E x E -> T
            E is laz
        ti : T
            identity element of T
        ei : E
            identity element of E
        """
        self.f = f
        self.g = g
        self.h = h
        self.ti = ti
        self.ei = ei
        self.height = height = len(array).bit_length()
        self.n = n = 2**height
        self.dat = dat = [ti] * n + array + [ti] * (n - len(array))
        self.laz = [ei] * (2 * n)
        for i in range(n - 1, 0, -1):  # build
            dat[i] = f(dat[i << 1], dat[i << 1 | 1])

    def reflect(self, k):
        dat = self.dat
        ei = self.ei
        laz = self.laz
        g = self.g
        return self.dat[k] if laz[k] is ei else g(dat[k], laz[k])

    def evaluate(self, k):
        laz = self.laz
        ei = self.ei
        reflect = self.reflect
        dat = self.dat
        h = self.h
        if laz[k] is ei:
            return
        laz[(k << 1) | 0] = h(laz[(k << 1) | 0], laz[k])
        laz[(k << 1) | 1] = h(laz[(k << 1) | 1], laz[k])
        dat[k] = reflect(k)
        laz[k] = ei

    def thrust(self, k):
        height = self.height
        evaluate = self.evaluate
        for i in range(height, 0, -1):
            evaluate(k >> i)

    def recalc(self, k):
        dat = self.dat
        reflect = self.reflect
        f = self.f
        while k:
            k >>= 1
            dat[k] = f(reflect((k << 1) | 0), reflect((k << 1) | 1))

    def update(self, a, b, x):  # set value at position [a, b) (0-indexed)
        thrust = self.thrust
        n = self.n
        h = self.h
        laz = self.laz
        recalc = self.recalc
        a += n
        b += n - 1
        l = a
        r = b + 1
        thrust(a)
        thrust(b)
        while l < r:
            if l & 1:
                laz[l] = h(laz[l], x)
                l += 1
            if r & 1:
                r -= 1
                laz[r] = h(laz[r], x)
            l >>= 1
            r >>= 1
        recalc(a)
        recalc(b)

    def set_val(self, a, x):
        n = self.n
        thrust = self.thrust
        dat = self.dat
        laz = self.laz
        recalc = self.recalc
        ei = self.ei
        a += n
        thrust(a)
        dat[a] = x
        laz[a] = ei
        recalc(a)

    def query(self, a, b):  # result on interval [a, b) (0-indexed)
        f = self.f
        ti = self.ti
        n = self.n
        thrust = self.thrust
        reflect = self.reflect
        a += n
        b += n - 1
        thrust(a)
        thrust(b)
        l = a
        r = b + 1
        vl = vr = ti
        while l < r:
            if l & 1:
                vl = f(vl, reflect(l))
                l += 1
            if r & 1:
                r -= 1
                vr = f(reflect(r), vr)
            l >>= 1
            r >>= 1
        return f(vl, vr)


#general linear functions
array = [(0, 0, 0)] + [(0, 1, 0) if a else (1, 0, 0) for a in A]
f = lambda a, b: (a[0] + b[0], a[1] + b[1], a[2] + b[2] + a[1] * b[0])


def g(a, b):
    if b == -1:
        x = a[1]
        y = a[0]
        z = (x + y) * (x + y - 1) // 2 - x * (x - 1) // 2 - y * (
            y - 1) // 2 - a[2]
        return (x, y, z)
    else:
        return a


h = lambda a, b: a * b
ti = (0, 0, 0)
ei = 1
# b[0] * (a[0] * x + a[1]) + b[1]
# = b[0] * a[0] * x + (b[0] * a[1] + b[1])

LST = LazySegmentTree(array=array, ti=ti, ei=ei, f=f, g=g, h=h)

for t, l, r in zip(T, L, R):
    r += 1
    if t == 1:
        LST.update(l, r, -1)
    else:
        print(LST.query(l, r)[2])
