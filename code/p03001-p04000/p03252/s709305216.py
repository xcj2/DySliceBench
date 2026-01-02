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

s = input()
t = input()
f = defaultdict(lambda : None)
for i in range(len(s)):
    si,ti = s[i],t[i]
    if f[si] != None:
        if f[si] != ti:
            print("No")
            quit()
    else:
        f[si] = ti
f = defaultdict(lambda : None)
for i in range(len(s)):
    si,ti = s[i],t[i]
    if f[ti] != None:
        if f[ti] != si:
            print("No")
            quit()
    else:
        f[ti] = si

print("Yes")
