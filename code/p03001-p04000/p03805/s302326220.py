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
n,m = LI()
v = LIR(m)
p2 = [1]
for i in range(n):
    p2.append(p2[-1]*2)
dp = [[0 for i in range(p2[n])] for j in range(n)]
dp[0][1] = 1
for i in range(1,p2[n]):
    for k in range(n):
        for a,b in v:
            a -= 1
            b -= 1
            if k==a or k == b:
                c = p2[a]
                d = p2[b]
                if i&c and not i&d:
                    dp[b][i|d] += dp[k][i]
                if (not i&c) and i&d:
                    dp[a][i|c] += dp[k][i]
ans = 0
for i in range(1,n):
    ans += dp[i][-1]
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
