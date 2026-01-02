def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))

from collections import defaultdict, deque
from sys import exit
import math
import copy
from bisect import bisect_left

import sys
# sys.setrecursionlimit(1000000)
INF = 10 ** 17
MOD = 998244353

def main():
    n,m,kk = getList()

    k = m - 1
    ans = 0
    nck = 1
    rui = m
    for itr in range(1, n+1):
        if n - itr <= kk:
            # print(nck, rui)
            ans += (rui*nck) % MOD
            ans %= MOD
            # print(nck, n, itr)
        nck *= (n - itr)
        nck *= pow(itr, MOD-2, MOD)
        nck %= MOD
        rui *= k
        rui %= MOD
        # print(nck, rui)
    print(ans)


if __name__ == "__main__":
    main()

