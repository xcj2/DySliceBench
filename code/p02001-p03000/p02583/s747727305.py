
import collections
from functools import lru_cache


def read():
    return input().strip()


def readInt():
    return int(input().strip())


def readList():
    return list(map(int, input().strip().split()))


def solve(N, arr):
    arr.sort()
    ans = 0

    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                a, b, c = arr[i], arr[j], arr[k]

                if len(set([a, b, c])) == 3 and a+b > c:
                    ans += 1

    return ans


N = readInt()
arr = readList()

print(solve(N, arr))
