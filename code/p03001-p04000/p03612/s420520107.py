from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
import math
import bisect
import random
import sys


def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LIM(): return list(map(lambda x:int(x) - 1, sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def LIRM(n): return [LIM() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
mod = 1000000007


n = I()
nums = LI()
cnt = 0
ans = 0
for i in range(n):
    if nums[i] == i + 1:
        cnt += 1
    else:
        if cnt:
            ans += (cnt + 1) // 2
        cnt = 0
if cnt:
    ans += (cnt + 1) // 2



print(ans)


