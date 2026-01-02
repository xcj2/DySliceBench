from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate
import sys


def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LIM(): return list(map(lambda x:int(x) - 1, sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def LIRM(n): return [LIM() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
mod = 1000000007


def main():
    n = I()
    monster = LI()
    ret = 0
    ans = sum(monster)
    savor_lim = LI()
    for i in range(n - 1, -1, -1):
        k = min(savor_lim[i], monster[i + 1])
        monster[i + 1] -= k
        savor_lim[i] -= k
        monster[i] -= min(savor_lim[i], monster[i])
    return ans - sum(monster)



print(main())