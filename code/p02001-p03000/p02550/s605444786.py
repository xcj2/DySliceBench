from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from math import gcd
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, gcd
from operator import mul
from functools import reduce


sys.setrecursionlimit(2147483647)
INF = 10 ** 13
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().rstrip().split()
def S(): return sys.stdin.readline().rstrip()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]

mod=10**9+7

n,x,m=LI()
s={x%m:(1,x%m)}
L=[x%m]
now=x%m
cycle=1
ret=x%m
diff=0
pre=0
for i in range(2,m+2):
    now=pow(now,2,m)
    ret += now
    if now in s:
        pre, pre_ret = s[now]
        cycle=i-pre
        diff=ret-pre_ret
        break
    s[now]=(i,ret)


ans=diff*((n-pre)//cycle)+pre_ret
for k in range((n-pre)%cycle):
    now = pow(now, 2, m)
    ans+=now

print(ans)






