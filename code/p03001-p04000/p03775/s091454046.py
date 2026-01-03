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
n = I()
ans = int(math.log10(n)+1)
for i in range(2,int(n**0.5)+1):
    if n%i == 0:
        ans = min(ans, max(int(math.log10(i)+1),int(math.log10(n//i)+1)))
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
