from collections import defaultdict
from heapq import heappush, heappop
import math
import bisect
import random

def LI(): return list(map(int, input().split()))
def I(): return int(input())
def LIM(): return list(map(lambda x:int(x) - 1, input().split()))
def LS(): return input().split()
def S(): return input()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def LIRM(n): return [LIM() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
mod = 1000000007


n = I()

for i in range(n):
    for j in range(i + 1, n):
        k = 0
        while (i ^ j) & (1 << k) == 0:
            k += 1
        print(k + 1, end = ' ')
    print('')