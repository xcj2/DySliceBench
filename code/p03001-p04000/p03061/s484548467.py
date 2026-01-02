try:
    from math import gcd
except:
    from fractions import gcd
import operator
from collections import deque


class Segtree:
    """
    st = Segtree(4, f=operator.add, e=0)
    st[1:] = [4, 9, 16]
    st[0] = -99
    assert st[-1] == 16
    assert st[:] == [-99, 4, 9, 16]
    assert st.grasp(1, 3) == 13
    """

    def __init__(self, n, f=operator.add, e=0):
        """all(f(v, e) == f(e, v) == v for v in data)"""
        self.r = range(n)
        self.size = 2 ** ((n - 1).bit_length())
        self.tree = [e] * (2 * self.size)
        self.f = f
        self.iden = e

    def __len__(self):
        return len(self.r)

    def __list__(self):
        return self.tree[self.size-1:self.size-1+len(self.r)]

    def __repr__(self):
        return repr(list(self))

    def grasp(self, i=0, j=None):
        """reduce(f, data[i:j], e)"""
        if j is None:
            j = len(self)
        i = self.size - 1 + max(i, 0)
        j = self.size - 1 + min(j, len(self))
        ans = self.iden
        while j - i > 0:
            if i & 1 is 0:
                ans = self.f(self.tree[i], ans)
            if j & 1 is 0:
                ans = self.f(ans, self.tree[j-1])
            i = i >> 1
            j = (j - 1) >> 1
        return ans

    def __getitem__(self, i):
        r = self.r[i]
        if isinstance(r, int):
            return self.tree[self.size - 1 + r]
        else:
            return [self.tree[self.size - 1 + ri] for ri in r]

    def __setitem__(self, i, v):
        """Extra elements will be ignored when i is a slice."""
        r = self.r[i]
        if isinstance(r, int):
            r = [r]
            v = [v]
        q = deque()
        s = set()

        def addnext(j):
            k = (j - 1) // 2
            if k >= 0 and k not in s:
                q.append(k)
                s.add(k)

        for ri, vi in zip(r, v):
            j = self.size - 1 + ri
            self.tree[j] = vi
            addnext(j)
        while len(q):
            j = q.popleft()
            # s.remove(j)
            vl = self.tree[2 * j + 1]
            vr = self.tree[2 * j + 2]
            self.tree[j] = self.f(vl, vr)
            addnext(j)


N = int(input())
A = [int(s) for s in input().split()]
st = Segtree(N, f=gcd, e=0)
st[:] = A
ans = max([gcd(st.grasp(0, i), st.grasp(i+1)) for i in range(N)])
print(ans)
