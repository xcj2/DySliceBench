from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
from decimal import *
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, gcd
from operator import mul
from functools import reduce
from operator import mul
from pprint import pprint



sys.setrecursionlimit(2147483647)
INF = 10 ** 20
def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
def I(): return int(sys.stdin.readline())
def FI(): return float(sys.stdin.readline())
def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()
def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 1000000007


n = I()
D = defaultdict(lambda:defaultdict(int))
for j in range(n):
    a = input()
    r = len(a) - a.find(".") - 1 if "." in a else 0
    a = a.replace(".", "")
    cnt1 = -r
    cnt2 = -r
    a = int(a)
    while a % 2 == 0:
        a //= 2
        cnt1 += 1
    while a % 5 == 0:
        a //= 5
        cnt2 += 1
    D[cnt1][cnt2] += 1

ans = 0
for i in range(-20, 30):
    for k in range(-10, 15):
        for j in range(-20, 30):
            for l in range(-10, 15):
                if i + j >= 0 and k + l >= 0:
                    if i == j and k == l:
                        ans += D[i][k] * (D[j][l] - 1)
                    else:
                        ans += D[i][k] * D[j][l]

print(ans // 2)
