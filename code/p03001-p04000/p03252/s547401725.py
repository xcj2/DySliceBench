from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
from bisect import bisect_left, bisect_right
import random
from itertools import permutations, accumulate, combinations
import sys
import string



INF = float('inf')
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
mod = 10 ** 9 + 7



s = S()
t = S()
s_dict = defaultdict(int)
t_dict = defaultdict(int)
for i in range(len(s)):
    if s_dict[s[i]] and s_dict[s[i]] != t[i]:
        print('No')
        break
    else:
        s_dict[s[i]] = t[i]
    if t_dict[t[i]] and t_dict[t[i]] != s[i]:
        print('No')
        break
    else:
        t_dict[t[i]] = s[i]
else:
    print('Yes')




