# Ref: https://atcoder.jp/contests/practice2/submissions/16814531
class SegTree():
    def __init__(self, a, func, idem):
        # the number of nodes is 2n - 1
        self.n = 1 << len(a).bit_length()
        self.size = len(a)
        self.func = func
        self.idem = idem # Identity element
        self.node = [idem] * (2 * self.n - 1)
        for i in range(len(a) + self.n - 2, -1, -1):
            if i >= self.n - 1:
                self.node[i] = a[i - self.n + 1]
            else:
                self.node[i] = self.func(self.node[2 * i + 1], self.node[2 * i + 2])
            
    def get(self, x):
        return self.node[x + self.n - 1]

    def set(self, x, val):
        x += self.n - 1
        self.node[x] = val
        while x > 0:
            x = (x - 1) >> 1
            self.node[x] = self.func(self.node[2*x+1], self.node[2*x+2])
        return
    
    def prod(self, l, r):
        L, R = l + self.n, r + self.n
        s_l, s_r = self.idem, self.idem
        while L < R:
            if R & 1:
                R -= 1
                s_r = self.func(self.node[R-1], s_r)
            if L & 1:
                s_l = s_l = self.func(s_l, self.node[L-1])
                L += 1
            L >>= 1
            R >>= 1
        return self.func(s_l, s_r)

    def max_right(self, l, val):
        if l == self.size:
            return self.size
        L = l + self.n
        s = self.idem
        while 1:
            while L % 2 == 0:
                L >>= 1
            if not val(self.func(s, self.node[L - 1])):
                while L < self.n:
                    L <<= 1
                    if val(self.func(s, self.node[L-1])):
                        s = self.func(s, self.node[L-1])
                        L += 1
                return L - self.n
            s = self.func(s, self.node[L - 1])
            L += 1
            if (L & -L) == L:
                return self.size

    def min_left(self, r, val):
        if r == 0:
            return 0
        R = r + self.n
        s = self.idem
        while True:
            R -= 1
            while R > 1 and R % 2:
                R >>= 1
            if not val(self.func(self.node[R - 1], s)):
                while R < self.n:
                    R = (R << 1) + 1
                    if val(self.func(self.node[R - 1], s)):
                        s = self.func(self.node[R - 1], s)
                        R -= 1
                return R + 1 - self.n
            s = self.func(self.node[R - 1], s)
            if (R & -R) == R:
                return 0
            
import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
st = SegTree(A, max, 0)
for _ in range(Q):
    t, x, y = map(int, input().split())
    if t == 1:
        st.set(x - 1, y)
    elif t == 2:
        print(st.prod(x - 1, y))
    else:
        print(st.max_right(x - 1, lambda z : z < y) + 1)