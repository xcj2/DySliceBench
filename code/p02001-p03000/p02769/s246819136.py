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

# MOD = 998244353

def get_factorials(max, mod=None):
    """
    階乗 0!, 1!, 2!, ..., max!
    :param int max:
    :param int mod:
    """
    ret = [1]
    n = 1
    if mod:
        for i in range(1, max + 1):
            n *= i
            n %= mod
            ret.append(n)
    else:
        for i in range(1, max + 1):
            n *= i
            ret.append(n)
    return ret


def mod_invs(max, mod):
    """
    逆元 0, 1/1, 1/2, 1/3, ..., 1/max
    :param int max:
    :param int mod:
    """
    invs = [1] * (max + 1)
    invs[0] = 0
    for x in range(2, max + 1):
        invs[x] = (-(mod // x) * invs[mod % x]) % mod
    return invs


def factorial_invs(max, mod):
    """
    階乗 0!, 1!, 2!, ..., max! の逆元
    :param int max:
    :param int mod:
    """
    ret = [1]
    r = 1
    for inv in mod_invs(max, mod)[1:]:
        r = r * inv % mod
        ret.append(r)
    return ret


class Combination:
    def __init__(self, max, mod):
        """
        :param int max:
        :param int mod: 3 以上の素数であること
        """
        self._factorials = get_factorials(max, mod)
        self._finvs = factorial_invs(max, mod)
        self._mod = mod

    def ncr(self, n, r):
        """
        :param int n:
        :param int r:
        :rtype: int
        """
        if n < r:
            return 0
        return self._factorials[n] * self._finvs[r] % self._mod * self._finvs[n - r] % self._mod


N, K = list(map(int, sys.stdin.buffer.readline().split()))


@lru_cache(maxsize=None)
def solve(li, k):
    li = eval(li)
    if k == 0:
        return {','.join(map(str, li))}
    ret_s = set()
    for i in range(len(li)):
        if li[i] > 0:
            for j in range(len(li)):
                if i == j:
                    continue
                cp = li[:]
                cp[i] -= 1
                cp[j] += 1
                ret_s |= solve(str(cp), k - 1)
    return ret_s


# print(solve(str([0] * N), K))

comb = Combination(N * 2 + 100, MOD)
if K >= N - 1:
    ans = comb.ncr(N * 2 - 1, N - 1)
    print(ans)
    exit()


@lru_cache(maxsize=None)
def solve2(n, k, size):
    if size == 0:
        return 0
    if k >= n - 1:
        return comb.ncr(n * 2 - 1, n - 1)
    ret = 0
    for i in range(k + 1):
        ret += solve2(n - i, k, size - 1)
    return ret


# ゼロが何個あるか
# 最大 K こ
ans = 0
for zero_cnt in range(K + 1):
    # ゼロを置く場所を選ぶ
    a = comb.ncr(N, zero_cnt)
    # ゼロ以外の場所に全部1を置く
    r = N - zero_cnt
    # r から (N - r == zero_cnt) 個選ぶ重複組合せ
    b = comb.ncr(r + zero_cnt - 1, zero_cnt)
    ans += a * b % MOD
    ans %= MOD
print(ans)
