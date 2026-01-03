from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor
from operator import mul
from functools import reduce


sys.setrecursionlimit(2147483647)
INF = 10 ** 13
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
mod = 1000000007


def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in [0]*(n-1)]
    g = [set() for _ in [0]*n]
    [g[a-1].add(b-1) for a, b in ab]
    [g[b-1].add(a-1) for a, b in ab]
    only = []
    sign = [False]*n
    for i in range(n):
        if len(g[i]) == 1:
            only.append(i)
    while only:
        i = only.pop()
        if not g[i]:
            print("Second")
            return
        j = g[i].pop()
        g[j].remove(i)
        if sign[i] and not g[j]:
            print("First")
            return
        if not sign[i] and sign[j]:
            print("First")
            return
        if not sign[j] and not sign[i]:
            sign[j] = True
        if len(g[j]) == 1:
            only.append(j)


main()
