#!usr/bin/env python3
from collections import defaultdict
from collections import deque
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
"""
a,b,c,d,e,f = LI()
a *= 100
b *= 100
ans = [a,0]
for i in range(f//a+1):
    for j in range((f-a*i)//b+1):
        for k in range((f-a*i-b*j)//c+1):
            for l in range((f-a*i-b*j-c*k)//d+1):
                if i or j or k or l:
                    s = c*k+d*l
                    w = a*i+b*j
                    q = w*e//100
                    if s <= q:
                        if w+s <= f:
                            if ans[1]/ans[0] < s/(s+w):
                                ans = [w+s,s]
print(*ans)
"""

#D
n = I()
a = LIR(n)
d = [[a[i][j] for i in range(n)] for j in range(n)]
l = [[1 for j in range(n)] for i in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if d[i][j] >= d[i][k]+d[k][j]:
                d[i][j] = d[i][k]+d[k][j]
                l[i][j] = l[i][k]+l[k][j]

if a != d:
    print(-1)
    quit()
ans = 0
for i in range(n):
    for j in range(n):
        if l[i][j] == 4:
            ans += d[i][j]
ans //= 2
print(ans)
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
