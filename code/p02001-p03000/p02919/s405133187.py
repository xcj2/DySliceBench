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
    n = I()
    print(n**3)
    return

#B
def B():
    n = I()
    a = LI()
    b = LI()
    c = LI()
    ans = sum(b)
    for i in range(n-1):
        x = a[i]
        y = a[i+1]
        if y == x+1:
            ans += c[x-1]
    print(ans)
    return

#C
def C():
    n = I()
    b = LI()
    b.append(float("inf"))
    a = [min(b[i],b[i-1]) for i in range(n)]
    print(sum(a))
    return

#D
def D():
    n,k = LI()
    a = S()
    ans = 0
    for i in range(n-1):
        if a[i] == a[i+1]:
            ans += 1
    print(min(n-1,ans+2*k))
    return

#E
def E():
    def add(i):
        while i < len(bit):
            bit[i] += 1
            i += i&-i

    def sum(i):
        res = 0
        while i > 0:
            res += bit[i]
            i -= i&-i
        return res

    n = I()
    p = LI()
    p = [(p[i],i+2) for i in range(n)]
    p.sort(key = lambda x:-x[0])
    bit = [0]*(n+3)
    add(p[0][1])
    ans = 0
    for pi,i in p[1:]:
        s = sum(i)
        l = 0
        r = i
        while r-l > 1:
            m = (l+r)>>1
            if sum(m) == s:
                r = m
            else:
                l = m
        x1 = r

        l = i
        r = n+2
        while r-l > 1:
            m = (l+r)>>1
            if sum(m) == s:
                l = m
            else:
                r = m
        x2 = r

        s_ = s-1
        l = 0
        r = x1
        while r-l > 1:
            m = (l+r)>>1
            if sum(m) == s_:
                r = m
            else:
                l = m
        x3 = r

        s_ = s+1
        l = x2
        r = n+2
        while r-l > 1:
            m = (l+r)>>1
            if sum(m) == s_:
                l = m
            else:
                r = m
        x4 = r
        ans += pi*((x1-x3)*(x2-i)+(x4-x2)*(i-x1))
        add(i)
    print(ans)
    return

#F
def F():
    n = I()
    s = LI()
    s.sort()
    s = s[::-1]
    m = 1<<n
    f = [-1]*m
    f[0] = 0
    for i in range(n):
        k = 0
        l = 0
        for j in range(1<<i):
            while f[k] != i:
                k += 1
            while f[l] >= i or s[k] <= s[l]:
                l += 1
                if l == m:
                    print("No")
                    return
            f[l] = i+1
            k += 1
        for j in range(m):
            if f[j] >= 0:
                f[j] = i+1
    print("Yes")
    return

#Solve
if __name__ == "__main__":
    E()
