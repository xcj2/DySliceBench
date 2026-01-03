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
def S(): return list(sys.stdin.readline())[:-1]
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
"""
x,y = LI()
f = [0,1,2,1,3,1,3,1,1,3,1,3,1]
if f[x] == f[y]:
    print("Yes")
else:
    print("No")
"""
#B
"""
h,w = LI()
a = SR(h)
print("#"*(w+2))
for i in range(h):
    print("#",end = "")
    for j in a[i]:
        print(j,end = "")
    print("#")
print("#"*(w+2))
"""
#C
"""
h,w = LI()
ans = float("inf")
x = w//2
y = h//2
if not w%2:
    for i in range(1,h):
        if (h-i)%2 == 0:
            ans = min(ans,abs(w*i-w*(h-i)//2))
        ans = min(ans,abs(w*i-x*(h-i)))
else:
    for i in range(1,h):
        if (h-i)%2 == 0:
            ans = min(ans,abs(w*i-w*(h-i)//2))
        if w*i < x*(h-i):
            ans = min(ans,abs(w*i-(x+1)*(h-i)))
        elif w*i < (x+1)*(h-i):
            ans = min(ans,h-i)
        else:
            ans = min(ans,abs(w*i-x*(h-i)))
if not h%2:
    for i in range(1,w):
        if (w-i)%2 == 0:
            ans = min(ans,abs(h*i-h*(w-i)//2))
        ans = min(ans,abs(h*i-y*(w-i)))
else:
    for i in range(1,w):
        if (w-i)%2 == 0:
            ans = min(ans,abs(h*i-h*(w-i)//2))
        if h*i < y*(w-i):
            ans = min(ans,abs(h*i-(y+1)*(w-i)))
        elif h*i < (y+1)*(w-i):
            ans = min(ans,w-i)
        else:
            ans = min(ans,abs(h*i-y*(w-i)))
print(ans)
"""

#D
n = I()
a = LI()
q = []
s = 0
for i in range(n):
    heappush(q,a[i])
    s += a[i]
fl = [s]

for i in range(n,2*n):
    heappush(q,a[i])
    s -= heappop(q)
    s += a[i]
    fl.append(s)
q = []
s = 0
for i in range(2*n,3*n)[::-1]:
    heappush(q,-a[i])
    s += a[i]
fr = [s]

for i in range(n,2*n)[::-1]:
    heappush(q,-a[i])
    s += heappop(q)
    s += a[i]
    fr.append(s)
print(max(list(map(lambda x: x[0]-x[1], zip(fl,fr[::-1])))))
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
