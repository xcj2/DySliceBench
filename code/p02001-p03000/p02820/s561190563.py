from collections import defaultdict, deque, Counter
from heapq import heappush, heappop
from itertools import permutations, accumulate
from math import sqrt, ceil, floor, factorial
from bisect import bisect_left, bisect_right
from copy import deepcopy
from operator import itemgetter
from functools import reduce
#from fractions import gcd
#from math import gcd
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

n, k = Is()
r, s, p = Is()
t = S()
flag = [False]*n
ans = 0
for i in range(n):
    if i >= k and t[i-k] == t[i] and not flag[i-k]:
        flag[i] = True
        continue
    if t[i] == 'r':
        ans += p
    elif t[i] == 's':
        ans += r
    else:
        ans += s

print(ans)