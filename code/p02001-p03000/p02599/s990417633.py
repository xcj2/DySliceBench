#!usr/bin/env python3
import sys
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LIR(n):
    return [LI() for i in range(n)]
class BIT:
    def __init__(self, size):
        self.size = size + 1
        self.dat = [0]*self.size

    def add(self, i, x=1):
        while i < self.size:
            self.dat[i] += x
            i += i&-i

    # sum[l,r)
    # sum[0,l] (r = None)
    def sum(self, l, r=None):
        if r is None:
            res = 0
            while l > 0:
                res += self.dat[l]
                l -= l&-l
            return res

        else:
            rres = 0
            while r > 0:
                rres += self.dat[r]
                r -= r&-r
            l -= 1
            lres = 0
            while l > 0:
                lres += self.dat[l]
                l -= l&-l
            return rres - lres


def solve():
    n,Q = LI()
    c = LI()
    q = LIR(Q)
    q = [[i,q[i]] for i in range(Q)]
    q.sort(key = lambda x:x[1][1])
    bit = BIT(n+1)
    i = 0
    p = [None]*(n+1)
    ans = [0]*Q
    for ind,(l, r) in q:
        while i < r:
            ci = c[i]
            j = p[ci]
            if j is not None:
                bit.add(j,-1)
            bit.add(i+1)
            p[ci] = i+1
            i += 1
        ans[ind] = bit.sum(l,r)
    for i in ans:
        print(i)
    return

#Solve
if __name__ == "__main__":
    solve()
