import math
import os
import sys
from functools import lru_cache

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7
# MOD = 998244353

N = int(sys.stdin.buffer.readline())


@lru_cache(maxsize=None)
def func(n, k):
    if n < k:
        return n
    if n % k == 0:
        return func(n // k, k)
    else:
        # return func(n - k, k)
        return n % k


def test(N):
    cnt = 0
    for k in range(2, N + 1):
        c = func(N, k)
        if c == 1:
            cnt += 1
        print(k, c)
    print(cnt)


def get_divisors(n):
    """
    n の約数をリストで返す
    :param int n:
    :rtype: list of int
    """
    ret = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            ret.append(i)
            if n // i != i:
                ret.append(n // i)
    return ret


# test(N)

# k == N - 1 の約数のとき 1 になる
ans = len(get_divisors(N - 1))
for k in get_divisors(N):
    if (N - 1) % k == 0:
        continue
    p = N // k
    if p >= k:
        ans += func(N // k, k) == 1
print(ans)
