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

h_max = max(D1.values())
w_max = max(D2.values())
A=[i for i,v in D1.items() if v==h_max]
B=[i for i,v in D2.items() if v==w_max]

flg = 1
for i in A:
    for j in B:
        if (i, j) not in s:
            flg = 0
            break

print(w_max+h_max-flg)




