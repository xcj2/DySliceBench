from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations
import sys
import string


INF = float('inf')
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LIM(): return list(map(lambda x:int(x) - 1, sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def LIRM(n): return [LIM() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
mod = 1000000007


s = S()
k = I()
L = []
cnt = 0
ret = 1
if len(s) == 1:
    print(k // 2)
else:
    for j in range(len(s) - 1):
        if s[j] != s[0]:
            break

    for l in range(len(s) - 1):
        if s[-1] != s[-1 - l]:
            break


    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            ret += 1
        else:
            if ret > 1:
                cnt += ret // 2
            ret = 1


    cnt += ret // 2


    ans = cnt * k
    if len(set(s)) == 1 and k % 2:
        ans = k * len(s) // 2
    elif s[0] == s[-1] and j % 2 and l % 2:
        ans += k - 1
    print(ans)