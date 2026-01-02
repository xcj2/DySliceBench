from collections import Counter
from collections import defaultdict
import math
import random
import heapq as hq
from math import sqrt
import sys
from functools import reduce


def input():
    return sys.stdin.readline().strip()


def iinput():
    return int(input())


def tinput():
    return input().split()


def rinput():
    return map(int, tinput())


def rlinput():
    return list(rinput())


mod = int(1e9)+7


def factors(n):
    return set(reduce(list.__add__,
                      ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


# ----------------------------------------------------

if __name__ == "__main__":
    n, weigh = rinput()
    w, v = [], []
    for i in range(n):
        wi, vi = rinput()
        w.append(wi)
        v.append(vi)

    mxv = sum(v)
    dp = [[99999999999 for i in range(mxv+1)]for j in range(n+1)]
    for i in range(n+1):
        dp[i][0]=0
    # print(w_v)
    for item in range(1, n+1):
        for val in range(1, mxv+1):
            if v[item-1] <= val:
                dp[item][val] = min(
                    dp[item-1][val-v[item-1]]+w[item-1], dp[item-1][val])
            else:
                dp[item][val] = dp[item-1][val]
    # print(dp)
    ans=0
    for i in range(mxv+1):
        if dp[n][i]<=weigh:
            ans=i
    print(ans)

