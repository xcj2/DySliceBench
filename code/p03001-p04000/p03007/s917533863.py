from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_right, bisect_left
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, gamma, log
from operator import mul
from functools import reduce
from copy import deepcopy

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
mod = 10 ** 9 + 7


n = I()
A = LI()
if all([a > 0 for a in A]):
    now = min(A)
    print(sum(A) - now * 2)
    A.remove(now)
    last = A.pop()
    while A:
        nxt = A.pop()
        print(now, nxt)
        now -= nxt
    print(last, now)
elif all([a < 0 for a in A]):
    now = max(A)
    print(-sum(A) + now * 2)
    A.remove(now)
    while A:
        nxt = A.pop()
        print(now, nxt)
        now -= nxt
else:
    print(sum([abs(i) for i in A]))
    minus = []
    plus = []
    for a in A:
        if a > 0:
            plus += [a]
        elif a < 0:
            minus += [a]
        else:
            if not plus:
                plus += [a]
            else:
                minus += [a]
    minus_now = minus.pop()
    plus_now = plus.pop()
    while plus:
        nxt = plus.pop()
        print(minus_now, nxt)
        minus_now -= nxt
    while minus:
        nxt = minus.pop()
        print(plus_now, nxt)
        plus_now -= nxt
    print(plus_now, minus_now)
