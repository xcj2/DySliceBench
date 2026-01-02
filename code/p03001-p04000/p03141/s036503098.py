#!usr/bin/env python3
from collections import defaultdict
import math
def LI(): return list(map(int, input().split()))
def II(): return int(input())
def LS(): return input().split()
def S(): return input()
def IIR(n): return [II() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
mod = 1000000007

#A
"""
n,a,b = LI()
ans = [min(a,b),max(0,a+b-n)]
print(ans[0],ans[1])
"""

#B
"""
n = II()
a = S()
b = S()
c = S()
ans = 0
for i in range(n):
    if a[i] == b[i]:
        if b[i] == c[i]:
            continue
        else:
            ans += 1
    else:
        if b[i] == c[i] or c[i] == a[i]:
            ans += 1
        else:
            ans += 2
print(ans)
"""

#C
n = II()
c = LIR(n)
c.sort(key = lambda x:-x[0]-x[1])
ans = 0
i = 0
for i in range(n):
    x,y = c.pop(0)
    if i%2 == 0:
        ans += x
    else:
        ans -= y
print(ans)

#D

#E

#F

#G

#H

#I

#J

#K

#L

#M

#N

#O

#P

#Q

#R

#S

#T
