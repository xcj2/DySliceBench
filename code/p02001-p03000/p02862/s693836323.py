import sys
sys.setrecursionlimit(10**6)

x, y = [int(i) for i in input().split()]

MOD = 10 ** 9 + 7

import functools
import math

def mpow(x, n):
    result = 1
    while n > 0:
        if (n & 1):
            result = (result * x) % MOD
        x = (x * x) % MOD
        n >>= 1
    return result

# 方程式を解けば解が一意に定まるため、全パターンを試すのは無駄
def solver_not_good():
    factorial = [0] * (10 ** 6 + 1)
    inverse = [0] * (10 ** 6 + 1)
    factorial[0] = 1
    inverse[0] = 1
    for i in range(1, 10 ** 6 + 1):
        factorial[i] = (i * factorial[i-1]) % MOD
        inverse[i] = mpow(factorial[i], MOD - 2) % MOD

    total = 0
    twopath_maxnum = x // 2
    for twopath_num in range(twopath_maxnum + 1):
        onepath_num = x - twopath_num * 2
        if (onepath_num * 2 + twopath_num * 1) == y:
            a = factorial[onepath_num + twopath_num]
            b = inverse[onepath_num]
            c = inverse[twopath_num]
            total += (a * b * c) % MOD
    return total

def solver_better():
    # 剰余演算を都度挟みたいため、math.factorialは使えない
    factorial = [0] * (10 ** 6 + 1)
    factorial[0] = 1
    for i in range(1, 10 ** 6 + 1):
        factorial[i] = (i * factorial[i-1]) % MOD

    # x + y が3の倍数でないときは到達できない
    if ((x + y) % 3) != 0:
        return 0

    a = (2 * x - y) // 3
    b = (2 * y - x) // 3

    # x座標/y座標のどちらかに先に到達してしまう
    if a < 0 or b < 0:
        return 0

    return (factorial[a+b] * (mpow(factorial[a], MOD - 2) % MOD) * (mpow(factorial[b], MOD -2) % MOD)) % MOD

#solver = solver_not_good
solver = solver_better
print(solver())
