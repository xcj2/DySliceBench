# Solution using a lazy segment tree

from bisect import bisect_left
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


class SegmentTree:  # 0-indexed
    def __init__(self, array, operation=min, identity=10**30):
        self.identity = identity
        self.n = len(array)
        self.N = 1 << (self.n - 1).bit_length()
        self.tree = [self.identity] * 2 * self.N
        self.lazy = [None] * 2 * self.N
        self.opr = operation
        for i in range(self.n):
            self.tree[i+self.N-1] = array[i]
        for i in range(self.N-2, -1, -1):
            self.tree[i] = self.opr(self.tree[2*i+1], self.tree[2*i+2])

    def values(self):
        for i in range(self.n-1):
            self.query(i, i+1)
        return self.tree[self.N-1:self.n+self.N-1]

    def getindex(self, l, r):
        l = (l + self.N)
        r = (r + self.N)
        lm = l // (l & -l) >> 1
        rm = r // (r & -r) >> 1
        while r-l > 0:
            if r <= rm:
                yield r
            if l <= lm:
                yield l
            l = l >> 1
            r = r >> 1
        while l:
            yield l
            l = l >> 1

    def propagates(self, *indices):
        for i in reversed(indices):
            i -= 1
            v = self.lazy[i]
            if v is None:
                continue
            self.lazy[2*i+1] = self.tree[2*i+1] = v >> 1
            self.lazy[2*i+2] = self.tree[2*i+2] = v >> 1
            self.lazy[i] = None

    def update(self, p, q, x):
        if p == q:
            return None
        indices = tuple(self.getindex(p, q))
        self.propagates(*indices)
        p += self.N-1
        q += self.N-2
        while q-p > 0:
            if p % 2 == 0:
                self.lazy[p] = self.tree[p] = x
            if q % 2 == 1:
                self.lazy[q] = self.tree[q] = x
            p = p//2
            q = q//2 - 1
            x <<= 1
        if p == q:
            self.lazy[p] = self.tree[p] = x
        for i in indices:
            i -= 1
            self.tree[i] = self.opr(self.tree[2*i+1], self.tree[2*i+2])

    def query(self, p, q):  # [p,q)
        if q <= p:
            print("Oops!  That was no valid number.  Try again...")
            exit()
        self.propagates(*self.getindex(p, q))
        p += self.N-1
        q += self.N-2
        res = self.identity
        while q-p > 0:
            if p % 2 == 0:
                res = self.opr(res, self.tree[p])
            if q % 2 == 1:
                res = self.opr(res, self.tree[q])
            p = p//2
            q = q//2 - 1
        if p == q:
            res = self.opr(res, self.tree[p])
        return res


n, q = map(int, input().split())

Works = []
for _ in range(n):
    s, t, x = map(int, input().split())
    Works.append((s, t, x))
Works = sorted(Works, key=lambda w: -w[2])

People = []
for _ in range(q):
    People.append(int(input()))

ST = SegmentTree([-1]*q)

for s, t, x in Works:
    left = bisect_left(People, s-x)
    right = bisect_left(People, t-x)
    ST.update(left, right, x)

for x in ST.values():
    print(x)
