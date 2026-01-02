from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor


INF = float('inf')
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LIM(): return list(map(lambda x:int(x) - 1, sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def LIRM(n): return [LIM() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
mod = 1000000007



def main():
    flag = True
    L = LIR(3)
    diff_list = [[0] * 3 for _ in range(3)]
    for x in range(3):
        for y in range(3):
            diff_list[y][x] = L[y][x] - L[y - 1][x]


    for i, j, k in diff_list:
        if not i == j == k:
            flag = False


    diff_list = [[0] * 3 for _ in range(3)]
    for y in range(3):
        for x in range(3):
            diff_list[x][y] = L[y][x] - L[y][x - 1]


    for i, j, k in diff_list:
        if not i == j == k:
            flag = False


    if flag:
        return 'Yes'
    else:
        return 'No'


print(main())







