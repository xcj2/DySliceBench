from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
from bisect import bisect_left, bisect_right
import random
from itertools import permutations, accumulate, combinations
import sys
import string
from copy import deepcopy

INF = float('inf')


def LI(): return list(map(int, sys.stdin.readline().split()))


def I(): return int(sys.stdin.readline())


def LS(): return sys.stdin.readline().split()


def S(): return sys.stdin.readline().strip()


def IR(n): return [I() for i in range(n)]


def LIR(n): return [LI() for i in range(n)]


def SR(n): return [S() for i in range(n)]


def LSR(n): return [LS() for i in range(n)]


def SRL(n): return [list(S()) for i in range(n)]


def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]


mod = 10 ** 9 + 7

h,w,m= LI()
s=set()
D1=defaultdict(int)
D2=defaultdict(int)
for _ in range(m):
    h,w=LI()
    D1[h-1]+=1
    D2[w-1]+=1
    s.add((h-1,w-1))

A=[[v,i] for i,v in D1.items()]+[[-INF,-INF]]
B=[[v,i] for i,v in D2.items()]+[[-INF,-INF]]
A.sort(reverse=True)
B.sort(reverse=True)
a_now=0
b_now=0
ans=-INF
for i in range(3*10**5):
    av,ak=A[a_now]
    bv,bk = B[b_now]
    res=av+bv-int((ak,bk) in s)
    ans=max(ans,res)
    if a_now==len(A)-2 and b_now==len(B)-2:
        break
    elif A[a_now+1][0]+B[b_now][0]>A[a_now][0]+B[b_now+1][0]:
        a_now+=1
    else:
        b_now+=1

print(ans)




