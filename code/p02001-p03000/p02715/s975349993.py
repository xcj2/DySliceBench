import bisect
import collections
import functools
import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline
ACMOD = 1000000007
INF = 1 << 62


def lmi():
    return list(map(int, input().split()))


def llmi(n):
    return [lmi() for _ in range(n)]


# pattern of x で割れる
@functools.lru_cache(maxsize=None)
def f(x):
    return K//x
    a = 0
    for i in range(1, K + 1):
        if i % x == 0:
            a += 1
    return a % ACMOD


@functools.lru_cache(maxsize=None)
def make_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    return frozenset(divisors)


@functools.lru_cache(maxsize=None)
def get_diff(x):
    """
    xで割れるときにいくら増加するか
    2 -> 1 でカウント済みなので1
    """
    if x == 1:
        return 1
    ans = x
    for v in make_divisors(x):
        if v != x:
            ans -= get_diff(v)
    return ans % ACMOD


@functools.lru_cache(maxsize=None)
def pow(base_val, pow_val):
    if pow_val == 1:
        return base_val
    if pow_val == 0:
        return 1
    t = pow(base_val, pow_val // 2) % ACMOD
    return (t * t % ACMOD * (base_val if pow_val % 2 else 1)) % ACMOD


# for i in range(1, 100000):
#     get_diff(i)
#
# print("ok")
N, K = lmi()

ans = 0
for i in range(1, K + 1):
    ans += (pow(f(i), N) % ACMOD) * get_diff(i) % ACMOD
    # print(i,f(i), get_diff(i))

print(ans % ACMOD)
