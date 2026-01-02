#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from itertools import permutations
import sys
import math
import bisect
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
    def size(p):
        return (p[2]-p[0])*(p[3]-p[1])

    def cut(p,s):
        u,l,d,r = p
        x = r-l
        y = d-u
        s %= 2*(x+y)
        if s < x:
            a,b = [u,l,d,l+s], [u,l+s,d,r]
        elif s < x+y:
            s -= x
            a,b = [u,l,u+s,r], [u+s,l,d,r]
        elif s < 2*x+y:
            s -= x+y
            s = x-s
            a,b = [u,l,d,l+s],[u,l+s,d,r]
        else:
            s -= 2*x+y
            s = y-s
            a,b = [u,l,u+s,r], [u+s,l,d,r]
        if size(b) < size(a):
            a,b = b,a
        return a,b

    while 1:
        n,w,h = LI()
        if n == w == h == 0:
            break
        q = [[0,0,h,w]]
        for _ in range(n):
            i,s = LI()
            i -= 1
            p = q.pop(i)
            a,b = cut(p,s)
            q.append(a)
            q.append(b)
        s = [size(p) for p in q]
        s.sort()
        print(*s)
    return

#Solve
if __name__ == "__main__":
    solve()

