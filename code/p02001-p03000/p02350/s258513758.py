import sys
write = sys.stdout.write


class LazySegmentTree():
    def __init__(self,
                 array,
                 ti,
                 ei,
                 f=lambda: None,
                 g=lambda: None,
                 h=lambda: None):
        """
        Parameters
        ----------
        array : list
            to construct segment tree from
        ti : T
            identity element of T
        ei : E
            identity element of E
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
        """
        self.f = f
        self.g = g
        self.h = h
        self.ti = ti
        self.ei = ei
        self.LV = LV = (len(array) - 1).bit_length()
        self.N0 = N0 = 2**LV
        self.data = data = [ti] * N0 + array + [ti] * (N0 - len(array))
        self.lazy = [ei] * (2 * N0)
        '''
        for i in range(N0 - 1, 0, -1):  # build
            data[i] = f(data[i << 1], data[i << 1 | 1])
        '''
        for i in range(N0 - 1, 0, -1):  # build
            data[i] = data[i << 1] if data[i << 1] < data[i << 1
                                                          | 1] else data[i << 1
                                                                         | 1]

    def gindex(self, l, r):
        LV = self.LV
        N0 = self.N0
        L = (l + N0) >> 1
        R = (r + N0) >> 1
        lc = 0 if l & 1 else (L & -L).bit_length()
        rc = 0 if r & 1 else (R & -R).bit_length()
        ret = []
        for i in range(LV):
            if rc <= i:
                ret += [R]
            if L < R and lc <= i:
                ret += [L]
            L >>= 1
            R >>= 1
        return ret

    def propagates(self, *ids):
        data = self.data
        lazy = self.lazy
        for i in reversed(ids):
            v = lazy[i - 1]
            if v is ei:
                continue
            '''
            data[2 * i - 1] = g(data[2 * i - 1], v)
            data[2 * i] = g(data[2 * i], v)
            lazy[2 * i - 1] = h(lazy[2 * i - 1], v)
            lazy[2 * i] = h(lazy[2 * i], v)
            '''
            data[2 * i - 1] = v
            data[2 * i] = v
            lazy[2 * i - 1] = v
            lazy[2 * i] = v

            lazy[i - 1] = ei

    def update(self, l, r, x):
        data = self.data
        lazy = self.lazy
        N0 = self.N0
        *ids, = self.gindex(l, r)
        self.propagates(*ids)
        L = N0 + l
        R = N0 + r
        while L < R:
            '''
            if R & 1:
                R -= 1
                lazy[R - 1] = h(lazy[R - 1], x)
                data[R - 1] = g(data[R - 1], x)
            if L & 1:
                lazy[L - 1] = h(lazy[L - 1], x)
                data[L - 1] = g(data[L - 1], x)
                L += 1
            '''
            if R & 1:
                R -= 1
                lazy[R - 1] = x
                data[R - 1] = x
            if L & 1:
                lazy[L - 1] = x
                data[L - 1] = x
                L += 1
            L >>= 1
            R >>= 1
        for i in ids:
            '''
            data[i - 1] = f(data[2 * i - 1], data[2 * i])
            '''
            data[i - 1] = data[
                2 * i - 1] if data[2 * i - 1] < data[2 * i] else data[2 * i]

    def query(self, l, r):
        data = self.data
        N0 = self.N0
        ti = self.ti
        self.propagates(*self.gindex(l, r))
        L = N0 + l
        R = N0 + r
        vl = vr = ti
        while L < R:
            '''
            if R & 1:
                R -= 1
                vr = f(data[R - 1], vr)
            if L & 1:
                vl = f(vl, data[L - 1])
                L += 1
            '''
            if R & 1:
                R -= 1
                vr = data[R - 1] if data[R - 1] < vr else vr
            if L & 1:
                vl = vl if vl < data[L - 1] else data[L - 1]
                L += 1
            L >>= 1
            R >>= 1
        '''
        return f(vl, vr)
        '''
        return vl if vl < vr else vr


I = sys.stdin.read()[:-1].split('\n')
N, Q = map(int, I[0].split())

ti = 2**31 - 1  #float('inf')
ei = None
#f = lambda tl, tr: tl if tl < tr else tr
#g = lambda t, e: t if e is ei else e
#h = lambda eo, en: eo if en is ei else en
LST = LazySegmentTree([ti] * N, ti, ei)
ans = []
for r in I[1:]:
    t, *cmd = map(int, r.split())
    if t:
        s, t = cmd
        ans.append(str(LST.query(s, t + 1)))
    else:
        s, t, x = cmd
        LST.update(s, t + 1, x)

write("\n".join(ans))
write("\n")

