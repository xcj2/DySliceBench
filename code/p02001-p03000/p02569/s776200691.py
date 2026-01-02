# self.data: 1-indexed
#    __1__
#  _2_   _3_
# 4   5 6   7

# f(f(a, b), c) == f(a, f(b, c))

class LazySegmentTree:
    # a = [default] * n
    # O(n)
    def __init__(self, n, f, default=(0, 0, 1)):
        self.num_leaf = 2 ** (n-1).bit_length()
        self.data = [default] * (2*self.num_leaf)
        self.lazy = [True] * (2*self.num_leaf)
        self.f = f

    # You can use first_update before you use update.
    # a[i] = x
    # O(log(n))
    def first_update(self, i, x):
        i += self.num_leaf
        self.data[i] = x
        i >>= 1
        while i > 0:
            self.data[i] = self.f(self.data[2*i], self.data[2*i+1])
            i >>= 1

    def gindex(self, l, r):
        lis = []
        l += self.num_leaf
        r += self.num_leaf
        lm = (l // (l & -l)) >> 1
        rm = (r // (r & -r)) >> 1
        while l < r:
            if l <= lm:
                lis.append(l)
            if r <= rm:
                lis.append(r)
            l >>= 1
            r >>= 1
        while l:
            lis.append(l)
            l >>= 1
        lis.reverse()
        return lis

    def lazy_processing(self, i):
        self.data[i] = (self.data[i][1] * self.data[i][2] - self.data[i][0], self.data[i][2], self.data[i][1])
        self.lazy[i] = not self.lazy[i]

    # from parent to children
    def propagate(self, lis):
        for i in lis:
            if self.lazy[i]:
                continue
            self.lazy_processing(2*i)
            self.lazy_processing(2*i+1)
            self.lazy[i] = True

    # update a[l:r]
    def update(self, l, r):
        lis = self.gindex(l, r)

        # top-down propagation
        self.propagate(lis)

        l += self.num_leaf
        r += self.num_leaf - 1
        while l < r:
            if l & 1:
                self.lazy_processing(l)
                l += 1
            if not r & 1:
                self.lazy_processing(r)
                r -= 1
            l >>= 1
            r >>= 1
        if l == r:
            self.lazy_processing(l)

        # bottom-up propagation
        lis.reverse()
        for i in lis:
            self.data[i] = self.f(self.data[2*i], self.data[2*i+1])

    # return f(a[l:r])
    def query(self, l, r):
        # top-down propagation
        self.propagate(self.gindex(l, r))

        l += self.num_leaf
        r += self.num_leaf - 1
        lres, rres = (0, 1, 0), self.data[0] # self.data[0] == default
        while l < r:
            if l & 1:
                lres = self.f(lres, self.data[l])
                l += 1
            if not r & 1:
                rres = self.f(self.data[r], rres)
                r -= 1
            l >>= 1
            r >>= 1
        if l == r:
            res = self.f(self.f(lres, self.data[l]), rres)
        else:
            res = self.f(lres, rres)
        return res

from sys import stdin
input = stdin.buffer.readline

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    def f(tup1, tup2):
        return (tup1[0] + tup2[0] + tup1[2] * tup2[1], tup1[1] + tup2[1], tup1[2] + tup2[2])

    lst = LazySegmentTree(n, f=f)

    for i, x in enumerate(a):
        lst.first_update(i, (0, 1-x, x))

    ans = []
    for _ in range(q):
        t, l, r = list(map(int, input().split()))
        if t == 1:
            lst.update(l-1, r)
        else:
            ans.append(lst.query(l-1, r)[0])

    for i in ans:
        print(i)

main()
