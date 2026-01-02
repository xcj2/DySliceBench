import os
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7


# MOD = 998244353

def div_mod(a, b, mod):
    """
    (a // b) % mod
    mod は 3 以上の素数を指定
    フェルマーの小定理より mod p の世界で b^(p-1) は必ず 1 になるので
    b の逆元 (b と掛けると 1 になる数) は b^(p-2)
    :param int a:
    :param int b:
    :param int mod:
    :return:
    """
    return a * pow(b, mod - 2, mod) % mod


def mod_inv(a, mod):
    """
    a の逆元
    :param int a:
    :param int mod:
    :return:
    """
    return pow(a, mod - 2, mod)


def get_factorials(max, mod=None):
    """
    階乗 0!, 1!, 2!, ..., max!
    :param int max:
    :param int mod:
    :return:
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
    逆元のリスト 0 から max まで
    :param int max:
    :param int mod:
    """
    invs = [1] * (max + 1)
    for x in range(2, max + 1):
        invs[x] = (-(mod // x) * invs[mod % x]) % mod
    return invs


def factorial_invs(max, mod):
    """
    階乗 0!, 1!, 2!, ..., max! の逆元
    :param int max:
    :param int mod:
    """
    ret = []
    r = 1
    for inv in mod_invs(max, mod):
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


X, Y = list(map(int, sys.stdin.readline().split()))

if (X + Y) % 3 != 0:
    print(0)
    exit()

X, Y = min(X, Y), max(X, Y)
if X * 2 < Y:
    print(0)
    exit()

comb = Combination(max=(X + Y) // 3, mod=MOD)
print(comb.ncr((X + Y) // 3, X - (X + Y) // 3))

# dp = np.zeros((X + 1, Y + 1), dtype=int)
# dp[0][0] = 1
# for x, y in itertools.product(range(X), range(Y)):
#     if x + 1 <= X and y + 2 <= Y:
#         dp[x + 1, y + 2] += dp[x, y]
#     if x + 2 <= X and y + 1 <= Y:
#         dp[x + 2, y + 1] += dp[x, y]
# print(dp)
