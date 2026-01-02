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
a = IR(2)
b = IR(2)
print(min(a)+min(b))
"""

#B
"""
n = I()
d, x = LI()
a = IR(n)
ans = x
for i in a:
    k = 0
    while k * i + 1 <= d:
        ans += 1
        k += 1
print(ans)
"""

#C
n = I()
a = LI()
a.insert(0, 0)
a.append(0)
ans = 0
for i in range(1, n + 2):
    ans += abs(a[i] - a[i - 1])
#print(ans)
for k in range(1, n + 1):
    if a[k - 1] < a[k]:
        if a[k] > a[k + 1]:
            print(ans - 2 * min(abs(a[k] - a[k - 1]), abs(a[k] - a[k + 1])))
        else:
            print(ans)
    if a[k - 1] > a[k]:
        if a[k] < a[k + 1]:
            print(ans - 2 * min(abs(a[k] - a[k - 1]), abs(a[k] - a[k + 1])))
        else:
            print(ans)
    if a[k - 1] == a[k]:
        print(ans)