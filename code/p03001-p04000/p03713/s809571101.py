#!usr/bin/env python3
from collections import defaultdict
from heapq import heappush, heappop
import sys
import math
import bisect
import random
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS():return list(map(list, sys.stdin.readline().split()))
def S(): return list(sys.stdin.readline())[:-1]
def IR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = I()
    return l
def LIR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = LI()
    return l
def SR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = S()
    return l
def LSR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = SR()
    return l
mod = 1000000007

#A

#B

#C
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
