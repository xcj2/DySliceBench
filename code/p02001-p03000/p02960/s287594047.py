import math
from math import gcd,pi,sqrt
INF = float("inf")
MOD = 10**9 + 7

import sys
sys.setrecursionlimit(10**6)
import itertools
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
    s = input()
    n = len(s)
    dp = [[0]*13 for i in range(n+1)]
    dp[0][0] = 1

    for i,s in enumerate(s[::-1],start = 1):
        p10 = pow(10,i-1,13)
        if s!= "?":
            for k in range(13):
                dp[i][(int(s)*p10 + k)%13] += dp[i-1][k]
                dp[i][(int(s)*p10 + k)%13] %= MOD
        else:
            for j in range(10):
                for k in range(13):
                    dp[i][(j*p10 + k)%13] += dp[i-1][k]
                    dp[i][(j*p10 + k)%13] %= MOD
    print(dp[n][5] % MOD)


if __name__=="__main__":
    main()
