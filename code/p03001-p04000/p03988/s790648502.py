import sys
import math
import copy
from heapq import heappush, heappop, heapify
from functools import cmp_to_key
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter
# sys.setrecursionlimit(1000000)

# input aliases
input = sys.stdin.readline
getS = lambda: input().strip()
getN = lambda: int(input())
getList = lambda: list(map(int, input().split()))
getZList = lambda: [int(x) - 1 for x in input().split()]

INF = float("inf")
MOD = 10**9 + 7
divide = lambda x: pow(x, MOD-2, MOD)

def pim():
    print("Impossible")
    sys.exit()
def pp():
    print("Possible")
    sys.exit()
def solve():
    n = getN()
    nums = getList()
    cnt = Counter(nums)
    mx = max(nums)
    mn = min(nums)

    if cnt[mx] < 2:
        pim()
    if mn < (mx + 1) // 2:
        pim()

    if mx % 2 == 0:
        if cnt[mx//2] != 1:
            pim()
    else:
        if cnt[(mx+1) // 2] != 2:
            pim()

    for i in range((mx + 1) // 2 + 1, mx+1):
        if cnt[i] < 2:
            pim()

    pp()


def main():
    n = getN()
    for _ in range(n):
        solve()

    return
if __name__ == "__main__":
    # main()
    solve()





