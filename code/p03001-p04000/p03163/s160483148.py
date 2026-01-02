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
    n, w = rinput()
    w_v = []
    for i in range(n):
        w_v.append(rlinput())
    dp = [[0 for i in range(w+1)]for j in range(n+1)]
    # print(w_v)
    for item in range(1, n+1):
        for weight in range(1, w+1):
            if weight >= w_v[item-1][0]:
                dp[item][weight] = max(dp[item-1][weight-w_v[item-1][0]]+w_v[item-1][1],dp[item-1][weight])
            else:
                dp[item][weight] =dp[item-1][weight]
    print(dp[n][w])
