#!usr/bin/env python3
from collections import defaultdict
from heapq import heappush, heappop
import sys
import math
import bisect
import random
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS(): return list(map(list, sys.stdin.readline().split()))
def S(): return list(sys.stdin.readline())[:-1]
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
mod = 1000000007


#A
def check(n):
    n = list(map(int,list(str(n))))
    s = 0
    for i in n:
        s += f[i]
    return s == 0
n,k = LI()
d = LI()
f = [0 for i in range(10)]
for i in d:
    f[i] = 1
while 1:
    if check(n):
        print(n)
        quit()
    n += 1
#B

#C

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
