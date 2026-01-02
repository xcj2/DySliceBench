#!usr/bin/env python3
from collections import defaultdict
from heapq import heappush, heappop
import sys
import math
import bisect
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return list(sys.stdin.readline())
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
mod = 1000000007

#A
"""
x, y = LS()
if x > y:
    print(">")
elif x == y:
    print("=")
else:
    print("<")
"""

#B
"""
x, y, z = LI()
print((x-z)//(y+z))
"""

#C
"""
n, m = LI()
print((m*1900+(n-m)*100)*2**m)
"""

# D
# 解説AC
# 山札のどれからとってもいいという話ではないのか！！！！
n, z, w = LI()
a = LI()
if n == 1:
    print(abs(a[0] - w))
else:
    print(max(abs(a[-1] - w), abs(a[-1] - a[-2])))