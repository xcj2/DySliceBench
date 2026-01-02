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
    s = list(input())
    n = len(s)
    alp = list("abcdefghijklmnopqrstuvwxyz")
    f = {}
    for i in range(26):
        f[alp[i]] = i
    if n == 26:
        if s == alp[::-1]:
            print(-1)
        else:
            d = [1]*26
            m = f[s[-1]]
            d[m] = 0
            for i in range(n-1)[::-1]:
                if m > f[s[i]]:
                    break
                m = f[s[i]]
                d[m] = 0
            k = f[s[i]]
            for j in range(k+1,n):
                if not d[j]:
                    break
            s = s[:i]+[alp[j]]
            print(*s,sep = "")
    else:
        d = [1]*26
        for i in s:
            d[f[i]] = 0
        for i in range(26):
            if d[i]:
                break
        s += [alp[i]]
        print(*s,sep = "")
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
