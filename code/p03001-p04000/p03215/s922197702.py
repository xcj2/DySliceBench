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

class BIT():
    # A1 ... AnのBIT(1-indexed)
    def __init__(self, n):
        self.n = n
        self.BIT = [0] * (n + 2)

    # A1 ~ Aiまでの和 O(logN)
    def query(self, idx):
        res_sum = 0
        while idx > 0:
            res_sum += self.BIT[idx]
            idx -= idx & (-idx)
        return res_sum

    # Ai += x O(logN)
    def update(self, idx, x):
        # print(idx)
        while idx <= self.n:
            # print(idx)
            self.BIT[idx] += x
            idx += idx & (-idx)
        return

    def show(self):
        print(self.BIT)


def solve():
    n, k = getList()
    lis = [0] + getList()
    for i in range(n):
        lis[i+1] += lis[i]

    ka = []
    for i in range(n):
        for j in range(i+1, n+1):
            ka.append(lis[j]-lis[i])

    ans = 0
    for rui in range(50, -1, -1):
        ok = []
        tgt = pow(2, rui)
        for kaka in ka:
            if kaka & tgt == tgt:
                ok.append(kaka)
        if len(ok) >= k:
            ans += tgt
            ka = ok

    print(ans)





def main():
    n = getN()
    for _ in range(n):
        solve()

    return
if __name__ == "__main__":
    # main()
    solve()