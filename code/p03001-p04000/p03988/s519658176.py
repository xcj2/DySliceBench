from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, acos, asin, atan, sqrt, tan, cos, pi
from operator import mul
from functools import reduce
from pprint import pprint


sys.setrecursionlimit(10 ** 7)
INF = 10 ** 20
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
mod = 998244353


n = I()
A = LI()
D = Counter(A)
min_a = min(A)
max_a = min_a * 2 if D[min_a] == 1 else min_a * 2 - 1
if D[min_a] > 2:
    print("Impossible")
    exit()
flg = 0
for i in range(min_a + 1, max_a + 1):
    if D[i] < 2:
        print("Impossible")
        exit()
    D[i] -= 2

for k in D.keys():
    if k > max_a:
        print("Impossible")
        exit()

print("Possible")

















