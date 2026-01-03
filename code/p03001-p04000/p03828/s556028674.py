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


# primeFactorDecomposition(12): {2: 2, 3: 1}
def prime_factor_decomposition(n):
    import math
    m = defaultdict(int)
    while n > 1:
        find_factor = False
        for i in range(2, int(math.sqrt(n)) + 1):

            if n % i == 0:
                m[i] += 1
                n //= i
                find_factor = True
                break

        if not find_factor:
            m[n] += 1
            break

    return m


def main():
    N = int(input())
    MOD = 10 ** 9 + 7

    d = defaultdict(int)
    for x in range(1, N + 1):
        p = prime_factor_decomposition(x)
        for k, v in p.items():
            d[k] += v

    ans = 1
    for k, v in d.items():
        ans *= (v + 1)
        ans %= MOD
    print(ans % MOD)


if __name__ == '__main__':
    main()
