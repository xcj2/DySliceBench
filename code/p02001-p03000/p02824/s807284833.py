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

def judge(n, m, v, p, nums, idx):
    if idx >= n - p:
        return True
    cur = nums[idx] + m
    cnt = 0
    for i in range(0, n):
        if idx == i:
            continue
        if i > n - p:
            break
        comp = nums[i]
        if comp > cur:
            return False
        cnt += min(m, cur - comp)
    # print(idx, cnt)
    if cnt >= m * (v - p):
        return True
    else:
        return False


def solve():
    n, m, v, p = getList()
    nums = getList()
    nums.sort()
    mn = 0
    mx = n-1
    while(mx - mn > 1):
        mid = (mx + mn) // 2
        if judge(n, m, v, p, nums, mid):
            mx = mid
        else:
            mn = mid

    if judge(n, m, v, p, nums, mn):
        ans = mn
    else:
        ans = mx
    # print(nums)
    # print(ans)
    print(n - ans )

def main():
    n = getN()
    for _ in range(n):
        solve()

    return
if __name__ == "__main__":
    # main()
    solve()





