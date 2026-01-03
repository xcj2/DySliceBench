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
    n,a = i_map()
    x = i_list()
    x.insert(0,0)

    dp = [[[0]*(n*a+1) for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0][0] = 1

    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n*a + 1):
                dp[i][j][k] = dp[i - 1][j][k]
                if k >= x[i]:
                    dp[i][j][k] += dp[i - 1][j - 1][k - x[i]]

    ans = 0
    for j in range(1, n+1):
        ans += dp[n][j][a*j]
    print(ans)

  

if __name__=="__main__":
    main()

    