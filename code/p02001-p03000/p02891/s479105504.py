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
    s = S()
    k = I()
    n = len(s)
    for i in range(n):
        if s[i] != s[0]:
            break
    else:
        print((k*n)>>1)
        return
    s += s
    t = s[i-1]
    for j in range(n)[::-1]:
        if s[j] != t:
            break
    s = s[i:j+1]
    ans = (i>>1)+((n-1-j)>>1)+((n-1-j+i)>>1)*(k-1)
    i = 0
    n = len(s)
    while i < n:
        t = s[i]
        l = 0
        while i < n and t == s[i]:
            i += 1
            l += 1
        ans += (l >> 1)*k
    print(ans)
    return

#B
def B():

    return

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
    A()
