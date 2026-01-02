#!/usr/bin/env python3

import math
from functools import lru_cache


def ncr(n, r):
    r = min(r, n - r)
    # 桁が小さいときは直接 math.factorial を使ったほうが早い
    if n + r < 4000:
        return math.factorial(n) // math.factorial(n-r) // math.factorial(r)
    if r == 0:
        return 1
    if r == 1:
        return n
    numerator = list(range(n - r + 1, n + 1))
    denominator = list(range(1, r+1))
    for p in range(2, r + 1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p - 1, r, p):
                numerator[k - offset] //= pivot
                denominator[k] //= pivot
    result = 1
    for k in range(r):
        result *= numerator[k]
    return result


# 穴なしで n step 離れている場合の組み合わせ
def no_hole(n):
    count = 0
    m = n // 2
    for i in range(0, m+1):
        count += ncr(n-i, i)
    return count


# 穴なしで n step 離れている場合の組み合わせ(高速化版)
@lru_cache(maxsize=8192)
def no_hole2(n):
    if n <= 5:
        return (1, 1, 2, 3, 5, 8)[n]
    if n % 2:
        h = (n-1) // 2
        m1 = no_hole2(h-1)
        m0 = no_hole2(h)
        return 2 * m1 * m0 + m0 * m0
    else:
        h = n // 2
        m2 = no_hole2(h-2)
        m1 = no_hole2(h-1)
        m0 = no_hole2(h)
        return m1 * m1 + m2 * m0 + m1 * m0


def solv(n, m, a):
    ans = 1
    current_pos = 0
    for pos in a:
        dist = pos - 1 - current_pos
        if dist < 0:
            return 0
        ans *= no_hole2(dist)
        current_pos = pos + 1
    dist = n - current_pos
    ans *= no_hole2(dist)
    return ans


if __name__ == '__main__':

    n, m = map(int, input().split())
    a = [int(input()) for _ in range(m)]

    ans = solv(n, m, a)

    P_NUM = 1000000007
    print(ans % P_NUM)
