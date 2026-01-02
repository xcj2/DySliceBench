import sys
import math
import copy
import random
import itertools
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

dic = dict()

def zalg(s):
    n = len(s)
    ret = [0] * n
    ret[0] = n
    i, j = 1, 0
    while i < n:
        while i + j < n and s[j] == s[i+j]:
            j += 1
        ret[i] = j

        if j == 0:
            i += 1
            continue

        k = 1
        while k < j and k + ret[k] < j:
            ret[i + k] = ret[k]
            k += 1

        i += k
        j -= k

    return ret

def solve(n=None, s1=None, s2=None):
    n = getN()
    s = list(getS())
    ans = 0
    for i in range(n):
        ps = s[i:]
        z = zalg(ps)
        for i, zz in enumerate(z):
            if i >= zz:
                ans = max(ans, zz)
    print(ans)

def main():
    n = getN()
    for _ in range(n):
        solve()
    return


if __name__ == "__main__":
    # main()
    solve()

