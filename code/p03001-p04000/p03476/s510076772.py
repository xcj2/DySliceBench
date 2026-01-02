import sys
from collections import defaultdict, Counter
from itertools import product, groupby, count, permutations, combinations
from math import pi, sqrt, ceil, floor
from collections import deque
from bisect import bisect, bisect_left, bisect_right
from string import ascii_lowercase
from functools import lru_cache, reduce
from operator import xor
from heapq import heappush, heappop
INF = float("inf")
sys.setrecursionlimit(10**7)

# 4近傍（右, 下, 左, 上）
dy4, dx4 = [0, -1, 0, 1], [1, 0, -1, 0]


def inside(y: int, x: int, H: int, W: int) -> bool: return 0 <= y < H and 0 <= x < W


# nより小さい素数のリストを生成
def make_prime_list(n: int):
    num = [True] * n
    num[0] = num[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if num[i]:
            for j in range(i ** 2, n, i):
                num[j] = False

    return num


class CumulativeSum:
    def __init__(self, l):
        self.dp = [0] * (len(l) + 1)
        for i, v in enumerate(l):
            self.dp[i + 1] = v + self.dp[i]

    # return sum(l[left] + l[left + 1] + ... + l[right])
    def total(self, left, right):
        assert 0 <= left <= right < len(self.dp)
        return self.dp[right + 1] - self.dp[left]


def main():
    Q = int(input())

    prime_list = make_prime_list(10 ** 5 + 5)
    memo = [0] * (10 ** 5 + 5)
    for i in range(10 ** 5 + 1):
        memo[i] = prime_list[i] and prime_list[(i + 1) // 2]

    c = CumulativeSum(memo)
    for _ in range(Q):
        l, r = map(int, input().split())
        print(c.total(l, r))


if __name__ == '__main__':
    main()
