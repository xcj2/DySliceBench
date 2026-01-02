class DualSegmentTree():

    def __init__(self, n, op, e):
        self.n = n
        self.op = op
        self.e = e
        self.depth = (self.n - 1).bit_length()
        self.size = 1 << self.depth
        self.lazy = [self.e] * ((self.size << 1) + 1)

    def update(self, l, r, x):
        l += self.size
        r += self.size
        self.propagate(l)
        self.propagate(r-1)
        while l < r:
            if r&1:
                r -= 1              # 半開区間なので先に引いてる
                self.lazy[r] = self.op(x, self.lazy[r])
            if l&1:
                self.lazy[l] = self.op(x, self.lazy[l])
                l += 1
            l = l // 2
            r = r // 2

    def propagate(self, i):
        for k in range(self.depth,0,-1):
            x = i>>k
            if self.lazy[x] == self.e:
                continue
            self.lazy[(x<<1)+1] = self.op(self.lazy[x], self.lazy[(x<<1)+1])
            self.lazy[x<<1] = self.op(self.lazy[x], self.lazy[x<<1])
            self.lazy[x] = self.e

    def get(self, i):
        i += self.size
        self.propagate(i)
        return self.lazy[i]

    def __getitem__(self, i):
        return self.get(i)

    def __iter__(self):
        for x in range(1, self.size):
            if self.lazy[x] == self.e:
                continue
            self.lazy[(x<<1)+1] = self.op(self.lazy[x], self.lazy[(x<<1)+1])
            self.lazy[x<<1] = self.op(self.lazy[x], self.lazy[x<<1])
            self.lazy[x] = self.e
        for a in self.lazy[self.size:self.size+self.n]:
            yield a

    def __str__(self):
        for x in range(1, self.size):
            if self.lazy[x] == self.e:
                continue
            self.lazy[(x<<1)+1] = self.op(self.lazy[x], self.lazy[(x<<1)+1])
            self.lazy[x<<1] = self.op(self.lazy[x], self.lazy[x<<1])
            self.lazy[x] = self.e
        return str(self.lazy[self.size:self.size + self.n])

##################################################################################################################
import sys
from bisect import *
input = sys.stdin.readline

N, Q = map(int, input().split())

e = -1
op = lambda x, y: x if x != e else y
st = DualSegmentTree(Q, op, e)

Qu = [list(map(int, input().split())) for _ in range(N)]
Qu.sort(key=lambda x:x[2], reverse=True)

D = [int(input()) for _ in range(Q)]

for q in Qu:
    S, T, X = q
    L = bisect_left(D,S-X)
    R = bisect_left(D,T-X)
    st.update(L, R, X)
print(*st, sep="\n")
