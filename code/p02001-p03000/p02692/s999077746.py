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


n, a, b, c = LI()
ans = []
D = {'A':a, 'B':b, 'C':c}
sx = SR(n)
for i in range(n):
    s = sx[i]
    s1 = s[0]
    s2 = s[1]
    if D[s1] == D[s2] == 0:
        print('No')
        exit()
    elif D[s[0]] == D[s[1]] == 1 and i + 1 < n:
        if s1 in sx[i + 1]:
            D[s1] += 1
            D[s2] -= 1
            ans += [s1]
        else:
            D[s2] += 1
            D[s1] -= 1
            ans += [s2]
    else:
        if D[s1] > D[s2]:
            ans += [s2]
            D[s1] -= 1
            D[s2] += 1
        else:
            ans += [s1]
            D[s1] += 1
            D[s2] -= 1

print('Yes')
print(*ans, sep='\n')