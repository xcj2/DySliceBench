import math
from math import gcd,pi,sqrt
INF = float("inf")
MOD = 10**9 + 7

import sys
sys.setrecursionlimit(10**6)
import itertools
import bisect
from collections import Counter,deque
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_row(N): return [i_input() for _ in range(N)]
def i_row_list(N): return [i_list() for _ in range(N)]
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
def s_row(N): return [s_input for _ in range(N)]
def s_row_str(N): return [s_list() for _ in range(N)]
def s_row_list(N): return [list(s_input()) for _ in range(N)]


def main():
    n,m = i_map()
    a = set([i_input() for i in range(m)])

    dp = [INF] * (n+1)

    dp[0] = 1
    if 1 not in a:
        dp[1] = 1
    else:
        dp[1] = 0

    for i in range(2,n+1):
        if i  not in a:
            dp[i] = dp[i-1] + dp[i-2]
        else:
            dp[i] = 0
    print(dp[n]%MOD)




if __name__=="__main__":
    main()
