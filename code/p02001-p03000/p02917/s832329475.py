import sys
from collections import defaultdict, deque
import math

# import copy
# from bisect import bisect_left, bisect_right
# import heapq

# sys.setrecursionlimit(1000000)

# input aliases
input = sys.stdin.readline

getS = lambda: input().strip()
getN = lambda: int(input())
getList = lambda: list(map(int, input().split()))
getZList = lambda: [int(x) - 1 for x in input().split()]

INF = 10 ** 20
MOD = 10**9 + 7

def divide(k):
    return pow(k, MOD-2, MOD)


def make_nck(n):
    ret = [1]
    for i in range(1, n+1):
        ret.append((ret[-1] * (n + 1 - i) * divide(i)) % MOD)

    # print(ret)
    return ret

def make_nigojyo(n):
    ret = [1]

    for i in range(1, n+1):
        ret.append((ret[-1] * 25) % MOD)

    # print(ret)
    return ret


def solve():
    n = getN()
    a = getList()
    ans = 0
    for i, j in zip(a, a[1:]):
        ans += min(i, j)
    ans += a[0] + a[-1]

    print(ans)



def main():
    n = getN()
    for _ in range(n):
        solve()


if __name__ == "__main__":
    # main()
    solve()