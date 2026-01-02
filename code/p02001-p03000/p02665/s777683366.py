from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, cos, radians, pi, sin
from operator import mul
from functools import reduce
from operator import mul

mod = 10 ** 9 + 7
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

n = I()
A = LI()
max_ret = 0
min_ret = 0
max_arr = [0] * (n + 1)
min_arr = [0] * (n + 1)
for i in range(n, -1, -1):
    max_ret = max_ret + A[i]
    min_ret = (min_ret + 1) // 2 + A[i]
    max_arr[i] = max_ret
    min_arr[i] = min_ret

if max_ret >= 1 >= min_ret:
    ans = 1
    ret = 1
    for j in range(1, n + 1):
        ret = min((ret - A[j-1]) * 2, max_arr[j])
        ans += ret
    print(ans)
else:
    print(-1)






