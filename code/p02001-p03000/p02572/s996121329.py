
import collections
from functools import lru_cache
import bisect

INF = float("inf")
ZERO = 0
ONE = 1


def read():
    return input().strip()


def readInt():
    return int(input().strip())


def readList():
    return list(map(int, input().strip().split()))


def solve(N, arr):
    ans = 0
    MOD = 10**9 + 7
    prefixSums = [0]

    for num in arr:
        prefixSums.append(prefixSums[-1] + num)

    for i, num in enumerate(arr):
        ans = (ans + num * (prefixSums[-1] - prefixSums[i+1])) % MOD

    return ans % MOD


N = readInt()
arr = readList()

print(solve(N, arr))
