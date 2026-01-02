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
import pprint
sys.setrecursionlimit(10 ** 9)


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


n, p = LI()
D = defaultdict(int)
D[0] += 1
s = S()
ans = 0
rem = 0
if p == 2 or p == 5:
    for i in range(n - 1, -1, -1):
        if int(s[i]) % p == 0:
            ans += i + 1
    print(ans)
    exit()


k = 1
for i in range(n - 1, -1, -1):
    d = int(s[i])
    rem = (k * d + rem) % p
    k = k * 10 % p
    ans += D[rem]
    D[rem] += 1


print(ans)
