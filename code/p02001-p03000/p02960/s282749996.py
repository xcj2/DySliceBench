from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate
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
def SRL(n): return [list(S()) for i in range(n)]
mod = 1000000007


def main():
    s = S().strip()
    dp = [0] * 13
    dp[0] = 1
    trans_list = [i * 10 % 13 for i in range(13)]
    for i in s:
        nxt_dp = [0] * 13
        for j in range(13):
            if i == '?':
                for k in range(10):
                    nxt_dp[(trans_list[j] + k) % 13] += dp[j]
                    nxt_dp[(trans_list[j] + k) % 13] %= mod
            else:
                nxt_dp[(trans_list[j] + int(i)) % 13] += dp[j]
                nxt_dp[(trans_list[j] + int(i)) % 13] %= mod
        dp = nxt_dp

    return dp[5]


print(main())