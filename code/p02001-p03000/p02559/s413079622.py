"""
n,q = map(int,input().split())
a = list(map(int,input().split()))

def segfunc(x,y):
    return x + y

def init(init_val):
    #set_val
    for i in range(n):
        seg[i+num-1]=init_val[i]
    #built
    for i in range(num-2,-1,-1) :
        seg[i]=segfunc(seg[2*i+1],seg[2*i+2])

def update(k,x):
    k += num-1
    seg[k] = x
    while k:
        k = (k-1)//2
        seg[k] = segfunc(seg[k*2+1],seg[k*2+2])

def query(p,q):
    if q<=p:
        return ide_ele
    p += num-1
    q += num-2
    res=ide_ele
    while q-p>1:
        if p&1 == 0:
            res = segfunc(res,seg[p])
        if q&1 == 1:
            res = segfunc(res,seg[q])
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = segfunc(res,seg[p])
    else:
        res = segfunc(segfunc(res,seg[p]),seg[q])
    return res

#####単位元######
ide_ele = 0

#num:n以上の最小の2のべき乗
num =2**(n-1).bit_length()
seg=[ide_ele]*2*num
init(a)

for _ in range(q):
    q1,p,x = map(int,input().split())
    if q1 == 0:
        update(p, seg[p+num-1] + x)
    else:
        print(query(p, x))
"""



from typing import Callable, List, TypeVar

T = TypeVar("T")

class SegmentTree:
    """Segment Tree"""

    __slots__ = ["e", "op", "_n", "_size", "tree"]

    def __init__(self, a: List[T], e: T, op: Callable[[T, T], T]) -> None:
        self.e = e
        self.op = op
        self._n = len(a)
        self._size = 1 << (self._n - 1).bit_length()

        self.tree = [e] * self._size + a + [e] * (self._size - self._n)
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def _update(self, k: int) -> None:
        """Update the value of a[k]."""
        self.tree[k] = self.op(self.tree[2 * k], self.tree[2 * k + 1])

    def set(self, k: int, x: T) -> None:
        """Assign x to a[k] in O(log n)."""
        assert 0 <= k < self._n

        k += self._size
        self.tree[k] = x
        while k:
            k >>= 1
            self._update(k)

    def get(self, k: int) -> T:
        """Return a[k] in O(1)."""
        assert 0 <= k < self._n
        return self.tree[k + self._size]

    def prod(self, l: int, r: int) -> T:
        """Return op(a[l], ..., a[r - 1]). Return e, if l == r.
        Complexity: O(log n)
        """
        assert 0 <= l <= r <= self._n

        sml, smr = self.e, self.e
        l += self._size
        r += self._size

        while l < r:
            if l & 1:
                sml = self.op(sml, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self.op(self.tree[r], smr)
            l >>= 1
            r >>= 1
        return self.op(sml, smr)

    def prod_all(self) -> T:
        """Return op(a[0], ..., a[n - 1]. Return e if n == 0.
        Complexity: O(1)
        """
        return self.tree[1]

    def max_right(self, l: int, f: Callable[[T], bool]) -> int:
        """
        Return an index r satisfying both:
            1. r = l or f(op(a[l], a[l + 1], ..., a[r - 1])) = true
            2. r = n or f(op(a[l], a[l + 1], ..., a[r])) = false.

        If f is monotone, this is the maximum r satisfying:
            f(op(a[l], a[l + 1], ..., a[r - 1])) = true.

        Complexity: O(log n)
        """
        assert 0 <= l <= self._n
        assert f(self.e)

        if l == self._n:
            return self._n

        l += self._size
        sm = self.e

        while True:
            while not l & 1:
                l >>= 1

            if not f(self.op(sm, self.tree[l])):
                while l < self._size:
                    l *= 2
                    if f(self.op(sm, self.tree[l])):
                        sm = self.op(sm, self.tree[l])
                        l += 1
                return l - self._size

            sm = self.op(sm, self.tree[l])
            l += 1

            if (l & -l) == l:
                break

        return self._n

    def min_left(self, r: int, f: Callable[[T], bool]) -> int:
        """
        Return an index l satisfying both:
            1. l = r or f(op(a[l], a[l + 1], ..., a[r - 1])) = true
            2. l = 0 or f(op(a[l - 1], a[l + 1], ..., a[r - 1])) = false.
        If f is monotone, this is the minimum l satisfying:
            f(op(a[l], a[l + 1], ..., a[r - 1])) = true.

        Complexity: O(log n)
        """
        assert 0 <= r <= self._n
        assert f(self.e)

        if not r:
            return 0

        r += self._size
        sm = self.e

        while True:
            r -= 1
            while r > 1 and r % 2:
                r >>= 1

            if not f(self.op(self.tree[r], sm)):
                while r < self._size:
                    r = 2 * r + 1
                    if f(self.op(self.tree[r], sm)):
                        sm = self.op(self.tree[r], sm)
                        r -= 1
                return r + 1 - self._size

            if (r & -r) == r:
                break

        return 0

def add(x, y):
    return x + y

n,q = map(int,input().split())
a = list(map(int,input().split()))
tree = SegmentTree(a, 0, add)

for _ in range(q):
    t,p,x = map(int,input().split())
    if t == 0:
        tree.set(p, tree.get(p) + x)
    else:
        print(tree.prod(p, x))
