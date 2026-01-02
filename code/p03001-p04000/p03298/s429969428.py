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

    return
#B
def B():

    return

#C
def C():
    n = I()
    s = S()
    d = defaultdict(lambda : 0)
    alp = list("abcdefghijklmnopqrstuvwxyz")
    f = {}
    for i in range(26):
        f[alp[i]] = i+1
    for i in range(2*n):
        s[i] = f[s[i]]
    for i in range(n>>1):
        s[i],s[n-i-1] = s[n-i-1],s[i]
    k = 27
    m = 1<<n
    p = [1<<j for j in range(n)]
    for i in range(m):
        r = 0
        b = 0
        for j in range(n):
            if i&p[j]:
                r *= k
                r += s[j]
            else:
                b *= k
                b += s[j]
        d[(r,b)] += 1
    ans = 0
    for i in range(m):
        r = 0
        b = 0
        for j in range(n):
            if i&p[j]:
                r *= k
                r += s[j+n]
            else:
                b *= k
                b += s[j+n]
        ans += d[(r,b)]
    print(ans)
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
    C()
