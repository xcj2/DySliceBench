from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
from pprint import pprint
from copy import deepcopy
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor
from operator import mul
from functools import reduce
from pprint import pprint


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
mod = 1000000007


def gcd(i, j):
    while j:
        i, j = j, i % j
    return i


n, a_ratio, b_ratio = LI()
solution = LIR(n)
dp = {(0, 0): 0}
for a, b, c in solution:
    for (ai, bi), ci in list(dp.items()):
        # listにしないとduring iteration dictionary changeみたいなerrorでる。
        # メモ：defaultdictはもともと存在しないkeyを参照するだけでkey:valueが追加される。
        # これによって、key: INFが追加されるのはまずい。だからgetで
        dp[(ai + a, bi + b)] = min(dp.get((ai + a, bi + b), INF), ci + c)


ans = INF
for i in range(1, max(400 // a_ratio, 400 // b_ratio)):
    ans = min(ans, dp.get((a_ratio * i, b_ratio * i), INF))

print(ans if ans != INF else -1)



