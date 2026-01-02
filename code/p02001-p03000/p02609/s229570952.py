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
mod = 10 ** 9 + 7

n = I()
x = input()
cnt = x.count("1")
if cnt == 1:
    for i in range(n):
        if x[i] == "1":
            print(0)
        elif i == n - 1:
            print(2)
        else:
            print(1)
    exit()

def f(x):
  if x==0:
    return 0
  return 1+f(x%bin(x).count('1'))

xx = int(x, 2)
Y = xx % (cnt + 1)
Z = xx % (cnt - 1)
for i in range(n):
    if x[i] == '1':
        print(1 + f((Z - pow(2, n - i - 1, cnt - 1)) % (cnt - 1)))
    else:
        print(1 + f((Y + pow(2, n - i - 1, cnt + 1)) % (cnt + 1)))