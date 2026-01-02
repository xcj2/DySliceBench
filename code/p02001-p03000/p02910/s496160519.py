from collections import defaultdict, deque, Counter
from heapq import heappush, heappop
from itertools import permutations, accumulate, combinations, combinations_with_replacement
from math import sqrt, ceil, floor, factorial
from bisect import bisect_left, bisect_right
from copy import deepcopy
from operator import itemgetter
from functools import reduce
#from fractions import gcd
#from math import gcd
import sys
def I(): return int(input())
def Is(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def TI(): return tuple(map(int, input().split()))
def IR(n): return [I() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def TIR(n): return [TI() for _ in range(n)]
def S(): return input()
def Ss(): return input().split()
def LS(): return list(input())
def SR(n): return [S() for _ in range(n)]
def SsR(n): return [Ss() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
sys.setrecursionlimit(10**6)
MOD = 10**9+7
INF = float('inf')


s = S()
n = len(s)

for i in range(n):
    if i % 2 == 0 and not s[i] in "RUD":
        print("No")
        exit()
    elif i % 2 == 1 and not s[i] in "LUD":
        print("No")
        exit()

print("Yes")