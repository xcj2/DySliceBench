
import collections
from functools import lru_cache


def read():
    return input().strip()


def readInt():
    return int(input().strip())


def readList():
    return list(map(int, input().strip().split()))


def solve(N, arr):
    l = 0
    r = N-1

    ans = 0

    while l < r:
        while l < r and arr[l] != "W":
            l += 1

        while l < r and arr[r] != "R":
            r -= 1

        if l < r:
            ans += 1
            l += 1
            r -= 1

    return ans


N = readInt()
arr = [ch for ch in read()]

print(solve(N, arr))
