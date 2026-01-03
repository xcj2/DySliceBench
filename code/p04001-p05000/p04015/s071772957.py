import sys
import math
import copy
from heapq import heappush, heappop, heapify
from functools import cmp_to_key
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter
sys.setrecursionlimit(1000000)

# input aliases
input = sys.stdin.readline
getS = lambda: input().strip()
getN = lambda: int(input())
getList = lambda: list(map(int, input().split()))
getZList = lambda: [int(x) - 1 for x in input().split()]

INF = float("inf")
MOD = 10**9 + 7
divide = lambda x: pow(x, MOD-2, MOD)

def search(arr):
    ret = [0] * 3000
    ret[0] = 1
    for num in arr:
        tmp = copy.copy(ret)
        for i in range(2700):
            tmp[i + num] += ret[i]
        ret = tmp
    return ret

def solve():
    n, k = getList()
    nums = getList()
    pos = []
    neg = []
    zero = 0
    for num in nums:
        if num == k:
            zero += 1
        if num < k:
            neg.append(k - num)
        if num > k:
            pos.append(num - k)

    posarr = search(pos)
    negarr = search(neg)

    ans = 0
    for i in range(2800):
        ans += posarr[i] * negarr[i]
    # print(posarr)
    # print(negarr)
    print(ans * pow(2, zero) - 1)

def main():
    n = getN()
    for _ in range(n):
        solve()

    return
if __name__ == "__main__":
    # main()
    solve()





