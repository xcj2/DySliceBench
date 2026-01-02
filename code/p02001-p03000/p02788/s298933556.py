import sys
sys.setrecursionlimit(2147483647)
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
input = lambda:sys.stdin.readline().rstrip()

class LazySegmentTree(object):
    def __init__(self, A, dot, unit, compose, identity, act):
        # A : array of monoid (M, dot, unit)
        # (S, compose, identity) : sub monoid of End(M)
        # compose : (f, g) -> fg (f, g in S)
        # act : (f, x) -> f(x) (f in S, x in M)
        logn = (len(A) - 1).bit_length()
        n = 1 << logn
        tree = [unit] * (2 * n)
        for i, v in enumerate(A):
            tree[i + n] = v
        for i in range(n - 1, 0, -1):
            tree[i] = dot(tree[i << 1], tree[i << 1 | 1])
        self._n, self._logn, self._tree, self._lazy = n, logn, tree, [identity] * (2 * n)
        self._dot, self._unit, self._compose, self._identity, self._act = dot, unit, compose, identity, act

    def _ascend(self, i):
        tree, lazy, dot, act = self._tree, self._lazy, self._dot, self._act
        while i > 1:
            i >>= 1
            tree[i] = act(lazy[i], dot(tree[i << 1], tree[i << 1 | 1]))

    def _descend(self, i):
        tree, lazy, identity, compose, act = self._tree, self._lazy, self._identity, self._compose, self._act
        for k in range(self._logn, 0, -1):
            p = i >> k
            f = lazy[p]
            tree[p << 1], lazy[p << 1] = act(f, tree[p << 1]), compose(f, lazy[p << 1])
            tree[p << 1 | 1], lazy[p << 1 | 1] = act(f, tree[p << 1 | 1]), compose(f, lazy[p << 1 | 1])
            lazy[p] = identity

    # A[i] <- f(A[i]) for all i in [l, r)
    def range_act(self, l, r, f):
        l += self._n
        r += self._n
        # propagation isn't necessary if S is commutative
        # self._descend(l)
        # self._descend(r - 1)
        l0, r0 = l, r
        tree, lazy, act, compose = self._tree, self._lazy, self._act, self._compose
        while l < r:
            if l & 1:
                tree[l], lazy[l] = act(f, tree[l]), compose(f, lazy[l])
                l += 1
            if r & 1:
                r -= 1
                tree[r], lazy[r] = act(f, tree[r]), compose(f, lazy[r])
            l >>= 1
            r >>= 1
        self._ascend(l0)
        self._ascend(r0 - 1)

    # calculate product of A[l:r]
    def sum(self, l, r):
        l += self._n
        r += self._n
        self._descend(l)
        self._descend(r - 1)
        l_val = r_val = self._unit
        tree, dot = self._tree, self._dot
        while l < r:
            if l & 1:
                l_val = dot(l_val, tree[l])
                l += 1
            if r & 1:
                r -= 1
                r_val = dot(tree[r], r_val)
            l >>= 1
            r >>= 1
        return dot(l_val, r_val)

from operator import add
def resolve():
    n, d, a = map(int, input().split())
    XH = [None] * n
    coordinates = set() # for coordinates compression
    for i in range(n):
        x, h = map(int, input().split())
        XH[i] = [x, (h - 1) // a + 1] # 初めから何回減らすかだけ持てばよい
        coordinates.add(x)
        coordinates.add(x + 2 * d + 1) # [x, x + 2d + 1) に減らす
    XH.sort()
    compress = {v : i for i, v in enumerate(sorted(coordinates))}

    n = len(compress)
    A = [0] * n
    for i in range(len(XH)):
        A[compress[XH[i][0]]] = XH[i][1]

    res = 0
    tree = LazySegmentTree(A, max, 0, add, 0, add) # 区間 add, 1点取得ができればよいので、区間拡張しなくてよい max にしておく
    for x, h in XH:
        # もし x が生き残っていたら、[x, x + 2d + 1) から hp を引く
        hp = tree.sum(compress[x], compress[x] + 1)
        if hp <= 0:
            continue
        res += hp
        tree.range_act(compress[x], compress[x + 2 * d + 1], -hp)

    print(res)
resolve()