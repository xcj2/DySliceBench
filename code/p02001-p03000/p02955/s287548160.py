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
    a,b,c = LI()
    c -= a-b
    print(max(0,c))
    return

#B
def B():
    n = I()
    ans = 0
    for i in range(1,n+1):
        s = str(i)
        if len(s)%2:
            ans += 1
    print(ans)
    return

#C
def C():
    n = I()
    h = LI()
    h[0] -= 1
    for i in range(n-1):
        if h[i+1] < h[i]:
            print("No")
            return
        if h[i+1] > h[i]:
            h[i+1] -= 1
    print("Yes")
    return

#D
def D():
    s = S()
    n = len(s)
    ans = [0]*n
    l = 0
    i = 0
    while i < n:
        if s[i] == "L":
            j = i
            while i < n and s[i] == "L":
                i += 1
                l += 1
            if l:
                if (l+j-i)%2:
                    ans[j-1] = l-l//2
                    ans[j] = l//2
                else:
                    ans[j-1] = l//2
                    ans[j] = l-l//2
            l = 0
        else:
            l += 1
            i += 1
    print(*ans)
    return

#E
def E():
    def factor(n):
        if n == 1:
            return [1]
        if n < 4:
            return [1,n]
        i = 2
        res = [1]
        while i**2 <= n:
            if n%i == 0:
                res.append(i)
                if n//i != i:
                    res.append(n//i)
            i += 1
        res.append(n)
        res.sort()
        return res

    n,k = LI()
    a = LI()
    s = sum(a)
    f = factor(s)
    for i in f[::-1]:
        s = 0
        b = [[a[j]%i,-a[j]%i] for j in range(n)]
        b.sort()
        for j in range(n-1):
            b[j+1][0] += b[j][0]
            b[j+1][1] += b[j][1]
        for j in range(n-1):
            if b[j][0] == b[n-1][1]-b[j][1]:
                break
        s = b[j][0]
        if s <= k:
            print(i)
            return
    return

#F
def F():

    return

#Solve
if __name__ == "__main__":
    E()
