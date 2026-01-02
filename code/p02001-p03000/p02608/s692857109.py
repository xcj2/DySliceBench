
import collections
from functools import lru_cache

from math import sqrt


def read():
    return input().strip()


def readInt():
    return int(input().strip())


def readList():
    return list(map(int, input().strip().split()))


def solve(n):
    f = [0 for _ in range(n+1)]

    for x in range(1, int(sqrt(n) + 1)):
        for y in range(1, int(sqrt(n) + 1)):
            for z in range(1, int(sqrt(n) + 1)):
                s = x**2 + y**2 + z**2 + x*y + y*z + z*x

                if 0 <= s <= n:
                    f[s] += 1

    return "\n".join(map(str, f[1:]))


n = readInt()
print(solve(n))
