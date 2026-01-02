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

def solve():
    def add(i,x,bit):
        while i < len(bit):
            bit[i] += x
            i += i&-i
    def sum(i,bit):
        res = 0
        while i :
            res += bit[i]
            i -= i&-i
        return res
    Q = I()
    q = LIR(Q)
    bit = [0]*(Q+1)
    bit2  = [0]*(Q+1)
    bit3 = [0]*(Q+1)
    bit4 = [0]*(Q+1)
    A = []
    for qi in q:
        if qi[0] == 1:
            a = qi[1]
            A.append(a)
    qa = [i for i in A]
    qa.sort()
    ia = {i:bisect.bisect_left(qa,i) for i in A}
    revqa = [-i for i in qa[::-1]]
    revia = {i:bisect.bisect_left(revqa,-i) for i in A}
    sb = 0
    n = 0
    for qi in q:
        if qi[0] == 1:
            a,b = qi[1:]
            ia[a] += 1
            revia[a] += 1
            i = ia[a]
            revi = revia[a]
            add(i,1,bit)
            add(i,a,bit2)
            add(revi,1,bit3)
            add(revi,a,bit4)
            sb += b
            n += 1
        else:
            l = 0
            r = Q
            k = (n-1)>>1
            while r-l > 1:
                m = (l+r) >> 1
                if sum(m,bit) <= k:
                    l = m
                else:
                    r = m
            fa = qa[l]
            i = ia[fa]
            revi = revia[fa]
            s1 = sum(l,bit)
            s2 = sum(l,bit2)
            s3 = sum(revi,bit3)
            s4 = sum(revi,bit4)
            s = fa*s1-s2+s4-fa*s3+sb
            print(fa,s)
    return

#Solve
if __name__ == "__main__":
    solve()
