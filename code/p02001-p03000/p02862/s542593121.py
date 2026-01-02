import math
from functools import lru_cache
from operator import mul
from functools import reduce


def cmb(n, r, mod):
    numerator = reduce(lambda x, y: x * y % mod, [n - r + k + 1 for k in range(r)])
    denominator = reduce(lambda x, y: x * y % mod, [k + 1 for k in range(r)])
    return numerator * pow(denominator, mod - 2, mod) % mod


def combinations_count(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom


def my_factorial(n, mod):
    if n == 1:
        return 1
    return (n * my_factorial(n-1, mod)) % mod


@lru_cache(maxsize=None)
def for_factorial(n):
    val = 1
    for i in range(2, n + 1):
        val = (val * i)
    return val



x, y = map(int, input().split())
mod = 1000000007
cnt = (x + y) // 3
if (x + y) % 3 != 0:
    print(0)
    exit()
m = min(x, y)
num_2 = m - cnt
num_1 = cnt - num_2
ans = cmb(cnt, num_1, mod)
print(ans)

