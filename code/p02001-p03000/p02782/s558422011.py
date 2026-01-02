import os
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7


# MOD = 998244353


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


R1, C1, R2, C2 = list(map(int, sys.stdin.buffer.readline().split()))

comb = Combination(max=10 ** 6 * 2 + 100, mod=MOD)


# 解説
# ある要素に注目して残りを選ぶ数を数えると分かる
# ncr(n, r) == ncr(n-1,r) + (n-1,r-1)
# nhr(n, r) == sum([nhr(n-1,k) for k in range(r)])

# g(r, c) を f(i, j) (0<=i<=r, 0<=j<=c) の総和とすると
# g(R2, C2) - g(R1-1, C2) - g(R2, C1-1) + g(R1-1, C1-1)

def f(n, r):
    return comb.ncr(n + r, r)


# @debug
def g(r, c):
    # ret = 0
    # for i in range(1, c + 2):
    #     ret += f(r, i)
    #     ret %= MOD

    # f(r,k) (k=[1,c+1]) の和
    return f(r + 1, c + 1) - f(r, 0)


ans = g(R2, C2) - g(R1 - 1, C2) - g(R2, C1 - 1) + g(R1 - 1, C1 - 1)
ans %= MOD
print(ans)
