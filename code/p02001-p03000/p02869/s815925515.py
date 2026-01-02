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
    n,k = LI()
    if k == 1:
        for i in range(n):
            print(i+1,i+1+n,i+1+2*n)
        return
    a = [i+k for i in range(n)]
    b = [i+n+k for i in range(n)]
    c = [i+2*n+k for i in range(n)]
    if n%2 == 0:
        ans = [[a[i],b[(i+n-k)%n],c[2*i]] if 2*i < n else [a[i],b[(i+n-k)%n],c[(2*i+1)%n]] for i in range(n)]
    else:
        ans = [[a[i],b[(i+n-k)%n],c[(2*i)%n]] for i in range(n)]
    for a,b,c in ans:
        if a+b > c:
            print(-1)
            return
    for a in ans:
        print(*a)
    return
def test():
    def change(m):
        res = []
        for i in range(3*n):
            res.append(m%n)
            m //= n
        return res

    def check(a):
        return a[0]+a[1] <= a[2]
    n,k = LI()
    l = [k+i for i in range(3*n)]
    print(n**(3*n))
    f = [change(i) for i in range(n**(3*n))]
    for k in f[::-1]:
        if all([k.count(i) == n for i in range(n)]):
            a = [[l[i] for i in range(3*n) if k[i] == j] for j in range(n)]
            if all([check(i) for i in a]):
                print(a)
#Solve
if __name__ == "__main__":
    solve()
