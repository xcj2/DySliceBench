#!usr/bin/env python3
from collections import defaultdict
from heapq import heappush, heappop
import math
import bisect
import random
def LI(): return list(map(int, input().split()))
def I(): return int(input())
def LS(): return input().split()
def S(): return list(input())
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
mod = 1000000007

#A
"""
s = input().split("/")
if int(s[0]) > 2019:
    print("TBD")
elif int(s[0]) == 2019:
    if int(s[1]) > 4:
        print("TBD")
    elif int(s[1]) == 4:
        if int(s[2]) > 30:
            print("TBD")
        else:
            print("Heisei")
    else:
        print("Heisei")
else:
    print("Heisei")
"""

#B
n = I()
ans = 0
for i in range(n):
    x,u = input().split()
    x = float(x)
    if u == "JPY":
        ans += x
    else:
        ans += x*380000.0
print(ans)
#C
"""
n,a,b,c = LI()
l = IR(n)
f = [True for i in range(3)]
ans = 0
for i in range(n):
    for d in range(3):
        if abs(l[i]-[a,b,c][d]) <= 10 and f[d]:
            ans += abs(l[i]-[a,b,c][d])
            f[d] = False
            l[i] = -float("inf")
k = False
for i in f:
    if i:
        k = True
        break
if not k:
    print(ans)
    quit()
"""
#D
"""
a,b,q = LI()
s = IR(a)
t = IR(b)
for i in range(q):
    x = I()
    c = bisect.bisect_left(s,x)
    ans = float("inf")
    k = abs(x-s[c-1])
    y = s[c-1]
    d = bisect.bisect_left(t,y)
    ans = min(ans,k+abs(y-t[d-1]))
    if d < b:
        ans = min(ans,k+abs(y-t[d-1]),min(abs(x-s[c-1]),abs(t[d]-x))+abs(t[d]-s[c-1]))
    ans = min(k,ans)
    if c < a:
        k = abs(x-s[c])
        y = s[c]
        d = bisect.bisect_left(t,y)
        if d == b:
            if t[-1] < x:
                k = min(s[c]-x,x-t[d-1])+s[c]-t[d-1]
        else:
            if abs(y-t[d-1]) < abs(y-t[d]):
                if t[d-1] < x:
                    k = min(s[c]-x,x-t[d-1])+s[c]-t[d-1]
            else:
                k += abs(y-t[d])
        ans = min(k,ans)
    print(ans)
"""
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
