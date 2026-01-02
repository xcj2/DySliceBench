from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, gcd, sqrt
from operator import mul
from functools import reduce
from operator import mul
from pprint import pprint
from copy import deepcopy



sys.setrecursionlimit(2147483647)
INF = 10 ** 20
def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
def I(): return int(sys.stdin.buffer.readline())
def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()
def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 2


n = I()
s = S()
l = len(s)
L = []
one_cnt = 0
for i in range(l - 1):
    ret = abs(int(s[i]) - int(s[i + 1]))
    L += [ret]
    if ret == 1:
        one_cnt += 1

m = 0
for j in range(l - 1):
    m += int(l - 2 & j == j) * L[j]
    m %= 2

if m % 2:
    print(1)
    exit()
else:
    if one_cnt:
        print(0)
    else:
        L = [k // 2 for k in L]
        ret2 = 0
        for jj in range(l - 1):
            ret2 += int(l - 2 & jj == jj) * L[jj]
            ret2 %= 2
        if ret2:
            print(2)
        else:
            print(0)












