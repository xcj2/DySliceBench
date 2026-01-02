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
a = input()
b = input()
if a[2] == b[0] and a[1] == b[1] and a[0] == b[2]:
    print("YES")
else:
    print("NO")
"""

#B
"""
n = I()
n = int(math.sqrt(n))
print(n**2)
"""

#C
n = I()
a = LI()
a.sort()
b = LI()
b.sort()
c = LI()
c.sort()
ans = 0
for i in b:
    x = bisect.bisect_left(a, i)
    x = x * (n - bisect.bisect_right(c, i))
    ans += x
print(ans)