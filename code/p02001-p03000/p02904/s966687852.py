#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res
def IR(n):
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def LSR(n):
    return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

#A
def A():
    h,w,a,b = LI()
    ans = [1]*a+[0]*(w-a)
    ans_ = [0]*a+[1]*(w-a)
    for i in range(h):
        if i < b:
            print(*ans,sep = "")
        else:
            print(*ans_,sep = "")
    return

#B
def B():
    class SegmentTree:
        def __init__(self, size, default, op = min):
            self.size = 2**size.bit_length()
            self.dat = [default]*(self.size*2)
            self.op = op

        def update(self, i, x):
            i += self.size
            self.dat[i] = x
            while i > 0:
                i >>= 1
                self.dat[i] = self.op(self.dat[i*2], self.dat[i*2+1])

        def add(self, i, x):
            i += self.size
            self.dat[i] = self.op(self.dat[i], x)
            while i > 0:
                i >>= 1
                self.dat[i] = self.op(self.dat[i], x)

        def get(self, a, b = None):
            if b is None:
                b = a + 1
            l, r = a + self.size, b + self.size
            res = None
            while l < r:
                if l & 1:
                    if res is None:
                        res = self.dat[l]
                    else:
                        res = self.op(res, self.dat[l])
                    l += 1

                if r & 1:
                    r -= 1
                    if res is None:
                        res = self.dat[r]
                    else:
                        res = self.op(res, self.dat[r])
                l >>= 1
                r >>= 1
            return res
    n,k = LI()
    p = LI()
    for i in range(n):
        p[i] += 1
    mi = SegmentTree(n,n,min)
    ma = SegmentTree(n,0,max)
    for i in range(n):
        mi.update(i,p[i])
        ma.update(i,p[i])
    min_p = [mi.get(i,i+k) for i in range(n-k+1)]
    max_p = [ma.get(i,i+k) for i in range(n-k+1)]
    s = 1
    for i in range(k-1):
        if p[i] < p[i+1]:
            s += 1
        else:
            s = 1
    ans = 1
    a = s >= k
    f = 0
    for i in range(1,n-k+1):
        if p[i+k-2] < p[i+k-1]:
            s += 1
        else:
            s = 1
        if s >= k:
            f |= 1
            continue
        elif min_p[i-1] != p[i-1] or max_p[i] != p[i+k-1]:
            ans += 1
    if not a and f:
        ans += 1
    print(ans)
    return
def B_():
    n,k = LI()
    p = LI()
    for i in range(n-k+1):
        print(i)
        s = p[i:i+k]
        s.sort()
        print(p[:i]+s+p[i+k:])
#C
def C():

    return

#D
def D():

    return

#E
def E():

    return

#F
def F():

    return

#Solve
if __name__ == "__main__":
    B()
