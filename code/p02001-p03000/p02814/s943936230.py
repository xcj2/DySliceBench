from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_right, bisect_left
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from copy import deepcopy
from math import factorial, ceil, floor, gamma, log
from operator import mul
from functools import reduce



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
mod = 10 ** 9 + 7


n, m = LI()
A = LI()

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

for i in range(n):
    A[i] //= 2
    if i == 0:
        ret = A[i]
        c0 = 0
        a0 = A[0]
        while a0 % 2 == 0:
            a0 //= 2
            c0 += 1
    else:
        ret = lcm(ret, A[i])
        if ret > m:
            print(0)
            exit()
        c = 0
        while A[i] % 2 == 0:
            A[i] //= 2
            c += 1
        if c != c0:
            print(0)
            exit()


print((m // ret + 1) // 2)