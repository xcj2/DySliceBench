from collections import defaultdict, Counter
from itertools import product, groupby, count, permutations, combinations
from math import pi, sqrt
from collections import deque
from bisect import bisect, bisect_left, bisect_right
from string import ascii_lowercase
from functools import lru_cache
import sys
sys.setrecursionlimit(10000)
INF = float("inf")
YES, Yes, yes, NO, No, no = "YES", "Yes", "yes", "NO", "No", "no"
dy4, dx4 = [0, 1, 0, -1], [1, 0, -1, 0]
dy8, dx8 = [0, -1, 0, 1, 1, -1, -1, 1], [1, 0, -1, 0, 1, 1, -1, -1]


def inside(y, x, H, W):
    return 0 <= y < H and 0 <= x < W


def ceil(a, b):
    return (a + b - 1) // b


def main():
    N = int(input())
    C = Counter(list(map(int, input().split())))
    MOD = 10 ** 9 + 7

    ans = 1
    num_zero = 0
    for k, v in C.items():
        if k == 0:
            num_zero += 1
        elif v == 2:
            ans *= 2
            ans %= MOD
        else:
            print(0)
            return
    
    if N % 2 != num_zero:
        print(0)
        return

    print(ans)


if __name__ == '__main__':
    main()
