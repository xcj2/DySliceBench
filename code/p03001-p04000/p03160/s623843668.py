
# ########## ------ Import ------- ##########

import sys
import math
from collections import Counter
from collections import deque as deq
from functools import lru_cache

# ########## ------ Define -------- #########

INT_MAX = float("inf")
INT_MIN = float("-inf")

# ########## ------ Input Functions ---- #########

input = sys.stdin.readline


def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))


def insr():
    s = input()
    return(list(s[:len(s) - 1]))


def invr():
    return(map(int, input().split()))


# ########## ------ Code ------- ##########
def go(i):
    if i == 0:
        dp[i] = 0
        return dp[i]
    if i == 1:
        dp[i] = abs(a[0] - a[i])
        return dp[i]

    if dp[i] != -1:
        return dp[i]

    dp[i] = min(abs(a[i] - a[i - 1]) + go(i - 1),
                abs(a[i] - a[i - 2]) + go(i - 2))
    return dp[i]


t = inp()
a = inlt()

if t == 1:
    print(0)
elif t == 2:
    print(abs(a[0] - a[1]))

else:
    dp=[-1]*t
    dp[0] = 0
    dp[1] = abs(a[0] - a[1])
    for i in range(2, t):
        dp[i] = min(abs(a[i] - a[i - 1]) + dp[i - 1],
                    abs(a[i] - a[i - 2]) + dp[i - 2])


    print(dp[t - 1])
