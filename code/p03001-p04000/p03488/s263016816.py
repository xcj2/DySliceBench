#!usr/bin/env python3
from collections import defaultdict
from heapq import heappush, heappop
import sys
import math
import bisect
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return list(sys.stdin.readline().rstrip())
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
mod = 1000000007

#A
"""
a, b = LI()
print((a+b+1)//2)
"""

#B
"""
a = S()
a = a[:-1]
b = S()
b = b[:-1]
a.sort()
b.sort(reverse=True)
if a < b:
    print("Yes")
else:
    print("No")
"""

#C
"""
n = I()
a = LI()
a.sort()
seta = set(a)
ans = 0
for i in seta:
    x = bisect.bisect_right(a,i) - bisect.bisect_left(a,i)
    if x != 0 and x >= i:
        ans += x - i
    else:
        ans += x
print(ans)        
"""

# D
# 解説AC
# X,Y軸に分解して、移動は常に同じ方向に行われる（TFFFTならFは常に同じ方向）
# ためTFFFFFTFFFF→TF5TF4として考えて奇数番目のFがx偶数番目がyに寄与
# あとはDP
s = S()
X, Y = LI()
dx = defaultdict(int)
dy = defaultdict(int)
i = 0
num = 0
lis = []
for i in range(len(s)):
    if s[i] == "T":
        lis.append(num)
        num = 0
    else:
        num += 1
if s[-1] == "F":
    lis.append(num)
dx[lis[0]] = True
dy[0] = True
for i in range(1, len(lis)):
    if not i % 2:
        ndx = defaultdict(int)
        for key, _ in dx.items():
            ndx[key + lis[i]] = True
            ndx[key - lis[i]] = True
        dx = ndx
    else:
        ndy = defaultdict(int)
        for key, _ in dy.items():
            ndy[key + lis[i]] = True
            ndy[key - lis[i]] = True
        dy = ndy
if dx[X] and dy[Y]:
    print("Yes")
else:
    print("No")