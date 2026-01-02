import sys
input = sys.stdin.readline
N,Q = map(int,input().split())
LRD = [tuple(map(int,input().split())) for i in range(Q)]
MOD = 998244353

class LazySegTree:
    def __init__(self, op, e, mapping, composition, _id, arr=[]):
        self.op = op
        self.e = e
        self.mapping = mapping
        self.composition = composition
        self.id = _id
        self.n = len(arr)
        self.log = self._ceil_pow2(self.n)
        self.size = 1 << self.log
        self.d = [e()] * (2*self.size)
        self.lz = [_id()] * self.size
        for i in range(self.n):
            self.d[self.size + i] = arr[i]
        for i in range(self.size-1, 0, -1):
            self._update(i)

    def _ceil_pow2(self, n):
        assert n >= 0
        x = 0
        while (1<<x) < n:
            x += 1
        return x

    def set(self, p, x):
        assert 0 <= p < self.n
        p += self.size
        for i in range(self.log, 0, -1):
            self._push(p >> i)
        self.d[p] = x
        for i in range(1, self.log+1):
            self._update(p >> i)

    def get(self, p):
        assert 0 <= p < self.n
        p += self.size
        for i in range(self.log, 0, -1):
            self._push(p >> i)
        return self.d[p]

    def prod(self, l, r):
        assert 0 <= l <= r <= self.n
        if l==r: return self.e()
        l += self.size
        r += self.size
        for i in range(self.log, 0, -1):
            if ((l >> i) << i) != l: self._push(l >> i)
            if ((r >> i) << i) != r: self._push(r >> i)
        sml = smr = self.e()
        while l < r:
            if l&1:
                sml = self.op(sml, self.d[l])
                l += 1
            if r&1:
                r -= 1
                smr = self.op(self.d[r], smr)
            l >>= 1
            r >>= 1
        return self.op(sml, smr)

    def all_prod(self):
        return self.d[1]

    def apply(self, p, f):
        assert 0 <= p < self.n
        p += self.size
        for i in range(self.log, 0, -1):
            self._push(p >> i)
        self.d[p] = self.mapping(f, self.d[p])
        for i in range(1, self.log+1):
            self._update(p >> i)

    def apply_lr(self, l, r, f):
        assert 0 <= l <= r <= self.n
        if l==r: return
        l += self.size
        r += self.size
        for i in range(self.log, 0, -1):
            if ((l >> i) << i) != l: self._push(l >> i)
            if ((r >> i) << i) != r: self._push((r-1) >> i)

        l2,r2 = l,r
        while l < r:
            if l&1:
                self._all_apply(l, f)
                l += 1
            if r&1:
                r -= 1
                self._all_apply(r, f)
            l >>= 1
            r >>= 1
        l,r = l2,r2

        for i in range(1, self.log+1):
            if ((l >> i) << i) != l: self._update(l >> i)
            if ((r >> i) << i) != r: self._update((r-1) >> i)

    def _update(self, k):
        self.d[k] = self.op(self.d[2*k], self.d[2*k+1])
    def _all_apply(self, k, f):
        self.d[k] = self.mapping(f, self.d[k])
        if k < self.size:
            self.lz[k] = self.composition(f, self.lz[k])
    def _push(self, k):
        self._all_apply(2*k, self.lz[k])
        self._all_apply(2*k+1, self.lz[k])
        self.lz[k] = self.id()

inv9 = pow(9,MOD-2,MOD)
def op(l,r):
    lx,lw = l
    rx,rw = r
    return ((lx*rw + rx)%MOD, (lw*rw)%MOD)
def e():
    return (0,1)
def mapping(l,r):
    if l==0: return r
    rx,rw = r
    return (((rw-1)*inv9*l)%MOD, rw)
def composition(l,r):
    return r if l==0 else l
def _id():
    return 0

segt = LazySegTree(op, e, mapping, composition, _id, [(1,10) for i in range(N)])
ans = []
for l,r,d in LRD:
    l -= 1
    segt.apply_lr(l,r,d)
    ans.append(segt.all_prod()[0])
print(*ans, sep='\n')