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


sys.setrecursionlimit(2147483647)
INF = 1 << 100
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


n, m = LI()
A = sorted(LI(), reverse=True)
max_num = 10 ** 5 * 2 + 1
D = [0] * max_num
acc = [0] + A
for i in range(1, n):
    acc[i + 1] += acc[i]

for i in A:
    D[i] += 1

for i in range(max_num - 1, 0, -1):
    D[i - 1] += D[i]

ok = 1
ng = max(A) * 2 + 1
while ng > ok + 1:
    mid = (ng + ok) // 2
    ret = 0
    happiness = 0
    for i in range(n):
        d = D[max(mid - A[i], 0)]
        ret += d
    if ret >= m:
        ok = mid
    else:
        ng = mid


ret2 = 0
ans = 0
for i in range(n):
    d2 = D[max(ng - A[i], 0)]
    ret2 += d2
    ans = ans + d2 * A[i] + acc[d2]

ans += (m - ret2) * ok
print(ans)



