#!usr/bin/env python3
import math
import sys
import bisect
def LI(): return [int(x) for x in sys.stdin.buffer.readline().split()]
def I(): return int(sys.stdin.buffer.readline())
def LIR(n):
    return [LI() for i in range(n)]

class SegmentTree:
    def __init__(self, size, f=lambda x,y : x+y, default=0):
        self.size = 2**(size-1).bit_length()
        self.default = default
        self.dat = [default]*(self.size*2)
        self.f = f

    def update(self, i, x):
        i += self.size
        self.dat[i] = x
        while i > 0:
            i >>= 1
            self.dat[i] = self.f(self.dat[i*2], self.dat[i*2+1])

    def get(self, a, b=None):
        if b is None:
            b = a + 1
        l, r = a + self.size, b + self.size
        lres, rres = self.default, self.default
        while l < r:
            if l & 1:
                lres = self.f(lres, self.dat[l])
                l += 1

            if r & 1:
                r -= 1
                rres = self.f(self.dat[r], rres)
            l >>= 1
            r >>= 1
        res = self.f(lres, rres)
        return res

def solve():
    n,d,a = LI()
    g = LIR(n)
    g.sort()
    X = [i for (i,_) in g]
    s = SegmentTree(n)
    ans = 0
    for i in range(n):
        x = g[i][0]
        j = bisect.bisect_left(X,x-2*d)
        h = g[i][1]-s.get(j,i)
        if h <= 0:
            continue
        k = math.ceil(h/a)
        ans += k
        s.update(i,k*a)
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
