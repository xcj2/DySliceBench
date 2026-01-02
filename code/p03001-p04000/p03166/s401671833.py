from collections import Counter
from collections import defaultdict
import math
import random
import heapq as hq
from math import sqrt
import sys
from functools import reduce

sys.setrecursionlimit(10000000)
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

def dfs(i):
    visited[i] = True
    for node in g[i]:
        if not visited[node]:
            dfs(node)
        dp[i] = max(dp[i], 1+ dp[node])



if __name__ == "__main__":
    n, m = rinput()
    g = defaultdict(list)
    for i in range(m):
        x, y = rinput()
        g[x].append(y)
    dp = [0]*(n+1)
    visited = [False]*(n+1)
    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
            # print('-=============================')
    # print(dp)
    print(max(dp))


# 5 3
# 2 3
# 2 4
# 5 2
# 5 1
# 1 4
# 4 3
# 1 3