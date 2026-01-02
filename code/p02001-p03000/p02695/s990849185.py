from collections import defaultdict, deque, Counter
from heapq import heappush, heappop
from itertools import permutations, accumulate
from math import sqrt
from bisect import bisect_left, bisect_right
from copy import deepcopy
import sys
def I(): return int(input())  # '123' -> 123
def Is(): return map(int, input().split())  # '123 456' -> 123, 456
def LI(): return list(map(int, input().split()))  # '123 456' -> [123, 456]
def TI(): return tuple(map(int, input().split()))  # '123 456' -> (123, 456)
def IR(n): return [I() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def TIR(n): return [TI() for _ in range(n)]
def S(): return input()
def Ss(): return input().split()  # 'aa bb' -> 'aa','bb' or ['aa','bb']
def LS(): return list(input())  # 'abc123' -> ['a','b','c','1','2','3']
def SR(n): return [S() for _ in range(n)]
def SsR(n): return [Ss() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
sys.setrecursionlimit(1000000)
MOD = 1000000007
INF = float('inf')



N, M, Q = Is()
ABCD = TIR(Q)
ans = -INF

def dfs(A):
    global ans
    if len(A) == N:
        score = 0
        for a, b, c, d in ABCD:
            if A[b - 1] - A[a - 1] == c:
                score += d
        ans = max(ans, score)
    else:
        ret = 0
        amax = max(A) if len(A) != 0 else 1
        for i in range(amax, M+1):
            dfs(A + [i])

dfs([])
print(ans)
