#!/usr/bin/env python3
import sys
def input(): return sys.stdin.readline().rstrip()

# ライブラリ参照https://atcoder.jp/contests/practice2/submissions/16579094


class LazySegmentTree():
    def __init__(self, init, unitX, unitA, f, g, h):
        self.f = f  # (X, X) -> X
        self.g = g  # (X, A, size) -> X
        self.h = h  # (A, A) -> A
        self.unitX = unitX
        self.unitA = unitA
        self.f = f
        if type(init) == int:
            self.n = init
            # self.n = 1 << (self.n - 1).bit_length()
            self.X = [unitX] * (self.n * 2)
            self.size = [1] * (self.n * 2)
        else:
            self.n = len(init)
            # self.n = 1 << (self.n - 1).bit_length()
            self.X = [unitX] * self.n + init + [unitX] * (self.n - len(init))
            self.size = [0] * self.n + [1] * \
                len(init) + [0] * (self.n - len(init))
            for i in range(self.n-1, 0, -1):
                self.X[i] = self.f(self.X[i*2], self.X[i*2 | 1])

        for i in range(self.n - 1, 0, -1):
            self.size[i] = self.size[i*2] + self.size[i*2 | 1]

        self.A = [unitA] * (self.n * 2)

    def update(self, i, x):
        i += self.n
        self.X[i] = x
        i >>= 1
        while i:
            self.X[i] = self.f(self.X[i*2], self.X[i*2 | 1])
            i >>= 1

    def calc(self, i):
        return self.g(self.X[i], self.A[i], self.size[i])

    def calc_above(self, i):
        i >>= 1
        while i:
            self.X[i] = self.f(self.calc(i*2), self.calc(i*2 | 1))
            i >>= 1

    def propagate(self, i):
        self.X[i] = self.g(self.X[i], self.A[i], self.size[i])
        self.A[i*2] = self.h(self.A[i*2], self.A[i])
        self.A[i*2 | 1] = self.h(self.A[i*2 | 1], self.A[i])
        self.A[i] = self.unitA

    def propagate_above(self, i):
        H = i.bit_length()
        for h in range(H, 0, -1):
            self.propagate(i >> h)

    def propagate_all(self):
        for i in range(1, self.n):
            self.propagate(i)

    def getrange(self, l, r):
        l += self.n
        r += self.n
        l0, r0 = l // (l & -l), r // (r & -r) - 1
        self.propagate_above(l0)
        self.propagate_above(r0)

        al = self.unitX
        ar = self.unitX
        while l < r:
            if l & 1:
                al = self.f(al, self.calc(l))
                l += 1
            if r & 1:
                r -= 1
                ar = self.f(self.calc(r), ar)
            l >>= 1
            r >>= 1
        return self.f(al, ar)

    def getvalue(self, i):
        i += self.n
        self.propagate_above(i)
        return self.calc(i)

    def operate_range(self, l, r, a):
        l += self.n
        r += self.n
        l0, r0 = l // (l & -l), r // (r & -r) - 1
        self.propagate_above(l0)
        self.propagate_above(r0)
        while l < r:
            if l & 1:
                self.A[l] = self.h(self.A[l], a)
                l += 1
            if r & 1:
                r -= 1
                self.A[r] = self.h(self.A[r], a)
            l >>= 1
            r >>= 1

        self.calc_above(l0)
        self.calc_above(r0)

    # Find r s.t. calc(l, ..., r-1) = True and calc(l, ..., r) = False
    def max_right(self, l, z):
        if l >= self.n:
            return self.n
        l += self.n
        s = self.unitX
        while 1:
            while l % 2 == 0:
                l >>= 1
            if not z(self.f(s, self.calc(l))):
                while l < self.n:
                    l *= 2
                    if z(self.f(s, self.calc(l))):
                        s = self.f(s, self.calc(l))
                        l += 1
                return l - self.n
            s = self.f(s, self.calc(l))
            l += 1
            if l & -l == l:
                break
        return self.n

    # Find l s.t. calc(l, ..., r-1) = True and calc(l-1, ..., r-1) = False
    def min_left(self, r, z):
        if r <= 0:
            return 0
        r += self.n
        s = self.unitX
        while 1:
            r -= 1
            while r > 1 and r % 2:
                r >>= 1
            if not z(self.f(self.calc(r), s)):
                while r < self.n:
                    r = r * 2 + 1
                    if z(self.f(self.calc(r), s)):
                        s = self.f(self.calc(r), s)
                        r -= 1
                return r + 1 - self.n
            s = self.f(self.calc(r), s)
            if r & -r == r:
                break
        return 0


def main():
    P = 998244353
    def f(x, y): return ((x[0] + y[0]) % P, x[1]+y[1])
    def g(x, a, s): return ((x[1]*a) % P, x[1]) if a != 10**10 else x
    def h(a, b): return b if b != 10**10 else a
    unitX = (0, 0)
    unitA = 10**10
    N, Q = map(int, input().split())
    A = [(1, 1)]
    for _ in range(N-1):
        now = A[-1][0]
        A.append(((now*10) % P, (now*10) % P))
    st = LazySegmentTree(A[::-1], unitX, unitA, f, g, h)
    #print(st.getrange(0, N))

    for _ in range(Q):
        l, r, d = map(int, input().split())
        st.operate_range(l-1, r, d)
        print(st.getrange(0, N)[0])


if __name__ == '__main__':
    main()