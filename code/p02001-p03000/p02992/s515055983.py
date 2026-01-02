import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
from collections import deque, Counter, defaultdict
def getN():
    return int(input())
def getList():
    return list(map(int, input().split()))
import math
import copy
import bisect
MOD = 10**9 + 7
from logging import getLogger, StreamHandler, DEBUG, WARNING
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
# handler.setLevel(WARNING)
# logger.setLevel(WARNING)
logger.addHandler(handler)
def main():
    n,k = getList()

    # =================約数列挙=================
    divisors = []
    tmp_div = n + 1
    for i in range(1, int(math.sqrt(n)) + 3):
        if tmp_div * i > n:
            other = n // i
            if i > other:
                break
            elif i == other:
                divisors.append(i)
                break
            else:
                divisors.append(i)
                divisors.append(other)

    divisors.sort()
    n_div = len(divisors)
    # =================約数列挙=================

    # =================dp[0]の作成=============
    diff = [divisors[0]]
    for i, j in zip(divisors, divisors[1:]):
        diff.append(j - i)
    dp = copy.copy(diff)
    # print(dp)
    # =================dp[0]の作成=============

    for iteration in range(k-1):
        dp_copy = []
        tmp = sum(dp) % MOD
        dp_copy.append((tmp * diff[0]) % MOD)
        for cid, dp_content in enumerate(range(n_div - 1)):
            tmp -= dp[n_div - dp_content - 1]
            dp_copy.append((tmp * diff[cid+1]) % MOD)

        dp = copy.copy(dp_copy)

        # print(dp)
    print(sum(dp) % MOD)
    # print(acc)
    # print(n_div)
if __name__ == "__main__":
    main()